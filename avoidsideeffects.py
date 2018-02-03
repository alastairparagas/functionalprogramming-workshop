import psycopg2
import os

'''
Executes the provided SQL query
@param {string} sql_query
@param {list} parameters
@returns {list[tuple]}
'''
def db_query(sql_query, parameters=None):
  if not isinstance(sql_query, basestring):
    raise TypeError("sql_query must be a string")
  if parameters is not None and not isinstance(parameters, list):
    raise TypeError("parameters must be a list")
    
  db = psycopg2.connect(
    database=os.getenv("POSTGRES_DB"),
    user=os.getenv("POSTGRES_USER"),
    password=os.getenv("POSTGRES_PASSWORD"),
    host=os.getenv("POSTGRES_HOST")
  )
  
  db_cursor = db.cursor()
  if parameters is None:
    db_cursor.execute(sql_query)
  else:
    db_cursor.execute(sql_query, parameters)
  db.commit()
  
  results = db_cursor.fetchall()
  
  db_cursor.close()
  db.close()
  return results

