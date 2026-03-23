# layout.py — Макеты слайдов

class SlideLayout:
    """Макет слайда: определяет расположение placeholder-зон."""

    # Стандартные типы макетов для презентаций академии
    TYPES = [
        'title',            # только заголовок
        'title_content',    # заголовок + контент
        'two_column',       # два столбца
        'stats_table',      # таблица статистики
        'player_card',      # карточка игрока
        'tournament_result',# результаты турнира
        'blank',            # пустой
    ]

    def __init__(self, layout_id, layout_type='blank'):
        self.layout_id = layout_id
        self.layout_type = layout_type
        self.placeholders = []   # список Placeholder объектов
        self.master = None       # родительский мастер-слайд

    def add_placeholder(self, placeholder):
        # Добавить зону-заполнитель в макет
        self.placeholders.append(placeholder)

    def apply_to(self, slide):
        # Применить макет к слайду: разместить placeholder-ы
        for ph in self.placeholders:
            ph.attach_to_slide(slide)

    def render_placeholders(self, context):
        # Отрисовать рамки placeholder-ов (в режиме редактирования)
        for ph in self.placeholders:
            ph.render_outline(context)

    def to_dict(self):
        return {
            'layout_id': self.layout_id,
            'layout_type': self.layout_type,
            'placeholders': [ph.to_dict() for ph in self.placeholders],
        }


class Placeholder:
    """Зона-заполнитель на макете (заголовок, текст, изображение и т.д.)."""

    def __init__(self, ph_id, ph_type, x, y, width, height):
        self.ph_id = ph_id
        self.ph_type = ph_type   # 'title', 'body', 'image', 'footer', 'stats'
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.content = None      # привязанный элемент контента

    def attach_to_slide(self, slide):
        # Зарегистрировать placeholder на слайде
        pass

    def render_outline(self, context):
        # Нарисовать пунктирную рамку placeholder-а
        pass

    def to_dict(self):
        return {
            'ph_id': self.ph_id,
            'ph_type': self.ph_type,
            'x': self.x, 'y': self.y,
            'width': self.width, 'height': self.height,
        }
