# dashboard.py — Дашборд академии

class AcademyDashboard:
    """Главная панель академии. Отображает ключевые показатели."""

    def __init__(self, academy):
        self.academy = academy
        self.widgets = []

    def load(self):
        # Загрузить данные академии и инициализировать виджеты
        self._init_widgets()
        self.refresh()

    def _init_widgets(self):
        # Создать виджеты: бюджет, рейтинг, список игроков, ближайшие турниры
        self.widgets = [
            BudgetWidget(self.academy.budget),
            RatingWidget(self.academy.rating),
            PlayerListWidget(self.academy.players),
            UpcomingTournamentsWidget(self.academy.schedule),
        ]

    def refresh(self):
        # Обновить все виджеты актуальными данными
        for widget in self.widgets:
            widget.update()

    def render(self):
        # Отрисовать дашборд на экране
        for widget in self.widgets:
            widget.draw()
