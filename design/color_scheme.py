# color_scheme.py — Цветовая схема

class ColorScheme:
    """Цветовая палитра презентации академии."""

    def __init__(self, primary='#1A3C6E', secondary='#E8F0FE',
                 accent='#FFD700', text='#212121', background='#FFFFFF'):
        self.primary = primary          # основной цвет (синий академии)
        self.secondary = secondary      # вторичный цвет
        self.accent = accent            # акцентный цвет (золото трофея)
        self.text = text                # цвет основного текста
        self.background = background    # цвет фона
        self.success = '#4CAF50'        # победа / положительный результат
        self.danger = '#F44336'         # поражение / предупреждение
        self.neutral = '#9E9E9E'        # нейтральный / ничья

    @classmethod
    def preset(cls, name):
        # Вернуть цветовую схему по названию пресета
        presets = {
            'academy_blue': cls(
                primary='#1A3C6E', secondary='#E8F0FE',
                accent='#FFD700', text='#212121', background='#FFFFFF'
            ),
            'dark_stadium': cls(
                primary='#0D0D0D', secondary='#1E1E1E',
                accent='#00E5FF', text='#F5F5F5', background='#121212'
            ),
            'clean_white': cls(
                primary='#2196F3', secondary='#F5F5F5',
                accent='#FF5722', text='#333333', background='#FFFFFF'
            ),
            'trophy_gold': cls(
                primary='#B8860B', secondary='#FFF8DC',
                accent='#8B0000', text='#1A1A1A', background='#FFFFF0'
            ),
        }
        return presets.get(name, cls())

    def get_result_color(self, result):
        # Вернуть цвет по результату матча: 'win', 'loss', 'draw'
        mapping = {
            'win': self.success,
            'loss': self.danger,
            'draw': self.neutral,
        }
        return mapping.get(result, self.text)

    def to_dict(self):
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
