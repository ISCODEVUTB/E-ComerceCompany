from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.app.routers import product, user, cart, order, devolutions
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
app.include_router(product.router, prefix="/productos", tags=["Productos"])
app.include_router(user.router, prefix="/usuarios", tags=["Usuarios"])
app.include_router(cart.router, prefix="/carritos", tags=["Carritos"])
app.include_router(order.router, prefix="/ordenes", tags=["Órdenes"])
app.include_router(devolutions.router, prefix="/devoluciones", tags=["Devoluciones"])

@app.get("/")
def read_root():
    return {"message": "Hola Mundo"}