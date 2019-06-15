import pymysql.cursors;


class DAOService:
    def __init__(self):
        self.connection = pymysql.connect(host='localhost',
                                          user='root',
                                          password='toor',
                                          db='counter',
                                          charset='utf8mb4',
                                          cursorclass=pymysql.cursors.DictCursor)

    @staticmethod
    def select_all(self):
        try:
            with self.connection.cursor() as cursor:

                sql = "SELECT * FROM in_out "

                cursor.execute(sql)

                print("cursor.description: ", cursor.description)

                print()

                for row in cursor:
                    print(row)

        finally:
            self.connection.close()

    @staticmethod
    def insert_in_out_people(self, in_out_param):

            with self.connection as cursor:
                sql = "INSERT INTO in_out VALUES(%s)"

                DAOService.delete_all(DAOService())

                cursor.execute(sql, in_out_param)

    @staticmethod
    def  delete_all(self):
        with self.connection as cursor:
            sql = "DELETE FROM in_out"

            cursor.execute(sql)

