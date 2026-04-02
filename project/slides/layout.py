# layout.py — Макеты слайдов

class SlideLayout:
    """
    Макет слайда презентации.

    Определяет расположение и типы placeholder-зон на слайде.
    Наследует стиль от родительского мастер-слайда.

    Attributes:
        layout_id (str): Уникальный идентификатор макета.
        layout_type (str): Тип макета из списка TYPES.
        placeholders (list): Список объектов Placeholder.
        master: Родительский MasterSlide или None.
    """

    TYPES = [
        'title', 'title_content', 'two_column',
        'stats_table', 'player_card', 'tournament_result', 'blank',
    ]

    def __init__(self, layout_id, layout_type='blank'):
        self.layout_id = layout_id
        self.layout_type = layout_type
        self.placeholders = []
        self.master = None

    def add_placeholder(self, placeholder):
        """
        Добавить зону-заполнитель в макет.

        Args:
            placeholder (Placeholder): Объект placeholder для добавления.
        """
        self.placeholders.append(placeholder)

    def apply_to(self, slide):
        """
        Применить макет к слайду: разместить placeholder-ы.

        Args:
            slide (Slide): Слайд для применения макета.
        """
        for ph in self.placeholders:
            ph.attach_to_slide(slide)

    def render_placeholders(self, context):
        """
        Отрисовать рамки placeholder-ов в режиме редактирования.

        Args:
            context: Графический контекст для отрисовки.
        """
        for ph in self.placeholders:
            ph.render_outline(context)

    def to_dict(self):
        """
        Сериализовать макет в словарь для сохранения.

        Returns:
            dict: Словарь с параметрами макета.
        """
        return {
            'layout_id': self.layout_id,
            'layout_type': self.layout_type,
            'placeholders': [ph.to_dict() for ph in self.placeholders],
        }


class Placeholder:
    """
    Зона-заполнитель на макете слайда.

    Attributes:
        ph_id (str): Уникальный идентификатор placeholder-а.
        ph_type (str): Тип: 'title', 'body', 'image', 'footer', 'stats'.
        x (int): Координата X на слайде.
        y (int): Координата Y на слайде.
        width (int): Ширина зоны в пикселях.
        height (int): Высота зоны в пикселях.
        content: Привязанный элемент контента или None.
    """

    def __init__(self, ph_id, ph_type, x, y, width, height):
        self.ph_id = ph_id
        self.ph_type = ph_type
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.content = None

    def attach_to_slide(self, slide):
        """
        Зарегистрировать placeholder на слайде.

        Args:
            slide (Slide): Слайд для регистрации.
        """
        pass

    def render_outline(self, context):
        """
        Нарисовать пунктирную рамку placeholder-а.

        Args:
            context: Графический контекст для отрисовки.
        """
        pass

    def to_dict(self):
        """
        Сериализовать placeholder в словарь.

        Returns:
            dict: Словарь с параметрами placeholder-а.
        """
        return {
            'ph_id': self.ph_id,
            'ph_type': self.ph_type,
            'x': self.x, 'y': self.y,
            'width': self.width, 'height': self.height,
        }
