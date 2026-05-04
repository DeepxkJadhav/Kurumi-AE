from __future__ import annotations

import sys
import math
import os
from pathlib import Path

from direct.showbase.ShowBase import ShowBase
from panda3d.core import AmbientLight, CardMaker, DirectionalLight, TransparencyAttrib, loadPrcFileData

from window import find_model


loadPrcFileData("", "window-title Kurumi-AE 3D Viewer")
loadPrcFileData("", "win-size 420 560")
loadPrcFileData("", "undecorated true")
loadPrcFileData("", "always-on-top true")
loadPrcFileData("", "framebuffer-alpha true")
loadPrcFileData("", "background-color 0 0 0 0")


class KurumiPandaViewer(ShowBase):
    def __init__(self, model_path: Path | None) -> None:
        super().__init__()
        self.disableMouse()
        self.model = None
        self.angle = 0.0
        self.setup_lights()
        self.camera.setPos(0, -7, 2.1)
        self.camera.lookAt(0, 0, 1.25)
        if model_path:
            self.load_model(model_path)
        else:
            self.load_placeholder()
        self.taskMgr.add(self.spin_task, "kurumi-spin")
        test_exit_ms = os.environ.get("KURUMI_AE_TEST_EXIT_MS")
        if test_exit_ms:
            self.taskMgr.doMethodLater(int(test_exit_ms) / 1000, self.exit_task, "kurumi-test-exit")

    def setup_lights(self) -> None:
        ambient = AmbientLight("ambient")
        ambient.setColor((0.45, 0.38, 0.42, 1))
        self.render.setLight(self.render.attachNewNode(ambient))

        key = DirectionalLight("key")
        key.setColor((0.95, 0.82, 0.75, 1))
        key_np = self.render.attachNewNode(key)
        key_np.setHpr(-35, -55, 0)
        self.render.setLight(key_np)

    def load_model(self, model_path: Path) -> None:
        self.model = self.loader.loadModel(str(model_path))
        self.model.reparentTo(self.render)
        self.model.setScale(1.0)
        self.model.setPos(0, 0, 0)
        self.model.setTransparency(TransparencyAttrib.MAlpha)

    def load_placeholder(self) -> None:
        card = CardMaker("kurumi-placeholder")
        card.setFrame(-0.85, 0.85, -1.25, 1.25)
        self.model = self.render.attachNewNode(card.generate())
        self.model.setP(-90)
        self.model.setZ(1.15)
        self.model.setColor(0.42, 0.04, 0.16, 0.92)
        self.model.setTransparency(TransparencyAttrib.MAlpha)

        face = CardMaker("kurumi-face")
        face.setFrame(-0.38, 0.38, -0.38, 0.38)
        face_np = self.model.attachNewNode(face.generate())
        face_np.setY(-0.01)
        face_np.setZ(0.62)
        face_np.setColor(0.95, 0.76, 0.66, 1)
        face_np.setTransparency(TransparencyAttrib.MAlpha)

    def spin_task(self, task):
        if self.model:
            self.angle += 0.35
            self.model.setH(self.angle)
            self.model.setZ(math.sin(task.time * 2.0) * 0.05)
        return task.cont

    def exit_task(self, task):
        self.userExit()
        return task.done


def main() -> int:
    model_path = Path(sys.argv[1]) if len(sys.argv) > 1 else find_model()
    if model_path and not model_path.exists():
        print(f"Model not found: {model_path}")
        model_path = None
    app = KurumiPandaViewer(model_path)
    if model_path:
        print(f"Loaded model: {model_path}")
    else:
        print("No model found. Showing Panda3D placeholder.")
    app.run()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
