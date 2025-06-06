<template>
  <div class="container py-4">
    <div class="row mb-4">
      <div class="col-12">
        <input class="form-control" v-model="busqueda" placeholder="Buscar productos..." />
      </div>
    </div>
    <div class="row">
      <div class="col-12 col-sm-6 col-md-4 col-lg-3 mb-4" v-for="producto in productosFiltrados" :key="producto.id">
        <div class="card h-100">
          <img v-if="producto.imagen_url" :src="producto.imagen_url" class="card-img-top" style="height:150px;object-fit:cover;">
          <div class="card-body">
            <h5 class="card-title">{{ producto.nombre }}</h5>
            <p class="card-text">${{ producto.precio }}</p>
            <button class="btn btn-primary w-100" @click="agregarAlCarrito(producto)">Agregar</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import eventBus from '../eventBus';

export default {
  data() {
    return {
      productos: [],
      busqueda: ""
    }
  },
  computed: {
    productosFiltrados() {
      return this.productos.filter(p =>
        p.nombre.toLowerCase().includes(this.busqueda.toLowerCase())
      );
    }
  },
  methods: {
    agregarAlCarrito(producto) {
      let carrito = JSON.parse(localStorage.getItem('carrito') || '[]');
      carrito.push(producto);
      localStorage.setItem('carrito', JSON.stringify(carrito));
      eventBus.emit('carrito-actualizado'); // <-- Cambiado para mitt
    }
  },
  mounted() {
    fetch('http://localhost:8000/productos/')
      .then(res => res.json())
      .then(data => {
        this.productos = data;
      })
      .catch(err => {
        console.error('Error al cargar productos:', err);
      });
  }
}
</script>