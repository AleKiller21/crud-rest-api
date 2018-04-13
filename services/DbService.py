from pymysql import connect


class DbService:
    """Singleton service used to handle all database operations"""

    db = None

    @staticmethod
    def execute(query, operation, *params):
        if not DbService.db:
            DbService.db = connect(host='localhost', user='root', password='ajfz1995', database='cruddemo')

        cursor = DbService.db.cursor()

        try:
            rows_affected = cursor.execute(query, params)
            if operation == 'r':
                result = cursor.fetchall()
                cursor.close()
                return result

            else:
                DbService.db.commit()
                cursor.close()
                return rows_affected

        except Exception as e:
            DbService.db.rollback()
            print(e)
            raise Exception('An error has ocurred. Please try again later')
