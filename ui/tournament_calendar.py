# tournament_calendar.py — Календарь турниров

class TournamentCalendar:
    """Панель с расписанием и историей турниров академии."""

    def __init__(self, schedule):
        self.schedule = schedule  # список объектов Tournament
        self.selected_month = None

    def show_month(self, month, year):
        # Отфильтровать турниры по месяцу и году
        self.selected_month = (month, year)
        events = [t for t in self.schedule if t.date.month == month and t.date.year == year]
        self._render_calendar_grid(events)

    def _render_calendar_grid(self, events):
        # Нарисовать сетку календаря и разместить события по датам
        for day in range(1, 32):
            day_events = [e for e in events if e.date.day == day]
            if day_events:
                self._highlight_day(day, day_events)

    def _highlight_day(self, day, events):
        # Выделить день с турниром и показать подсказку
        pass

    def on_event_click(self, tournament):
        # Открыть детальную карточку турнира
        TournamentDetailPanel(tournament).show()

    def navigate(self, direction):
        # Переключить месяц вперёд/назад
        # direction: +1 или -1
        pass
