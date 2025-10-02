# Guía de Uso - SignSpeak

## Inicio Rápido

1. **Iniciar la aplicación**
   ```bash
   python app.py
   ```

2. **Abrir en navegador**
   - Ve a http://localhost:5000
   - Permite acceso a la cámara cuando se solicite

3. **Comenzar a traducir**
   - Posiciona tu mano frente a la cámara
   - Realiza las señas reconocidas
   - El texto aparecerá en tiempo real

## Señas Reconocidas

El MVP actual reconoce 6 gestos básicos:

### 1. Letra A - Puño Cerrado
- **Cómo hacerla**: Cierra todos los dedos formando un puño
- **Uso**: Representa la letra "A" en el alfabeto de señas

### 2. Letra B - Mano Abierta
- **Cómo hacerla**: Extiende todos los dedos completamente
- **Uso**: Representa la letra "B"

### 3. Letra D - Dedo Índice
- **Cómo hacerla**: Extiende solo el dedo índice, mantén los demás cerrados
- **Uso**: Representa la letra "D"

### 4. Letra V - Victoria/Paz
- **Cómo hacerla**: Extiende el índice y el medio en forma de "V"
- **Uso**: Representa la letra "V" o el signo de paz/victoria

### 5. Letra W - Tres Dedos
- **Cómo hacerla**: Extiende índice, medio y anular
- **Uso**: Representa la letra "W"

### 6. Thumbs Up - Pulgar Arriba
- **Cómo hacerla**: Extiende solo el pulgar hacia arriba
- **Uso**: Gesto universal de aprobación

## Consejos para Mejor Reconocimiento

### Iluminación
- ✓ Usa iluminación frontal o lateral uniforme
- ✓ Evita luz directa detrás de ti (contraluz)
- ✗ No uses en lugares muy oscuros

### Distancia de la Cámara
- **Óptima**: 30-60 cm (12-24 pulgadas)
- **Mínima**: 20 cm
- **Máxima**: 1 metro

### Fondo
- ✓ Fondo simple y uniforme
- ✓ Color contrastante con tu piel
- ✗ Evita fondos muy ocupados o con muchos colores

### Posición de la Mano
- Mantén la palma hacia la cámara
- Centra tu mano en el video
- Mantén el gesto estable por 1-2 segundos
- No muevas la mano demasiado rápido

### Velocidad
- El sistema actualiza el reconocimiento cada 1.5 segundos
- Mantén cada gesto por al menos 2 segundos
- Espera a que aparezca el texto antes de cambiar de gesto

## Interfaz de Usuario

### Elementos de la Pantalla

1. **Video en Vivo**
   - Muestra el feed de tu cámara
   - Los puntos verdes indican detección de mano
   - Texto superpuesto muestra última seña detectada

2. **Panel de Texto Reconocido**
   - Indicador verde pulsante: sistema activo
   - Texto grande: última seña reconocida
   - Actualización en tiempo real

3. **Botón Limpiar Texto**
   - Resetea el texto reconocido
   - No afecta la detección continua

4. **Lista de Señas**
   - Referencia rápida de gestos reconocidos
   - Útil mientras practicas

## Flujo de Trabajo Típico

### Práctica Básica
1. Inicia la aplicación
2. Verifica que la cámara funcione
3. Practica cada gesto uno por uno
4. Observa la detección en tiempo real
5. Limpia y practica de nuevo

### Deletreo de Palabras
1. Planifica la palabra (ej: "BAD")
2. Haz el gesto para "B"
3. Espera confirmación (1-2 segundos)
4. Haz el gesto para "A"
5. Espera confirmación
6. Haz el gesto para "D"
7. Limpia para una nueva palabra

### Demostración
1. Prepara ejemplos claros
2. Asegúrate de buena iluminación
3. Practica la secuencia antes
4. Mantén gestos claros y pausados
5. Usa el panel de referencia si es necesario

## Limitaciones Actuales

- ⚠️ Solo reconoce una mano a la vez
- ⚠️ Vocabulario limitado (6 gestos)
- ⚠️ Requiere gestos estables (no movimiento rápido)
- ⚠️ No reconoce frases o palabras completas
- ⚠️ Sensible a condiciones de iluminación

## Solución de Problemas Comunes

### "No se detecta mi mano"
- Verifica que la cámara tenga permiso
- Mejora la iluminación
- Acerca más la mano a la cámara
- Prueba con un fondo más simple

### "El reconocimiento es incorrecto"
- Mantén el gesto más tiempo
- Asegúrate de posicionar los dedos correctamente
- Verifica la iluminación
- Consulta la lista de referencia

### "La detección es muy lenta"
- Cierra otras aplicaciones
- Actualiza drivers de la cámara
- Verifica que tu CPU no esté sobrecargada
- Reduce la calidad del video en configuración

### "El texto no se actualiza"
- Verifica la conexión entre frontend y backend
- Revisa la consola del navegador (F12)
- Reinicia la aplicación

## Atajos y Trucos

1. **Modo práctica**: Mantén abierta la lista de señas como referencia
2. **Calibración**: Prueba cada gesto varias veces al inicio
3. **Ambiente óptimo**: Prepara tu espacio antes de usar
4. **Sesiones cortas**: Practica 5-10 minutos para empezar
5. **Feedback visual**: Observa los landmarks (puntos verdes) para verificar detección

## Próximos Pasos

Una vez domines estos gestos básicos:
1. Espera actualizaciones con más letras
2. Comparte feedback para mejorar la detección
3. Propón nuevos gestos o funcionalidades
4. Contribuye al proyecto en GitHub

## Soporte y Feedback

- **Issues**: https://github.com/MRJonas343/SignSpeak/issues
- **Documentación**: Ver README.md
- **Instalación**: Ver INSTALL.md

¡Disfruta usando SignSpeak! 🤟
