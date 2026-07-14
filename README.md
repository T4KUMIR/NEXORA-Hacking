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
![Kali Linux](https://github.com/T4KUMIR/user-img/blob/2eb648547dc82f05cc7f92bf26c2d489a20059f9/Captura%20de%20pantalla%202026-07-14%20a%20la(s)%2014.03.07.png)

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

![Salida CSV](https://github.com/T4KUMIR/user-img/blob/5525a2d222b3fe07f809398cf7e39e2adb697fed/img%20cvs%20nexora.png)

### 🆕 Versión 2.0

- **[+]** Fake AP + Generador de diccionarios
- **[+]** Cracking de PIN WPS (Bully)
- **[~]** Interfaz mejorada

![Fake AP](https://github.com/T4KUMIR/user-img/blob/48142252a9c5d36f7ebd73106b6eb2d668819f9f/nexorap.png)

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
