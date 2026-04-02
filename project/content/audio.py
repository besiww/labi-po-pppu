# audio.py — Аудио-элемент на слайде

class Audio:
    """
    Аудио-элемент презентации академии.

    Используется для добавления звукового сопровождения на слайд:
    гимн академии, фоновая музыка, звуковые эффекты.

    Attributes:
        element_id (str): Уникальный идентификатор элемента.
        src (str): Путь к аудиофайлу (mp3, wav, ogg) или URL.
        x (int): Координата X иконки на слайде.
        y (int): Координата Y иконки на слайде.
        autoplay (bool): Воспроизводить автоматически при показе слайда.
        loop (bool): Зациклить воспроизведение.
        volume (float): Громкость от 0.0 до 1.0.
        show_icon (bool): Показывать иконку аудио на слайде.
        slide: Ссылка на родительский слайд.
    """

    def __init__(self, element_id, src='', x=0, y=0):
        self.element_id = element_id
        self.src = src
        self.x = x
        self.y = y
        self.autoplay = False
        self.loop = False
        self.volume = 1.0
        self.show_icon = True
        self.slide = None

    def play(self):
        """Начать воспроизведение аудио."""
        pass

    def pause(self):
        """Поставить воспроизведение на паузу."""
        pass

    def stop(self):
        """Остановить воспроизведение и перемотать в начало."""
        pass

    def set_volume(self, volume):
        """
        Установить громкость воспроизведения.

        Args:
            volume (float): Значение громкости от 0.0 (тишина) до 1.0 (максимум).
        """
        self.volume = max(0.0, min(1.0, volume))

    def render(self, context):
        """
        Отрисовать иконку аудио на слайде.

        Args:
            context: Графический контекст для отрисовки.
        """
        if self.show_icon:
            context.draw_audio_icon(self.x, self.y, self.src)

    def to_dict(self):
        """
        Сериализовать элемент в словарь для сохранения.

        Returns:
            dict: Словарь с параметрами аудио-элемента.
        """
        return {
            'type': 'audio',
            'element_id': self.element_id,
            'src': self.src,
            'x': self.x, 'y': self.y,
            'autoplay': self.autoplay,
            'loop': self.loop,
            'volume': self.volume,
            'show_icon': self.show_icon,
        }
