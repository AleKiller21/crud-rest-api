from pymysql import connect
from config import config
import os


class DbService:
    """Singleton service used to handle all database operations"""

    db = None
    env_name = os.getenv('python_api_env')
    env_config = config[env_name]

    @staticmethod
    def execute(query, operation, *params):
        if not DbService.db:
            DbService.db = connect(host=DbService.env_config['host'],
                                   user=DbService.env_config['user'],
                                   password=DbService.env_config['password'],
                                   database=DbService.env_config['database'])

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
