# table.py — Таблица данных на слайде

class Table:
    """
    Таблица данных на слайде презентации.

    Используется для отображения статистики игроков,
    результатов турниров и финансовых данных академии.

    Attributes:
        element_id (str): Уникальный идентификатор элемента.
        x (int): Координата X на слайде.
        y (int): Координата Y на слайде.
        width (int): Ширина таблицы в пикселях.
        height (int): Высота таблицы в пикселях.
        rows (int): Количество строк.
        cols (int): Количество столбцов.
        cells (list): Двумерный массив объектов Cell.
        header_row (bool): Первая строка является заголовком.
        style (str): Стиль таблицы: 'default', 'striped', 'academy_brand'.
        slide: Ссылка на родительский слайд.
    """

    def __init__(self, element_id, rows=3, cols=3, x=0, y=0, width=500, height=200):
        self.element_id = element_id
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rows = rows
        self.cols = cols
        self.cells = [[Cell(r, c) for c in range(cols)] for r in range(rows)]
        self.header_row = True
        self.style = 'default'
        self.slide = None

    def set_cell(self, row, col, value, bold=False, color=None, align='left'):
        """
        Установить значение и стиль ячейки таблицы.

        Args:
            row (int): Индекс строки (начиная с 0).
            col (int): Индекс столбца (начиная с 0).
            value (str): Значение ячейки.
            bold (bool): Жирное начертание. По умолчанию False.
            color (str, optional): Цвет текста в формате HEX.
            align (str): Выравнивание: 'left', 'center', 'right'.
        """
        cell = self.cells[row][col]
        cell.value = value
        cell.bold = bold
        if color:
            cell.color = color
        cell.align = align

    def set_column_width(self, col, width):
        """
        Задать ширину столбца.

        Args:
            col (int): Индекс столбца.
            width (int): Ширина в пикселях.
        """
        for row in self.cells:
            row[col].width = width

    def load_from_data(self, headers, rows_data):
        """
        Заполнить таблицу из списка заголовков и строк данных.

        Args:
            headers (list): Список заголовков столбцов.
            rows_data (list): Список строк, каждая строка — список значений.

        Example:
            table.load_from_data(
                ['Игрок', 'Голы', 'Передачи'],
                [['Иванов', 5, 3], ['Петров', 2, 7]]
            )
        """
        self.cols = len(headers)
        self.rows = len(rows_data) + 1
        self.cells = [[Cell(r, c) for c in range(self.cols)] for r in range(self.rows)]
        for c, h in enumerate(headers):
            self.set_cell(0, c, h, bold=True)
        for r, row in enumerate(rows_data, start=1):
            for c, val in enumerate(row):
                self.set_cell(r, c, str(val))

    def render(self, context):
        """
        Отрисовать таблицу на слайде.

        Args:
            context: Графический контекст для отрисовки.
        """
        cell_h = self.height / self.rows
        cell_w = self.width / self.cols
        for r in range(self.rows):
            for c in range(self.cols):
                cell = self.cells[r][c]
                cx = self.x + c * cell_w
                cy = self.y + r * cell_h
                is_header = self.header_row and r == 0
                context.draw_cell(cell.value, cx, cy, cell_w, cell_h,
                                  bold=cell.bold or is_header,
                                  color=cell.color, align=cell.align,
                                  striped=(self.style == 'striped' and r % 2 == 0))

    def to_dict(self):
        """
        Сериализовать элемент в словарь для сохранения.

        Returns:
            dict: Словарь с параметрами таблицы.
        """
        return {
            'type': 'table',
            'element_id': self.element_id,
            'x': self.x, 'y': self.y,
            'width': self.width, 'height': self.height,
            'rows': self.rows, 'cols': self.cols,
            'cells': [[c.to_dict() for c in row] for row in self.cells],
            'header_row': self.header_row,
            'style': self.style,
        }


class Cell:
    """
    Ячейка таблицы.

    Attributes:
        row (int): Индекс строки.
        col (int): Индекс столбца.
        value (str): Текстовое значение ячейки.
        bold (bool): Жирное начертание.
        color (str): Цвет текста в формате HEX.
        align (str): Выравнивание текста.
        width (int): Ширина ячейки в пикселях или None.
    """

    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.value = ''
        self.bold = False
        self.color = '#000000'
        self.align = 'left'
        self.width = None

    def to_dict(self):
        """
        Сериализовать ячейку в словарь.

        Returns:
            dict: Словарь с параметрами ячейки.
        """
        return {'row': self.row, 'col': self.col, 'value': self.value,
                'bold': self.bold, 'color': self.color, 'align': self.align}
