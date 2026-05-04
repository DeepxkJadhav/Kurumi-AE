from __future__ import annotations

import shutil
from pathlib import Path
from urllib.parse import urlparse

import requests


ASSETS_DIR = Path("assets")
SUPPORTED_EXTENSIONS = {".glb", ".gltf", ".fbx", ".obj"}


def ensure_assets_dir() -> None:
    ASSETS_DIR.mkdir(exist_ok=True)


def validate_extension(path: Path) -> None:
    if path.suffix.lower() not in SUPPORTED_EXTENSIONS:
        raise ValueError(f"Unsupported model format: {path.suffix}")


def copy_local_model(source: Path) -> Path:
    if not source.exists():
        raise FileNotFoundError(source)
    validate_extension(source)
    ensure_assets_dir()
    target = ASSETS_DIR / f"kurumi_model{source.suffix.lower()}"
    shutil.copy2(source, target)
    return target


def download_direct_url(url: str) -> Path:
    parsed = urlparse(url)
    suffix = Path(parsed.path).suffix.lower()
    if suffix not in SUPPORTED_EXTENSIONS:
        raise ValueError("Direct URL must end in .glb, .gltf, .fbx, or .obj")
    ensure_assets_dir()
    target = ASSETS_DIR / f"kurumi_model{suffix}"
    with requests.get(url, stream=True, timeout=30) as response:
        response.raise_for_status()
        with target.open("wb") as file:
            for chunk in response.iter_content(chunk_size=1024 * 512):
                if chunk:
                    file.write(chunk)
    return target


def confirm_license() -> bool:
    print("Only continue if you have permission to use this model.")
    print("Check the model license, especially for commercial use or redistribution.")
    return input("Type YES to confirm you have rights to use it: ").strip() == "YES"


def main() -> int:
    print("Kurumi-AE model setup")
    print("1. Copy a local model file")
    print("2. Download from a direct model URL")
    print("3. Show recommended search guidance")
    choice = input("Choose 1, 2, or 3: ").strip()

    if choice == "3":
        print("Search Sketchfab or another source for a legally usable GLB/GLTF model.")
        print("Recommended query: Kurumi Tokisaki GLB")
        print("Place the file at assets/kurumi_model.glb")
        return 0

    if not confirm_license():
        print("Cancelled. No model was downloaded or copied.")
        return 1

    try:
        if choice == "1":
            target = copy_local_model(Path(input("Local model path: ").strip().strip('"')))
        elif choice == "2":
            target = download_direct_url(input("Direct model URL: ").strip())
        else:
            print("Unknown choice.")
            return 1
    except Exception as exc:
        print(f"Model setup failed: {exc}")
        return 1

    print(f"Model ready: {target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
