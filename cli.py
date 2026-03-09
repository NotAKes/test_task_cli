import cmd
from shapes import Point, Line, Circle, Square
from canvas import Canvas


class ShapeCLI(cmd.Cmd):
    intro = 'Добро пожаловать в CLI для управления фигурами. Введите help или ? для получения списка команд.\n'
    prompt = '> '

    def __init__(self):
        super().__init__()
        self.canvas = Canvas()

    def do_create(self, args: str):
        """Создает фигуру. Использование: create <shape_type> <parameters>"""
        args = args.split()
        if not args:
            print("Ошибка: укажите тип фигуры. Наберите 'help create' для справки.")
            return
        shape_type = args[0].lower()
        params = args[1:]
        try:
            if shape_type == "point":
                if len(params) != 2: raise ValueError("для создания точки укажите 2 параметра (x y).")
                x, y = map(float, params)
                shape = Point(x, y)
            elif shape_type == "line":
                if len(params) != 4: raise ValueError("для создания отрезка укажите 4 параметра (x1 y1 x2 y2).")
                x1, y1, x2, y2 = map(float, params)
                shape = Line(Point(x1, y1), Point(x2, y2))
            elif shape_type == "circle":
                if len(params) != 3: raise ValueError("для создания круга укажите 3 параметра (x y radius).")
                x, y, radius = map(float, params)
                shape = Circle(Point(x, y), radius)
            elif shape_type == "square":
                if len(params) != 3: raise ValueError("для создания квадрата укажите 3 параметра (x y side).")
                x, y, side = map(float, params)
                shape = Square(Point(x, y), side)
            else:
                print(f"Ошибка: неизвестный тип фигуры '{shape_type}'. Наберите 'help create' для справки.")
                return
            shape_id = self.canvas.add_shape(shape)
            print(f"Фигура создана с ID {shape_id}: {shape}")
        except ValueError as e:
            print(f"Ошибка: {e}")

    def do_delete(self, args: str):
        """Удаляет фигуру по её ID. Использование: delete <shape_id>"""
        try:
            shape_id = int(args.strip())
            if self.canvas.del_shape(shape_id):
                print(f"Фигура с ID {shape_id} удалена.")
            else:
                print(f"Ошибка: фигура с ID {shape_id} не найдена.")
        except ValueError:
            print("Ошибка: укажите числовой ID фигуры для удаления. Наберите 'help delete' для справки.")

    def do_list(self, args: str):
        """Выводит список всех фигур на холсте с их ID и описанием."""
        if not self.canvas.get_all_shapes():
            print("На холсте нет фигур.")
            return
        for shape_id, shape in self.canvas.get_all_shapes().items():
            print(f"ID {shape_id}: {shape}")


    def do_exit(self, args: str):
        """Завершает работу CLI."""
        print("Завершение работы.")
        return True

if __name__ == '__main__':
    ShapeCLI().cmdloop()
