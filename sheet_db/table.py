from gspread.exceptions import WorksheetNotFound
from sheet_db.utils import ALPHA_COLS


class SheetTable(object):
    def __init__(self, table_name, db_sheet, upsert=False, opt=None):
        self.table_name = table_name
        self.db = db_sheet
        self.table = self._get_table(upsert, opt)

    def _get_table(self, upsert, opt):
        try:
            table = self.db.worksheet(self.table_name)
            self.col_count = table.col_count
            self.row_count = table.row_count
            _cols = [table.cell(col=n, row=1) for n in range(1, self.col_count+1)]
            if len(_cols) == 1 and _cols[0] == '':
                self.cols = []
            else:
                self.cols = _cols

            return table
        except WorksheetNotFound:
            if upsert:
                table = self.db.add_worksheet(
                    table_name,
                    rows=1,
                    cols=1
                )
                self.col_count = 1
                self.rows_count = 1
                self.cols = []

                return table
            raise
        except:
            raise
    
    def create(self):
        pass

    def read(self):
        pass
    
    def update(self):
        pass
    
    def delete(self):
        pass