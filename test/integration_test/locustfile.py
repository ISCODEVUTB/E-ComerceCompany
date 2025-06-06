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

    @task
    def ver_carrito(self):
        # 1. Acceder al carrito
        response = self.client.get("/carritos/1")  # Cambia el ID según corresponda
        if response.status_code == 200 and response.json():
            carrito = response.json()
            productos = carrito.get("productos", [])
            total = carrito.get("total", 0)
            assert total >= 0, "El total debe ser mayor o igual a 0"
            for producto in productos:
                assert "nombre" in producto
                assert "imagen_url" in producto
                assert "precio" in producto
                assert "cantidad" in producto
                assert "subtotal" in producto

    @task
    def modificar_cantidad(self):
        # 2. Modificar la cantidad de un producto (ejemplo: producto con ID 1)
        self.client.put("/carritos/1/productos/1", json={"cantidad": 2})

    @task
    def eliminar_producto(self):
        # 3. Eliminar un producto del carrito (ejemplo: producto con ID 1)
        self.client.delete("/carritos/1/productos/1")

    @task
    def proceder_checkout(self):
        # 4. Proceder al checkout (simulación)
        self.client.post("/ordenes/", json={"carrito_id": 1})