import sqlite3


def create_register_user():
    try:
        sqlite_connection = sqlite3.connect('TelegramBotFH.db')  # Ниже код на SQL языке
        sqlite_create_table_query = '''CREATE TABLE IF NOT EXISTS register_clients (
                                    UserID INTEGER NOT NULL UNIQUE,
                                    Name TEXT,
                                    User_Name text UNIQUE,
                                    Registration text);'''

        cursor = sqlite_connection.cursor()
        print("База данных подключена к SQLite")
        cursor.execute(sqlite_create_table_query)
        sqlite_connection.commit()
        print("Таблица SQLite создана")

        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при подключении к sqlite", error)
    finally:
        if (sqlite_connection):
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")


def upgrade_register_user(user_information: dict):
    try:
        sqlite_connection = sqlite3.connect('TelegramBotFH.db')
        cursor = sqlite_connection.cursor()
        cursor.execute('SELECT * FROM register_clients WHERE UserID=?', (user_information['UserID'],))
        user_id = cursor.fetchone()

        if user_id:
            sqlite_insert_change_with_param = f"""UPDATE register_clients SET Name=?, User_Name=?, Registration=?
            WHERE UserID=?"""
            data_tuple = tuple(user_id)
            print(data_tuple)

        else:
            sqlite_insert_change_with_param = """INSERT INTO register_clients (UserID, Name, User_Name, Registration)
                                                                               VALUES (?, ?, ?, ?);"""
            data_tuple = tuple(user_information.values())

        cursor.execute(sqlite_insert_change_with_param, data_tuple)

        sqlite_connection.commit()
        cursor.close()
        sqlite_connection.close()


    except sqlite3.Error as error:
        print(f'ru: Ошибка в db_client -> Функция upgrade_register_user {error}\n')
        # logging.warning(f'Ошибка в IC_UserInformation {error}\n')
