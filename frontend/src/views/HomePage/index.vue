<script>
import SlipCard from '@/views/HomePage/SlipCard.vue'

export default {
  name: "MainPage",
  components: { SlipCard },
  mounted() {

  },
  methods: {
    newSplit() {
      this.slips.push({
        description: "",
        value: 0,
        appointment_date: "",
        due_date: "",
        status: "PENDENTE"
      });
    }
  },
  data() {
    return {
      user: {
        name: "Elaine"
      },
      slips: [
        // {
        //   id: 1,
        //   description: "Vivo",
        //   value: 32.00,
        //   appointment_date: "2024-06-12",
        //   due_date: "2024-06-12",
        //   status: "PENDENTE"
        // },
        // {
        //   id: 2,
        //   description: "Vivo",
        //   value: 32.00,
        //   appointment_date: "2024-06-12",
        //   due_date: "2024-06-12",
        //   status: "PENDENTE"
        // },
        // {
        //   id: 3,
        //   description: "Vivo",
        //   value: 32.00,
        //   appointment_date: "2024-06-12",
        //   due_date: "2024-06-12",
        //   status: "PENDENTE"
        // }
      ]
    }
  }
}
</script>

<template>
  <div class="home">
    <header class="header">
      <h1 class="header__logo">PagueEmDia</h1>
      <span>{{ user.name }}</span>
    </header>
    <main class="home__main">
      <div class="flex items-center justify-center">
        <button class="button" @click="newSplit">Novo boleto</button>
      </div>
      <div class="grid grid-cols-4 gap-6" v-if="slips.length > 0">
        <SlipCard :slip="slip" v-for="(slip, index) in slips" :key="index" @delete="this.slips.splice(this.slips.indexOf(slip), 1)"/>
      </div>
      <span v-else class="self-center text-lg">Você ainda não tem boletos</span>
    </main>
  </div>
</template>

<style scoped>

.home {
  @apply flex flex-col gap-6
}

.header {
  border: 2px solid var(--pallete-color-grey-1);
  height: 56px;
  @apply flex items-center justify-between w-full px-6
}

.header__logo {
  color: var(--pallete-color-main-1);
  @apply text-xl font-semibold
}

.home__main {
  @apply flex flex-col gap-6 px-6
}

.button {
  background-color: var(--pallete-color-main-1);
  color: white;
  @apply px-5 py-2.5 rounded-md border-none cursor-pointer
}

</style>