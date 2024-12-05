<template>
  <div id="app">
    <header class="app-header">
      <h1 class="title">Kryptografia: Szyfrowanie i Odszyfrowywanie</h1>
      <p class="subtitle">Bezpieczne szyfrowanie i odszyfrowywanie wiadomości</p>
    </header>
    <main class="main-content">
      <HelloWorld />
    </main>
    <footer class="footer">
      <p>Stworzone dla projektu z przedmiotu Kryptografia.</p>
    </footer>
  </div>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue';

export default {
  name: 'App',
  components: {
    HelloWorld,
  },
};
</script>

<style scoped>
/* Global stylizacja */
#app {
  font-family: Arial, sans-serif;
  color: #fff;
  display: flex;
  flex-direction: column;
  min-height: 100vh;
  background: linear-gradient(135deg, #1e293b, #3c4858);
  margin: 0;
}

/* Nagłówek */
.app-header {
  text-align: center;
  padding: 2rem 0;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.title {
  font-size: 2.5rem;
  margin: 0;
}

.subtitle {
  font-size: 1.2rem;
  color: #ccc;
  margin: 0.5rem 0 0;
}

/* Główna treść */
.main-content {
  flex: 1;
  padding: 2rem;
  display: flex;
  justify-content: center;
  align-items: center;
}

/* Stopka */
.footer {
  background-color: #111827;
  text-align: center;
  padding: 1rem 0;
  font-size: 0.9rem;
}

footer p {
  margin: 0;
}
</style>
