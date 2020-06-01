
class DB:
    self.server = None
    self.port = None
    self.user = None
    self.password = None
    self.db = db
    def __init__(self):

    def add_to_table(self, table, row):

    def read_from_table(self, param, table, cond):
        query = "SELECT %s FROM %s%s;" %(param, table, cond)
        
    def remove_from_table(self, table, row):
