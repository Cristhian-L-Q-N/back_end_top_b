

from contextlib import asynccontextmanager
import aiomysql


@asynccontextmanager
async def connect_to_database():
    connection = await aiomysql.connect(
        host='containers-us-west-24.railway.app',
        port=5828,
        user='root',
        password='IJDLZQVMpvbnBAuOsGBg',
        db='railway',
        cursorclass=aiomysql.DictCursor
    )
    try:
        yield connection
        print("Conexión establecida")
    finally:
        connection.close()

