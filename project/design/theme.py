# theme.py — Тема оформления презентации

class Theme:
    """
    Тема оформления презентации академии.

    Объединяет цветовую схему, схему шрифтов и фон в единый
    стилевой пакет, который применяется к мастер-слайду.

    Attributes:
        name (str): Название темы.
        color_scheme: Объект ColorScheme или None.
        font_scheme: Объект FontScheme или None.
        background: Объект Background или None.
    """

    PRESETS = ['academy_blue', 'dark_stadium', 'clean_white', 'trophy_gold']

    def __init__(self, name='academy_blue'):
        self.name = name
        self.color_scheme = None
        self.font_scheme = None
        self.background = None

    @classmethod
    def from_preset(cls, preset_name):
        """
        Создать тему из встроенного пресета.

        Args:
            preset_name (str): Название пресета из списка PRESETS.

        Returns:
            Theme: Готовый объект темы.
        """
        theme = cls(name=preset_name)
        theme.color_scheme = ColorScheme.preset(preset_name)
        theme.font_scheme = FontScheme.preset(preset_name)
        theme.background = Background.preset(preset_name)
        return theme

    def apply_to_master(self, master):
        """
        Применить тему к мастер-слайду.

        Args:
            master (MasterSlide): Мастер-слайд для применения темы.
        """
        master.color_scheme = self.color_scheme
        master.font_scheme = self.font_scheme
        master.background = self.background

    def customize(self, primary_color=None, font_name=None, bg_color=None):
        """
        Точечно изменить параметры темы.

        Args:
            primary_color (str, optional): Новый основной цвет в формате HEX.
            font_name (str, optional): Новый шрифт заголовков.
            bg_color (str, optional): Новый цвет фона в формате HEX.
        """
        if primary_color and self.color_scheme:
            self.color_scheme.primary = primary_color
        if font_name and self.font_scheme:
            self.font_scheme.heading_font = font_name
        if bg_color and self.background:
            self.background.color = bg_color

    def to_dict(self):
        """
        Сериализовать тему в словарь для сохранения.

        Returns:
            dict: Словарь с параметрами темы.
        """
        return {
            'name': self.name,
            'color_scheme': self.color_scheme.to_dict() if self.color_scheme else None,
            'font_scheme': self.font_scheme.to_dict() if self.font_scheme else None,
        }


class FontScheme:
    """
    Схема шрифтов презентации.

    Attributes:
        heading_font (str): Шрифт заголовков.
        body_font (str): Шрифт основного текста.
        heading_size (int): Размер шрифта заголовков в пунктах.
        body_size (int): Размер шрифта основного текста в пунктах.
    """

    def __init__(self, heading_font='Arial', body_font='Arial',
                 heading_size=32, body_size=14):
        self.heading_font = heading_font
        self.body_font = body_font
        self.heading_size = heading_size
        self.body_size = body_size

    @classmethod
    def preset(cls, name):
        """
        Создать схему шрифтов из пресета.

        Args:
            name (str): Название пресета темы.

        Returns:
            FontScheme: Объект схемы шрифтов.
        """
        presets = {
            'academy_blue': cls('Montserrat', 'Open Sans', 36, 14),
            'dark_stadium': cls('Bebas Neue', 'Roboto', 40, 13),
            'clean_white':  cls('Lato', 'Lato', 32, 14),
            'trophy_gold':  cls('Playfair Display', 'Georgia', 34, 14),
        }
        return presets.get(name, cls())

    def to_dict(self):
        """
        Сериализовать схему шрифтов в словарь.

        Returns:
            dict: Словарь с параметрами шрифтов.
        """
        return {
            'heading_font': self.heading_font,
            'body_font': self.body_font,
            'heading_size': self.heading_size,
            'body_size': self.body_size,
        }
