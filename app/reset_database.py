from database.database import Database


if __name__ == '__main__':
    database = Database()
    database.reset()
    print("[DATABASE] Reset database.")