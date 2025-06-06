<template>
  <div
    class="card shadow position-fixed"
    style="top: 20px; right: 20px; width: 320px; z-index: 2000;"
  >
    <div class="card-body p-3">
      <button class="btn-close float-end" @click="$emit('cerrar')"></button>
      <h5 class="card-title mb-3">Mi cuenta</h5>
      <div v-if="usuario">
        <p><strong>Nombre:</strong> {{ usuario.nombre_usuario }}</p>
        <p><strong>Correo:</strong> {{ usuario.correo_electronico }}</p>
        <p><strong>Rol:</strong> {{ usuario.rol }}</p>
        <button class="btn btn-secondary btn-sm mb-3" @click="cerrarSesion">Cerrar sesión</button>
        <!-- Panel de administración solo para admin -->
        <div v-if="usuario.rol === 'admin'" class="mt-3">
          <h6>Panel de administración</h6>
          <form @submit.prevent="agregarProducto">
            <input class="form-control mb-2" v-model="nuevoProducto.nombre" placeholder="Nombre del producto" required />
            <input class="form-control mb-2" v-model.number="nuevoProducto.precio" placeholder="Precio" type="number" required />
            <input class="form-control mb-2" v-model.number="nuevoProducto.stock" placeholder="Stock" type="number" required />
            <button class="btn btn-success btn-sm w-100" type="submit">Agregar producto</button>
          </form>
          <p v-if="mensajeAdmin" class="mt-2 alert alert-info py-1 px-2">{{ mensajeAdmin }}</p>
        </div>
      </div>
      <div v-else>
        <h6 v-if="modo === 'registro'">Regístrate</h6>
        <h6 v-else>Inicia sesión</h6>
        <div v-if="modo === 'registro'">
          <input class="form-control mb-2" v-model="nuevoUsuario.nombre_usuario" placeholder="Nombre" />
          <input class="form-control mb-2" v-model="nuevoUsuario.correo_electronico" placeholder="Correo" />
          <input class="form-control mb-2" v-model="nuevoUsuario.contrasena" placeholder="Contrasena" type="password" />
          <button class="btn btn-primary btn-sm w-100" @click="registrarUsuario">Registrarse</button>
          <button class="btn btn-link btn-sm w-100" @click="modo = 'login'">¿Ya tienes cuenta? Inicia sesión</button>
        </div>
        <div v-else>
          <input class="form-control mb-2" v-model="loginUsuario.correo_electronico" placeholder="Correo" />
          <input class="form-control mb-2" v-model="loginUsuario.contrasena" placeholder="Contrasena" type="password" />
          <button class="btn btn-success btn-sm w-100" @click="iniciarSesion">Iniciar sesión</button>
          <button class="btn btn-link btn-sm w-100" @click="modo = 'registro'">¿No tienes cuenta? Regístrate</button>
        </div>
        <p v-if="mensaje" class="mt-2 alert alert-info py-1 px-2">{{ mensaje }}</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      usuario: null,
      modo: "login", // "login" o "registro"
      nuevoUsuario: {
        nombre_usuario: "",
        correo_electronico: "",
        contrasena: ""
      },
      loginUsuario: {
        correo_electronico: "",
        contrasena: ""
      },
      mensaje: "",
      // Para el panel admin:
      nuevoProducto: {
        nombre: "",
        precio: null,
        stock: null
      },
      mensajeAdmin: ""
    }
  },
  methods: {
    cerrarSesion() {
      localStorage.removeItem('usuario');
      this.usuario = null;
      this.mensaje = "";
      this.modo = "login";
    },
    async registrarUsuario() {
      if (
        !this.nuevoUsuario.nombre_usuario ||
        !this.nuevoUsuario.correo_electronico ||
        !this.nuevoUsuario.contrasena
      ) {
        this.mensaje = "Completa todos los campos para registrarte.";
        return;
      }
      try {
        const res = await fetch('http://localhost:8000/usuarios/', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            nombre_usuario: this.nuevoUsuario.nombre_usuario,
            correo_electronico: this.nuevoUsuario.correo_electronico,
            contrasena: this.nuevoUsuario.contrasena,
            rol: "cliente"
          })
        });
        if (!res.ok) {
          const error = await res.json();
          throw new Error(error.detail || 'Error al registrar usuario');
        }
        const usuario = await res.json();
        this.usuario = usuario;
        localStorage.setItem('usuario', JSON.stringify(usuario));
        this.mensaje = "¡Usuario registrado!";
        this.nuevoUsuario = { nombre_usuario: "", correo_electronico: "", contrasena: "" };
        this.modo = "login";
      } catch (err) {
        this.mensaje = err.message;
      }
    },
    async iniciarSesion() {
      if (
        !this.loginUsuario.correo_electronico ||
        !this.loginUsuario.contrasena
      ) {
        this.mensaje = "Completa todos los campos para iniciar sesión.";
        return;
      }
      try {
        const res = await fetch('http://localhost:8000/usuarios/login', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            correo_electronico: this.loginUsuario.correo_electronico,
            contrasena: this.loginUsuario.contrasena
          })
        });
        if (!res.ok) {
          const error = await res.json();
          throw new Error(error.detail || 'Error al iniciar sesión');
        }
        const usuario = await res.json();
        this.usuario = usuario;
        localStorage.setItem('usuario', JSON.stringify(usuario));
        this.mensaje = "¡Sesión iniciada!";
        this.loginUsuario = { correo_electronico: "", contrasena: "" };
      } catch (err) {
        this.mensaje = err.message;
      }
    },
    async agregarProducto() {
      if (!this.nuevoProducto.nombre || !this.nuevoProducto.precio || !this.nuevoProducto.stock) {
        this.mensajeAdmin = "Completa todos los campos del producto.";
        return;
      }
      try {
        const res = await fetch('http://localhost:8000/productos/', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            nombre: this.nuevoProducto.nombre,
            precio: this.nuevoProducto.precio,
            stock: this.nuevoProducto.stock
          })
        });
        if (!res.ok) {
          const error = await res.json();
          throw new Error(error.detail || 'Error al agregar producto');
        }
        this.mensajeAdmin = "¡Producto agregado!";
        this.nuevoProducto = { nombre: "", precio: null, stock: null };
      } catch (err) {
        this.mensajeAdmin = err.message;
      }
    }
  },
  mounted() {
    const usuarioGuardado = localStorage.getItem('usuario');
    if (usuarioGuardado) {
      this.usuario = JSON.parse(usuarioGuardado);
    }
  }
}
</script>

