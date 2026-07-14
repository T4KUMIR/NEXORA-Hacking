#!/usr/bin/env python 
# -*- coding: utf-8 -*-

import os
import sys
import time
import getpass
from colorama import Fore, Style, init


# Inicializar colorama para mejor soporte multiplataforma
init(autoreset=True)

# Constantes de colores ANSI
RED = '\033[1;31m'
BLUE = '\033[1;34m'
GREEN = '\033[1;32m'
YELLOW = '\033[1;33m'
MAGENTA = '\033[1;35m'
WHITE = '\033[1;37m'
CYAN = '\033[1;36m'
END = '\033[0m'

# Función para limpiar pantalla (multiplataforma)
def clear_screen():
    """Limpia la pantalla de manera multiplataforma"""
    os.system('cls' if os.name == 'nt' else 'clear')

clear_screen()

# ============================================================
# FUNCIONES DE INTERFAZ
# ============================================================

def banner():
    """Muestra el banner principal de la aplicación"""

    print(f"""{CYAN}
════════════════════════════════════════════════════════════════════

{BLUE}
███╗   ██╗███████╗██╗  ██╗ ██████╗ ██████╗  █████╗
████╗  ██║██╔════╝╚██╗██╔╝██╔═══██╗██╔══██╗██╔══██╗
██╔██╗ ██║█████╗   ╚███╔╝ ██║   ██║██████╔╝███████║
██║╚██╗██║██╔══╝   ██╔██╗ ██║   ██║██╔══██╗██╔══██║
██║ ╚████║███████╗██╔╝ ██╗╚██████╔╝██║  ██║██║  ██║
╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝

{GREEN}                 NEXORA - HACK v2.1{END}
{WHITE}         Advanced Wireless Security Toolkit{END}
{YELLOW}               by T4KUMIR{END}

{CYAN}════════════════════════════════════════════════════════════════════{END}
""")

def menu():
    """Muestra el menú principal de opciones"""
    print(""" \033[0;31m[\033[1;37m1\033[0;31m] \033[0;32mIniciar el modo monitor
 \033[0;31m[\033[1;37m2\033[0;31m] \033[0;32mDetener el modo monitor
 \033[0;31m[\033[1;37m3\033[0;31m] \033[0;32mVer mi interfaz
 \033[0;31m[\033[1;37m4\033[0;31m] \033[0;32mReiniciar red
 \033[0;31m[\033[1;37m5\033[0;31m] \033[0;32mEscanear redes cercanas
 \033[0;31m[\033[1;37m6\033[0;31m] \033[0;32mCapturar Handshake
 \033[0;31m[\033[1;37m7\033[0;31m] \033[0;32mDescifrar clave
 \033[0;31m[\033[1;37m8\033[0;31m] \033[0;32mAtacar redes WPS (\033[1;32mBully\033[0;32m)\033[0m
 \033[0;31m[\033[1;37m9\033[0;31m] \033[0;32mFalsificar MAC
 \033[0;31m[\033[1;37m10\033[0;31m] \033[0;32mFake AP
 \033[0;32m[\033[1;37m0\033[0;32m] \033[0;31mSalir\033[0m\n
""")


def goodbye():
    """Muestra el mensaje de despedida"""

    usuario = getpass.getuser()

    print(f"""
\033[1;36m══════════════════════════════════════════════════════\033[0m

\033[1;34m
███╗   ██╗███████╗██╗  ██╗ ██████╗ ██████╗  █████╗
████╗  ██║██╔════╝╚██╗██╔╝██╔═══██╗██╔══██╗██╔══██╗
██╔██╗ ██║█████╗   ╚███╔╝ ██║   ██║██████╔╝███████║
██║╚██╗██║██╔══╝   ██╔██╗ ██║   ██║██╔══██╗██╔══██║
██║ ╚████║███████╗██╔╝ ██╗╚██████╔╝██║  ██║██║  ██║
╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝
\033[0m

\033[1;32mGoodbye, {usuario}!\033[0m

\033[1;37mThank you for using NEXORA-HACK.\033[0m
\033[1;36mSession closed successfully.\033[0m

\033[1;36m══════════════════════════════════════════════════════\033[0m
""")


# ============================================================
# PUNTO DE ENTRADA
# ============================================================

if __name__ == "__main__":
    banner()
    menu()


