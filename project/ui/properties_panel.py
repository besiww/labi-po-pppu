# properties_panel.py — Панель свойств игрока и академии

class PlayerPropertiesPanel:
    """
    Детальная карточка игрока.

    Отображает характеристики, статистику, историю тренировок
    и информацию о контракте выбранного игрока.

    Attributes:
        player: Объект игрока с данными.
    """

    def __init__(self, player):
        self.player = player

    def show(self):
        """Отобразить панель свойств игрока."""
        self._render_header()
        self._render_stats()
        self._render_contract_info()
        self._render_training_history()

    def _render_header(self):
        """Отрисовать заголовок: имя, фото, позиция, возраст, национальность."""
        pass

    def _render_stats(self):
        """Отрисовать характеристики игрока в виде полос прогресса."""
        stats = self.player.get_stats()
        for stat_name, value in stats.items():
            self._draw_stat_bar(stat_name, value)

    def _draw_stat_bar(self, name, value):
        """
        Нарисовать полосу прогресса для характеристики.

        Args:
            name (str): Название характеристики.
            value (int): Значение от 0 до 100.
        """
        pass

    def _render_contract_info(self):
        """Отрисовать информацию о контракте: срок, зарплата, статус."""
        pass

    def _render_training_history(self):
        """Отрисовать историю тренировок и динамику роста характеристик."""
        pass

    def edit(self):
        """Перейти в режим редактирования карточки игрока."""
        pass


class AcademyPropertiesPanel:
    """
    Панель свойств академии.

    Отображает общую информацию, состояние инфраструктуры
    и финансовые показатели академии.

    Attributes:
        academy: Объект академии с данными.
    """

    def __init__(self, academy):
        self.academy = academy

    def show(self):
        """Отобразить панель свойств академии."""
        self._render_general_info()
        self._render_infrastructure()
        self._render_finances()

    def _render_general_info(self):
        """Отрисовать общую информацию: название, лига, страна, репутация."""
        pass

    def _render_infrastructure(self):
        """Отрисовать карточки объектов инфраструктуры академии."""
        for facility in self.academy.facilities:
            self._draw_facility_card(facility)

    def _draw_facility_card(self, facility):
        """
        Отрисовать карточку объекта инфраструктуры.

        Args:
            facility: Объект инфраструктуры (стадион, база, медцентр).
        """
        pass

    def _render_finances(self):
        """Отрисовать финансовые показатели: бюджет, доходы, расходы."""
        pass
