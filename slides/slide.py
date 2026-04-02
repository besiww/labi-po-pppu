# slide.py — Базовый класс слайда презентации

class Slide:
    """
    Один слайд презентации академии.

    Хранит список элементов контента, ссылки на макет и мастер-слайд,
    а также заметки докладчика и параметры перехода.

    Attributes:
        slide_id (int): Уникальный идентификатор слайда.
        layout: Объект SlideLayout или None.
        master: Объект MasterSlide или None.
        elements (list): Список контентных элементов на слайде.
        notes (str): Заметки докладчика.
        hidden (bool): Скрытый слайд (не показывается в показе).
        transition: Объект анимации перехода или None.
    """

    def __init__(self, slide_id, layout=None):
        self.slide_id = slide_id
        self.layout = layout
        self.master = None
        self.elements = []
        self.notes = ''
        self.hidden = False
        self.transition = None

    def add_element(self, element):
        """
        Добавить элемент на слайд.

        Args:
            element: Объект элемента (TextBlock, Image, Shape, Table и др.).
        """
        element.slide = self
        self.elements.append(element)

    def remove_element(self, element_id):
        """
        Удалить элемент со слайда по идентификатору.

        Args:
            element_id (str): Идентификатор удаляемого элемента.
        """
        self.elements = [e for e in self.elements if e.element_id != element_id]

    def get_element(self, element_id):
        """
        Найти элемент на слайде по идентификатору.

        Args:
            element_id (str): Идентификатор искомого элемента.

        Returns:
            object: Найденный элемент или None.
        """
        for e in self.elements:
            if e.element_id == element_id:
                return e
        return None

    def apply_layout(self, layout):
        """
        Применить макет к слайду.

        Args:
            layout (SlideLayout): Макет для применения.
        """
        self.layout = layout
        layout.apply_to(self)

    def apply_master(self, master):
        """
        Привязать мастер-слайд.

        Args:
            master (MasterSlide): Мастер-слайд с глобальным оформлением.
        """
        self.master = master

    def render(self, context):
        """
        Отрисовать слайд: мастер, макет, затем все элементы.

        Args:
            context: Графический контекст для отрисовки.
        """
        if self.master:
            self.master.render_background(context)
        if self.layout:
            self.layout.render_placeholders(context)
        for element in self.elements:
            element.render(context)

    def to_dict(self):
        """
        Сериализовать слайд в словарь для сохранения.

        Returns:
            dict: Словарь с параметрами слайда.
        """
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
        """
        Восстановить слайд из словаря.

        Args:
            data (dict): Словарь с параметрами слайда.
            layout_registry (dict): Словарь layout_id -> SlideLayout.
            master_registry (dict): Словарь master_id -> MasterSlide.

        Returns:
            Slide: Восстановленный объект слайда.
        """
        layout = layout_registry.get(data.get('layout_id'))
        slide = cls(slide_id=data['slide_id'], layout=layout)
        slide.notes = data.get('notes', '')
        slide.hidden = data.get('hidden', False)
        master_id = data.get('master_id')
        if master_id:
            slide.master = master_registry.get(master_id)
        return slide
