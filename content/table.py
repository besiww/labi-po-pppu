# table.py — Таблица данных на слайде

class Table:
    """Таблица: статистика игроков, результаты турниров, финансовые данные."""

    def __init__(self, element_id, rows=3, cols=3, x=0, y=0, width=500, height=200):
        self.element_id = element_id
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rows = rows
        self.cols = cols
        # Двумерный массив ячеек
        self.cells = [[Cell(r, c) for c in range(cols)] for r in range(rows)]
        self.header_row = True      # первая строка — заголовок
        self.style = 'default'      # 'default', 'striped', 'academy_brand'
        self.slide = None

    def set_cell(self, row, col, value, bold=False, color=None, align='left'):
        # Установить значение и стиль ячейки
        cell = self.cells[row][col]
        cell.value = value
        cell.bold = bold
        if color:
            cell.color = color
        cell.align = align

    def set_column_width(self, col, width):
        # Задать ширину столбца
        for row in self.cells:
            row[col].width = width

    def load_from_data(self, headers, rows_data):
        # Заполнить таблицу из списка заголовков и строк данных
        # headers: ['Игрок', 'Голы', 'Передачи', 'Рейтинг']
        # rows_data: [['Иванов', 5, 3, 82], ...]
        self.cols = len(headers)
        self.rows = len(rows_data) + 1
        self.cells = [[Cell(r, c) for c in range(self.cols)] for r in range(self.rows)]
        for c, h in enumerate(headers):
            self.set_cell(0, c, h, bold=True)
        for r, row in enumerate(rows_data, start=1):
            for c, val in enumerate(row):
                self.set_cell(r, c, str(val))

    def render(self, context):
        # Отрисовать таблицу с ячейками и стилями
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
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.value = ''
        self.bold = False
        self.color = '#000000'
        self.align = 'left'
        self.width = None

    def to_dict(self):
        return {'row': self.row, 'col': self.col, 'value': self.value,
                'bold': self.bold, 'color': self.color, 'align': self.align}
