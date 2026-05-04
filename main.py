from __future__ import annotations

import os
import sys

from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QSystemTrayIcon
from PyQt5.QtGui import QIcon, QPixmap, QPainter, QColor

from core.config import read_config
from core.decision import choose_greeting
from core.loop import MascotLoop
from core.state import MascotMood, MascotState
from core.voice import VoiceEngine
from window import KurumiOverlay


def create_tray_icon() -> QIcon:
    pixmap = QPixmap(64, 64)
    pixmap.fill(QColor(0, 0, 0, 0))
    painter = QPainter(pixmap)
    painter.setRenderHint(QPainter.Antialiasing)
    painter.setBrush(QColor(120, 15, 45))
    painter.setPen(QColor(245, 190, 95))
    painter.drawEllipse(6, 6, 52, 52)
    painter.drawText(20, 40, "K")
    painter.end()
    return QIcon(pixmap)


def main() -> int:
    app = QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)
    app.setApplicationName("Kurumi-AE")

    config = read_config()
    state = MascotState()
    voice = VoiceEngine(enabled=True, config=config)
    window = KurumiOverlay(state, voice, config)
    window.show()

    tray = QSystemTrayIcon(create_tray_icon(), app)
    tray.setToolTip("Kurumi-AE")
    tray.activated.connect(lambda reason: window.show() if reason == QSystemTrayIcon.Trigger else None)
    tray.show()

    greeting = choose_greeting()
    state.set_mood(MascotMood.GREETING, greeting)
    window.set_state(state)
    voice.speak(greeting)

    loop = MascotLoop(state)
    loop.state_changed.connect(window.set_state)
    loop.start()

    test_exit_ms = os.environ.get("KURUMI_AE_TEST_EXIT_MS")
    if test_exit_ms:
        QTimer.singleShot(int(test_exit_ms), app.quit)

    return app.exec_()


if __name__ == "__main__":
    raise SystemExit(main())
