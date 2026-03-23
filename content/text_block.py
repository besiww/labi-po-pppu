# text_block.py — Текстовый блок на слайде

class TextBlock:
    """Текстовый элемент: заголовок, абзац, подпись к статистике."""

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
        self.align = 'left'     # 'left', 'center', 'right', 'justify'
        self.slide = None

    def set_style(self, font_name=None, font_size=None, bold=None,
                  italic=None, color=None, align=None):
        # Применить стиль к текстовому блоку
        if font_name:  self.font_name = font_name
        if font_size:  self.font_size = font_size
        if bold is not None:   self.bold = bold
        if italic is not None: self.italic = italic
        if color:  self.color = color
        if align:  self.align = align

    def set_text(self, text):
        # Обновить содержимое текстового блока
        self.text = text

    def render(self, context):
        # Отрисовать текст с заданными стилями в указанных координатах
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
