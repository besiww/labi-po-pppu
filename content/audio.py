# audio.py — Аудио-элемент на слайде

class Audio:
    """Аудио: гимн академии, звуковое сопровождение презентации."""

    def __init__(self, element_id, src='', x=0, y=0):
        self.element_id = element_id
        self.src = src          # путь к аудиофайлу (mp3, wav, ogg)
        self.x = x
        self.y = y
        self.autoplay = False   # воспроизводить автоматически при показе слайда
        self.loop = False       # зациклить воспроизведение
        self.volume = 1.0       # громкость 0.0–1.0
        self.show_icon = True   # показывать иконку аудио на слайде
        self.slide = None

    def play(self):
        # Начать воспроизведение аудио
        pass

    def pause(self):
        # Поставить на паузу
        pass

    def stop(self):
        # Остановить и перемотать в начало
        pass

    def set_volume(self, volume):
        # Установить громкость (0.0–1.0)
        self.volume = max(0.0, min(1.0, volume))

    def render(self, context):
        # Отрисовать иконку аудио на слайде (если show_icon=True)
        if self.show_icon:
            context.draw_audio_icon(self.x, self.y, self.src)

    def to_dict(self):
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
