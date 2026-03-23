# toolbar.py — Тулбар с вкладками навигации

class MainToolbar:
    """Главный тулбар приложения с вкладками разделов."""

    TABS = ['Главная', 'Игроки', 'Турниры', 'Тренировки', 'Финансы', 'Инфраструктура']

    def __init__(self, app):
        self.app = app
        self.active_tab = 'Главная'

    def render(self):
        # Отрисовать тулбар с кнопками вкладок
        for tab in self.TABS:
            is_active = (tab == self.active_tab)
            self._draw_tab(tab, is_active)

    def _draw_tab(self, label, is_active):
        # Нарисовать кнопку вкладки, выделить активную
        pass

    def on_tab_click(self, tab_name):
        # Переключить активную вкладку и загрузить соответствующую панель
        if tab_name not in self.TABS:
            return
        self.active_tab = tab_name
        self._load_panel(tab_name)

    def _load_panel(self, tab_name):
        # Маппинг вкладок на панели
        panels = {
            'Главная':        lambda: AcademyDashboard(self.app.academy).load(),
            'Игроки':         lambda: ScoutingPanel(self.app.scout_service).search(),
            'Турниры':        lambda: TournamentCalendar(self.app.schedule).show_month(*self.app.current_date),
            'Тренировки':     lambda: TrainingPanel(self.app.academy).load(),
            'Финансы':        lambda: FinancePanel(self.app.academy).load(),
            'Инфраструктура': lambda: AcademyPropertiesPanel(self.app.academy).show(),
        }
        panels[tab_name]()
