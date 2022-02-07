import sqlite3


class database:
    def __init__(self, discord = None, userid = None):
        self.conn = sqlite3.connect('db.sqlite')
        self.cur = self.conn.cursor()
        self.userid = userid
        self.discord = discord
        self.cur.execute('''CREATE TABLE IF NOT EXISTS members
        (id INTEGER PRIMARY KEY, discord TEXT, user_id TEXT, money INT, score INT, rank TEXT)''')


    def add_user(self):
        if self.check_user():
            return False
        else:
            self.cur.execute("""INSERT INTO members VALUES(NULL, ?, ?, ?, ?, ?);""", (str(self.discord), self.userid, 0, 0, 'На калибровке'))
            self.conn.commit()

    def database_members(self):
        sqlite_select_query = """SELECT * FROM members"""
        self.cur.execute(sqlite_select_query)
        record = self.cur.fetchall()
        for i in record:
            if int(i[2]) == self.userid:
                return i
        return False

    def check_user(self):
        sqlite_select_query = """SELECT * FROM members"""
        self.cur.execute(sqlite_select_query)
        record = self.cur.fetchall()
        for i in record:
            if int(i[2]) == self.userid:
                return True
        return False
