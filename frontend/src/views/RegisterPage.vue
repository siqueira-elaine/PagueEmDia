<script>
import axios from "axios";
import {REGISTER} from "@/services/api.js";

export default {
  name: "RegisterPage",
  data() {
    return {
      user: {
        password: "",
        username: ""
      },
      response: ""
    }
  },
  methods: {
    register() {
      if (this.user.username.length === 0) {
        this.response = "Nome de usuário não pode ser vazio";
        return;
      }
      if (this.user.password.length === 0) {
        this.response = "Senha não pode ser vazia";
        return;
      }

      axios.post(REGISTER,this.user).then(() => {
        this.$router.push("/login")
      }).catch((response) => {
        this.response = "Nome de usuário já existe"
      })
    }
  }
}
</script>

<template>
  <div class="flex flex-col gap-12 justify-center items-center h-screen w-screen">
    <h1 class="logo">PagueEmDia</h1>
    <div class="login-container">
      <h2 class="text-2xl font-normal self-center">Registrar</h2>
      <div class="flex flex-col gap-3">
        <input class="login-container__input" placeholder="Usuário" type="text" v-model="user.username"/>
        <input class="login-container__input" placeholder="Senha" type="password" v-model="user.password"/>
      </div>
      <div class="flex flex-col gap-3">
        <span class="w-full text-center" v-show="response.length !== 0">
          {{response}}
        </span>
        <button class="login__button main" @click="register">Registrar</button>
        <RouterLink to="/login" class="login__button aside">
          Voltar
        </RouterLink>
      </div>
    </div>
  </div>
</template>


<style scoped>

.login-container {
  width: 450px;
  border: 2px solid var(--pallete-color-grey-1);
  @apply flex flex-col rounded-md p-6 gap-6
}

.logo {
  color: var(--pallete-color-main-1);
  @apply text-2xl font-semibold;
}

.login-container__input {
  border: 2px solid var(--pallete-color-grey-1);
  @apply rounded-md p-3;
}

.login__button {
  @apply px-5 py-3 rounded-md border-none cursor-pointer text-center
}

.login__button.main {
  background-color: var(--pallete-color-main-1);
  color: white;
}

.login__button.aside {
  background-color: var(--pallete-color-grey-2);
}


</style>