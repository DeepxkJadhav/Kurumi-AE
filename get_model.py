from __future__ import annotations

from pathlib import Path

from download_model import ASSETS_DIR, SUPPORTED_EXTENSIONS, main as download_main


def existing_model() -> Path | None:
    for suffix in (".glb", ".gltf", ".fbx", ".obj"):
        candidate = ASSETS_DIR / f"kurumi_model{suffix}"
        if candidate.exists():
            return candidate
    if ASSETS_DIR.exists():
        for path in ASSETS_DIR.rglob("*"):
            if path.suffix.lower() in SUPPORTED_EXTENSIONS:
                return path
    return None


def main() -> int:
    model = existing_model()
    if model:
        print(f"Existing model found: {model}")
        return 0
    print("No Kurumi-AE 3D model found.")
    print("This helper will open the guided model setup.")
    return download_main()


if __name__ == "__main__":
    raise SystemExit(main())
