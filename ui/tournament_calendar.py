# tournament_calendar.py — Календарь турниров

class TournamentCalendar:
    """
    Панель с расписанием и историей турниров академии.

    Отображает календарную сетку с отмеченными датами турниров,
    позволяет переключаться между месяцами и открывать детали события.

    Attributes:
        schedule (list): Список объектов Tournament.
        selected_month (tuple): Текущий отображаемый месяц (month, year) или None.
    """

    def __init__(self, schedule):
        self.schedule = schedule
        self.selected_month = None

    def show_month(self, month, year):
        """
        Отобразить турниры за указанный месяц.

        Args:
            month (int): Номер месяца (1–12).
            year (int): Год.
        """
        self.selected_month = (month, year)
        events = [t for t in self.schedule if t.date.month == month and t.date.year == year]
        self._render_calendar_grid(events)

    def _render_calendar_grid(self, events):
        """
        Нарисовать сетку календаря с событиями.

        Args:
            events (list): Список турниров для отображения.
        """
        for day in range(1, 32):
            day_events = [e for e in events if e.date.day == day]
            if day_events:
                self._highlight_day(day, day_events)

    def _highlight_day(self, day, events):
        """
        Выделить день с турниром и показать подсказку.

        Args:
            day (int): День месяца.
            events (list): Список турниров в этот день.
        """
        pass

    def on_event_click(self, tournament):
        """
        Открыть детальную карточку турнира.

        Args:
            tournament: Объект турнира.
        """
        TournamentDetailPanel(tournament).show()

    def navigate(self, direction):
        """
        Переключить отображаемый месяц.

        Args:
            direction (int): +1 для следующего месяца, -1 для предыдущего.
        """
        pass
