# scouting_panel.py — Панель скаутинга

class ScoutingPanel:
    """Панель поиска и оценки новых игроков для академии."""

    def __init__(self, scout_service):
        self.scout_service = scout_service
        self.filters = {}
        self.results = []

    def set_filter(self, position=None, age_range=None, min_rating=None, region=None):
        # Установить фильтры поиска игроков
        self.filters = {
            'position': position,
            'age_range': age_range,
            'min_rating': min_rating,
            'region': region,
        }

    def search(self):
        # Запустить поиск по заданным фильтрам
        self.results = self.scout_service.find_players(**self.filters)
        self._render_results()

    def _render_results(self):
        # Отобразить список найденных игроков в таблице
        for player in self.results:
            self._render_player_row(player)

    def _render_player_row(self, player):
        # Строка: имя, возраст, позиция, рейтинг, стоимость
        pass

    def on_player_select(self, player):
        # Открыть карточку игрока для детального просмотра
        PlayerPropertiesPanel(player).show()

    def recruit(self, player):
        # Предложить контракт выбранному игроку
        if self.scout_service.can_afford(player):
            self.scout_service.sign(player)
        else:
            self._show_budget_warning()

    def _show_budget_warning(self):
        # Показать предупреждение о нехватке бюджета
        pass
