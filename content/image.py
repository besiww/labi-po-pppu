# image.py — Изображение на слайде

class Image:
    """
    Изображение на слайде презентации.

    Используется для вставки фото игроков, логотипов академии,
    тактических схем и других графических материалов.

    Attributes:
        element_id (str): Уникальный идентификатор элемента.
        src (str): Путь к файлу изображения или URL.
        x (int): Координата X на слайде.
        y (int): Координата Y на слайде.
        width (int): Ширина изображения в пикселях.
        height (int): Высота изображения в пикселях.
        crop (tuple): Область обрезки (left, top, right, bottom) или None.
        opacity (float): Прозрачность от 0.0 до 1.0.
        border: Объект Border или None.
        slide: Ссылка на родительский слайд.
    """

    def __init__(self, element_id, src='', x=0, y=0, width=200, height=200):
        self.element_id = element_id
        self.src = src
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.crop = None
        self.opacity = 1.0
        self.border = None
        self.slide = None

    def load(self):
        """
        Загрузить изображение из src в память.

        Returns:
            object: Объект изображения.

        Raises:
            FileNotFoundError: Если файл не найден по указанному пути.
        """
        pass

    def set_crop(self, left, top, right, bottom):
        """
        Задать область обрезки изображения.

        Args:
            left (int): Отступ слева в пикселях.
            top (int): Отступ сверху в пикселях.
            right (int): Отступ справа в пикселях.
            bottom (int): Отступ снизу в пикселях.
        """
        self.crop = (left, top, right, bottom)

    def resize(self, width, height, keep_aspect=True):
        """
        Изменить размер изображения.

        Args:
            width (int): Новая ширина в пикселях.
            height (int): Новая высота в пикселях.
            keep_aspect (bool): Сохранять пропорции. По умолчанию True.
        """
        if keep_aspect:
            ratio = min(width / self.width, height / self.height)
            self.width = int(self.width * ratio)
            self.height = int(self.height * ratio)
        else:
            self.width = width
            self.height = height

    def render(self, context):
        """
        Отрисовать изображение на слайде.

        Args:
            context: Графический контекст для отрисовки.
        """
        context.draw_image(self.src, self.x, self.y,
                           self.width, self.height,
                           crop=self.crop, opacity=self.opacity)

    def to_dict(self):
        """
        Сериализовать элемент в словарь для сохранения.

        Returns:
            dict: Словарь с параметрами изображения.
        """
        return {
            'type': 'image',
            'element_id': self.element_id,
            'src': self.src,
            'x': self.x, 'y': self.y,
            'width': self.width, 'height': self.height,
            'crop': self.crop,
            'opacity': self.opacity,
        }
