<script>
export default {
  name: "SlipCard",
  props: {
    slip: {}
  },
  methods: {
    deleteSlip() {
      this.$emit("delete");
    },
    saveSlip() {
      this.$emit("save");
    }
  }
}
</script>

<template>
  <div class="slip">
    <div class="flex flex-col gap-1.5">
      <div class="flex gap-2 items-center">
        <input class="border-none text-xl w-full" placeholder="Boleto"/>
        <select class="slip__input pr-1.5">
          <option :selected="slip.status === 'PENDENTE'">PENDENTE</option>
          <option :selected="slip.status === 'PAGO'">PAGO</option>
          <option :selected="slip.status === 'CANCELADO'">CANCELADO</option>
        </select>
      </div>
      <div class="flex gap-3 items-center">
        <label class="text-2xl">R$</label>
        <input class="w-full text-2xl border-none" type="number" placeholder="0,00" :value="slip.value"/>
      </div>
    </div>
    <div class="flex gap-12 items-center">
      <div class="flex flex-col gap-3 w-1/2">
        <label class="slip__label">Vencimento</label>
        <input type="date" class="slip__input cursor-pointer" :value="slip.appointment_date">
      </div>
      <div class="flex flex-col gap-3 w-1/2">
        <label class="slip__label">Pagamento</label>
        <input type="date" class="slip__input cursor-pointer" :value="slip.due_date">
      </div>
    </div>
    <div class="flex gap-3 items-center justify-end mt-6">
      <button class="slip__button main" @click="saveSlip">Salvar</button>
      <button class="slip__button severe" @click="deleteSlip">Excluir</button>
    </div>
  </div>
</template>

<style scoped>

.slip {
  border: 2px solid var(--pallete-color-grey-1);
  @apply flex flex-col rounded-lg p-6 gap-3
}

.slip__label {
  color: var(--pallete-color-font-2);
}

.slip__input {
  background-color: transparent;
  @apply border-none
}

.slip__button {
  background-color: var(--pallete-color-main-1);
  color: white;
  @apply px-5 py-2.5 rounded-md border-none cursor-pointer
}

.slip__button.main {
  background-color: var(--pallete-color-main-1);
  color: white;
}


.slip__button.severe {
  background-color: var(--pallete-color-red-1);
  color: white;
}

</style>