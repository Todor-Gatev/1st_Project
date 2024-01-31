from project.table.table import Table


class InsideTable(Table):
    def min_table_number(self):
        return 1

    def max_table_number(self):
        return 50

    def table_number_error_message(self):
        return "Inside table's number must be between 1 and 50 inclusive!"
