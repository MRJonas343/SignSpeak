# SignSpeak 🤟

Traductor de Lengua de Señas a Texto con IA en tiempo real

## 📋 Descripción

SignSpeak es una aplicación web MVP que utiliza visión por computadora e inteligencia artificial para traducir lengua de señas a texto en tiempo real. La aplicación captura video desde la cámara del dispositivo, detecta las manos usando MediaPipe, y reconoce gestos básicos que se traducen a texto.

## ✨ Características

- **Captura de video en tiempo real** desde la cámara web
- **Detección de manos** usando MediaPipe Hands
- **Reconocimiento de gestos básicos**:
  - A - Puño cerrado
  - B - Mano abierta (5 dedos)
  - D - Solo dedo índice
  - V - Índice y medio (paz/victoria)
  - W - Índice, medio y anular
  - 👍 - Pulgar arriba
- **Interfaz web simple y responsive** con FastAPI
- **Traducción en tiempo real** mostrada en pantalla
- **Función de reseteo** para limpiar el texto reconocido

## 🛠️ Tecnologías

- **Backend**: Python 3.8+, FastAPI, Uvicorn
- **IA/ML**: MediaPipe, OpenCV
- **Frontend**: HTML5, CSS3, JavaScript

## 📦 Instalación

### Prerrequisitos

- Python 3.8 o superior
- Cámara web funcional
- pip (gestor de paquetes de Python)

### Pasos

1. Clonar el repositorio:
```bash
git clone https://github.com/MRJonas343/SignSpeak.git
cd SignSpeak
```

2. Crear y activar un entorno virtual (recomendado):
```bash
# En Windows
python -m venv venv
venv\Scripts\activate

# En Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

3. Instalar las dependencias:
```bash
pip install -r requirements.txt
```

## 🚀 Uso

1. Iniciar la aplicación:
```bash
python app.py
```

2. Abrir un navegador web y navegar a:
```
http://localhost:5000
```

3. Permitir el acceso a la cámara cuando se solicite

4. Realizar señas frente a la cámara y observar el texto reconocido en tiempo real

5. Usar el botón "Limpiar Texto" para resetear la traducción

## 📱 Cómo Funciona

1. **Captura de Video**: La aplicación accede a la cámara web y captura frames en tiempo real
2. **Detección de Manos**: MediaPipe Hands detecta y rastrea 21 puntos clave de la mano
3. **Reconocimiento de Gestos**: El algoritmo analiza la posición de los dedos para reconocer gestos
4. **Estabilización**: Se usa un buffer para evitar detecciones falsas y estabilizar el reconocimiento
5. **Visualización**: El texto reconocido se muestra en la interfaz web en tiempo real

## 🎯 Alcance MVP

Este es un MVP (Minimum Viable Product) enfocado en:
- Reconocimiento básico de 5-6 gestos/letras
- Traducción simple a texto
- Interfaz funcional y limpia
- Pipeline completo: Cámara → IA → Texto

## 🔮 Futuras Mejoras

- [ ] Ampliar el vocabulario de señas (alfabeto completo A-Z)
- [ ] Reconocimiento de palabras y frases completas
- [ ] Traducción de texto a voz (Text-to-Speech)
- [ ] Historial de traducciones
- [ ] Exportación de texto a archivo
- [ ] Soporte multilenguaje
- [ ] Optimización para dispositivos móviles
- [ ] Entrenamiento de modelo personalizado con más gestos
- [ ] Modo de práctica/aprendizaje

## 🤝 Contribuir

Las contribuciones son bienvenidas. Por favor:

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT.

## 👥 Autor

- MRJonas343

## 🙏 Agradecimientos

- MediaPipe por su excelente framework de detección de manos
- La comunidad de código abierto