<script>
import axios from 'axios'
import {mountTokenHeader, SLIPS, USER} from '@/services/api.js'

import SlipCard from '@/views/HomePage/SlipCard.vue'

export default {
  name: "MainPage",
  components: {SlipCard},
  mounted() {
    axios.get(USER + "/" + this.userId, mountTokenHeader(this.accessToken)).then((response) => {
      this.user = response.data;
    }).then(() => {
      axios.get(SLIPS, mountTokenHeader(this.accessToken)).then((response) => {
        this.slips = response.data;
      })
    }).catch(() => {
      this.$router.push("/login");
    });
  },
  methods: {
    newSlip() {
      let slipToCreate = {
        description: "Novo boleto",
        value: 0
      };
      axios.post(SLIPS, slipToCreate, mountTokenHeader(this.accessToken)).then((response) => {
        slipToCreate = response.data;
        slipToCreate.due_date = null;
        slipToCreate.payment_date = null;
        this.slips.push(response.data);
      })
    },
    deleteSlip(slip) {
      axios.delete(SLIPS + "/" + slip.id, mountTokenHeader(this.accessToken)).then(() => {
        this.slips.splice(this.slips.indexOf(slip), 1)
      });
    },
    saveSlip(index, slip) {
      axios.put(SLIPS + "/" + slip.id, slip, mountTokenHeader(this.accessToken)).then(() => {
        this.slips[index] = slip;
      });
    },
    exit() {
      this.$router.push('/login')
    }
  },
  data() {
    return {
      accessToken: localStorage.getItem("key"),
      userId: localStorage.getItem("userId"),
      user: {
        username: ""
      },
      slips: []
    }
  }
}
</script>

<template>
  <div class="home">
    <header class="header">
      <h1 class="header__logo">PagueEmDia</h1>
      <div class="flex gap-6 items-center">
        <span>{{ user.username }}</span>
        <button class="home__exit-button" @click="exit">Sair</button>
      </div>
    </header>
    <main class="home__main">
      <div class="flex items-center justify-center">
        <button class="button" @click="newSlip">Novo boleto</button>
      </div>
      <div class="grid grid-cols-4 gap-6 h-full" v-if="slips.length > 0">
        <SlipCard
            :slip="slip" v-for="(slip, index) in slips" :key="index"

            @save="saveSlip(index, $event)"
            @delete="deleteSlip(slip)"
        />
      </div>
      <span v-else class="self-center text-lg">Você ainda não tem boletos</span>
    </main>
  </div>
</template>

<style scoped>

.home {
  @apply flex flex-col
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
  @apply flex flex-col gap-6 p-6
}

.button {
  background-color: var(--pallete-color-main-1);
  color: white;
  @apply px-5 py-2.5 rounded-md border-none cursor-pointer
}

.home__exit-button {
  color: var(--pallete-color-red-1);
  background-color: transparent;
  @apply px-3 py-1.5 rounded-md border-none cursor-pointer
}

.home__exit-button:hover {
  background-color: var(--pallete-color-grey-2);
}

</style>