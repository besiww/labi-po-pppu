# career_manager.py — Менеджер карьеры

import json

class CareerManager:
    """Управление карьерой: создание, сохранение, загрузка."""

    def __init__(self):
        self.current_career = None

    def new_career(self, academy_name, manager_name, difficulty='normal'):
        # Создать новую карьеру с начальными параметрами
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
        # Начальный бюджет зависит от сложности
        budgets = {'easy': 5_000_000, 'normal': 2_000_000, 'hard': 500_000}
        return budgets.get(difficulty, 2_000_000)

    def save(self, filepath):
        # Сериализовать состояние карьеры в JSON и записать на диск
        if not self.current_career:
            raise ValueError("Нет активной карьеры для сохранения")
        data = self.current_career.to_dict()
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    def load(self, filepath):
        # Загрузить карьеру из файла сохранения
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        self.current_career = Career.from_dict(data)
        return self.current_career

    def get_simulation_state(self):
        # Вернуть текущее состояние симуляции (дата, сезон, очередь событий)
        if not self.current_career:
            return None
        return {
            'season': self.current_career.season,
            'date': str(self.current_career.current_date),
            'pending_events': self.current_career.event_queue,
        }


class Career:
    """Модель карьеры тренера в академии."""

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
        # Инициализировать стартовый состав, расписание и начальную дату
        self.current_date = '2024-07-01'
        self.players = self._generate_starting_squad()
        self.event_queue = self._generate_season_schedule()

    def _generate_starting_squad(self):
        # Сгенерировать стартовый состав из молодых игроков
        # Возвращает список объектов Player
        return []

    def _generate_season_schedule(self):
        # Сгенерировать расписание турниров и тренировок на сезон
        return []

    def to_dict(self):
        # Сериализовать карьеру в словарь для сохранения
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
        # Восстановить карьеру из словаря
        career = cls(
            academy_name=data['academy_name'],
            manager_name=data['manager_name'],
            difficulty=data['difficulty'],
            season=data['season'],
            budget=data['budget'],
        )
        career.current_date = data['current_date']
        career.results = data.get('results', [])
        # career.players = [Player.from_dict(p) for p in data.get('players', [])]
        return career
