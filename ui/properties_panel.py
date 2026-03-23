# properties_panel.py — Панель свойств игрока и академии

class PlayerPropertiesPanel:
    """Детальная карточка игрока: характеристики, статистика, контракт."""

    def __init__(self, player):
        self.player = player

    def show(self):
        # Отобразить панель свойств игрока
        self._render_header()
        self._render_stats()
        self._render_contract_info()
        self._render_training_history()

    def _render_header(self):
        # Имя, фото, позиция, возраст, национальность
        pass

    def _render_stats(self):
        # Характеристики: скорость, техника, физика, ментальность и т.д.
        stats = self.player.get_stats()
        for stat_name, value in stats.items():
            self._draw_stat_bar(stat_name, value)

    def _draw_stat_bar(self, name, value):
        # Нарисовать полосу прогресса для характеристики (0–100)
        pass

    def _render_contract_info(self):
        # Срок контракта, зарплата, статус
        pass

    def _render_training_history(self):
        # История тренировок и динамика роста характеристик
        pass

    def edit(self):
        # Перейти в режим редактирования (для тренера)
        pass


class AcademyPropertiesPanel:
    """Панель свойств академии: инфраструктура, репутация, финансы."""

    def __init__(self, academy):
        self.academy = academy

    def show(self):
        self._render_general_info()
        self._render_infrastructure()
        self._render_finances()

    def _render_general_info(self):
        # Название, лига, страна, год основания, репутация
        pass

    def _render_infrastructure(self):
        # Стадион, тренировочная база, медцентр — уровни и состояние
        for facility in self.academy.facilities:
            self._draw_facility_card(facility)

    def _draw_facility_card(self, facility):
        # Карточка объекта: название, уровень, стоимость апгрейда
        pass

    def _render_finances(self):
        # Бюджет, доходы, расходы, трансферный баланс
        pass
