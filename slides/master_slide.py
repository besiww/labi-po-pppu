# master_slide.py — Мастер-слайд

class MasterSlide:
    """
    Мастер-слайд презентации академии.

    Определяет глобальное оформление всей презентации:
    фон, цветовую схему, шрифты, логотип и нижний колонтитул.
    Все дочерние макеты наследуют стиль мастера.

    Attributes:
        master_id (str): Уникальный идентификатор мастер-слайда.
        name (str): Название мастера.
        background: Объект Background или None.
        color_scheme: Объект ColorScheme или None.
        font_scheme: Объект FontScheme или None.
        layouts (list): Список дочерних макетов SlideLayout.
        logo: Объект Image с логотипом академии или None.
        footer_text (str): Текст нижнего колонтитула.
    """

    def __init__(self, master_id, name='Default'):
        self.master_id = master_id
        self.name = name
        self.background = None
        self.color_scheme = None
        self.font_scheme = None
        self.layouts = []
        self.logo = None
        self.footer_text = ''

    def add_layout(self, layout):
        """
        Добавить макет, наследующий стиль мастера.

        Args:
            layout (SlideLayout): Макет для добавления.
        """
        layout.master = self
        self.layouts.append(layout)

    def get_layout(self, layout_type):
        """
        Найти макет по типу.

        Args:
            layout_type (str): Тип макета из SlideLayout.TYPES.

        Returns:
            SlideLayout: Найденный макет или None.
        """
        for layout in self.layouts:
            if layout.layout_type == layout_type:
                return layout
        return None

    def apply_theme(self, theme):
        """
        Применить тему оформления к мастер-слайду.

        Args:
            theme (Theme): Тема с цветами, шрифтами и фоном.
        """
        self.color_scheme = theme.color_scheme
        self.font_scheme = theme.font_scheme
        self.background = theme.background

    def render_background(self, context):
        """
        Отрисовать фон мастера, логотип и нижний колонтитул.

        Args:
            context: Графический контекст для отрисовки.
        """
        if self.background:
            self.background.render(context)
        if self.logo:
            self.logo.render(context)
        if self.footer_text:
            self._render_footer(context)

    def _render_footer(self, context):
        """
        Нарисовать нижний колонтитул слайда.

        Args:
            context: Графический контекст для отрисовки.
        """
        pass

    def to_dict(self):
        """
        Сериализовать мастер-слайд в словарь для сохранения.

        Returns:
            dict: Словарь с параметрами мастер-слайда.
        """
        return {
            'master_id': self.master_id,
            'name': self.name,
            'layouts': [l.to_dict() for l in self.layouts],
            'footer_text': self.footer_text,
        }


class SlideManager:
    """
    Менеджер списка слайдов и их иерархии в презентации.

    Управляет порядком слайдов, регистрирует мастера и макеты,
    поддерживает операции добавления, удаления, перемещения и дублирования.

    Attributes:
        slides (list): Упорядоченный список объектов Slide.
        masters (dict): Словарь master_id -> MasterSlide.
        layouts (dict): Словарь layout_id -> SlideLayout.
    """

    def __init__(self):
        self.slides = []
        self.masters = {}
        self.layouts = {}

    def add_slide(self, slide, position=None):
        """
        Добавить слайд в презентацию.

        Args:
            slide (Slide): Слайд для добавления.
            position (int, optional): Позиция вставки. По умолчанию в конец.
        """
        if position is None:
            self.slides.append(slide)
        else:
            self.slides.insert(position, slide)

    def remove_slide(self, slide_id):
        """
        Удалить слайд из презентации по идентификатору.

        Args:
            slide_id (int): Идентификатор удаляемого слайда.
        """
        self.slides = [s for s in self.slides if s.slide_id != slide_id]

    def move_slide(self, slide_id, new_position):
        """
        Переместить слайд на новую позицию в списке.

        Args:
            slide_id (int): Идентификатор перемещаемого слайда.
            new_position (int): Новая позиция в списке.
        """
        slide = self._find(slide_id)
        if slide:
            self.slides.remove(slide)
            self.slides.insert(new_position, slide)

    def duplicate_slide(self, slide_id):
        """
        Создать копию слайда и вставить её следом за оригиналом.

        Args:
            slide_id (int): Идентификатор копируемого слайда.

        Returns:
            Slide: Новый слайд-копия или None если оригинал не найден.
        """
        original = self._find(slide_id)
        if not original:
            return None
        import copy
        clone = copy.deepcopy(original)
        clone.slide_id = self._generate_id()
        idx = self.slides.index(original)
        self.slides.insert(idx + 1, clone)
        return clone

    def get_visible_slides(self):
        """
        Получить список видимых (не скрытых) слайдов.

        Returns:
            list: Список объектов Slide с hidden=False.
        """
        return [s for s in self.slides if not s.hidden]

    def register_master(self, master):
        """
        Зарегистрировать мастер-слайд в менеджере.

        Args:
            master (MasterSlide): Мастер-слайд для регистрации.
        """
        self.masters[master.master_id] = master

    def register_layout(self, layout):
        """
        Зарегистрировать макет в менеджере.

        Args:
            layout (SlideLayout): Макет для регистрации.
        """
        self.layouts[layout.layout_id] = layout

    def _find(self, slide_id):
        for s in self.slides:
            if s.slide_id == slide_id:
                return s
        return None

    def _generate_id(self):
        """
        Сгенерировать уникальный id для нового слайда.

        Returns:
            int: Новый уникальный идентификатор.
        """
        return max((s.slide_id for s in self.slides), default=0) + 1
