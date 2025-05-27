from pydantic import BaseModel
from typing import Optional, List

class UsuarioBase(BaseModel):
    nombre: str
    correo_electronico: str
    rol: str

class UsuarioCreate(UsuarioBase):
    contrasena: str

class Usuario(UsuarioBase):
    id: int

    class Config:
        orm_mode = True

class ProductoBase(BaseModel):
    nombre: str
    descripcion: Optional[str] = None
    precio: float
    inventario: int

class ProductoCreate(ProductoBase):
    pass

class Producto(ProductoBase):
    id: int

    class Config:
        orm_mode = True

class CarritoItemBase(BaseModel):
    producto_id: int
    cantidad: int
    precio_unitario: float

class CarritoItem(CarritoItemBase):
    id: int

    class Config:
        orm_mode = True

class CarritoBase(BaseModel):
    usuario_id: int
    estado: str

class Carrito(CarritoBase):
    id: int
    items: List[CarritoItem] = []

    class Config:
        orm_mode = True

class OrdenBase(BaseModel):
    usuario_id: int
    carrito_id: int
    monto_total: float
    estado: str

class Orden(OrdenBase):
    id: int

    class Config:
        orm_mode = True

class DevolucionBase(BaseModel):
    orden_id: int
    usuario_id: int
    motivo: Optional[str] = None

class Devolucion(DevolucionBase):
    id: int

    class Config:
        orm_mode = True