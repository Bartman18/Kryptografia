# 🔐 Encryption & Decryption Web App

A simple web application for encrypting and decrypting messages using a secret key.  
Built with **Vue.js** for the frontend and **Django** for the backend.

## 🚀 Features

- ✅ Generate a **secure encryption key**.
- ✅ Encrypt a message and **download it as a `.txt` file**.
- ✅ Upload an encrypted file to **decrypt** the message.
- ✅ Simple UI with **tab-based navigation** for encryption and decryption.

---

## 🛠️ Technologies Used

### **Frontend (Vue.js)**
- ⚡ Vue 3 with **Composition API**
- 📡 Axios for API requests
- 🎨 Bootstrap for styling

### **Backend (Django)**
- 🐍 Django with **Django REST Framework**
- 🔑 **Secrets** library for key generation
- 🔏 **Simple character-based encryption algorithm**

---

## 🔧 Installation Guide

### **1️⃣ Backend (Django) Setup***Clone the repository**:
   ```sh
   git clone https://github.com/your-repo.git
   cd your-repo
   ```

2. **Create a virtual environment and activate it**:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```sh
   pip install django
   ```

4. **Run the Django server**:
   ```sh
   python manage.py runserver
   ```
   The API will be available at: **[http://localhost:8000/](http://localhost:8000/)**

---

### **2️⃣ Frontend (Vue.js) Setup**

1. **Navigate to the frontend directory**:
   ```sh
   cd frontend
   ```

2. **Install dependencies**:
   ```sh
   npm install
   ```

3. **Run the Vue.js application**:
   ```sh
   npm run dev
   ```
   The frontend will be available at: **[http://localhost:5173/](http://localhost:5173/)**

---

## 📜 API Endpoints

### 🔑 Generate Encryption Key
- **Endpoint:** `GET /api/generate-key/`
- **Response:**
  ```json
  {
    "key": "your_generated_key"
  }
  ```

### 🔒 Encrypt a Message
- **Endpoint:** `POST /api/encrypt/`
- **Request:**
  ```json
  {
    "text": "Your message",
    "key": "YourSecretKey"
  }
  ```
- **Response:**
  ```json
  {
    "encrypted_text": "EncryptedMessage"
  }
  ```

### 🔓 Decrypt a Message
- **Endpoint:** `POST /api/decrypt/`
- **Request:**
  ```json
  {
    "text": "EncryptedMessage",
    "key": "YourSecretKey"
  }
  ```
- **Response:**
  ```json
  {
    "decrypted_text": "Your original message"
  }
  ```

---

## 🎮 How to Use

### 🔒 **Encryption**
1. Enter the text you want to encrypt.
2. Click **"Generate Key"** to create a secure key.
3. Click **"Encrypt & Download"** to encrypt and save the file.

### 🔓 **Decryption**
1. Upload the `.txt` file containing the encrypted message and key.
2. The decrypted message will be displayed.
