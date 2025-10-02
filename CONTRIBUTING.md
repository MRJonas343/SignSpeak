# Guía de Contribución - SignSpeak

¡Gracias por tu interés en contribuir a SignSpeak! Este documento te guiará en el proceso de contribución.

## 🌟 Formas de Contribuir

- 🐛 Reportar bugs
- 💡 Sugerir nuevas características
- 📝 Mejorar documentación
- 🎨 Mejorar diseño UI/UX
- 🔧 Implementar características
- 🧪 Agregar tests
- 🌍 Traducir a otros idiomas

## 🚀 Proceso de Contribución

### 1. Fork y Clone

```bash
# Fork el repositorio en GitHub
# Luego clona tu fork
git clone https://github.com/TU_USUARIO/SignSpeak.git
cd SignSpeak
```

### 2. Crear Branch

```bash
# Crea un branch descriptivo
git checkout -b feature/nueva-caracteristica
# o
git checkout -b fix/corregir-bug
```

### 3. Configurar Entorno

```bash
# Crea entorno virtual
python -m venv venv

# Activa el entorno
source venv/bin/activate  # Linux/Mac
# o
venv\Scripts\activate  # Windows

# Instala dependencias
pip install -r requirements.txt
```

### 4. Hacer Cambios

- Escribe código limpio y bien documentado
- Sigue las convenciones de estilo del proyecto
- Agrega comentarios cuando sea necesario
- Actualiza documentación si es relevante

### 5. Probar Cambios

```bash
# Prueba tu código
python test_gesture_logic.py

# Ejecuta la aplicación
python app.py

# Verifica que todo funcione correctamente
```

### 6. Commit

```bash
# Agrega los cambios
git add .

# Commit con mensaje descriptivo
git commit -m "feat: agregar reconocimiento de letra E"
# o
git commit -m "fix: corregir detección de pulgar"
```

#### Convenciones de Commit

Usa prefijos claros:
- `feat:` - Nueva característica
- `fix:` - Corrección de bug
- `docs:` - Cambios en documentación
- `style:` - Formato, estilo (no afecta código)
- `refactor:` - Refactorización de código
- `test:` - Agregar o modificar tests
- `chore:` - Tareas de mantenimiento

### 7. Push y Pull Request

```bash
# Push a tu fork
git push origin feature/nueva-caracteristica
```

Luego en GitHub:
1. Ve a tu fork
2. Click en "New Pull Request"
3. Selecciona tu branch
4. Describe tus cambios detalladamente
5. Submit el PR

## 📋 Checklist para Pull Requests

Antes de enviar tu PR, verifica:

- [ ] El código funciona correctamente
- [ ] No hay errores de sintaxis
- [ ] Los tests pasan (si aplica)
- [ ] La documentación está actualizada
- [ ] El commit message es descriptivo
- [ ] No hay archivos innecesarios (logs, cache, etc.)
- [ ] El código sigue las convenciones del proyecto

## 🎨 Guía de Estilo

### Python

```python
# Bueno ✓
def recognize_gesture(hand_landmarks):
    """
    Recognizes hand gesture from landmarks
    
    Args:
        hand_landmarks: MediaPipe hand landmarks object
    
    Returns:
        str: Recognized gesture or None
    """
    landmarks = hand_landmarks.landmark
    # ... código ...
    return gesture

# Malo ✗
def r(h):
    l=h.landmark
    # ... código sin documentación ...
    return g
```

### Convenciones

- Usa snake_case para funciones y variables
- Usa PascalCase para clases
- 4 espacios de indentación
- Máximo 80-100 caracteres por línea
- Docstrings para funciones públicas
- Comentarios para lógica compleja

### HTML/CSS

```html
<!-- Bueno ✓ -->
<div class="video-section">
    <div class="video-container">
        <!-- contenido -->
    </div>
</div>

<!-- Malo ✗ -->
<div class="vs"><div class="vc">
<!-- contenido -->
</div></div>
```

- Usa kebab-case para clases CSS
- Indentación consistente
- Agrupa estilos relacionados
- Usa comentarios para secciones

### JavaScript

```javascript
// Bueno ✓
async function updateDisplay() {
    const display = document.getElementById('textDisplay');
    if (recognizedText) {
        display.textContent = recognizedText;
    }
}

// Malo ✗
function u(){let d=document.getElementById('textDisplay');d.textContent=r;}
```

- Usa camelCase para variables y funciones
- Usa const/let (no var)
- Código autodocumentado
- Comentarios para lógica compleja

## 🧪 Testing

### Tests Existentes

```bash
# Ejecutar tests
python test_gesture_logic.py
```

### Agregar Nuevos Tests

Si agregas nuevos gestos, agrega tests:

```python
def test_new_gesture():
    """Test para nuevo gesto"""
    landmarks = create_test_landmarks(...)
    result = recognize_gesture_test(landmarks)
    assert result == "EXPECTED", f"Expected 'EXPECTED', got '{result}'"
    print("✓ Test passed")
```

## 📝 Documentación

### Estructura de Documentación

