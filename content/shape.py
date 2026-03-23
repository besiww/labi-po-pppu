# shape.py — Фигуры и графические элементы

class Shape:
    """Геометрическая фигура: прямоугольник, круг, стрелка (для тактик)."""

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
        self.rotation = 0       # угол поворота в градусах
        self.label = None       # текстовая метка внутри фигуры
        self.slide = None

    def set_fill(self, color, opacity=1.0):
        self.fill_color = color
        self.opacity = opacity

    def set_border(self, color, width):
        self.border_color = color
        self.border_width = width

    def rotate(self, angle):
        # Повернуть фигуру на заданный угол
        self.rotation = (self.rotation + angle) % 360

    def render(self, context):
        # Отрисовать фигуру с заливкой и рамкой
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
