from project.table.table import Table


class OutsideTable(Table):
    def min_table_number(self):
        return 51

    def max_table_number(self):
        return 100

    def table_number_error_message(self):
        return "Outside table's number must be between 51 and 100 inclusive!"
