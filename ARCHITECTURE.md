# Arquitectura de SignSpeak

## Visión General

SignSpeak es una aplicación web que traduce lengua de señas a texto en tiempo real utilizando visión por computadora e inteligencia artificial.

## Diagrama de Arquitectura

```
┌─────────────────────────────────────────────────────────────┐
│                         Usuario                              │
│                    (Hace señas frente a la cámara)          │
└──────────────────────────┬──────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────┐
│                    Navegador Web                             │
│  ┌──────────────────────────────────────────────────────┐  │
│  │               Frontend (HTML/CSS/JS)                  │  │
│  │  - Interfaz de usuario                                │  │
│  │  - Visualización de video                             │  │
│  │  - Display de texto reconocido                        │  │
│  │  - Polling cada 1 segundo para actualizar texto       │  │
│  └──────────────┬───────────────────────┬─────────────────┘  │
└─────────────────┼───────────────────────┼─────────────────────┘
                  │                       │
                  │ HTTP Request          │ Video Stream
                  │ (GET /get_text)       │ (GET /video_feed)
                  │                       │
                  ▼                       ▼
┌─────────────────────────────────────────────────────────────┐
│                    Backend FastAPI (app.py)                  │
│  ┌──────────────────────────────────────────────────────┐  │
│  │              Rutas / Endpoints                        │  │
│  │  - / (index)         → Renderiza página principal    │  │
│  │  - /video_feed       → Stream de video procesado     │  │
│  │  - /get_text         → Último texto reconocido       │  │
│  │  - /reset            → Limpiar texto                 │  │
│  └──────────────┬───────────────────────────────────────┘  │
│                 │                                            │
│                 ▼                                            │
│  ┌──────────────────────────────────────────────────────┐  │
│  │         Procesamiento de Video                        │  │
│  │  1. Captura frame de cámara (OpenCV)                 │  │
│  │  2. Flip horizontal (efecto espejo)                  │  │
│  │  3. Conversión BGR → RGB                             │  │
│  │  4. Envío a MediaPipe                                │  │
│  └──────────────┬───────────────────────────────────────┘  │
│                 │                                            │
│                 ▼                                            │
│  ┌──────────────────────────────────────────────────────┐  │
│  │            MediaPipe Hands                            │  │
│  │  - Detección de manos                                 │  │
│  │  - Extracción de 21 landmarks (puntos clave)         │  │
│  │  - Tracking continuo                                  │  │
│  └──────────────┬───────────────────────────────────────┘  │
│                 │                                            │
│                 ▼                                            │
│  ┌──────────────────────────────────────────────────────┐  │
│  │        Reconocimiento de Gestos                       │  │
│  │  - Análisis de posiciones de dedos                   │  │
│  │  - Cálculo de dedos extendidos                       │  │
│  │  - Mapeo a letra/gesto                               │  │
│  │  - Buffer para estabilización                        │  │
│  └──────────────┬───────────────────────────────────────┘  │
│                 │                                            │
│                 ▼                                            │
│  ┌──────────────────────────────────────────────────────┐  │
│  │            Variables Globales                         │  │
│  │  - last_gesture: último gesto reconocido             │  │
│  │  - gesture_buffer: cola de últimos 10 gestos         │  │
│  │  - last_update_time: timestamp de última actualiz.   │  │
│  └──────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────┐
│                      Cámara Web                              │
│              (Dispositivo de captura de video)               │
└─────────────────────────────────────────────────────────────┘
```

## Flujo de Datos

### 1. Inicialización
```
Usuario inicia app.py
  → Uvicorn server con FastAPI inicia en puerto 5000
  → MediaPipe Hands se inicializa
  → Variables globales se configuran
```

### 2. Carga de Página
```
Usuario abre http://localhost:5000
  → FastAPI sirve templates/index.html usando Jinja2Templates
  → Browser renderiza interfaz
  → JavaScript inicia polling cada 1 segundo
  → <img> tag solicita video stream
```

