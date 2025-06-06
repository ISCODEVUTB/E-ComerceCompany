<template>
  <div class="modal-backdrop" v-if="visible">
    <div class="modal-dialog" style="max-width:350px;margin:100px auto;">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title">Pago Simulado</h5>
          <button type="button" class="btn-close" @click="$emit('cerrar')"></button>
        </div>
        <div class="modal-body">
          <form @submit.prevent="pagar">
            <input class="form-control mb-2" v-model="nombre" placeholder="Nombre en la tarjeta" required />
            <input class="form-control mb-2" v-model="numero" placeholder="Número de tarjeta" maxlength="16" required />
            <input class="form-control mb-2" v-model="cvv" placeholder="CVV" maxlength="4" required />
            <button class="btn btn-success w-100" type="submit">Pagar</button>
          </form>
          <div v-if="mensaje" class="alert alert-info mt-2">{{ mensaje }}</div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: ['visible', 'total'],
  data() {
    return {
      nombre: '',
      numero: '',
      cvv: '',
      mensaje: ''
    }
  },
  methods: {
    pagar() {
      // Aquí puedes simular el pago y emitir un evento al padre
      this.mensaje = "¡Pago simulado exitoso! Gracias por tu compra.";
      setTimeout(() => {
        this.$emit('pagado');
        this.mensaje = '';
      }, 1500);
    }
  }
}
</script>

<style scoped>
.modal-backdrop {
  position: fixed;
  top: 0; left: 0; right: 0; bottom: 0;
  background: rgba(0,0,0,0.3);
  z-index: 3000;
}
</style>