# Documentation: Text Encryption and Decryption Tool

## English

### Overview

This tool allows users to encrypt and decrypt text messages securely using the `cryptography` library. The application provides a simple interface for encrypting text, saving the encrypted data, and decrypting it with authorization.

### Features

- Generate and store a secret key for encryption.
- Encrypt user-inputted text and save it securely.
- Decrypt text only with the correct authorization.
- User-friendly graphical interface using `tkinter`.

### Installation

To install the required dependencies, use the following command:

```sh
pip install cryptography
```

### Usage

1. **Encryption**
   - Enter the text you want to encrypt.
   - Click the "Encrypt" button.
   - The encrypted message is saved to a file.
2. **Decryption**
   - Enter the authorization key.
   - Click "Decrypt" to retrieve the original message.

### Code Explanation

1. **Key Generation**
   - Generates a unique encryption key and saves it for future use.
2. **Encryption Function**
   - Uses the key to encrypt user-inputted text and saves it to a file.
3. **Decryption Function**
   - Requires authorization to retrieve and decrypt the saved message.

---

## Español

### Descripción General

Esta herramienta permite a los usuarios encriptar y desencriptar mensajes de texto de manera segura utilizando la biblioteca `cryptography`. La aplicación proporciona una interfaz simple para encriptar texto, guardar los datos encriptados y desencriptarlos con autorización.

### Características

- Generar y almacenar una clave secreta para la encriptación.
- Encriptar texto ingresado por el usuario y guardarlo de manera segura.
- Desencriptar el texto solo con la autorización correcta.
- Interfaz gráfica amigable utilizando `tkinter`.

### Instalación

Para instalar las dependencias necesarias, usa el siguiente comando:

```sh
pip install cryptography
```

### Uso

1. **Encriptación**
   - Ingresa el texto que deseas encriptar.
   - Haz clic en el botón "Encriptar".
   - El mensaje encriptado se guardará en un archivo.
2. **Desencriptación**
   - Ingresa la clave de autorización.
   - Haz clic en "Desencriptar" para recuperar el mensaje original.

### Explicación del Código

1. **Generación de Clave**
   - Genera una clave única de encriptación y la guarda para su uso futuro.
2. **Función de Encriptación**
   - Usa la clave para encriptar el texto ingresado por el usuario y lo guarda en un archivo.
3. **Función de Desencriptación**
   - Requiere autorización para recuperar y desencriptar el mensaje guardado.

Created by Th3Mayar - Jose Francisco