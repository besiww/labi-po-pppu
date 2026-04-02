# background.py — Фон слайда

class Background:
    """
    Фон слайда презентации.

    Поддерживает четыре типа фона: сплошной цвет, градиент,
    изображение и паттерн.

    Attributes:
        bg_type (str): Тип фона: 'solid', 'gradient', 'image', 'pattern'.
        color (str): Цвет фона для типа 'solid' в формате HEX.
        gradient_start (str): Начальный цвет градиента в формате HEX.
        gradient_end (str): Конечный цвет градиента в формате HEX.
        gradient_angle (int): Угол градиента в градусах.
        image_src (str): Путь к фоновому изображению.
        image_opacity (float): Прозрачность фонового изображения от 0.0 до 1.0.
        pattern_name (str): Название паттерна: 'dots', 'lines', 'grid'.
    """

    TYPES = ['solid', 'gradient', 'image', 'pattern']

    def __init__(self, bg_type='solid', color='#FFFFFF'):
        self.bg_type = bg_type
        self.color = color
        self.gradient_start = None
        self.gradient_end = None
        self.gradient_angle = 135
        self.image_src = None
        self.image_opacity = 1.0
        self.pattern_name = None

    @classmethod
    def solid(cls, color):
        """
        Создать сплошной фон.

        Args:
            color (str): Цвет в формате HEX.

        Returns:
            Background: Объект фона.
        """
        return cls(bg_type='solid', color=color)

    @classmethod
    def gradient(cls, start_color, end_color, angle=135):
        """
        Создать градиентный фон.

        Args:
            start_color (str): Начальный цвет в формате HEX.
            end_color (str): Конечный цвет в формате HEX.
            angle (int): Угол градиента в градусах. По умолчанию 135.

        Returns:
            Background: Объект фона.
        """
        bg = cls(bg_type='gradient')
        bg.gradient_start = start_color
        bg.gradient_end = end_color
        bg.gradient_angle = angle
        return bg

    @classmethod
    def from_image(cls, src, opacity=1.0):
        """
        Создать фон из изображения.

        Args:
            src (str): Путь к файлу изображения.
            opacity (float): Прозрачность от 0.0 до 1.0. По умолчанию 1.0.

        Returns:
            Background: Объект фона.
        """
        bg = cls(bg_type='image')
        bg.image_src = src
        bg.image_opacity = opacity
        return bg

    @classmethod
    def preset(cls, name):
        """
        Создать фон из пресета темы.

        Args:
            name (str): Название пресета темы.

        Returns:
            Background: Объект фона.
        """
        presets = {
            'academy_blue':  cls.solid('#FFFFFF'),
            'dark_stadium':  cls.gradient('#0D0D0D', '#1A1A2E', 180),
            'clean_white':   cls.solid('#FAFAFA'),
            'trophy_gold':   cls.gradient('#FFFFF0', '#FFF8DC', 160),
        }
        return presets.get(name, cls.solid('#FFFFFF'))

    def render(self, context):
        """
        Отрисовать фон на слайде.

        Args:
            context: Графический контекст для отрисовки.
        """
        if self.bg_type == 'solid':
            context.fill_background(self.color)
        elif self.bg_type == 'gradient':
            context.fill_gradient(self.gradient_start, self.gradient_end,
                                  self.gradient_angle)
        elif self.bg_type == 'image':
            context.draw_background_image(self.image_src, self.image_opacity)
        elif self.bg_type == 'pattern':
            context.draw_pattern(self.pattern_name, self.color)

    def to_dict(self):
        """
        Сериализовать фон в словарь для сохранения.

        Returns:
            dict: Словарь с параметрами фона.
        """
        return {
            'bg_type': self.bg_type,
            'color': self.color,
            'gradient_start': self.gradient_start,
            'gradient_end': self.gradient_end,
            'gradient_angle': self.gradient_angle,
            'image_src': self.image_src,
            'image_opacity': self.image_opacity,
            'pattern_name': self.pattern_name,
        }
