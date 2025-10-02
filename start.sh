#!/bin/bash
# SignSpeak Quick Start Script

echo "================================="
echo "   SignSpeak - Quick Start"
echo "================================="
echo ""

# Check Python version
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 no está instalado"
    echo "Por favor instala Python 3.8 o superior"
    exit 1
fi

PYTHON_VERSION=$(python3 --version | cut -d' ' -f2 | cut -d'.' -f1,2)
echo "✓ Python detectado: $(python3 --version)"

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo ""
    echo "📦 Creando entorno virtual..."
    python3 -m venv venv
    echo "✓ Entorno virtual creado"
fi

# Activate virtual environment
echo ""
echo "🔄 Activando entorno virtual..."
source venv/bin/activate
echo "✓ Entorno virtual activado"

# Install dependencies
echo ""
echo "📥 Instalando dependencias..."
if [ -f "requirements.txt" ]; then
    pip install --upgrade pip -q
    pip install -r requirements.txt
    if [ $? -eq 0 ]; then
        echo "✓ Dependencias instaladas"
    else
        echo "❌ Error al instalar dependencias"
        echo "Intenta instalarlas manualmente: pip install -r requirements.txt"
        exit 1
    fi
else
    echo "❌ requirements.txt no encontrado"
    exit 1
fi

# Start the application
echo ""
echo "================================="
echo "🚀 Iniciando SignSpeak..."
echo "================================="
echo ""
echo "La aplicación estará disponible en:"
echo "  👉 http://localhost:5000"
echo ""
echo "Presiona Ctrl+C para detener el servidor"
echo ""

python3 app.py
