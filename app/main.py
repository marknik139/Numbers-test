from psycopg2 import connect


from converter import convert_values
from check import check_changes
from config import host, user, password, db_name


while(True):


    def rewrite_database():

        """Перезапись значений в таблицу PostgreSQL. При добавлении
        новой записи в google sheets все столбцы должны быть NOT NULL и соответствовать 
        формату"""

        with connection.cursor() as cursor:
                cursor.execute(
                    """DELETE FROM price_table"""
                )
                temp = convert_values()
                sql = """
                    INSERT INTO price_table (id, order_num, price_doll, price_rub, test_time) 
                    VALUES(%s, %s, %s, %s, %s)"""
                for i in range(len(temp)):
                    cursor.execute(sql, temp[i])


    try:

        connection = connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )
        connection.autocommit = True


        #Попытка создания таблицы, в случае её отсутствия 
        try:
            
            with connection.cursor() as cursor:
                cursor.execute(
                    """CREATE TABLE price_table(
                    id SERIAL PRIMARY KEY,
                    order_num INT,
                    price_doll INT,
                    price_rub NUMERIC (10,2),
                    test_time DATE);"""
                )
                print('[INFO] Table created succesfully')
        except:
            pass


        rewrite_database()


        while (True):
            
            if (check_changes()):
                rewrite_database()

    except:
        pass