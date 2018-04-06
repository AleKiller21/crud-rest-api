from pymysql import connect


class DbService:
    """Singleton service used to handle all database operations"""

    db = None

    @staticmethod
    def execute(query, operation, *params):
        if not DbService.db:
            DbService.db = connect(host='localhost', user='root', password='sandals', database='cruddemo')

        cursor = DbService.db.cursor()

        try:
            cursor.execute(query, params)
            if operation == 'r':
                result = cursor.fetchall()
                cursor.close()
                return result

            else:
                DbService.db.commit()
                cursor.close()
                return DbService.__generate_write_response(operation)

        except Exception as e:
            DbService.db.rollback()
            print(e)
            return "fallo"

    @staticmethod
    def __generate_write_response(operation):
        if operation == 'c':
            return {'message': "User created"}
        elif operation == 'u':
            return {'message': "User has been updated"}
        else:
            return {'message': "User has been deleted"}
