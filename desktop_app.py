# -*- coding: utf-8 -*-
"""Kurumi-AE Dedicated Native Desktop Application Runner."""

import os
import sys
import time
import urllib.request
import subprocess

PORT = 48911
URL = f"http://127.0.0.1:{PORT}/"
TITLE = "Kurumi-AE • 刻々帝 (Zafkiel)"
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

def is_server_running() -> bool:
    try:
        req = urllib.request.Request(URL, method="GET")
        with urllib.request.urlopen(req, timeout=1.5) as resp:
            return resp.status in (200, 405)
    except Exception:
        return False

def ensure_server():
    if is_server_running():
        print("[Kurumi-AE] Backend service is already active on port 48911.")
        return
    print("[Kurumi-AE] Starting backend server in background...")
    # Use uv run python launcher.py
    uv_bin = os.path.expanduser(r"~\.local\bin\uv.exe")
    if not os.path.isfile(uv_bin):
        uv_bin = "uv"
    subprocess.Popen(
        [uv_bin, "run", "python", "launcher.py"],
        cwd=PROJECT_ROOT,
        creationflags=subprocess.CREATE_NO_WINDOW if os.name == "nt" else 0
    )
    for i in range(35):
        time.sleep(1)
        if is_server_running():
            print(f"[Kurumi-AE] Backend online after {i+1}s.")
            return
    print("[Kurumi-AE] Notice: Continuing to window launch...")

def run_desktop():
    ensure_server()

    # Strategy 1: Native pywebview (Edge WebView2) - true standalone desktop window
    try:
        import webview
        print(f"[Kurumi-AE] Summoning Native Desktop Window: {TITLE}")
        webview.create_window(
            title=TITLE,
            url=URL,
            width=1380,
            height=890,
            min_size=(960, 680),
            background_color="#0a0507",
            text_select=True,
            zoomable=True,
            focus=True
        )
        webview.start(debug=False)
        return
    except Exception as exc:
        print(f"[Kurumi-AE] pywebview launch note: {exc}. Trying dedicated application mode...")

    # Strategy 2: Isolated Edge/Chrome App Mode with isolated profile directory
    # Passing --user-data-dir ensures it NEVER merges into normal browser tabs
    profile_dir = os.path.expandvars(r"%LOCALAPPDATA%\Kurumi-AE\desktop-profile")
    os.makedirs(profile_dir, exist_ok=True)

    browser_candidates = [
        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        os.path.expandvars(r"%LOCALAPPDATA%\Google\Chrome\Application\chrome.exe"),
    ]

    for exe in browser_candidates:
        if os.path.isfile(exe):
            print(f"[Kurumi-AE] Summoning Isolated Desktop App via {os.path.basename(exe)}...")
            cmd = [
                exe,
                f"--user-data-dir={profile_dir}",
                f"--app={URL}",
                "--window-size=1380,890",
                "--no-first-run",
                "--no-default-browser-check"
            ]
            proc = subprocess.Popen(cmd)
            proc.wait()
            return

    # Ultimate fallback: system default open
    os.system(f'start "" "{URL}"')

if __name__ == "__main__":
    run_desktop()
