# career_manager.py — Менеджер карьеры

import json

class CareerManager:
    """
    Менеджер карьеры тренера теннисной академии.

    Обеспечивает создание новой карьеры, сохранение и загрузку
    прогресса, а также доступ к текущему состоянию симуляции.

    Attributes:
        current_career (Career): Текущая активная карьера или None.
    """

    def __init__(self):
        self.current_career = None

    def new_career(self, academy_name, manager_name, difficulty='normal'):
        """
        Создать новую карьеру с начальными параметрами.

        Args:
            academy_name (str): Название академии.
            manager_name (str): Имя менеджера.
            difficulty (str): Сложность: 'easy', 'normal', 'hard'.

        Returns:
            Career: Созданный объект карьеры.
        """
        self.current_career = Career(
            academy_name=academy_name,
            manager_name=manager_name,
            difficulty=difficulty,
            season=1,
            budget=self._starting_budget(difficulty),
        )
        self.current_career.initialize()
        return self.current_career

    def _starting_budget(self, difficulty):
        """
        Определить начальный бюджет по уровню сложности.

        Args:
            difficulty (str): Уровень сложности.

        Returns:
            int: Начальный бюджет в условных единицах.
        """
        budgets = {'easy': 5_000_000, 'normal': 2_000_000, 'hard': 500_000}
        return budgets.get(difficulty, 2_000_000)

    def save(self, filepath):
        """
        Сохранить текущую карьеру в файл.

        Args:
            filepath (str): Путь к файлу сохранения.

        Raises:
            ValueError: Если нет активной карьеры для сохранения.
        """
        if not self.current_career:
            raise ValueError("Нет активной карьеры для сохранения")
        data = self.current_career.to_dict()
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    def load(self, filepath):
        """
        Загрузить карьеру из файла сохранения.

        Args:
            filepath (str): Путь к файлу сохранения.

        Returns:
            Career: Загруженный объект карьеры.
        """
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        self.current_career = Career.from_dict(data)
        return self.current_career

    def get_simulation_state(self):
        """
        Получить текущее состояние симуляции.

        Returns:
            dict: Словарь с сезоном, датой и очередью событий,
                  или None если карьера не активна.
        """
        if not self.current_career:
            return None
        return {
            'season': self.current_career.season,
            'date': str(self.current_career.current_date),
            'pending_events': self.current_career.event_queue,
        }


class Career:
    """
    Модель карьеры тренера в теннисной академии.

    Хранит все данные карьеры: состав игроков, расписание,
    финансы, историю результатов и очередь событий.

    Attributes:
        academy_name (str): Название академии.
        manager_name (str): Имя менеджера.
        difficulty (str): Уровень сложности.
        season (int): Текущий сезон.
        budget (int): Текущий бюджет.
        current_date (str): Текущая дата симуляции в формате YYYY-MM-DD.
        event_queue (list): Очередь предстоящих событий.
        players (list): Список игроков академии.
        results (list): История результатов матчей и турниров.
    """

    def __init__(self, academy_name, manager_name, difficulty, season, budget):
        self.academy_name = academy_name
        self.manager_name = manager_name
        self.difficulty = difficulty
        self.season = season
        self.budget = budget
        self.current_date = None
        self.event_queue = []
        self.players = []
        self.results = []

    def initialize(self):
        """Инициализировать стартовый состав, расписание и начальную дату."""
        self.current_date = '2024-07-01'
        self.players = self._generate_starting_squad()
        self.event_queue = self._generate_season_schedule()

    def _generate_starting_squad(self):
        """
        Сгенерировать стартовый состав из молодых игроков.

        Returns:
            list: Список объектов Player.
        """
        return []

    def _generate_season_schedule(self):
        """
        Сгенерировать расписание турниров и тренировок на сезон.

        Returns:
            list: Список событий сезона.
        """
        return []

    def to_dict(self):
        """
        Сериализовать карьеру в словарь для сохранения.

        Returns:
            dict: Словарь с данными карьеры.
        """
        return {
            'academy_name': self.academy_name,
            'manager_name': self.manager_name,
            'difficulty': self.difficulty,
            'season': self.season,
            'budget': self.budget,
            'current_date': self.current_date,
            'players': [p.to_dict() for p in self.players],
            'results': self.results,
        }

    @classmethod
    def from_dict(cls, data):
        """
        Восстановить карьеру из словаря.

        Args:
            data (dict): Словарь с данными карьеры.

        Returns:
            Career: Восстановленный объект карьеры.
        """
        career = cls(
            academy_name=data['academy_name'],
            manager_name=data['manager_name'],
            difficulty=data['difficulty'],
            season=data['season'],
            budget=data['budget'],
        )
        career.current_date = data['current_date']
        career.results = data.get('results', [])
        return career
