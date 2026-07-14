# 🛡️ Nexora

<p align="center">
  <img src="https://github.com/T4KUMIR/user-img/blob/7e89deedc3baca92096de80044120aa35a70a37c/nexora.png" alt="Nexora Logo">
</p>

<p align="center">
  <strong>Herramienta automatizada para pentesting de redes WiFi</strong>
  <br>
  Automatiza los procesos de aircrack-ng para análisis de seguridad
</p>

---

## 📋 Tabla de Contenidos

- [Descripción](#descripción)
- [Características](#características)
- [Requisitos](#requisitos)
- [Instalación](#instalación)
- [Uso](#uso)
- [Versiones Soportadas](#versiones-soportadas)
- [Actualizaciones](#actualizaciones)
- [Aviso Legal](#aviso-legal)
- [Autor](#autor)

---

## 📖 Descripción

**Nexora** es una herramienta de penetración para sistemas operativos Linux que automatiza el análisis de seguridad en redes inalámbricas. Proporciona una interfaz interactiva para realizar:

- Captura de handshakes WPA/WPA2
- Cracking de contraseñas WiFi
- Ataques a redes WPS
- Generación de puntos de acceso falsos
- Análisis de redes cercanas

**Uso:** Exclusivamente para pentesting autorizado y fines educativos.

---

## ✨ Características

### Funciones Principales

- **Modo Monitor**: Iniciación y control del modo monitor de la tarjeta WiFi
- **Escaneo de Redes**: Descubrimiento de redes WiFi cercanas
- **Captura de Handshake**: Captura automática del handshake WPA/WPA2
- **Cracking de Claves**: Descifrado de contraseñas mediante diccionario
- **Ataque WPS**: Fuerza bruta contra redes con WPS habilitado (Bully)
- **Falsificación MAC**: Cambio de dirección MAC
- **Fake AP**: Creación de puntos de acceso falsos
- **Generador de Diccionarios**: Herramienta para crear listas de APs

### Versiones y Actualizaciones

| Versión | Características |
|---------|-----------------|
| **1.0** | Funciones básicas de cracking WiFi |
| **2.0** | Fake AP, Generador de diccionarios, Bully (WPS) |
| **2.1** | Exportación de resultados en formato CSV |

---

## 🖥️ Versiones Soportadas

Las siguientes distribuciones han sido probadas exitosamente:

### Kali Linux (v2.1) ✔️
![Kali Linux Demo](https://user-images.githubusercontent.com/75953873/174921385-a512703d-a9d0-4ce5-837c-f7453401e140.png)

### Parrot OS (v2.0) ✔️
![Parrot OS Demo](https://user-images.githubusercontent.com/75953873/192111809-3f18078e-80ed-4470-aba7-d9c9fbf6f024.png)

### Linux Mint (v1.0) ✔️
![Linux Mint Demo](https://user-images.githubusercontent.com/75953873/139563944-7eef6e72-05fd-4481-bcc4-bffa6edbb512.png)

### Ubuntu (v1.0) ✔️
![Ubuntu Demo](https://user-images.githubusercontent.com/75953873/140593033-e8498792-2f3d-4651-8787-f882a43901b9.png)

---

## 📦 Requisitos

### Dependencias del Sistema

- Python 3.6+
- Bash 4.0+
- Privilegios de root/sudo
- Tarjeta WiFi compatible con modo monitor

### Herramientas Externas Requeridas

- `aircrack-ng` - Cracking de redes WiFi
- `airmon-ng` - Activación del modo monitor
- `airodump-ng` - Captura de paquetes
- `aireplay-ng` - Inyección de paquetes
- `wifite` / `bully` - Ataques WPS
- `macchanger` - Cambio de dirección MAC

---

## 🚀 Instalación

### Paso 1: Clonar el repositorio

```bash
git clone https://github.com/T4KUMIR/NEXORA-Hacking.git
cd NEXORA-Hacking
```

### Paso 2: Instalar dependencias

```bash
sudo bash requirements.sh
```

### Paso 3: Ejecutar la herramienta

```bash
sudo python3 nexora.py
```

---

## 📚 Uso

### Inicio Rápido

```bash
sudo python3 nexora.py
```

Se mostrará un menú interactivo con las siguientes opciones:

```
[1] Iniciar el modo monitor
[2] Detener el modo monitor
[3] Ver mi interfaz
[4] Reiniciar red
[5] Escanear redes cercanas
[6] Capturar Handshake
[7] Descifrar clave
[8] Atacar redes WPS (Bully)
[9] Falsificar MAC
[10] Fake AP
[0] Salir
```

### Ejemplo: Cracking WPA2

1. Selecciona opción **[1]** para iniciar modo monitor
2. Selecciona opción **[5]** para escanear redes
3. Selecciona opción **[6]** para capturar handshake
4. Selecciona opción **[7]** para descifrar con diccionario

### Ejemplo: Generar Diccionario

```bash
bash AP_generator.sh
```

Sigue las instrucciones para generar un diccionario personalizado.

---

## 🔄 Actualizaciones

### 🆕 Versión 2.1

- **[+]** Exportación de resultados en formato CSV
- **[~]** Mejoras en la interfaz de usuario
- **[~]** Optimizaciones de rendimiento

![Salida CSV](https://github.com/user-attachments/assets/42bff460-f6b1-4298-b7fd-da347e6ff05e)

### 🆕 Versión 2.0

- **[+]** Fake AP + Generador de diccionarios
- **[+]** Cracking de PIN WPS (Bully)
- **[~]** Interfaz mejorada

![Fake AP](https://user-images.githubusercontent.com/75953873/174706969-1ca06a64-e34c-4a99-9502-56291a2d188b.png)

---

## ⚠️ Aviso Legal

### Español
> **NO soy responsable del mal uso que se le pueda dar a esta herramienta.** Úsala exclusivamente para:
> - Pentesting autorizado
> - Auditorías de seguridad
> - Fines educativos y académicos
>
> El acceso no autorizado a sistemas informáticos es **ilegal** en la mayoría de jurisdicciones.

### English
> **I am NOT responsible for misuse of this tool.** Use it exclusively for:
> - Authorized penetration testing
> - Security audits
> - Educational and academic purposes
>
> Unauthorized access to computer systems is **illegal** in most jurisdictions.

---

## 👤 Autor

**t4kumir** - [@t4kumir](https://github.com/t4kumir)

---

## 📄 Licencia

Este proyecto está sujeto a las restricciones de uso indicadas en el aviso legal anterior.

---

## 🆘 Troubleshooting

### Problema: "Permiso denegado"
```bash
sudo python3 nexora.py
```
La herramienta requiere privilegios de root.

### Problema: "Tarjeta WiFi no detectada"
- Verifica que tu tarjeta WiFi sea compatible con modo monitor
- Instala los drivers necesarios para tu hardware

### Problema: "Comando no encontrado"
```bash
sudo bash requirements.sh
```
Reinstala las dependencias requeridas.

---

<p align="center">
  <strong>Úsalo responsablemente 🛡️</strong>
</p>
