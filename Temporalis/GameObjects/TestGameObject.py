from GameObjects.GameObject import GameObject

class TestGameObject(GameObject):
    def __init__(self, x, y, w, h):
        super().__init__(x, y, w, h)

    def draw(self, surface):
        super().draw(surface)

    def update(self):
        super().update()