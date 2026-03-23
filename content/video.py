# video.py — Видео-элемент на слайде

class Video:
    """Видео: нарезка голов, тренировочные моменты, обзор турнира."""

    def __init__(self, element_id, src='', x=0, y=0, width=320, height=180):
        self.element_id = element_id
        self.src = src          # путь к видеофайлу (mp4, webm) или URL
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.autoplay = False
        self.loop = False
        self.muted = False
        self.show_controls = True   # показывать элементы управления
        self.poster = None          # путь к превью-изображению
        self.start_time = 0         # начало воспроизведения в секундах
        self.end_time = None        # конец воспроизведения (None = до конца)
        self.slide = None

    def play(self):
        # Начать воспроизведение видео
        pass

    def pause(self):
        pass

    def seek(self, seconds):
        # Перемотать на указанную позицию
        pass

    def set_trim(self, start, end):
        # Задать диапазон воспроизведения
        self.start_time = start
        self.end_time = end

    def render(self, context):
        # Отрисовать видео или постер на слайде
        preview = self.poster if self.poster else self.src
        context.draw_video_frame(preview, self.x, self.y,
                                 self.width, self.height,
                                 show_controls=self.show_controls)

    def to_dict(self):
        return {
            'type': 'video',
            'element_id': self.element_id,
            'src': self.src,
            'x': self.x, 'y': self.y,
            'width': self.width, 'height': self.height,
            'autoplay': self.autoplay,
            'loop': self.loop,
            'muted': self.muted,
            'poster': self.poster,
            'start_time': self.start_time,
            'end_time': self.end_time,
        }