### 3. Stream de Video (Loop continuo)
```
Browser solicita /video_feed
  → get_camera() obtiene/inicializa cámara
  → Loop infinito:
      1. camera.read() captura frame
      2. cv2.flip() voltea horizontalmente
      3. cv2.cvtColor() convierte BGR→RGB
      4. hands.process() detecta manos
      5. Si se detecta mano:
         - mp_drawing.draw_landmarks() dibuja puntos
         - recognize_gesture() analiza posición
         - gesture_buffer.append() agrega a buffer
         - Si buffer tiene ≥5 elementos y pasaron >1.5s:
           → Actualiza last_gesture con gesto más común
      6. cv2.putText() añade texto al frame
      7. cv2.imencode() codifica a JPEG
      8. yield frame como multipart/x-mixed-replace
```

### 4. Actualización de Texto (Polling)
```
Cada 1 segundo, JavaScript ejecuta:
  fetch('/get_text')
    → Backend retorna: {'text': last_gesture}
    → JavaScript actualiza DOM con nuevo texto
```

### 5. Reset
```
Usuario hace clic en "Limpiar Texto"
  → fetch('/reset')
  → Backend limpia last_gesture y gesture_buffer
  → Retorna: {'status': 'ok'}
  → JavaScript limpia display local
```

## Componentes Técnicos

### Backend (Python/FastAPI)

#### Librerías Principales
- **FastAPI**: Framework web moderno y rápido
- **Uvicorn**: Servidor ASGI para FastAPI
- **OpenCV (cv2)**: Captura y procesamiento de video
- **MediaPipe**: Detección de manos y landmarks
- **NumPy**: Operaciones numéricas (uso indirecto)

#### Funciones Clave

**`get_camera()`**
- Singleton para instancia de cámara
- Evita múltiples inicializaciones
- Retorna objeto VideoCapture

**`recognize_gesture(hand_landmarks)`**
- Input: objeto con 21 landmarks de MediaPipe
- Lógica:
  - Compara posiciones Y de tips vs PIPs para dedos
  - Compara posición X para pulgar (diferente orientación)
  - Cuenta dedos extendidos
  - Mapea a gesto conocido
- Output: String con letra/gesto o None

**`generate_frames()`**
- Generador infinito de frames
- Maneja detección, reconocimiento y encoding
- Yield de bytes para streaming

#### Variables Globales
- `camera`: Instancia VideoCapture (lazy initialization)
- `last_gesture`: String del último gesto reconocido
- `gesture_buffer`: deque(maxlen=10) para estabilización
- `last_update_time`: timestamp para rate limiting

### Frontend (HTML/CSS/JavaScript)

#### Estructura HTML
- Header con título y descripción
- Grid responsive con 2 columnas:
  - Video section: Stream de cámara
  - Text section: Display de texto + controles + referencia

#### CSS
- Gradiente purple/blue para branding
- Cards con sombras y border-radius
- Responsive con flexbox
- Animación pulse para indicador de status

#### JavaScript
- `setInterval()` para polling cada 1 segundo
- Fetch API para GET requests
- Actualización del DOM basada en respuesta
- Manejo de estado local (recognizedText)

## Algoritmo de Reconocimiento de Gestos

### Landmarks de MediaPipe

MediaPipe detecta 21 puntos en la mano:
```
0:  WRIST (muñeca)
1-4:  THUMB (pulgar: CMC, MCP, IP, TIP)
5-8:  INDEX (índice: MCP, PIP, DIP, TIP)
9-12:  MIDDLE (medio: MCP, PIP, DIP, TIP)
13-16: RING (anular: MCP, PIP, DIP, TIP)
17-20: PINKY (meñique: MCP, PIP, DIP, TIP)
```

### Lógica de Detección

Para cada dedo (excepto pulgar):
```python
is_extended = landmark[TIP].y < landmark[PIP].y
```
- Y más pequeño = más arriba = extendido
- Y más grande = más abajo = doblado

