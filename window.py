from __future__ import annotations

import math
from pathlib import Path

from PyQt5.QtCore import QPoint, QRect, Qt, QTimer
from PyQt5.QtGui import QColor, QPainter, QPen
from PyQt5.QtWidgets import QApplication, QLabel, QMenu, QWidget

from core.ai import AIClient
from core.config import AppConfig
from core.decision import build_context_response
from core.perception import read_desktop_context
from core.state import MascotMood, MascotState
from core.voice import VoiceEngine


MODEL_EXTENSIONS = (".glb", ".gltf", ".fbx", ".obj")


def find_model(assets_dir: Path | str = "assets") -> Path | None:
    root = Path(assets_dir)
    preferred = [root / f"kurumi_model{ext}" for ext in MODEL_EXTENSIONS]
    for candidate in preferred:
        if candidate.exists():
            return candidate
    if root.exists():
        for ext in MODEL_EXTENSIONS:
            matches = sorted(root.rglob(f"*{ext}"))
            if matches:
                return matches[0]
    return None


class KurumiOverlay(QWidget):
    def __init__(self, state: MascotState, voice: VoiceEngine, config: AppConfig | None = None) -> None:
        super().__init__()
        self.state = state
        self.voice = voice
        self.ai = AIClient(config) if config else None
        self.drag_offset: QPoint | None = None
        self.phase = 0.0
        self.model_path = find_model()

        self.setWindowTitle("Kurumi-AE")
        self.setWindowFlags(
            Qt.FramelessWindowHint
            | Qt.WindowStaysOnTopHint
            | Qt.Tool
        )
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.setMouseTracking(True)
        self.setGeometry(self.state.x, self.state.y, self.state.width, self.state.height)
        self.setWindowOpacity(self.state.opacity)

        self.label = QLabel(self)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet(
            "QLabel { color: white; background: rgba(20, 0, 10, 150); "
            "border: 1px solid rgba(255, 110, 170, 160); border-radius: 8px; "
            "padding: 7px; font: 10pt 'Segoe UI'; }"
        )
        self.label.setWordWrap(True)

        self.timer = QTimer(self)
        self.timer.setInterval(16)
        self.timer.timeout.connect(self.animate)
        self.timer.start()

    def set_state(self, state: MascotState) -> None:
        self.state = state
        self.label.setText(state.message)
        self.update()

    def animate(self) -> None:
        self.phase += 0.045
        self.keep_inside_screen()
        self.update()

    def resizeEvent(self, event) -> None:  # noqa: N802
        self.label.setGeometry(18, self.height() - 78, self.width() - 36, 54)
        super().resizeEvent(event)

    def mousePressEvent(self, event) -> None:  # noqa: N802
        if event.button() == Qt.LeftButton:
            self.drag_offset = event.globalPos() - self.frameGeometry().topLeft()
        elif event.button() == Qt.RightButton:
            self.open_context_menu(event.globalPos())

    def mouseMoveEvent(self, event) -> None:  # noqa: N802
        if self.drag_offset is not None and event.buttons() & Qt.LeftButton:
            self.move(event.globalPos() - self.drag_offset)

    def mouseReleaseEvent(self, event) -> None:  # noqa: N802
        self.drag_offset = None
        self.keep_inside_screen()

    def mouseDoubleClickEvent(self, event) -> None:  # noqa: N802
        if event.button() == Qt.LeftButton:
            self.speak_context_response()

    def open_context_menu(self, pos: QPoint) -> None:
        menu = QMenu(self)
        speak_action = menu.addAction("Say something")
        fade_action = menu.addAction("Fade out / in")
        viewer_action = menu.addAction("Open 3D viewer")
        menu.addSeparator()
        quit_action = menu.addAction("Quit")

        selected = menu.exec_(pos)
        if selected == speak_action:
            self.speak_context_response()
        elif selected == fade_action:
            self.toggle_fade()
        elif selected == viewer_action:
            self.launch_viewer_hint()
        elif selected == quit_action:
            QApplication.quit()

    def speak_context_response(self) -> None:
        context = read_desktop_context()
        response = self.ai.context_response(context) if self.ai else build_context_response(context)
        self.state.mark_spoken(response)
        self.set_state(self.state)
        self.voice.speak(response)

    def toggle_fade(self) -> None:
        self.setWindowOpacity(0.25 if self.windowOpacity() > 0.5 else self.state.opacity)

    def launch_viewer_hint(self) -> None:
        message = "Run python run_panda.py to open the standalone 3D viewer."
        if self.model_path:
            message = f"3D model ready: {self.model_path}"
        self.state.mark_spoken(message)
        self.set_state(self.state)
        self.voice.speak(message)

    def keep_inside_screen(self) -> None:
        screen = QApplication.primaryScreen()
        if screen is None:
            return
        available: QRect = screen.availableGeometry()
        x = min(max(self.x(), available.left()), available.right() - self.width())
        y = min(max(self.y(), available.top()), available.bottom() - self.height())
        if x != self.x() or y != self.y():
            self.move(x, y)

    def paintEvent(self, event) -> None:  # noqa: N802
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        self.draw_shadow(painter)
        self.draw_mascot(painter)

    def draw_shadow(self, painter: QPainter) -> None:
        painter.setPen(Qt.NoPen)
        painter.setBrush(QColor(0, 0, 0, 80))
        painter.drawEllipse(90, self.height() - 88, self.width() - 180, 28)

    def draw_mascot(self, painter: QPainter) -> None:
        bounce = math.sin(self.phase) * 8
        talk = 1.0 if self.state.mood == MascotMood.SPEAKING else 0.0
        cx = self.width() // 2
        cy = 210 + int(bounce)

        hair = QColor(30, 20, 26)
        crimson = QColor(160, 18, 55)
        gold = QColor(236, 184, 78)
        skin = QColor(244, 210, 190)
        dress = QColor(52, 18, 34)

        painter.setPen(Qt.NoPen)
        painter.setBrush(hair)
        painter.drawEllipse(cx - 86, cy - 118, 172, 220)
        painter.setBrush(skin)
        painter.drawEllipse(cx - 56, cy - 92, 112, 120)
        painter.setBrush(dress)
        painter.drawRoundedRect(cx - 68, cy + 28, 136, 162, 28, 28)
        painter.setBrush(crimson)
        painter.drawPie(cx - 92, cy - 124, 184, 230, 210 * 16, 118 * 16)
        painter.setBrush(QColor(18, 12, 16))
        painter.drawEllipse(cx - 84, cy - 72, 30, 34)
        painter.drawEllipse(cx + 54, cy - 72, 30, 34)

        painter.setPen(QPen(QColor(40, 10, 20), 3))
        painter.setBrush(gold)
        painter.drawEllipse(cx - 34, cy - 35, 24, 24)
        painter.setBrush(crimson)
        painter.drawEllipse(cx + 14, cy - 35, 24, 24)

        painter.setPen(QPen(QColor(85, 30, 38), 3))
        mouth_h = 5 + int(10 * talk * (0.5 + abs(math.sin(self.phase * 4))))
        painter.drawArc(cx - 15, cy - 6, 30, mouth_h + 6, 200 * 16, 140 * 16)

        painter.setPen(QPen(gold, 4))
        painter.drawLine(cx - 48, cy + 74, cx + 48, cy + 74)
        painter.drawLine(cx - 34, cy + 102, cx + 34, cy + 102)

        painter.setPen(QPen(QColor(255, 210, 230, 210), 2))
        painter.drawArc(cx - 90, cy - 120, 180, 230, 230 * 16, 80 * 16)

        if self.model_path:
            painter.setPen(QPen(QColor(255, 235, 190), 2))
            painter.drawText(20, 28, f"3D ready: {self.model_path.name}")
        else:
            painter.setPen(QPen(QColor(255, 210, 225), 2))
            painter.drawText(20, 28, "Fallback 2D mode - add assets/kurumi_model.glb")
