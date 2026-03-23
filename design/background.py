# background.py — Фон слайда

class Background:
    """Фон слайда: сплошной цвет, градиент или изображение."""

    TYPES = ['solid', 'gradient', 'image', 'pattern']

    def __init__(self, bg_type='solid', color='#FFFFFF'):
        self.bg_type = bg_type
        self.color = color              # для solid
        self.gradient_start = None      # для gradient
        self.gradient_end = None
        self.gradient_angle = 135       # угол градиента в градусах
        self.image_src = None           # для image
        self.image_opacity = 1.0
        self.pattern_name = None        # для pattern ('dots', 'lines', 'grid')

    @classmethod
    def solid(cls, color):
        return cls(bg_type='solid', color=color)

    @classmethod
    def gradient(cls, start_color, end_color, angle=135):
        bg = cls(bg_type='gradient')
        bg.gradient_start = start_color
        bg.gradient_end = end_color
        bg.gradient_angle = angle
        return bg

    @classmethod
    def from_image(cls, src, opacity=1.0):
        bg = cls(bg_type='image')
        bg.image_src = src
        bg.image_opacity = opacity
        return bg

    @classmethod
    def preset(cls, name):
        # Вернуть фон по пресету темы
        presets = {
            'academy_blue':  cls.solid('#FFFFFF'),
            'dark_stadium':  cls.gradient('#0D0D0D', '#1A1A2E', 180),
            'clean_white':   cls.solid('#FAFAFA'),
            'trophy_gold':   cls.gradient('#FFFFF0', '#FFF8DC', 160),
        }
        return presets.get(name, cls.solid('#FFFFFF'))

    def render(self, context):
        # Отрисовать фон на слайде
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
