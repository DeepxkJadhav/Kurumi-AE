<p align="center">
  <img src="./assets/kurumi-tokisaki-date-a-live.gif" width="380" alt="Kurumi laughing GIF">
</p>

<p align="center">
  <img src="./assets/kurumi-laugh.gif" width="420" alt="Kurumi Tokisaki">
</p>

# 🌸 Kurumi-AE Desktop Mascot

An AI-powered desktop mascot application featuring **Kurumi Tokisaki from Date A Live**, now with **3D model support**!

## Features

✨ **3D Model Support**
- Full 3D Kurumi Tokisaki model
- Better performance than DesktopMate
- Multiple animation support
- Transparent background (wallpaper mode)

🎭 **Intelligent Behavior**
- Context-aware responses
- Voice interaction (text-to-speech)
- Dynamic state management
- Idle animations with blinking

🎨 **Customization**
- Easy model switching (GLB, GLTF, FBX formats)
- Window positioning and sizing
- Fade in/out animations
- Screen boundary detection

## Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Get Your 3D Model
```bash
python get_model.py
```
Or manually:
```bash
python download_model.py
```

This guides you to download a Kurumi 3D model from:
- **Sketchfab** (free & paid)
- **Direct URL** (any source)
- **Local file** (manual)

### 3. Run the Application
```bash
python main.py
```

### 3b. (Optional) Run standalone 3D viewer
If the 3D model doesn't appear inside the PyQt window, run the lightweight Panda3D viewer which opens a borderless always-on-top window showing the model:

```bash
python run_panda.py
# or specify a model explicitly
python run_panda.py assets/kurumi_model.glb
```

## File Structure

```
Kurumi-AE/
├── main.py                 # Main application
├── window.py              # 3D model rendering (updated)
├── get_model.py           # Quick model setup helper
├── download_model.py      # Advanced model downloader
├── 3D_MODEL_SETUP.md      # Detailed 3D setup guide
├── requirements.txt       # Python dependencies
├── assets/
│   ├── kurumi.png        # Fallback 2D image
│   └── kurumi_model/     # 3D model directory
│       └── kurumi_model.glb
└── core/
    ├── state.py          # Application state management
    ├── perception.py     # Screen/window detection
    ├── decision.py       # AI decision engine
    ├── voice.py          # Text-to-speech
    └── loop.py           # Main event loop
```

## 3D Model Setup Guide

### Recommended Models
1. **Sketchfab** (easiest)
   - Search: "Kurumi Tokisaki"
   - Format: GLB (recommended)
   - License: Check commercial use

2. **CG Trading** (high quality)
   - More detailed models available
   - Professional quality

### Format Support
| Format | Quality | Performance | Recommended |
|--------|---------|-------------|-------------|
| GLB    | High    | Excellent   | ✅ **YES**  |
| GLTF   | High    | Good        | ✅ YES     |
| FBX    | Very High | Fair      | Good       |
| OBJ    | Medium  | Fair        | Legacy     |

### Model Placement
```
Place your model file in one of these locations:
- assets/kurumi_model.glb      ← Recommended
- assets/kurumi_model.gltf
- assets/kurumi_model.fbx
- assets/kurumi_model.obj
```

## Configuration

Edit `main.py` to customize:
- Default window position
- Model rotation speed
- Animation timings
- Voice settings

## Troubleshooting

### Model Not Found?
```
⚠️  Model not found at assets/kurumi_model.*
```
**Solution**: Run `python download_model.py` or place model manually in `assets/` folder

### Performance Issues?
- Use GLB format instead of FBX
- Reduce model complexity
- Disable unnecessary animations

### Import Errors?
Install missing packages:
```bash
pip install panda3d requests PyQt5 psutil pygetwindow pyautogui
```

## Advanced Features

### Custom Animations
Edit `window.py` to add custom behaviors:
```python
def animate_model(self):
    # Add rotation, bounce, or other animations
    self.rotation_angle += speed
```

### Voice Customization
Edit `core/voice.py` for different TTS engines or voice properties

### AI Behavior
Modify `core/decision.py` to change mascot responses and behaviors

## Requirements

- **Python 3.8+**
- **PyQt5** - GUI framework
- **Panda3D** - 3D graphics engine
- **psutil** - System monitoring
- **pygetwindow** - Window detection
- **pyautogui** - Input automation

## Why 3D Over 2D?

### Advantages of 3D Models
✅ More expressive animations
✅ Professional appearance
✅ Better performance than DesktopMate
✅ Smooth rotations and transitions
✅ Support for armature-based animations
✅ Better community support (more models available)

### Why Not DesktopMate?
- Outdated technology
- Limited animation capabilities
- Smaller model library
- Less active development

## License & Credits

This project uses:
- **PyQt5** - Qt bindings for Python
- **Panda3D** - Free 3D engine
- **Date A Live** - Kurumi Tokisaki character

⚠️ **Important**: Ensure you have rights to use the 3D model you download. Check the license carefully before commercial use.

## Contributing

Feel free to submit issues or feature requests!

---

## Troubleshooting Reference

For detailed setup help, see [3D_MODEL_SETUP.md](3D_MODEL_SETUP.md)

For common issues, run:
```bash
python get_model.py
```

---

**Created with ❤️ for Kurumi fans**

**Version**: 2.0 (3D Edition)
**Last Updated**: January 2026

