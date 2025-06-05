from locust import HttpUser, task, between

class EcommerceUser(HttpUser):
    wait_time = between(1, 2)  # Espera entre 1 y 2 segundos entre tareas

    @task
    def listar_productos(self):
        self.client.get("/productos/")  # Cambia la ruta si tu endpoint es diferente

    def ver_producto(self, product_id):
        self.client.get(f"/productos/{product_id}/")

    def agregar_producto_al_carrito(self):
        # Aquí puedes agregar lógica para seleccionar un producto específico
        product_id = 1  # Cambia esto al ID del producto que deseas agregar
        self.client.post(f"/carrito/agregar/{product_id}/")

    def ver_carrito(self):
        self.client.get("/carrito/")