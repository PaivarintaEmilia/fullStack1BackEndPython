class User:
    def __init__(self, username, password, _id=None):
        self.id = _id
        self.username = username
        self.password = password


    def to_json(self):
        return {
            'id': self.id,
            'username': self.username,
            'password': self.password,
        }


class Income:
    def __init__(self, user_id, note, income_amount, income_date, _id=None):
        self.id = _id
        self.user_id = user_id
        self.note = note
        self.income_amount = income_amount
        self.income_date = income_date

    def to_json(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'note': self.note,
            'income_amount': self.income_amount,
            'income_date': self.income_date
        }


class ExpenseCategory:
    def __init__(self, user_id, category_name, user_defined=0, _id=None):
        self.id = _id
        self.user_id = user_id
        self.category_name = category_name
        self.user_defined = user_defined

    def to_json(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'category_name': self.category_name,
            'user_defined': self.user_defined
        }


class Expense:
    def __init__(self, user_id, category_id, expense_amount, note, expense_date, _id=None):
        self.id = _id
        self.user_id = user_id
        self.category_id = category_id
        self.expense_amount = expense_amount
        self.note = note
        self.expense_date = expense_date

    def to_json(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'category_id': self.category_id,
            'expense_amount': self.expense_amount,
            'note': self.note,
            'expense_date': self.expense_date
        }
