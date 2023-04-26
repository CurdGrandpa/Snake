import sqlite3

db_name = 'SnakeGame.db'


def add_table(cursor):
    cursor.execute("""CREATE TABLE IF NOT EXISTS game
        (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,
        player_name VARCHAR(45),
        result INTEGER
        )""")


def add_row(player_name, result):
    with sqlite3.connect(db_name) as connection:
        cursor = connection.cursor()

        add_table(cursor)
        cursor.execute("""INSERT INTO game (player_name, result) VALUES (?, ?)""", (player_name, result))
    rows_cleaning()


def get_result(cursor = None):
    connection, all_results = None, None
    if (cursor == None):
        connection = sqlite3.connect(db_name)
        cursor = connection.cursor()
    cursor.execute("SELECT * FROM game;")
    all_results = cursor.fetchall()
    if (cursor == None):
        connection.commit()
        cursor.close()
        connection.close()
    return all_results


def rows_cleaning():
    with sqlite3.connect(db_name) as connection:
        cursor = connection.cursor()

        rows = get_result()
        for i in range(0, len(rows)):
            for j in range(i, len(rows)):
                if (rows[i][2] < rows[j][2]):
                    rows[i], rows[j] = rows[j], rows[i]
        for i in range (10, len(rows)):
            cursor.execute("""DELETE FROM game WHERE id = ?""", (rows[i][0],))
