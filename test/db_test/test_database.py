from sqlalchemy import inspect
from backend.app.logic.database import engine  # Cambiado a un import absoluto

try:
    # Crear un inspector para la base de datos
    inspector = inspect(engine)
    
    # Obtener las tablas disponibles
    tables = inspector.get_table_names()
    
    # Imprimir las tablas
    print("Tablas en la base de datos:", tables)
    
    # Verificar que la conexión es exitosa
    assert len(tables) >= 0  # Si no hay tablas, la conexión sigue siendo válida
except Exception as e:
    print("Error al conectar con la base de datos:", e)
    assert False  # Falla el test si ocurre un error