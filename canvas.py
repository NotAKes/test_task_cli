from typing import Dict

from shapes import Shape


class Canvas:
    def __init__(self):
        self._shapes: Dict[int, Shape] = {}
        self._next_id: int = 1

    def add_shape(self, shape: Shape) -> int:
        shape_id = self._next_id
        self._shapes[shape_id] = shape
        self._next_id += 1
        return shape_id

    def del_shape(self, shape_id: int) -> bool:
        if shape_id in self._shapes:
            del self._shapes[shape_id]
            return True
        return False

    def get_all_shapes(self) -> Dict[int, Shape]:
        return self._shapes
