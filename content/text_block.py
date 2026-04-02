# text_block.py — Текстовый блок на слайде

class TextBlock:
    """
    Текстовый элемент на слайде презентации.

    Используется для заголовков, абзацев, подписей к статистике
    и любого текстового контента в презентации академии.

    Attributes:
        element_id (str): Уникальный идентификатор элемента.
        text (str): Текстовое содержимое блока.
        x (int): Координата X на слайде.
        y (int): Координата Y на слайде.
        width (int): Ширина блока в пикселях.
        height (int): Высота блока в пикселях.
        font_name (str): Название шрифта.
        font_size (int): Размер шрифта в пунктах.
        bold (bool): Жирное начертание.
        italic (bool): Курсивное начертание.
        color (str): Цвет текста в формате HEX.
        align (str): Выравнивание: 'left', 'center', 'right', 'justify'.
        slide: Ссылка на родительский слайд.
    """

    def __init__(self, element_id, text='', x=0, y=0, width=400, height=100):
        self.element_id = element_id
        self.text = text
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.font_name = 'Arial'
        self.font_size = 14
        self.bold = False
        self.italic = False
        self.color = '#000000'
        self.align = 'left'
        self.slide = None

    def set_style(self, font_name=None, font_size=None, bold=None,
                  italic=None, color=None, align=None):
        """
        Применить стиль к текстовому блоку.

        Args:
            font_name (str, optional): Название шрифта.
            font_size (int, optional): Размер шрифта в пунктах.
            bold (bool, optional): Жирное начертание.
            italic (bool, optional): Курсивное начертание.
            color (str, optional): Цвет текста в формате HEX.
            align (str, optional): Выравнивание текста.
        """
        if font_name:  self.font_name = font_name
        if font_size:  self.font_size = font_size
        if bold is not None:   self.bold = bold
        if italic is not None: self.italic = italic
        if color:  self.color = color
        if align:  self.align = align

    def set_text(self, text):
        """
        Обновить текстовое содержимое блока.

        Args:
            text (str): Новый текст.
        """
        self.text = text

    def render(self, context):
        """
        Отрисовать текстовый блок на слайде.

        Args:
            context: Графический контекст для отрисовки.
        """
        style = {
            'font': self.font_name,
            'size': self.font_size,
            'bold': self.bold,
            'italic': self.italic,
            'color': self.color,
            'align': self.align,
        }
        context.draw_text(self.text, self.x, self.y, self.width, self.height, style)

    def to_dict(self):
        """
        Сериализовать элемент в словарь для сохранения.

        Returns:
            dict: Словарь с параметрами текстового блока.
        """
        return {
            'type': 'text_block',
            'element_id': self.element_id,
            'text': self.text,
            'x': self.x, 'y': self.y,
            'width': self.width, 'height': self.height,
            'font_name': self.font_name,
            'font_size': self.font_size,
            'bold': self.bold,
            'italic': self.italic,
            'color': self.color,
            'align': self.align,
        }
