"""
Test script for gesture recognition logic
This can be run independently to verify the gesture recognition algorithm
"""

class MockLandmark:
    """Mock landmark for testing"""
    def __init__(self, x, y):
        self.x = x
        self.y = y

class MockHandLandmarks:
    """Mock hand landmarks for testing"""
    def __init__(self, landmarks):
        self.landmark = landmarks

def recognize_gesture_test(hand_landmarks):
    """
    Test version of gesture recognition
    Returns recognized letter or gesture
    """
    landmarks = hand_landmarks.landmark
    
    def is_finger_extended(tip_idx, pip_idx):
        return landmarks[tip_idx].y < landmarks[pip_idx].y
    
    # Thumb check
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
        return "A"
    elif extended_fingers == 1 and index_extended:
        return "D"
    elif extended_fingers == 2 and index_extended and middle_extended:
        return "V"
    elif extended_fingers == 3 and index_extended and middle_extended and ring_extended:
        return "W"
    elif extended_fingers == 5:
        return "B"
    elif extended_fingers == 1 and thumb_extended:
        return "THUMBS_UP"
    else:
        return None

def create_test_landmarks(thumb_x, thumb_y, index_tip_y, middle_tip_y, ring_tip_y, pinky_tip_y):
    """Create test landmarks for a hand gesture"""
    # Simplified landmark positions (only the ones we use)
    landmarks = [MockLandmark(0.5, 0.5) for _ in range(21)]
    
    # Thumb
    landmarks[3] = MockLandmark(0.3, 0.6)
    landmarks[4] = MockLandmark(thumb_x, thumb_y)
    
    # Index finger
    landmarks[6] = MockLandmark(0.4, 0.5)
    landmarks[8] = MockLandmark(0.4, index_tip_y)
    
    # Middle finger
    landmarks[10] = MockLandmark(0.5, 0.5)
    landmarks[12] = MockLandmark(0.5, middle_tip_y)
    
    # Ring finger
    landmarks[14] = MockLandmark(0.6, 0.5)
    landmarks[16] = MockLandmark(0.6, ring_tip_y)
    
    # Pinky
    landmarks[18] = MockLandmark(0.7, 0.5)
    landmarks[20] = MockLandmark(0.7, pinky_tip_y)
    
    return MockHandLandmarks(landmarks)

def run_tests():
    """Run gesture recognition tests"""
    print("Testing gesture recognition logic...\n")
    
    # Test 1: Closed fist (A)
    print("Test 1: Closed fist (gesture A)")
    landmarks = create_test_landmarks(0.3, 0.65, 0.6, 0.6, 0.6, 0.6)
    result = recognize_gesture_test(landmarks)
    print(f"Result: {result}")
    assert result == "A", f"Expected 'A', got '{result}'"
    print("✓ Passed\n")
    
    # Test 2: Open hand (B)
    print("Test 2: Open hand (gesture B)")
    landmarks = create_test_landmarks(0.2, 0.5, 0.2, 0.2, 0.2, 0.2)
    result = recognize_gesture_test(landmarks)
    print(f"Result: {result}")
    assert result == "B", f"Expected 'B', got '{result}'"
    print("✓ Passed\n")
    
    # Test 3: Index finger only (D)
    print("Test 3: Index finger only (gesture D)")
    landmarks = create_test_landmarks(0.3, 0.65, 0.2, 0.6, 0.6, 0.6)
    result = recognize_gesture_test(landmarks)
    print(f"Result: {result}")
    assert result == "D", f"Expected 'D', got '{result}'"
    print("✓ Passed\n")
    
    # Test 4: Peace sign (V)
    print("Test 4: Peace sign (gesture V)")
    landmarks = create_test_landmarks(0.3, 0.65, 0.2, 0.2, 0.6, 0.6)
    result = recognize_gesture_test(landmarks)
    print(f"Result: {result}")
    assert result == "V", f"Expected 'V', got '{result}'"
    print("✓ Passed\n")
    
    # Test 5: Three fingers (W)
    print("Test 5: Three fingers (gesture W)")
    landmarks = create_test_landmarks(0.3, 0.65, 0.2, 0.2, 0.2, 0.6)
    result = recognize_gesture_test(landmarks)
    print(f"Result: {result}")
    assert result == "W", f"Expected 'W', got '{result}'"
    print("✓ Passed\n")
    
    # Test 6: Thumbs up
    print("Test 6: Thumbs up")
    landmarks = create_test_landmarks(0.2, 0.5, 0.6, 0.6, 0.6, 0.6)
    result = recognize_gesture_test(landmarks)
    print(f"Result: {result}")
    assert result == "THUMBS_UP", f"Expected 'THUMBS_UP', got '{result}'"
    print("✓ Passed\n")
    
    print("=" * 50)
    print("All tests passed! ✓")
    print("=" * 50)

if __name__ == "__main__":
    run_tests()
