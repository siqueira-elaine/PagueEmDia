<script>
export default {
  name: "SlipCard",
  props: {
    slip: {}
  },
  data() {
    return {
      id: this.slip.id,
      value: this.slip.value,
      description: this.slip.description,
      due_date: this.slip.due_date == null ? null : this.slip.due_date.substring(0, this.slip.due_date.indexOf(" ")),
      payment_date: this.slip.payment_date == null ? null : this.slip.payment_date.substring(0, this.slip.payment_date.indexOf(" ")),
      status: this.slip.status
    }
  },
  methods: {
    saveSlip() {
      this.$emit("save", {
        description: this.description,
        due_date: this.due_date,
        payment_date: this.payment_date,
        status: this.status,
        value: this.value,
        id: this.id
      });
    },
    deleteSlip() {
      this.$emit("delete")
    }
  },
  computed: {
    hasChanges() {
      return this.slip.description !== this.description || this.slip.due_date !== this.due_date
          || this.slip.payment_date !== this.payment_date || this.slip.status !== this.status || this.slip.value !== this.value
    }
  }
}
</script>

<template>
  <div class="slip">
    <div class="flex flex-col gap-1.5">
      <div class="flex gap-2 items-center">
        <input class="border-none text-xl w-full" placeholder="Boleto" v-model="description"/>
        <select class="slip__input pr-1.5">
          <option :selected="slip.status === 'PENDING'" @click="status = 'PENDING'">PENDENTE</option>
          <option :selected="slip.status === 'PAID'" @click="status = 'PAID'">PAGO</option>
        </select>
      </div>
      <div class="flex gap-3 items-center">
        <label class="text-2xl">R$</label>
        <input class="w-full text-2xl border-none" type="number" placeholder="0,00" v-model="value"/>
      </div>
    </div>
    <div class="flex gap-12 items-center">
      <div class="flex flex-col gap-3 w-1/2">
        <label class="slip__label">Vencimento</label>
        <input type="date" class="slip__input cursor-pointer" v-model="payment_date">
      </div>
      <div class="flex flex-col gap-3 w-1/2"  v-show="status === 'PAID'">
        <label class="slip__label">Pagamento</label>
        <input type="date" class="slip__input cursor-pointer" v-model="due_date">
      </div>
    </div>
    <div class="flex gap-3 w-full">
      <button class="slip__button severe" @click="deleteSlip">Excluir</button>
      <button class="slip__button main" @click="saveSlip" v-show="hasChanges">Salvar</button>
    </div>
  </div>
</template>

<style scoped>

.slip {
  border: 2px solid var(--pallete-color-grey-1);
  @apply flex flex-col rounded-lg p-6 gap-6
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
  @apply px-5 py-2.5 rounded-md border-none cursor-pointer w-full
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