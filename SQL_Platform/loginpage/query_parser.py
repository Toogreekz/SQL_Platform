from tabulate import tabulate
import psycopg2


try:
    connection = psycopg2.connect(database='postgres', user='postgres', password='1234', host="localhost", port=5432)
    cursor = connection.cursor()
    CONNECTION = True
except (Exception, psycopg2.Error) as error:
    CONNECTION = False


def query_result(query):
    if CONNECTION:
        try:
            cursor.execute(query) # Если подается какая-то хрень, не работает даже с эталонным запросом!
            result = cursor.fetchall()
            columns = [desc[0] for desc in cursor.description]
            return True, tabulate(result, headers=columns)
        except psycopg2.errors.SyntaxError:
            return False, "Ошибка синтаксиса"
        except psycopg2.Error as error:
            return False, str(error)
        except Exception as error:
            return False, str(error)
        
    return False, "Connection to database failed."



'''print(query_result(
    """
    SELECT * FROM public."employees"
    """
))'''
