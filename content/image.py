# image.py — Изображение на слайде

class Image:
    """Изображение: фото игрока, логотип академии, тактическая схема."""

    def __init__(self, element_id, src='', x=0, y=0, width=200, height=200):
        self.element_id = element_id
        self.src = src          # путь к файлу или URL
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.crop = None        # (left, top, right, bottom) в пикселях
        self.opacity = 1.0      # прозрачность 0.0–1.0
        self.border = None      # объект Border или None
        self.slide = None

    def load(self):
        # Загрузить изображение из src в память
        # Вернуть объект изображения или выбросить исключение
        pass

    def set_crop(self, left, top, right, bottom):
        # Задать область обрезки изображения
        self.crop = (left, top, right, bottom)

    def resize(self, width, height, keep_aspect=True):
        # Изменить размер с сохранением пропорций (если keep_aspect=True)
        if keep_aspect:
            ratio = min(width / self.width, height / self.height)
            self.width = int(self.width * ratio)
            self.height = int(self.height * ratio)
        else:
            self.width = width
            self.height = height

    def render(self, context):
        # Отрисовать изображение на слайде
        context.draw_image(self.src, self.x, self.y,
                           self.width, self.height,
                           crop=self.crop, opacity=self.opacity)

    def to_dict(self):
        return {
            'type': 'image',
            'element_id': self.element_id,
            'src': self.src,
            'x': self.x, 'y': self.y,
            'width': self.width, 'height': self.height,
            'crop': self.crop,
            'opacity': self.opacity,
        }
