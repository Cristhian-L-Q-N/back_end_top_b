import aiomysql
import pymysql
from database import connect_to_database
from werkzeug.security import check_password_hash, generate_password_hash
from flask import Flask, jsonify, request
async def get_employees():
    connection = await connect_to_database()
    if connection:
        try:
            async with connection.cursor() as cursor:
                sql = "SELECT * FROM Employees"
                await cursor.execute(sql)
                employees = await cursor.fetchall()
                return employees
        
        except aiomysql.Error as e:
            print(f"Error al obtener empleados: {e}")
        
        finally:
            connection.close()

# Agrega aquí más funciones de consultas según tus necesidades

async def create_user(data):
    connection = await connect_to_database()
    if connection:
        try:
            async with connection.cursor() as cursor:
                name = data.get('name')
                user = data.get('user')
                password = data.get('password')
                role = data.get('role')
                hashed_password = generate_password_hash(password)
                
                sql = "INSERT INTO Empleado (Nombre, Usuario, Contrasena, Rol) VALUES (%s, %s, %s, %s)"
                await cursor.execute(sql, (name ,user, hashed_password, role))
                await connection.commit()
                
                return {"message": "User created successfully"}
        
        except aiomysql.Error as e:
            return {"error": str(e)}
        
        finally:
            connection.close()

async def get_empleados():
    connection=await connect_to_database()
    if connection:
        try:
            with connection.cursor() as cursor:
                sql = "SELECT ID_Empleado, Nombre, Usuario, Contrasena, Rol FROM Empleado"
                cursor.execute(sql)
                empleados = cursor.fetchall()

                resultados = [{"id_empleado":empleado['ID_Empleado'],"nombre": empleado['Nombre'], "usuario": empleado['Usuario'], "contrasena": empleado['Contrasena'], "rol": empleado['Rol']} for empleado in empleados]
                return jsonify(resultados)            
        except pymysql.Error as e:
            return jsonify({"error":"DataBase Error :{}".format(e)}),500
        finally:
            connection.close()