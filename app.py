from flask import Flask, render_template, Response, jsonify
import cv2
import mediapipe as mp
import numpy as np
from collections import deque
import time

app = Flask(__name__)

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.5
)

# Global variables
camera = None
last_gesture = ""
gesture_buffer = deque(maxlen=10)
last_update_time = time.time()

def get_camera():
    """Get or initialize camera"""
    global camera
    if camera is None:
        camera = cv2.VideoCapture(0)
    return camera

def recognize_gesture(hand_landmarks):
    """
    Simple gesture recognition based on finger positions
    Returns recognized letter or gesture
    """
    # Get landmark positions
    landmarks = hand_landmarks.landmark
    
    # Helper function to check if finger is extended
    def is_finger_extended(tip_idx, pip_idx):
        return landmarks[tip_idx].y < landmarks[pip_idx].y
    
    # Thumb check (uses x coordinate due to orientation)
    thumb_extended = landmarks[4].x < landmarks[3].x if landmarks[4].x < 0.5 else landmarks[4].x > landmarks[3].x
    
    # Check each finger
    index_extended = is_finger_extended(8, 6)
    middle_extended = is_finger_extended(12, 10)
    ring_extended = is_finger_extended(16, 14)
    pinky_extended = is_finger_extended(20, 18)
    
    # Count extended fingers
    extended_fingers = sum([
        thumb_extended,
        index_extended,
        middle_extended,
        ring_extended,
        pinky_extended
    ])
    
    # Simple gesture recognition
    if extended_fingers == 0:
        return "A"  # Fist
    elif extended_fingers == 1 and index_extended:
        return "D"  # Index finger only
    elif extended_fingers == 2 and index_extended and middle_extended:
        return "V"  # Peace sign / Victory
    elif extended_fingers == 3 and index_extended and middle_extended and ring_extended:
        return "W"
    elif extended_fingers == 5:
        return "B"  # Open hand
    elif extended_fingers == 1 and thumb_extended:
        return "THUMBS_UP"
    else:
        return None

def generate_frames():
    """Generate video frames with hand detection"""
    global last_gesture, gesture_buffer, last_update_time
    
    camera = get_camera()
    
    while True:
        success, frame = camera.read()
        if not success:
            break
        
        # Flip frame horizontally for mirror effect
        frame = cv2.flip(frame, 1)
        
        # Convert to RGB for MediaPipe
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        # Process the frame
        results = hands.process(rgb_frame)
        
        # Draw hand landmarks and recognize gesture
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                # Draw landmarks
                mp_drawing.draw_landmarks(
                    frame,
                    hand_landmarks,
                    mp_hands.HAND_CONNECTIONS
                )
                
                # Recognize gesture
                gesture = recognize_gesture(hand_landmarks)
                if gesture:
                    gesture_buffer.append(gesture)
                    
                    # Update gesture if stable for a short time
                    if len(gesture_buffer) >= 5:
                        most_common = max(set(gesture_buffer), key=gesture_buffer.count)
                        current_time = time.time()
                        if current_time - last_update_time > 1.5:  # Update every 1.5 seconds
                            last_gesture = most_common
                            last_update_time = current_time
        
        # Add text overlay
        cv2.putText(frame, f"Last Sign: {last_gesture}", (10, 30),
                   cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        
        # Encode frame
        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def index():
    """Render main page"""
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    """Video streaming route"""
    return Response(generate_frames(),
                   mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/get_text')
def get_text():
    """Get recognized text"""
    return jsonify({'text': last_gesture})

@app.route('/reset')
def reset():
    """Reset recognized text"""
    global last_gesture, gesture_buffer
    last_gesture = ""
    gesture_buffer.clear()
    return jsonify({'status': 'ok'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
