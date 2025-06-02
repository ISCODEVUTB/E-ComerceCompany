from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, DECIMAL
from sqlalchemy.orm import relationship
from backend.app.logic.database import Base
from datetime import datetime, timezone
USUARIOS_ID = "usuarios.id"

def utc_now():
    return datetime.now(timezone.utc)
class Usuario(Base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True, index=True)
    nombre_usuario = Column(String(100), nullable=False)
    correo_electronico = Column(String(100), unique=True, nullable=False)
    contraseña = Column(String(100), nullable=False)
    rol = Column(String(20), nullable=False)

    carritos = relationship("Carrito", back_populates="usuario")
    ordenes = relationship("Orden", back_populates="usuario")

class Producto(Base):
    __tablename__ = "productos"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    descripcion = Column(String, nullable=True)
    precio = Column(DECIMAL(10, 2), nullable=False)
    stock = Column(Integer, nullable=False)

    carrito_items = relationship("CarritoItem", back_populates="producto")
    items_orden = relationship("ItemOrden", back_populates="producto")

class Carrito(Base):
    __tablename__ = "carritos"
    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey(USUARIOS_ID), nullable=False)
    estado = Column(String(20), nullable=False, default="activo")
    creado_en = Column(DateTime(timezone=True), default=utc_now)

    usuario = relationship("Usuario", back_populates="carritos")
    items = relationship("CarritoItem", back_populates="carrito")

class CarritoItem(Base):
    __tablename__ = "carrito_items"
    id = Column(Integer, primary_key=True, index=True)
    carrito_id = Column(Integer, ForeignKey("carritos.id"), nullable=False)
    producto_id = Column(Integer, ForeignKey("productos.id"), nullable=False)
    cantidad = Column(Integer, nullable=False)
    precio_unitario = Column(DECIMAL(10, 2), nullable=False)

    carrito = relationship("Carrito", back_populates="items")
    producto = relationship("Producto", back_populates="carrito_items")

class Orden(Base):
    __tablename__ = "ordenes"
    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey(USUARIOS_ID), nullable=False)
    carrito_id = Column(Integer, ForeignKey("carritos.id"), nullable=False)
    monto_total = Column(DECIMAL(10, 2), nullable=False)
    creado_en = Column(DateTime(timezone=True), default=utc_now)
    estado = Column(String(20), nullable=False, default="pendiente")

    usuario = relationship("Usuario", back_populates="ordenes")
    carrito = relationship("Carrito")
    items = relationship("ItemOrden", back_populates="orden")

class ItemOrden(Base):
    __tablename__ = "items_orden"
    id = Column(Integer, primary_key=True, index=True)
    orden_id = Column(Integer, ForeignKey("ordenes.id"), nullable=False)
    producto_id = Column(Integer, ForeignKey("productos.id"), nullable=False)
    cantidad = Column(Integer, nullable=False)
    precio = Column(DECIMAL(10, 2), nullable=False)

    orden = relationship("Orden", back_populates="items")
    producto = relationship("Producto", back_populates="items_orden")

class Devolucion(Base):
    __tablename__ = "devoluciones"
    id = Column(Integer, primary_key=True, index=True)
    orden_id = Column(Integer, ForeignKey("ordenes.id"), nullable=False)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    motivo = Column(String, nullable=True)
    creado_en = Column(DateTime(timezone=True), default=utc_now)

    orden = relationship("Orden")
    usuario = relationship("Usuario")