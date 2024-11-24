import sqlite3


class Note:
    def __init__(self, name, phone, description):
        self.name = name
        self.phone = phone
        self.description = description

    def return_into_db(self):
        return f'"{self.name}", "{self.phone}", "{self.description}"'



class DBManager:
    def __init__(self):
        self.connection = sqlite3.connect('phone_manager.sl3')
        self.cursor = self.connection.cursor()

        self.create_table()

    def create_table(self):
        try:
            self.cursor.execute('CREATE TABLE phone (name TEXT, phone_number TEXT, description TEXT);')
            self.connection.commit()
            print('База создана!')
        except sqlite3.OperationalError:
            print('Подключение к базе успешное!')

    def add_note(self, note: Note):
        self.cursor.execute(f'INSERT INTO phone VALUES ({note.return_into_db()});')
        self.connection.commit()

    def return_all(self):
        self.cursor.execute('SELECT name, phone_number, description FROM phone;')

        return self.cursor.fetchall()

    def return_from_name(self, name):
        self.cursor.execute(f'SELECT name, phone_number, description FROM phone WHERE name="{name}";')

        return self.cursor.fetchall()





manager = DBManager()

#note1 = Note('Яна', "+123456789", "Колега")
#note2 = Note('Сергей', "+123123123", "Брат")

#manager.add_note(note2)
#manager.add_note(note2)

#print(manager.return_all())

print(manager.return_from_name('Сергей'))