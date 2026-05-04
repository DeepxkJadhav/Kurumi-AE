# Kurumi-AE Desktop Mascot

Kurumi-AE is a Windows desktop mascot prototype with a transparent always-on-top overlay, simple AI-like context reactions, text-to-speech, and optional Panda3D 3D model support.

This project does not include copyrighted Kurumi Tokisaki model files. Add your own licensed model under `assets/`.

## Features

- Transparent PyQt5 desktop overlay.
- Always-on-top draggable mascot.
- Fallback 2D mascot when no 3D model is installed.
- Panda3D standalone 3D viewer.
- GLB, GLTF, FBX, and OBJ model discovery.
- Idle motion, speaking mouth animation, fade toggle, and boundary detection.
- Lightweight context reactions from the active desktop window.
- Windows text-to-speech wrapper that fails quietly if speech is unavailable.

## Quick Start

Install dependencies:

```powershell
pip install -r requirements.txt
```

Run the overlay:

```powershell
python main.py
```

## Optional AI Setup

Kurumi-AE can use an OpenAI-compatible chat endpoint for short context reactions when you double-click her. Create a private `.env` file from `.env.example` and add your key there:

```powershell
copy .env.example .env
notepad .env
```

If your key starts with `sk-or-v1-`, Kurumi-AE will default to the OpenRouter-compatible base URL and model. Keep `.env` private.

## Natural Voice

Kurumi-AE can use cloud-generated speech so she does not sound like the built-in robotic Windows voice. This uses an OpenAI-compatible `/audio/speech` endpoint and falls back to Windows TTS if unavailable.

```text
KURUMI_AE_NATURAL_TTS=1
KURUMI_AE_TTS_BASE_URL=https://api.openai.com/v1
KURUMI_AE_TTS_MODEL=gpt-4o-mini-tts
KURUMI_AE_TTS_VOICE=shimmer
```

If natural TTS is off or unsupported by your provider, Kurumi-AE automatically prefers the first installed Windows female voice. You can force one with `KURUMI_AE_VOICE_NAME=Microsoft Zira Desktop`.

Run the model setup helper:

```powershell
python get_model.py
```

Run the standalone 3D viewer:

```powershell
python run_panda.py
python run_panda.py assets/kurumi_model.glb
```

## Model Placement

Preferred:

```text
assets/kurumi_model.glb
```

Also supported:

```text
assets/kurumi_model.gltf
assets/kurumi_model.fbx
assets/kurumi_model.obj
```

GLB is recommended for the best balance of quality and performance.

## Controls

- Drag the mascot with the left mouse button.
- Double-click to make Kurumi-AE react to the active window.
- Right-click for actions: speak, fade, 3D viewer hint, quit.

## File Structure

```text
Kurumi-AE/
├── main.py
├── window.py
├── run_panda.py
├── get_model.py
├── download_model.py
├── 3D_MODEL_SETUP.md
├── requirements.txt
├── assets/
└── core/
    ├── state.py
    ├── perception.py
    ├── decision.py
    ├── voice.py
    └── loop.py
```

## Troubleshooting

If no 3D model appears, place a licensed model at `assets/kurumi_model.glb` or run:

```powershell
python get_model.py
```

If the overlay opens but the 3D viewer does not, try:

```powershell
python run_panda.py
```

If speech does not play, the app will continue running. The default speech path uses Windows speech synthesis through PowerShell.

## License Notes

Kurumi Tokisaki and Date A Live belong to their respective rights holders. This app is a fan-project shell and does not redistribute character model assets. Check model licenses before use, especially for public release or commercial use.
