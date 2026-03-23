# master_slide.py — Мастер-слайд

class MasterSlide:
    """Мастер-слайд: глобальное оформление всей презентации академии."""

    def __init__(self, master_id, name='Default'):
        self.master_id = master_id
        self.name = name
        self.background = None      # объект Background
        self.color_scheme = None    # объект ColorScheme
        self.font_scheme = None     # объект FontScheme
        self.layouts = []           # дочерние макеты SlideLayout
        self.logo = None            # логотип академии (Image)
        self.footer_text = ''       # текст нижнего колонтитула

    def add_layout(self, layout):
        # Добавить макет, наследующий стиль мастера
        layout.master = self
        self.layouts.append(layout)

    def get_layout(self, layout_type):
        # Найти макет по типу
        for layout in self.layouts:
            if layout.layout_type == layout_type:
                return layout
        return None

    def apply_theme(self, theme):
        # Применить тему: цвета, шрифты, фон
        self.color_scheme = theme.color_scheme
        self.font_scheme = theme.font_scheme
        self.background = theme.background

    def render_background(self, context):
        # Отрисовать фон мастера на слайде
        if self.background:
            self.background.render(context)
        if self.logo:
            self.logo.render(context)
        if self.footer_text:
            self._render_footer(context)

    def _render_footer(self, context):
        # Нарисовать нижний колонтитул (название академии, дата, номер слайда)
        pass

    def to_dict(self):
        return {
            'master_id': self.master_id,
            'name': self.name,
            'layouts': [l.to_dict() for l in self.layouts],
            'footer_text': self.footer_text,
        }


class SlideManager:
    """Менеджер списка слайдов и их иерархии в презентации."""

    def __init__(self):
        self.slides = []        # упорядоченный список Slide
        self.masters = {}       # master_id -> MasterSlide
        self.layouts = {}       # layout_id -> SlideLayout

    def add_slide(self, slide, position=None):
        # Добавить слайд в конец или на указанную позицию
        if position is None:
            self.slides.append(slide)
        else:
            self.slides.insert(position, slide)

    def remove_slide(self, slide_id):
        # Удалить слайд по id
        self.slides = [s for s in self.slides if s.slide_id != slide_id]

    def move_slide(self, slide_id, new_position):
        # Переместить слайд на новую позицию в списке
        slide = self._find(slide_id)
        if slide:
            self.slides.remove(slide)
            self.slides.insert(new_position, slide)

    def duplicate_slide(self, slide_id):
        # Создать копию слайда и вставить её следом
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
        # Вернуть только видимые (не скрытые) слайды
        return [s for s in self.slides if not s.hidden]

    def register_master(self, master):
        self.masters[master.master_id] = master

    def register_layout(self, layout):
        self.layouts[layout.layout_id] = layout

    def _find(self, slide_id):
        for s in self.slides:
            if s.slide_id == slide_id:
                return s
        return None

    def _generate_id(self):
        # Сгенерировать уникальный id для нового слайда
        return max((s.slide_id for s in self.slides), default=0) + 1
