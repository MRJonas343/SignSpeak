# SignSpeak - Capturas de Pantalla y Demostración

## Interfaz Principal

La aplicación SignSpeak presenta una interfaz web moderna y limpia con las siguientes características:

### Layout de la Aplicación

```
╔════════════════════════════════════════════════════════════════╗
║                    🤟 SignSpeak                                ║
║            Traductor de Lengua de Señas a Texto con IA        ║
╠════════════════════════════════════════════════════════════════╣
║                                                                ║
║  ┌─────────────────────┐    ┌──────────────────────────┐     ║
║  │                     │    │ Texto Reconocido ●       │     ║
║  │                     │    │                          │     ║
║  │    Video Stream     │    │  ┌────────────────────┐ │     ║
║  │    con detección    │    │  │                    │ │     ║
║  │    de manos         │    │  │        V           │ │     ║
║  │                     │    │  │                    │ │     ║
║  │  [Mano con puntos   │    │  └────────────────────┘ │     ║
║  │   verdes marcados]  │    │                          │     ║
║  │                     │    │  ┌────────────────────┐ │     ║
║  │  Last Sign: V       │    │  │  🔄 Limpiar Texto  │ │     ║
║  │                     │    │  └────────────────────┘ │     ║
║  └─────────────────────┘    │                          │     ║
║                             │  Señas Reconocidas:      │     ║
║                             │  👆 A - Puño cerrado     │     ║
║                             │  👆 B - Mano abierta     │     ║
║                             │  👆 D - Solo índice      │     ║
║                             │  👆 V - Paz/victoria     │     ║
║                             │  👆 W - Tres dedos       │     ║
║                             │  👆 👍 - Pulgar arriba   │     ║
║                             └──────────────────────────┘     ║
╚════════════════════════════════════════════════════════════════╝
```

## Elementos Visuales

### 1. Header (Gradiente Purple/Blue)
- **Color de fondo**: Linear gradient de #667eea a #764ba2
- **Texto**: Blanco, fuente Segoe UI
- **Título**: 🤟 SignSpeak (tamaño grande)
- **Subtítulo**: "Traductor de Lengua de Señas a Texto con IA"

### 2. Panel de Video (Izquierda)
- **Fondo**: Negro (#000)
- **Contenido**: Stream de video en vivo
- **Overlay**: Landmarks verdes dibujados en la mano
- **Texto superpuesto**: "Last Sign: [LETRA]" en verde
- **Border radius**: 15px
- **Box shadow**: Sombra profunda para efecto 3D

### 3. Panel de Texto (Derecha)

#### Sección de Texto Reconocido
- **Fondo**: Gris claro (#f8f9fa)
- **Título**: "Texto Reconocido" con indicador verde pulsante
- **Display de texto**:
  - Fondo: Blanco
  - Border: Línea punteada morada (#667eea)
  - Texto: Grande (2em), centrado
  - Estado vacío: "Esperando señas..." en gris itálica

#### Controles
- **Botón Limpiar**:
  - Color: Rojo (#dc3545)
  - Texto: Blanco
  - Icono: 🔄
  - Hover: Levanta y agrega sombra

#### Lista de Referencia
- **Fondo**: Azul claro (#e7f3ff)
- **Título**: "Señas Reconocidas:" en morado
- **Items**: Lista con emoji 👆 antes de cada uno
- **Contenido**: Descripción de cada gesto

## Estados de la Aplicación

### Estado 1: Esperando
```
┌────────────────────┐
│                    │
│  Esperando señas...│
│                    │
└────────────────────┘
```
- Texto en gris, itálico
- No hay detección activa

### Estado 2: Detectando
```
┌────────────────────┐
│                    │
│         V          │
│                    │
└────────────────────┘
```
- Letra en negro, grande
- Indicador verde pulsante
- Video muestra landmarks verdes

### Estado 3: Actualizando
```
Video: Last Sign: V
Text Display: V
```
- Sincronización entre video y panel de texto
- Actualización cada 1 segundo

## Responsive Design

### Escritorio (>768px)
```
┌─────────────────────────────────┐
│           Header                │
├─────────────┬───────────────────┤
│             │                   │
│   Video     │   Texto + Info    │
│             │                   │
└─────────────┴───────────────────┘
```

### Móvil (<768px)
```
┌─────────────────┐
│     Header      │
├─────────────────┤
│                 │
│     Video       │
│                 │
├─────────────────┤
│                 │
│  Texto + Info   │
│                 │
└─────────────────┘
```

## Colores de la Paleta

```
Primary Purple:   #667eea
Secondary Purple: #764ba2
Success Green:    #28a745
Danger Red:       #dc3545
Light Gray:       #f8f9fa
Border Gray:      #e9ecef
Text Dark:        #333333
Text Light:       #adb5bd
Info Blue:        #e7f3ff
```

## Tipografía

```
Font Family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif

H1: 2.5em, bold
H2: 1.5em, bold
H3: 1.2em, bold
Body: 1em
Display Text: 2em (texto reconocido)
Button: 1em, bold
```

## Animaciones

### Indicador de Estado
```css
@keyframes pulse {
    0%, 100% { opacity: 1; }
    50%      { opacity: 0.5; }
}
```
- Duración: 2 segundos
- Loop infinito
- Aplicado al círculo verde junto a "Texto Reconocido"

### Hover en Botón
```css
transform: translateY(-2px);
box-shadow: 0 5px 15px rgba(220, 53, 69, 0.3);
```
- Transición suave de 0.3s
- Efecto de elevación

## Flujo Visual del Usuario

1. **Carga**: Usuario ve header con título prominente
2. **Video**: Stream de cámara se carga en panel izquierdo
3. **Detección**: Landmarks verdes aparecen cuando detecta mano
4. **Reconocimiento**: Texto "Last Sign: X" aparece sobre video
5. **Actualización**: Panel derecho actualiza con letra reconocida
6. **Feedback**: Indicador verde pulsa para confirmar sistema activo

## Accesibilidad

- ✓ Colores con buen contraste (WCAG AA)
- ✓ Texto legible (tamaños grandes)
- ✓ Indicadores visuales claros
- ✓ Botones con hover states obvios
- ✓ Layout responsive para diferentes dispositivos

## Performance Visual

- Stream de video a ~20-30 FPS
- Actualización de texto cada 1 segundo
- Sin lag visible en la UI
- Transiciones suaves en todas las animaciones

## Ejemplo de Uso Visual

```
1. Usuario hace gesto "V" (victoria)
   ↓
2. Video muestra mano con 21 puntos verdes
   ↓
3. Overlay: "Last Sign: V"
   ↓
4. Panel derecho actualiza después de ~1 segundo
   ↓
5. Display grande muestra: "V"
   ↓
6. Usuario puede hacer siguiente gesto o limpiar
```

## Notas de Diseño

- **Gradientes**: Agregan modernidad y profesionalismo
- **Sombras**: Crean profundidad y jerarquía visual
- **Border radius**: Suavizan la interfaz (15px en cards principales)
- **Espaciado**: Generoso (20-30px gaps) para claridad
- **Colores**: Purple theme para consistencia de marca
- **Feedback visual**: Múltiples indicadores (overlay, panel, indicator dot)

## Mejoras Futuras de UI

- [ ] Animación de transición entre letras
- [ ] Historial visual de letras anteriores
- [ ] Indicador de confianza (porcentaje de certeza)
- [ ] Tema oscuro/claro
- [ ] Customización de colores
- [ ] Efectos de partículas al reconocer gesto
- [ ] Tutorial interactivo para nuevos usuarios
