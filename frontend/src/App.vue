<script setup>
import { ref } from 'vue'

const productos = ref([])
const error = ref('')

async function cargarProductos() {
  try {
    const response = await fetch('http://localhost:8000/productos/')
    productos.value = await response.json()
  } catch (e) {
    error.value = 'No se pudieron cargar los productos'
  }
}

// Cargar productos al iniciar el componente
cargarProductos()
</script>

<template>
  <div id="app">
    <div class="cosmo-letrero">
      <span style="font-size:2.2rem; letter-spacing:0.12em;">✨ Cosmo Infinite ✨</span>
    </div>
    <button
      class="btn btn-outline-primary position-fixed"
      style="top: 20px; right: 20px; z-index: 1050;"
      @click="mostrarUsuario = !mostrarUsuario"
    >
      Mi cuenta
    </button>
    <Usuario v-if="mostrarUsuario" @cerrar="mostrarUsuario = false" />
    <Carrito />
    <AdminPanel v-if="esAdmin" />
    <Productos />
  </div>
</template>

<script>
import Productos from './components/Productos.vue'
import Usuario from './components/Usuario.vue'
import Carrito from './components/Carrito.vue'
import AdminPanel from './components/AdminPanel.vue'

export default {
  components: { Productos, Usuario, Carrito, AdminPanel },
  data() {
    return {
      mostrarUsuario: false
    }
  },
  computed: {
    esAdmin() {
      // Intenta obtener el usuario del localStorage (ajusta la clave si es diferente)
      try {
        const usuario = JSON.parse(localStorage.getItem('usuario') || '{}')
        return usuario.rol === 'admin'
      } catch {
        return false
      }
    }
  }
}
</script>

<style>
.cosmo-letrero {
  background-color: #282c34;
  color: #61dafb;
  padding: 10px 20px;
  text-align: center;
  position: relative;
  z-index: 1000;
  border-bottom: 1px solid #61dafb;
}
</style>