#!/bin/bash

# ============================================================
# Script de instalación de dependencias para Wifi-Hack
# ============================================================

set -euo pipefail

# Colores
RED='\033[1;31m'
GREEN='\033[1;32m'
YELLOW='\033[1;33m'
BLUE='\033[1;34m'
MAGENTA='\033[1;35m'
CYAN='\033[1;36m'
WHITE='\033[1;37m'
RESET='\033[0m'

# Variables globales
INSTALLED_COUNT=0
FAILED_COUNT=0
SKIPPED_COUNT=0
LOG_FILE="wifi-hack-install.log"

# ============================================================
# FUNCIONES AUXILIARES
# ============================================================

# Función para mostrar error
error() {
    printf "${RED}[ERROR]${RESET} %s\n" "$1" >&2
    echo "[ERROR] $1" >> "$LOG_FILE"
    exit 1
}

# Función para mostrar advertencia
warning() {
    printf "${YELLOW}[ADVERTENCIA]${RESET} %s\n" "$1"
    echo "[WARNING] $1" >> "$LOG_FILE"
}

# Función para mostrar éxito
success() {
    printf "${GREEN}[OK]${RESET} %s\n" "$1"
    echo "[OK] $1" >> "$LOG_FILE"
}

# Función para mostrar información
info() {
    printf "${BLUE}[INFO]${RESET} %s\n" "$1"
    echo "[INFO] $1" >> "$LOG_FILE"
}

# Función para mostrar status
status() {
    printf "${CYAN}[*]${RESET} %s\n" "$1"
    echo "[*] $1" >> "$LOG_FILE"
}

# Función para validar root
check_root() {
    if [[ $EUID -ne 0 ]]; then
        error "Este script debe ejecutarse con sudo o como root"
    fi
}

# Función para detectar el gestor de paquetes
detect_package_manager() {
    if command -v apt-get &> /dev/null; then
        echo "apt"
    elif command -v pacman &> /dev/null; then
        echo "pacman"
    elif command -v dnf &> /dev/null; then
        echo "dnf"
    elif command -v yum &> /dev/null; then
        echo "yum"
    else
        error "No se encontró un gestor de paquetes soportado"
    fi
}

# Función para actualizar lista de paquetes
update_packages() {
    local pm=$1
    info "Actualizando lista de paquetes..."
    
    case $pm in
        apt)
            apt-get update -qq || warning "No se pudo actualizar la lista con apt"
            ;;
        pacman)
            pacman -Sy --noconfirm > /dev/null || warning "No se pudo actualizar con pacman"
            ;;
        dnf|yum)
            $pm check-update -q > /dev/null || true
            ;;
    esac
}

# Función para verificar si un paquete está instalado
is_installed() {
    local package=$1
    local pm=$2
    
    case $pm in
        apt)
            dpkg -l | grep -q "^ii  $package" && return 0 || return 1
            ;;
        pacman)
            pacman -Q "$package" &> /dev/null && return 0 || return 1
            ;;
        dnf)
            dnf list installed "$package" &> /dev/null && return 0 || return 1
            ;;
        yum)
            yum list installed "$package" &> /dev/null && return 0 || return 1
            ;;
    esac
    return 1
}

# Función para instalar un paquete
install_package() {
    local package=$1
    local display_name=$2
    local pm=$3
    
    printf "\n${CYAN}═══════════════════════════════════════════════════════════${RESET}\n"
    printf "${MAGENTA}Instalando:${RESET} $display_name\n"
    printf "${CYAN}═══════════════════════════════════════════════════════════${RESET}\n"
    
    if is_installed "$package" "$pm"; then
        warning "El paquete '$display_name' ya está instalado"
        ((SKIPPED_COUNT++))
        return 0
    fi
    
    status "Descargando e instalando $display_name..."
    
    case $pm in
        apt)
            if apt-get install -y "$package" >> "$LOG_FILE" 2>&1; then
                success "$display_name instalado correctamente"
                ((INSTALLED_COUNT++))
            else
                error "No se pudo instalar $display_name"
                ((FAILED_COUNT++))
                return 1
            fi
            ;;
        pacman)
            if pacman -S --noconfirm "$package" >> "$LOG_FILE" 2>&1; then
                success "$display_name instalado correctamente"
                ((INSTALLED_COUNT++))
            else
                error "No se pudo instalar $display_name"
                ((FAILED_COUNT++))
                return 1
            fi
            ;;
        dnf)
            if dnf install -y "$package" >> "$LOG_FILE" 2>&1; then
                success "$display_name instalado correctamente"
                ((INSTALLED_COUNT++))
            else
                error "No se pudo instalar $display_name"
                ((FAILED_COUNT++))
                return 1
            fi
            ;;
        yum)
            if yum install -y "$package" >> "$LOG_FILE" 2>&1; then
                success "$display_name instalado correctamente"
                ((INSTALLED_COUNT++))
            else
                error "No se pudo instalar $display_name"
                ((FAILED_COUNT++))
                return 1
            fi
            ;;
    esac
}

