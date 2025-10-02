@echo off
REM SignSpeak Quick Start Script for Windows

echo =================================
echo    SignSpeak - Quick Start
echo =================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo X Python no esta instalado
    echo Por favor instala Python 3.8 o superior desde https://www.python.org/downloads/
    pause
    exit /b 1
)

echo √ Python detectado
python --version

REM Check if virtual environment exists
if not exist "venv\" (
    echo.
    echo Creando entorno virtual...
    python -m venv venv
    echo √ Entorno virtual creado
)

REM Activate virtual environment
echo.
echo Activando entorno virtual...
call venv\Scripts\activate.bat
echo √ Entorno virtual activado

REM Install dependencies
echo.
echo Instalando dependencias...
if exist "requirements.txt" (
    python -m pip install --upgrade pip -q
    pip install -r requirements.txt
    if errorlevel 1 (
        echo X Error al instalar dependencias
        echo Intenta instalarlas manualmente: pip install -r requirements.txt
        pause
        exit /b 1
    )
    echo √ Dependencias instaladas
) else (
    echo X requirements.txt no encontrado
    pause
    exit /b 1
)

REM Start the application
echo.
echo =================================
echo Iniciando SignSpeak...
echo =================================
echo.
echo La aplicacion estara disponible en:
echo   http://localhost:5000
echo.
echo Presiona Ctrl+C para detener el servidor
echo.

python app.py
pause
