# slide.py — Базовый класс слайда презентации

class Slide:
    """Один слайд презентации академии (отчёт, тактика, статистика)."""

    def __init__(self, slide_id, layout=None):
        self.slide_id = slide_id
        self.layout = layout        # объект SlideLayout
        self.master = None          # объект MasterSlide
        self.elements = []          # контентные элементы на слайде
        self.notes = ''             # заметки докладчика
        self.hidden = False         # скрытый слайд (не показывается в показе)
        self.transition = None      # анимация перехода

    def add_element(self, element):
        # Добавить элемент (текст, изображение, таблица и т.д.) на слайд
        element.slide = self
        self.elements.append(element)

    def remove_element(self, element_id):
        # Удалить элемент по идентификатору
        self.elements = [e for e in self.elements if e.element_id != element_id]

    def get_element(self, element_id):
        # Найти элемент по id
        for e in self.elements:
            if e.element_id == element_id:
                return e
        return None

    def apply_layout(self, layout):
        # Применить макет к слайду (переопределяет позиции placeholder-ов)
        self.layout = layout
        layout.apply_to(self)

    def apply_master(self, master):
        # Привязать мастер-слайд (фон, шрифты, цветовая схема)
        self.master = master

    def render(self, context):
        # Отрисовать слайд: сначала мастер, потом макет, потом элементы
        if self.master:
            self.master.render_background(context)
        if self.layout:
            self.layout.render_placeholders(context)
        for element in self.elements:
            element.render(context)

    def to_dict(self):
        # Сериализовать слайд для сохранения
        return {
            'slide_id': self.slide_id,
            'layout_id': self.layout.layout_id if self.layout else None,
            'master_id': self.master.master_id if self.master else None,
            'elements': [e.to_dict() for e in self.elements],
            'notes': self.notes,
            'hidden': self.hidden,
        }

    @classmethod
    def from_dict(cls, data, layout_registry, master_registry):
        # Восстановить слайд из словаря
        layout = layout_registry.get(data.get('layout_id'))
        slide = cls(slide_id=data['slide_id'], layout=layout)
        slide.notes = data.get('notes', '')
        slide.hidden = data.get('hidden', False)
        master_id = data.get('master_id')
        if master_id:
            slide.master = master_registry.get(master_id)
        return slide
