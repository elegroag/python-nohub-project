#database
import mysql.connector
from mysql.connector import errorcode

class Db:

    def __init__(self):
        pass

    def connectMysql(self):
        cnx = mysql.connector.connect(
            user='root', 
            host='', 
            database='', 
            password='', 
            port=''
        )
        return cnx

    def readQuery(self):
        cnx = self.connectMysql() 
        try:
            if cnx and cnx.is_connected():
                cursor = cnx.cursor()
                cursor.execute("""
                    SELECT 
                        co.usuario, 
                        co.progreso, 
                        co.estado, 
                        co.proceso, 
                        co.linea_comando, 
                        co.parametros, 
                        co.resultado, 
                        co.id, 
                        ce.procesador as ps  
                    FROM comandos co 
                    INNER JOIN comando_estructuras as ce ON ce.id = co.estructura 
                    WHERE ce.asyncro = 3 and co.estado='P' 
                    LIMIT 10 """
                )
                records  = cursor.fetchall()
                print("Total number of rows in table: ", cursor.rowcount)
                _list = []
                for row in records:
                    _dict = {
                        "usuario": row[0],
                        "progreso": row[1],
                        "estado": row[2],
                        "proceso": row[3],
                        "linea_comando": row[4],
                        "parametros": row[5],
                        "resultado": row[6],
                        "id": row[7],
                        "ps": row[8]
                    }
                    _list.append(_dict)
                return _list
            else :
                print("No conection")
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
                cnx.close()
        finally:
            if cnx.is_connected():
                cnx.close()
                cursor.close()
                # print("MySQL Close")      

    def updateQuery(self, _id, _estado):
        cnx = self.connectMysql() 
        try:
            if cnx and cnx.is_connected():
                cursor = cnx.cursor()
                cursor.execute("UPDATE comandos SET estado='{0}' WHERE id='{1}'".format(_estado, _id))
                print("Update Ok")
                return cursor.rowcount
            else :
                print("No conection")
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
                cnx.close()
        finally:
            if cnx.is_connected():
                cnx.close()
                cursor.close()
                # print("MySQL Close")        