```
README.md           - Descripción general y quick start
INSTALL.md         - Instrucciones detalladas de instalación
USAGE.md           - Guía de uso para usuarios finales
ARCHITECTURE.md    - Documentación técnica
CONTRIBUTING.md    - Esta guía
SCREENSHOTS.md     - Visual mockups y ejemplos
```

### Actualizar Documentación

Si tu cambio afecta:
- **Instalación**: Actualiza INSTALL.md
- **Uso**: Actualiza USAGE.md
- **Arquitectura**: Actualiza ARCHITECTURE.md
- **Nuevas características**: Actualiza README.md

## 🐛 Reportar Bugs

### Template de Bug Report

```markdown
**Descripción del Bug**
Descripción clara del problema

**Para Reproducir**
1. Paso 1
2. Paso 2
3. Ver error

**Comportamiento Esperado**
Lo que debería suceder

**Comportamiento Actual**
Lo que está sucediendo

**Screenshots**
Si aplica, agrega capturas

**Ambiente**
- OS: [Windows/Linux/Mac]
- Python: [version]
- Browser: [si es UI]

**Logs**
Pega logs o mensajes de error
```

## 💡 Sugerir Características

### Template de Feature Request

```markdown
**Descripción de la Característica**
Descripción clara de la nueva feature

**Problema que Resuelve**
¿Qué problema soluciona?

**Solución Propuesta**
¿Cómo funcionaría?

**Alternativas Consideradas**
Otras formas de resolver el problema

**Contexto Adicional**
Cualquier otra información relevante
```

## 🎯 Áreas de Enfoque

### Prioridad Alta

1. **Más Gestos**: Expandir alfabeto completo (A-Z)
2. **Precisión**: Mejorar algoritmo de reconocimiento
3. **Performance**: Optimizar velocidad de detección
4. **Documentación**: Más ejemplos y tutoriales

### Prioridad Media

1. **Text-to-Speech**: Agregar síntesis de voz
2. **Historial**: Guardar traducciones anteriores
3. **Export**: Descargar texto a archivo
4. **Configuración**: Ajustes personalizables

### Prioridad Baja

1. **Temas**: Dark/Light mode
2. **Idiomas**: Internacionalización
3. **Estadísticas**: Métricas de uso
4. **Gamificación**: Modo de práctica

## 🔧 Desarrollo Avanzado

### Agregar Nuevo Gesto

1. Analiza la posición de dedos para el gesto
2. Agrega lógica en `recognize_gesture()`
3. Actualiza lista en `index.html`
4. Agrega test en `test_gesture_logic.py`
5. Documenta en `USAGE.md`

Ejemplo:

```python
# En app.py, función recognize_gesture()
elif extended_fingers == 4 and not thumb_extended:
    return "E"  # Cuatro dedos sin pulgar
```

### Mejorar Precisión

Opciones:
1. Ajustar thresholds de detección
2. Aumentar tamaño del buffer
3. Agregar verificaciones adicionales
4. Entrenar modelo ML personalizado

### Optimizar Performance

```python
# Reducir resolución de video
camera.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# Ajustar confianza de MediaPipe
hands = mp_hands.Hands(
    min_detection_confidence=0.5,  # Menor = más rápido
    min_tracking_confidence=0.5
)

# Reducir calidad de JPEG
cv2.imencode('.jpg', frame, [cv2.IMWRITE_JPEG_QUALITY, 70])
```

## 🤝 Code Review

Cuando revisas PRs de otros:

- ✓ Sé constructivo y amable
- ✓ Prueba el código localmente
- ✓ Verifica que cumpla las guidelines
- ✓ Sugiere mejoras específicas
- ✓ Aprueba si todo está bien

## 🌍 Comunidad

### Comunicación

- **Issues**: Para bugs y features
- **Discussions**: Para preguntas generales
- **Pull Requests**: Para cambios de código

### Código de Conducta

- Sé respetuoso con todos
- Acepta críticas constructivas
- Enfócate en el código, no en la persona
- Ayuda a otros contributors
- Mantén un ambiente positivo

## 📚 Recursos Útiles

### Para Nuevos Contributors

- [Git Basics](https://git-scm.com/book/en/v2/Getting-Started-Git-Basics)
- [Python Style Guide (PEP 8)](https://www.python.org/dev/peps/pep-0008/)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [MediaPipe Hands](https://google.github.io/mediapipe/solutions/hands.html)

### Para Issues Específicos

- OpenCV: https://docs.opencv.org/
- MediaPipe: https://google.github.io/mediapipe/
- Flask: https://flask.palletsprojects.com/
- HTML/CSS: https://developer.mozilla.org/

## ❓ Preguntas

Si tienes preguntas:
1. Revisa la documentación existente
2. Busca en Issues cerrados
3. Abre un nuevo Issue con tag `question`
4. Se paciente, la comunidad te ayudará

## 🎉 Reconocimientos

Todos los contributors serán:
- Listados en README.md
- Mencionados en release notes
- Parte de la comunidad SignSpeak

---

¡Gracias por contribuir a SignSpeak! 🤟
