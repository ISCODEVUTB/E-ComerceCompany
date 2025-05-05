# backend/order_service/service.py

from pydantic import BaseModel
from typing import List

class Order(BaseModel):
    id: int
    user_id: int
    cart_id: int
    status: str
    address: str
    total: float

class OrderService:
    def __init__(self):
        self.orders: List[Order] = []

    def create_order(self, order: Order):
        self.orders.append(order)
        return {"message": "Order placed"}

    def get_orders_by_user(self, user_id: int):
        return [order for order in self.orders if order.user_id == user_id]

    def update_order(self, order_id: int, updated_order: Order):
        for i, order in enumerate(self.orders):
            if order.id == order_id:
                self.orders[i] = updated_order
                return {"message": "Order updated"}
        return None

    def delete_order(self, order_id: int):
        for order in self.orders:
            if order.id == order_id:
                self.orders.remove(order)
                return {"message": "Order canceled"}
        return None
