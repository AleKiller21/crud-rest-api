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
            rows_affected = cursor.execute(query, params)
            if operation == 'r':
                result = cursor.fetchall()
                cursor.close()
                return result

            else:
                DbService.db.commit()
                cursor.close()
                return DbService.__generate_write_response(operation, rows_affected)

        except Exception as e:
            DbService.db.rollback()
            print(e)
            return "fallo"

    @staticmethod
    def __generate_write_response(operation, rows_affected):
        if rows_affected == 0:
            return {'message': "No users with that id were affected"}
        elif operation == 'c':
            return {'message': "User has been created"}
        elif operation == 'u':
            return {'message': "User has been updated"}
        else:
            return {'message': "User has been deleted"}
