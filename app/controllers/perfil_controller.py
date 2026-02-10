import psycopg2
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.perfil_model import Perfil
from fastapi.encoders import jsonable_encoder

class PerfilController:
        
    def create_perfil(self, perfil: Perfil):   
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO perfiles (nombre,id,descripcion) VALUES (%s, %s, %s)", (perfil.nombre, perfil.apellido, perfil.descripcion))
            conn.commit()
            conn.close()
            return {"resultado": "Perfil creado"}
        except mysql.connector.Error as err:
            # Si falla el INSERT, los datos no quedan guardados parcialmente en la base de datos
            # Se usa para deshacer los cambios de la transacción activa cuando ocurre un error en el try.
            conn.rollback()
        finally:
            conn.close()
        

    def get_Perfil(self,perfil_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM perfiles WHERE id = %s", (perfil_id,))
            result = cursor.fetchone()
            payload = []
            content = {} 
            
            content={
                    'id':int(result[0]),
                    'nombre':result[1],
                    'descripcion':result[2],
                    
            }
            payload.append(content)
            
            json_data = jsonable_encoder(content)            
            if result:
               return  json_data
            else:
                ##Esto interrumpe la ejecución y responde al cliente con un código 404
                ## comunica al cliente de la API qué pasó (error HTTP).
                ##código 404,comportamiento correcto según las reglas HTTP
                raise HTTPException(status_code=404, detail="Perfil not found")  
                
        except mysql.connector.Error as err:
            # Se usa para deshacer los cambios de la transacción activa cuando ocurre un error en el try.
            ##Maneja el estado de la transacción en la base de datos.Si un INSERT, UPDATE o DELETE falla dentro de una transacción, rollback() revierte esos cambios.
            conn.rollback()
        finally:
            conn.close()
       
    def get_Perfils(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM perfiles")
            result = cursor.fetchall()
            payload = []
            content = {} 
            for data in result:
                content={
                    'id':data[0],
                    'nombre':data[1],
                    'cedula':data[2],
                    'edad':data[3],
                    'usuario':data[4],
                    'contrasena':data[5]
                }
                payload.append(content)
                content = {}
            json_data = jsonable_encoder(payload)        
            if result:
               return {"resultado": json_data}
            else:
                raise HTTPException(status_code=404, detail="Perfil not found")  
                
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()
    
    
       

##Perfil_controller = PerfilController()