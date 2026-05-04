# 3D Model Setup

Kurumi-AE can load user-provided 3D models from the `assets/` folder. The app intentionally does not ship copyrighted character models.

## Recommended Format

| Format | Quality | Performance | Recommendation |
| --- | --- | --- | --- |
| GLB | High | Excellent | Best default |
| GLTF | High | Good | Good |
| FBX | Very high | Fair | Secondary |
| OBJ | Medium | Fair | Legacy |

Use GLB first when possible.

## Placement

Put one model in one of these locations:

```text
assets/kurumi_model.glb
assets/kurumi_model.gltf
assets/kurumi_model.fbx
assets/kurumi_model.obj
```

The app searches those names first, then scans `assets/` for any supported model.

## Guided Setup

```powershell
python get_model.py
```

The helper can copy a local model or download from a direct URL. It requires you to confirm that you have permission to use the model before any copy or download happens.

## Suggested Sources

- Sketchfab: search for legally usable GLB/GLTF models.
- Paid model stores: check redistribution and commercial-use terms.
- Your own converted model: export as GLB where possible.

## Common Problems

Model not found:

```text
Fallback 2D mode - add assets/kurumi_model.glb
```

Fix: place a supported model under `assets/`.

Model loads slowly:

- Prefer GLB over FBX.
- Use a lower-poly model.
- Reduce texture sizes.

Model appears too large or too small:

- Start with `run_panda.py`.
- Adjust scale in `run_panda.py` after confirming the model loads.

Licensing:

- Do not redistribute models unless the license allows it.
- Fan models may still be restricted even when free to download.
