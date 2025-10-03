# Guía de Instalación Detallada

## Requisitos del Sistema

### Sistema Operativo
- Windows 10/11
- macOS 10.14+
- Linux (Ubuntu 20.04+, Debian, etc.)

### Software Requerido
- **Python 3.8 o superior**
  - Verificar: `python --version` o `python3 --version`
  - Descargar desde: https://www.python.org/downloads/
  
- **pip** (gestor de paquetes de Python)
  - Normalmente viene con Python
  - Verificar: `pip --version` o `pip3 --version`

- **Cámara web funcional**
  - Integrada o USB
  - Drivers actualizados

### Dependencias de Sistema (Linux)

En sistemas Linux, puede ser necesario instalar dependencias adicionales:

```bash
# Ubuntu/Debian
sudo apt-get update
sudo apt-get install -y python3-opencv
sudo apt-get install -y libglib2.0-0 libsm6 libxext6 libxrender-dev

# Fedora
sudo dnf install opencv python3-opencv
```

## Pasos de Instalación

### 1. Clonar el Repositorio

```bash
git clone https://github.com/MRJonas343/SignSpeak.git
cd SignSpeak
```

### 2. Crear Entorno Virtual (Recomendado)

Un entorno virtual aísla las dependencias del proyecto:

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Linux/macOS:**
```bash
python3 -m venv venv
source venv/bin/activate
```

Verás `(venv)` en tu prompt cuando esté activado.

### 3. Instalar Dependencias

```bash
pip install -r requirements.txt
```

Si tienes problemas de timeout, intenta:

```bash
# Instalar con timeout más largo
pip install --timeout 120 -r requirements.txt

# O instalar una por una
pip install fastapi
pip install uvicorn[standard]
pip install python-multipart
pip install jinja2
pip install opencv-python
pip install mediapipe
pip install numpy
```

### 4. Verificar Instalación

```bash
python -c "import fastapi; import uvicorn; import cv2; import mediapipe; print('✓ Todas las dependencias instaladas correctamente')"
```

## Ejecución

### Iniciar la Aplicación

```bash
python app.py
```

Deberías ver:
```
 * Running on http://0.0.0.0:5000
 * Running on http://127.0.0.1:5000
```

### Acceder a la Aplicación

Abre tu navegador y ve a:
- http://localhost:5000
- http://127.0.0.1:5000

## Solución de Problemas

### La cámara no se detecta

**Windows:**
- Verifica que la cámara esté habilitada en Configuración > Privacidad > Cámara
- Asegúrate de que no esté siendo usada por otra aplicación

**Linux:**
- Verifica permisos: `ls -l /dev/video*`
- Añade tu usuario al grupo video: `sudo usermod -a -G video $USER`
- Cierra sesión e inicia de nuevo

**macOS:**
- Otorga permisos de cámara en Preferencias del Sistema > Seguridad y Privacidad

### Error "ModuleNotFoundError"

Si ves errores como `ModuleNotFoundError: No module named 'fastapi'` o `'uvicorn'`:
- Asegúrate de que el entorno virtual esté activado
- Reinstala las dependencias: `pip install -r requirements.txt`

### Error "Address already in use"

Si el puerto 5000 está en uso:

```bash
# Encuentra el proceso
# Linux/macOS
lsof -i :5000
# Windows
netstat -ano | findstr :5000

# Mata el proceso o cambia el puerto en app.py
# Edita app.py, última línea:
app.run(debug=True, host='0.0.0.0', port=8080)
```

### Problemas de Rendimiento

Si el video se ve lento:
- Cierra otras aplicaciones que usen la cámara
- Reduce la calidad de video en `app.py`:
  ```python
  camera = cv2.VideoCapture(0)
  camera.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
  camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
  ```

### La detección de manos no funciona

- Asegúrate de tener buena iluminación
- Mantén la mano a una distancia de 30-60 cm de la cámara
- Fondo contrastante ayuda (evita fondos complejos)
- Verifica que los landmarks se dibujen en el video

## Desinstalación

1. Desactiva el entorno virtual: `deactivate`
2. Elimina la carpeta del proyecto
3. (Opcional) Elimina el entorno virtual: `rm -rf venv`

## Soporte

Si encuentras problemas:
1. Revisa los logs en la terminal donde ejecutaste `python app.py`
2. Abre un issue en: https://github.com/MRJonas343/SignSpeak/issues
3. Include:
   - Sistema operativo y versión
   - Versión de Python
   - Mensaje de error completo
   - Pasos para reproducir el problema
