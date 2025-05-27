from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import productos, usuarios, carritos, ordenes, devoluciones
app = FastAPI()

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir solicitudes desde cualquier origen
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos los métodos HTTP (GET, POST, etc.)
    allow_headers=["*"],  # Permitir todos los encabezados
)

# Registrar los routers
app.include_router(productos.router, prefix="/productos", tags=["Productos"])
app.include_router(usuarios.router, prefix="/usuarios", tags=["Usuarios"])
app.include_router(carritos.router, prefix="/carritos", tags=["Carritos"])
app.include_router(ordenes.router, prefix="/ordenes", tags=["Órdenes"])
app.include_router(devoluciones.router, prefix="/devoluciones", tags=["Devoluciones"])

@app.get("/")
def read_root():
    return {"message": "Hola Mundo"}