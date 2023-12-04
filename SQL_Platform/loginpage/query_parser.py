from tabulate import tabulate
import psycopg2


def query_result(query):
    try:
        connection = psycopg2.connect(database='postgres', user='postgres', password='1234', host="localhost", port=5432)
        cursor = connection.cursor()
        CONNECTION = True
    except (Exception, psycopg2.Error) as error:
        CONNECTION = False
        
    if CONNECTION:
        try:
            cursor.execute(query)
            result = cursor.fetchall()
            columns = [desc[0] for desc in cursor.description]
            
            cursor.connection.close()
            cursor = None
            CONNECTION = False
            
            return True, tabulate(result, headers=columns)
        
        except (psycopg2.Error, Exception, psycopg2.errors.SyntaxError) as error:
            
            cursor.connection.close()
            cursor = None
            CONNECTION = False
            
            return False, str(error)
        
    return False, "Connection to database failed."



'''print(query_result(
    """
    SELECT * FROM public."employees"
    """
))'''
