# video.py — Видео-элемент на слайде

class Video:
    """
    Видео-элемент презентации академии.

    Используется для вставки видеозаписей на слайд:
    нарезка голов, тренировочные моменты, обзор турнира.

    Attributes:
        element_id (str): Уникальный идентификатор элемента.
        src (str): Путь к видеофайлу (mp4, webm) или URL.
        x (int): Координата X на слайде.
        y (int): Координата Y на слайде.
        width (int): Ширина видео в пикселях.
        height (int): Высота видео в пикселях.
        autoplay (bool): Воспроизводить автоматически.
        loop (bool): Зациклить воспроизведение.
        muted (bool): Отключить звук.
        show_controls (bool): Показывать элементы управления.
        poster (str): Путь к превью-изображению.
        start_time (int): Начало воспроизведения в секундах.
        end_time (int): Конец воспроизведения в секундах (None — до конца).
        slide: Ссылка на родительский слайд.
    """

    def __init__(self, element_id, src='', x=0, y=0, width=320, height=180):
        self.element_id = element_id
        self.src = src
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.autoplay = False
        self.loop = False
        self.muted = False
        self.show_controls = True
        self.poster = None
        self.start_time = 0
        self.end_time = None
        self.slide = None

    def play(self):
        """Начать воспроизведение видео."""
        pass

    def pause(self):
        """Поставить воспроизведение на паузу."""
        pass

    def seek(self, seconds):
        """
        Перемотать видео на указанную позицию.

        Args:
            seconds (int): Позиция в секундах от начала видео.
        """
        pass

    def set_trim(self, start, end):
        """
        Задать диапазон воспроизведения видео.

        Args:
            start (int): Начальная позиция в секундах.
            end (int): Конечная позиция в секундах.
        """
        self.start_time = start
        self.end_time = end

    def render(self, context):
        """
        Отрисовать видео или постер на слайде.

        Args:
            context: Графический контекст для отрисовки.
        """
        preview = self.poster if self.poster else self.src
        context.draw_video_frame(preview, self.x, self.y,
                                 self.width, self.height,
                                 show_controls=self.show_controls)

    def to_dict(self):
        """
        Сериализовать элемент в словарь для сохранения.

        Returns:
            dict: Словарь с параметрами видео-элемента.
        """
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