# Función para instalar Python 3 y dependencias de pip
install_python_deps() {
    local pm=$1
    
    info "Verificando dependencias de Python..."
    
    # Verificar Python 3
    if ! command -v python3 &> /dev/null; then
        case $pm in
            apt)
                install_package "python3" "Python 3" "$pm"
                ;;
            pacman)
                install_package "python" "Python 3" "$pm"
                ;;
            dnf|yum)
                install_package "python3" "Python 3" "$pm"
                ;;
        esac
    else
        success "Python 3 ya está instalado"
        ((SKIPPED_COUNT++))
    fi
    
    # Instalar pip
    if ! command -v pip3 &> /dev/null; then
        case $pm in
            apt)
                install_package "python3-pip" "pip3" "$pm"
                ;;
            pacman)
                install_package "python-pip" "pip" "$pm"
                ;;
            dnf|yum)
                install_package "python3-pip" "pip3" "$pm"
                ;;
        esac
    else
        success "pip3 ya está instalado"
        ((SKIPPED_COUNT++))
    fi
}

# Función para mostrar banner
show_banner() {
    clear
    printf "\n${BLUE}╔═══════════════════════════════════════════════════════════╗${RESET}\n"
    printf "${BLUE}║${RESET}          ${YELLOW}Instalador Wifi-Hack${RESET}                      ${BLUE}║${RESET}\n"
    printf "${BLUE}║${RESET}    ${CYAN}Configuración de dependencias${RESET}                  ${BLUE}║${RESET}\n"
    printf "${BLUE}╚═══════════════════════════════════════════════════════════╝${RESET}\n\n"
}

# Función para mostrar resumen
show_summary() {
    printf "\n${BLUE}╔═══════════════════════════════════════════════════════════╗${RESET}\n"
    printf "${BLUE}║${RESET}               ${YELLOW}Resumen de Instalación${RESET}              ${BLUE}║${RESET}\n"
    printf "${BLUE}╚═══════════════════════════════════════════════════════════╝${RESET}\n"
    printf "${GREEN}[✓] Instalados: $INSTALLED_COUNT${RESET}\n"
    printf "${YELLOW}[~] Omitidos: $SKIPPED_COUNT${RESET}\n"
    if [[ $FAILED_COUNT -gt 0 ]]; then
        printf "${RED}[✗] Fallidos: $FAILED_COUNT${RESET}\n"
    fi
    printf "${BLUE}═══════════════════════════════════════════════════════════${RESET}\n\n"
    
    if [[ $FAILED_COUNT -eq 0 ]]; then
        success "¡Instalación completada exitosamente!"
        info "Log guardado en: $(pwd)/$LOG_FILE"
    else
        warning "La instalación completó con algunos errores"
        warning "Revisa el log para más detalles: $(pwd)/$LOG_FILE"
    fi
}

# ============================================================
# FUNCIÓN PRINCIPAL
# ============================================================

main() {
    show_banner
    
    # Validaciones iniciales
    check_root
    
    # Inicializar log
    > "$LOG_FILE"
    info "Iniciando instalación de dependencias..."
    info "Sistema: $(uname -s)"
    info "Kernel: $(uname -r)"
    
    # Detectar gestor de paquetes
    PKG_MANAGER=$(detect_package_manager)
    info "Gestor de paquetes detectado: $PKG_MANAGER"
    
    # Actualizar lista de paquetes
    update_packages "$PKG_MANAGER"
    
    # Array de paquetes a instalar
    declare -a PACKAGES=(
        "xterm"
        "aircrack-ng"
        "bully"
        "wifite"
        "mdk3"
        "macchanger"
        "curl"
        "wget"
    )
    
    # Instalar paquetes
    for package in "${PACKAGES[@]}"; do
        install_package "$package" "$(echo $package | sed 's/^./\U&/')" "$PKG_MANAGER" || true
    done
    
    # Instalar dependencias de Python
    install_python_deps "$PKG_MANAGER"
    
    # Instalar módulos de Python
    info "Instalando módulos de Python..."
    if pip3 install -q colorama 2>> "$LOG_FILE"; then
        success "colorama instalado"
        ((INSTALLED_COUNT++))
    else
        warning "No se pudo instalar colorama (opcional)"
    fi
    
    # Mostrar resumen
    show_summary
}

# ============================================================
# PUNTO DE ENTRADA
# ============================================================

if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    main "$@"
fi
