<script setup>
import { ref } from 'vue';
import axios from 'axios';

// Zakładki
const activeTab = ref('encrypt');

// Pola dla szyfrowania
const textToEncrypt = ref('');
const keyEncrypt = ref('');

// Pola dla odszyfrowywania
const decryptResult = ref('');

// Funkcja API do generowania klucza
async function generateKey() {
  try {
    const response = await axios.get('http://localhost:8000/api/generate-key/');
    keyEncrypt.value = response.data.key;
  } catch (error) {
    console.error('Error generating key:', error.response?.data || error.message);
  }
}

// Funkcja API do szyfrowania wiadomości
async function encrypt() {
  if (!keyEncrypt.value || !textToEncrypt.value) {
    alert('Proszę podać klucz i tekst do zaszyfrowania!');
    return;
  }
  try {
    const response = await axios.post('http://localhost:8000/api/encrypt/', {
      text: textToEncrypt.value,
      key: keyEncrypt.value,
    });

    // Generowanie pliku z kluczem i zaszyfrowaną wiadomością
    downloadEncryptedFile(keyEncrypt.value, response.data.encrypted_text);
  } catch (error) {
    console.error('Error encrypting text:', error.response?.data || error.message);
  }
}

// Funkcja do pobierania zaszyfrowanej wiadomości jako plik
function downloadEncryptedFile(key, encryptedText) {
  const content = `Key: ${key}\nEncrypted Message: ${encryptedText}`;
  const blob = new Blob([content], { type: 'text/plain' });
  const link = document.createElement('a');
  link.href = URL.createObjectURL(blob);
  link.download = 'encrypted_message.txt';
  link.click();
  URL.revokeObjectURL(link.href);
}

// Funkcja do obsługi wgrywania pliku i odszyfrowywania
function handleFileUpload(event) {
  const file = event.target.files[0];
  if (file && file.type === 'text/plain') {
    const reader = new FileReader();
    reader.onload = async () => {
      const content = reader.result;
      const [keyLine, encryptedMessageLine] = content.split('\n').map((line) => line.trim());

      // Wyodrębnij klucz i zaszyfrowaną wiadomość
      const key = keyLine.replace('Key: ', '');
      const encryptedMessage = encryptedMessageLine.replace('Encrypted Message: ', '');

      // Wywołaj API odszyfrowania
      await decryptMessage(key, encryptedMessage);
    };
    reader.readAsText(file);
  } else {
    alert('Proszę wgrać plik tekstowy (.txt), który zawiera klucz i zaszyfrowaną wiadomość.');
  }
}

// Funkcja API do odszyfrowania wiadomości
async function decryptMessage(key, encryptedMessage) {
  try {
    const response = await axios.post('http://localhost:8000/api/decrypt/', {
      text: encryptedMessage,
      key: key,
    });
    decryptResult.value = response.data.decrypted_text;
  } catch (error) {
    console.error('Error decrypting text:', error.response?.data || error.message);
    alert('Wystąpił błąd podczas odszyfrowywania wiadomości.');
  }
}
</script>

<template>
  <div class="hello-world">
    <div class="tabs d-flex justify-content-center mb-4">
      <button
        class="btn btn-outline-light me-2"
        :class="{ active: activeTab === 'encrypt' }"
        @click="activeTab = 'encrypt'"
      >
        Szyfrowanie
      </button>
      <button
        class="btn btn-outline-light"
        :class="{ active: activeTab === 'decrypt' }"
        @click="activeTab = 'decrypt'"
      >
        Odszyfrowanie
      </button>
    </div>

    <div class="content">
      <!-- Szyfrowanie -->
      <div v-if="activeTab === 'encrypt'">
        <h3 class="text-center mb-4">Szyfrowanie</h3>
        <textarea
          v-model="textToEncrypt"
          class="form-control mb-3"
          placeholder="Wprowadź tekst do zaszyfrowania"
        ></textarea>
        <div class="d-flex justify-content-between mb-3">
          <button class="btn btn-primary" @click="generateKey">Generuj Klucz</button>
          <input
            v-model="keyEncrypt"
            class="form-control w-50"
            readonly
            placeholder="Wygenerowany klucz"
          />
        </div>
        <button class="btn btn-success w-100" @click="encrypt">
          Zaszyfruj i Pobierz
        </button>
      </div>

      <!-- Odszyfrowanie -->
      <div v-if="activeTab === 'decrypt'">
        <h3 class="text-center mb-4">Odszyfrowanie</h3>
        <input
          type="file"
          @change="handleFileUpload"
          accept=".txt"
          class="form-control mb-3"
        />
        <textarea
          readonly
          class="form-control"
          :value="decryptResult"
          placeholder="Wynik odszyfrowania"
        ></textarea>
      </div>
    </div>
  </div>
</template>

<style scoped>
.hello-world {
  width: 100%;
  max-width: 800px;
  margin: 0 auto;
  padding: 2rem;
  background-color: rgba(255, 255, 255, 0.9);
  border-radius: 10px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.tabs button.active {
  background-color: #007bff;
  color: white;
}

textarea {
  resize: none;
}
</style>
