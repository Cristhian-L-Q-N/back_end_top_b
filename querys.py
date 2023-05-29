import aiomysql
import pymysql
from database import connect_to_database
from werkzeug.security import check_password_hash, generate_password_hash
from flask import Flask, jsonify, request

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
