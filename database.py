import sqlite3 as sq


class UserDatabase:
    def __init__(self):
        self.base = sq.connect("users.db")
        self.cur = self.base.cursor()
        self.base.execute('CREATE TABLE IF NOT EXISTS users(user_id TEXT, city TEXT, state TEXT)')

    def add_user(self, user_id, city=None, state=None):
        self.cur.execute('INSERT INTO users VALUES (?, ?, ?)', (user_id, city, state))
        self.base.commit()

    def set_user_city(self, user_id, city=None):
        self.cur.execute('UPDATE users SET city="{}" WHERE user_id="{}"'.format(city, user_id))
        self.base.commit()

    def set_user_state(self, user_id, state=None):
        self.cur.execute('UPDATE users SET state="{}" WHERE user_id="{}"'.format(state, user_id))
        self.base.commit()

    def get_user_by_id(self, user_id):
        user = self.cur.execute('SELECT user_id, city, state FROM users WHERE user_id="{}"'.format(user_id)).fetchall()
        if not user:
            return None
        return {"city": user[0][1], "state": user[0][2]}