Para pulgar (horizontal):
```python
is_extended = (landmark[4].x < landmark[3].x) si mano_izquierda
              else (landmark[4].x > landmark[3].x)
```

### Mapeo de Gestos

```
0 dedos extendidos → "A" (puño)
1 dedo (índice)    → "D"
1 dedo (pulgar)    → "THUMBS_UP"
2 dedos (í+m)      → "V" (victoria)
3 dedos (í+m+a)    → "W"
5 dedos            → "B" (mano abierta)
```

### Estabilización

Se usa un buffer de 10 elementos:
1. Cada frame agrega detección al buffer
2. Cuando buffer ≥ 5 elementos:
   - Calcula el gesto más común (moda)
   - Si pasaron >1.5 segundos desde última actualización:
     - Actualiza last_gesture
     - Reset del timer

Esto previene:
- False positives por frames ambiguos
- Cambios rápidos por movimiento de mano
- Flicker en el texto mostrado

## Consideraciones de Diseño

### Escalabilidad
- **Actual**: Single-threaded, una sesión
- **Futuro**: Múltiples sesiones con WebSockets o rooms

### Performance
- MediaPipe es eficiente (funciona en CPU)
- JPEG encoding es el bottleneck principal
- ~15-30 FPS es suficiente para UX fluida

### Precisión vs Velocidad
- Buffer de 10 frames balancea ambos
- Delay de 1.5s previene cambios espúreos
- Trade-off: Latencia por estabilidad

### Extensibilidad
- Fácil agregar nuevos gestos en recognize_gesture()
- Posible integrar ML model entrenado para más precisión
- Arquitectura soporta múltiples manos con cambios menores

## Dependencias y Versiones

```
fastapi==0.104.1      → Web framework
uvicorn==0.24.0       → ASGI server
python-multipart==0.0.6 → Form parsing
jinja2==3.1.2         → Template engine
opencv-python==4.8.1  → Computer vision
mediapipe==0.10.21    → Hand tracking
numpy==1.24.3         → Operaciones numéricas
```

## Seguridad

### Consideraciones Actuales
- ✓ No se guardan videos ni frames
- ✓ Procesamiento local (no se envía video a servidores)
- ✓ Sin autenticación (app local)
- ⚠️ debug=True en producción es riesgo

### Mejoras Recomendadas para Producción
- Desactivar debug mode
- Agregar rate limiting
- HTTPS para acceso remoto
- Validación de input
- CORS configurado apropiadamente

## Testing

### Pruebas Actuales
- `test_gesture_logic.py`: Unit tests para reconocimiento
- Verificación de sintaxis Python

### Pruebas Recomendadas
- Integration tests para endpoints FastAPI
- Tests de carga para streaming
- Tests de UI con Selenium
- Tests de precisión con dataset de gestos

## Deployment

### Local (Actual)
```bash
python app.py
```

### Producción (Recomendado)
```bash
uvicorn app:app --host 0.0.0.0 --port 5000 --workers 4
```

Con:
- Nginx como reverse proxy
- Supervisor para process management
- Docker para containerización

## Roadmap Técnico

### Corto Plazo
- [ ] Agregar más gestos (alfabeto completo)
- [ ] Mejorar precisión con ML model
- [ ] Historial de traducciones

### Mediano Plazo
- [ ] Text-to-Speech
- [ ] Soporte móvil (responsive + cámara)
- [ ] Modo offline con PWA

### Largo Plazo
- [ ] Reconocimiento de frases
- [ ] Múltiples lenguajes de señas
- [ ] AR/VR integration
- [ ] Collaborative features

## Referencias

- [MediaPipe Hands Documentation](https://google.github.io/mediapipe/solutions/hands.html)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [OpenCV Python Tutorials](https://docs.opencv.org/master/d6/d00/tutorial_py_root.html)
