import sqlite3


class database:
    def __init__(self, discord = None, userid = None):
        self.conn = sqlite3.connect('db.sqlite')
        self.cur = self.conn.cursor()
        self.userid = userid
        self.discord = discord
        self.cur.execute('''CREATE TABLE IF NOT EXISTS members
        (id INTEGER PRIMARY KEY, discord TEXT, user_id TEXT, money INT, score INT, rank TEXT, answer BOOLEAN)''')
        self.cur.execute('''CREATE TABLE IF NOT EXISTS quiz
                (id INTEGER PRIMARY KEY, correct_answer TEXT, answer BOOLEAN)''')
        self.conn.commit()

    def add_user(self):
        if self.check_user():
            return False
        else:
            self.cur.execute("""INSERT INTO members VALUES(NULL, ?, ?, ?, ?, ?, ?);""", (str(self.discord), self.userid, 0, 0, 'На калибровке', False))
            self.conn.commit()

    def add_quiz(self, correct_quiz):
        sqlite_select_query = """SELECT * FROM members"""
        self.cur.execute(sqlite_select_query)
        record = self.cur.fetchall()
        for i in record:
            self.cur.execute(f"""UPDATE members set answer = (?) where user_id = {i[2]}""", (False,))
        sqlite_select_query = """SELECT * FROM quiz"""
        self.cur.execute(sqlite_select_query)
        record = self.cur.fetchall()
        if not record:
            self.cur.execute("""INSERT INTO quiz VALUES(NULL, ?, ?);""", (correct_quiz, False))
            self.conn.commit()
        else:
            self.cur.execute("""UPDATE quiz set correct_answer = (?) where id = 1""", (correct_quiz,))
            self.cur.execute("""UPDATE quiz set answer = (?) where id = 1""", (False,))
            self.conn.commit()

    def close_quiz(self):
        self.cur.execute("""UPDATE quiz set answer = (?) where id = 1""", (True,))
        self.conn.commit()

    def close_quiz_user(self):
        self.cur.execute(f"""UPDATE members set answer = (?) where user_id = {self.userid}""", (True,))
        self.conn.commit()

    def isQuiz(self):
        sqlite_select_query = """SELECT * FROM quiz"""
        self.cur.execute(sqlite_select_query)
        record = self.cur.fetchall()
        return record[0][2]

    def isQuizUser(self):
        sqlite_select_query = """SELECT * FROM members"""
        self.cur.execute(sqlite_select_query)
        record = self.cur.fetchall()
        for row in record:
            if int(row[2]) == self.userid:
                return row[6]

    def get_correct_quiz(self):
        sqlite_select_query = """SELECT * FROM quiz"""
        self.cur.execute(sqlite_select_query)
        record = self.cur.fetchall()
        return record[0][1]

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

