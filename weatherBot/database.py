import logging
import sqlite3
from typing import Any, NoReturn

logger = logging.getLogger('TGBot')


class Database:
    def __init__(self, filename: str):
        self.con = sqlite3.connect(filename)

    def execute(self, sql, fetchone: bool = True) -> list | Any:
        cur = self.con.cursor()
        cur.execute(sql)
        data = cur.fetchall()
        if not fetchone:
            data = cur.fetchone()
        cur.close()
        self.con.commit()
        return data

    def create(self) -> NoReturn:
        sql = '''CREATE TABLE IF NOT EXISTS data (id INTEGER PRIMARY KEY,
                                                  user_id INT NOT NULL,
                                                  city INT NOT NULL);'''
        self.execute(sql)

    def close(self) -> NoReturn:
        self.con.close()

    def get_users(self) -> list:
        sql = '''SELECT user_id, city FROM data'''
        data = self.execute(sql)
        return data

    def get_cities(self, user_id: int) -> list:
        sql = f'''SELECT user_id, city FROM data WHERE user_id = {user_id}'''
        data = self.execute(sql)
        return [i[1] for i in data]

    def add(self, user_id: int, city: str) -> NoReturn:
        sql = f'''INSERT INTO data (`user_id`, city) VALUES ({user_id}, '{city}')'''
        self.execute(sql)
        logger.info(f'Add new user({user_id}) - city({city})')
