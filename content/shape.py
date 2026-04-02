# shape.py — Фигуры и графические элементы

class Shape:
    """
    Геометрическая фигура на слайде презентации.

    Используется для создания тактических схем, выделения зон корта,
    стрелок и декоративных элементов оформления.

    Attributes:
        element_id (str): Уникальный идентификатор элемента.
        shape_type (str): Тип фигуры: 'rectangle', 'circle', 'ellipse',
            'arrow', 'line', 'polygon'.
        x (int): Координата X на слайде.
        y (int): Координата Y на слайде.
        width (int): Ширина фигуры в пикселях.
        height (int): Высота фигуры в пикселях.
        fill_color (str): Цвет заливки в формате HEX.
        border_color (str): Цвет рамки в формате HEX.
        border_width (int): Толщина рамки в пикселях.
        opacity (float): Прозрачность от 0.0 до 1.0.
        rotation (int): Угол поворота в градусах.
        label: Текстовая метка внутри фигуры или None.
        slide: Ссылка на родительский слайд.
    """

    TYPES = ['rectangle', 'circle', 'ellipse', 'arrow', 'line', 'polygon']

    def __init__(self, element_id, shape_type='rectangle',
                 x=0, y=0, width=100, height=100):
        self.element_id = element_id
        self.shape_type = shape_type
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.fill_color = '#FFFFFF'
        self.border_color = '#000000'
        self.border_width = 1
        self.opacity = 1.0
        self.rotation = 0
        self.label = None
        self.slide = None

    def set_fill(self, color, opacity=1.0):
        """
        Задать цвет заливки фигуры.

        Args:
            color (str): Цвет в формате HEX.
            opacity (float): Прозрачность от 0.0 до 1.0.
        """
        self.fill_color = color
        self.opacity = opacity

    def set_border(self, color, width):
        """
        Задать параметры рамки фигуры.

        Args:
            color (str): Цвет рамки в формате HEX.
            width (int): Толщина рамки в пикселях.
        """
        self.border_color = color
        self.border_width = width

    def rotate(self, angle):
        """
        Повернуть фигуру на заданный угол.

        Args:
            angle (int): Угол поворота в градусах.
        """
        self.rotation = (self.rotation + angle) % 360

    def render(self, context):
        """
        Отрисовать фигуру на слайде.

        Args:
            context: Графический контекст для отрисовки.
        """
        context.draw_shape(
            self.shape_type,
            self.x, self.y, self.width, self.height,
            fill=self.fill_color,
            border_color=self.border_color,
            border_width=self.border_width,
            opacity=self.opacity,
            rotation=self.rotation,
        )
        if self.label:
            self.label.render(context)

    def to_dict(self):
        """
        Сериализовать элемент в словарь для сохранения.

        Returns:
            dict: Словарь с параметрами фигуры.
        """
        return {
            'type': 'shape',
            'element_id': self.element_id,
            'shape_type': self.shape_type,
            'x': self.x, 'y': self.y,
            'width': self.width, 'height': self.height,
            'fill_color': self.fill_color,
            'border_color': self.border_color,
            'border_width': self.border_width,
            'opacity': self.opacity,
            'rotation': self.rotation,
        }
