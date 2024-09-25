class Condition:
    def __init__(self, key, operator, value):
        self.key = key
        self.operator = operator
        self.value = value

    def to_sql_clause(self):
        if self.operator == 'LIKE':
            return f"{self.key} {self.operator} '%{self.value}%'"
        else:
            return f"{self.key} {self.operator} '{self.value}'"
