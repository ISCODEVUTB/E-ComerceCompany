<template>
  <div>
    <button
      class="btn btn-warning position-fixed"
      style="top: 70px; right: 20px; z-index: 1050;"
      @click="abrirCarrito"
    >
      🛒 Carrito <span v-if="carrito.length">({{ carrito.length }})</span>
    </button>
    <div
      v-if="mostrarCarrito"
      class="card shadow position-fixed"
      style="top: 120px; right: 20px; width: 320px; z-index: 2000;"
    >
      <div class="card-body p-3">
        <button class="btn-close float-end" @click="mostrarCarrito = false"></button>
        <h5 class="card-title mb-3">Mi carrito</h5>
        <ul class="list-group mb-2">
          <li class="list-group-item py-1 px-2 d-flex justify-content-between align-items-center"
              v-for="(item, idx) in carrito" :key="item.id">
            <span>{{ item.nombre }} - ${{ item.precio }}</span>
            <button class="btn btn-danger btn-sm" @click="eliminarDelCarrito(idx)">Eliminar</button>
          </li>
        </ul>
        <p class="mb-1"><strong>Total: ${{ total }}</strong></p>
        <button class="btn btn-success w-100" @click="finalizarCompra" :disabled="carrito.length === 0">Finalizar compra</button>
        <p v-if="mensaje" class="mt-2 alert alert-info py-1 px-2">{{ mensaje }}</p>
      </div>
    </div>
  </div>
</template>

<script>
import eventBus from '../eventBus';

export default {
  data() {
    return {
      mostrarCarrito: false,
      carrito: [],
      mensaje: ""
    }
  },
  computed: {
    total() {
      return this.carrito.reduce((sum, item) => sum + item.precio, 0);
    }
  },
  mounted() {
    this.actualizarCarrito();
    eventBus.on('carrito-actualizado', this.actualizarCarrito);
  },
  beforeUnmount() {
    eventBus.off('carrito-actualizado', this.actualizarCarrito);
  },
  methods: {
    actualizarCarrito() {
      const guardado = localStorage.getItem('carrito');
      this.carrito = guardado ? JSON.parse(guardado) : [];
    },
    abrirCarrito() {
      this.mostrarCarrito = true;
      this.actualizarCarrito();
    },
    eliminarDelCarrito(idx) {
      this.carrito.splice(idx, 1);
      localStorage.setItem('carrito', JSON.stringify(this.carrito));
      eventBus.emit('carrito-actualizado');
    },
    async finalizarCompra() {
      const usuario = JSON.parse(localStorage.getItem('usuario') || 'null');
      if (!usuario || !usuario.id) {
        this.mensaje = "Debes iniciar sesión o registrarte para comprar.";
        return;
      }
      const productos = this.carrito.map(item => ({
        producto_id: item.id,
        cantidad: 1 // Cambia esto si tienes lógica de cantidad
      }));
      try {
        const res = await fetch('https://e-comercecompany-production.up.railway.app/productos', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ productos })
        });
        if (!res.ok) {
          const error = await res.json();
          throw new Error(error.detail || 'Error al registrar la compra');
        }
        this.mensaje = "¡Compra realizada con éxito! (Stock actualizado)";
        this.carrito = [];
        localStorage.removeItem('carrito');
        this.mostrarCarrito = false;
        eventBus.emit('carrito-actualizado');
      } catch (err) {
        this.mensaje = err.message;
      }
    }
  }
}
</script>