<template>
  <div class="container py-4">
    <h2>Panel de Administración</h2>
    <form @submit.prevent="crearProducto" class="mb-4" enctype="multipart/form-data">
      <div class="mb-2">
        <input v-model="nuevoProducto.nombre" class="form-control" placeholder="Nombre" required />
      </div>
      <div class="mb-2">
        <input v-model="nuevoProducto.descripcion" class="form-control" placeholder="Descripción" required />
      </div>
      <div class="mb-2">
        <input v-model.number="nuevoProducto.precio" type="number" class="form-control" placeholder="Precio" required />
      </div>
      <div class="mb-2">
        <input v-model.number="nuevoProducto.stock" type="number" class="form-control" placeholder="Stock" required />
      </div>
      <div class="mb-2">
        <input type="file" class="form-control" @change="onFileChange" required />
      </div>
      <button class="btn btn-success" type="submit">Crear producto</button>
    </form>
    <div v-if="mensaje" class="alert alert-info">{{ mensaje }}</div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      nuevoProducto: {
        nombre: "",
        descripcion: "",
        precio: 0,
        stock: 0,
        imagen: null
      },
      mensaje: ""
    }
  },
  methods: {
    onFileChange(e) {
      this.nuevoProducto.imagen = e.target.files[0];
    },
    async crearProducto() {
      try {
        const token = localStorage.getItem('access_token') || localStorage.getItem('usuario') && JSON.parse(localStorage.getItem('usuario')).access_token;
        if (!this.nuevoProducto.imagen) {
          this.mensaje = "Selecciona una imagen.";
          return;
        }
        const formData = new FormData();
        formData.append("nombre", this.nuevoProducto.nombre);
        formData.append("descripcion", this.nuevoProducto.descripcion);
        formData.append("precio", this.nuevoProducto.precio);
        formData.append("stock", this.nuevoProducto.stock);
        formData.append("imagen", this.nuevoProducto.imagen);

        const res = await fetch('http://localhost:8000/productos/', {
          method: 'POST',
          headers: {
            'Authorization': `Bearer ${token}`
          },
          body: formData
        });
        if (!res.ok) {
          const error = await res.json();
          throw new Error(error.detail || 'Error al crear producto');
        }
        this.mensaje = "Producto creado correctamente";
        this.nuevoProducto = { nombre: "", descripcion: "", precio: 0, stock: 0, imagen: null };
      } catch (err) {
        this.mensaje = err.message;
      }
    }
  }
}
</script>