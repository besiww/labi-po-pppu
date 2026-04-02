# color_scheme.py — Цветовая схема

class ColorScheme:
    """
    Цветовая палитра презентации академии.

    Определяет основные, акцентные и функциональные цвета,
    используемые во всех элементах презентации.

    Attributes:
        primary (str): Основной цвет академии в формате HEX.
        secondary (str): Вторичный цвет в формате HEX.
        accent (str): Акцентный цвет (трофей, победа) в формате HEX.
        text (str): Цвет основного текста в формате HEX.
        background (str): Цвет фона в формате HEX.
        success (str): Цвет победы / положительного результата.
        danger (str): Цвет поражения / предупреждения.
        neutral (str): Нейтральный цвет / ничья.
    """

    def __init__(self, primary='#1A3C6E', secondary='#E8F0FE',
                 accent='#FFD700', text='#212121', background='#FFFFFF'):
        self.primary = primary
        self.secondary = secondary
        self.accent = accent
        self.text = text
        self.background = background
        self.success = '#4CAF50'
        self.danger = '#F44336'
        self.neutral = '#9E9E9E'

    @classmethod
    def preset(cls, name):
        """
        Создать цветовую схему из встроенного пресета.

        Args:
            name (str): Название пресета темы.

        Returns:
            ColorScheme: Объект цветовой схемы.
        """
        presets = {
            'academy_blue': cls('#1A3C6E', '#E8F0FE', '#FFD700', '#212121', '#FFFFFF'),
            'dark_stadium': cls('#0D0D0D', '#1E1E1E', '#00E5FF', '#F5F5F5', '#121212'),
            'clean_white':  cls('#2196F3', '#F5F5F5', '#FF5722', '#333333', '#FFFFFF'),
            'trophy_gold':  cls('#B8860B', '#FFF8DC', '#8B0000', '#1A1A1A', '#FFFFF0'),
        }
        return presets.get(name, cls())

    def get_result_color(self, result):
        """
        Получить цвет по результату матча.

        Args:
            result (str): Результат: 'win', 'loss' или 'draw'.

        Returns:
            str: Цвет в формате HEX.
        """
        mapping = {
            'win': self.success,
            'loss': self.danger,
            'draw': self.neutral,
        }
        return mapping.get(result, self.text)

    def to_dict(self):
        """
        Сериализовать цветовую схему в словарь.

        Returns:
            dict: Словарь с цветами схемы.
        """
        return {
            'primary': self.primary,
            'secondary': self.secondary,
            'accent': self.accent,
            'text': self.text,
            'background': self.background,
            'success': self.success,
            'danger': self.danger,
            'neutral': self.neutral,
        }
