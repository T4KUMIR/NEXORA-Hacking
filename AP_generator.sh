#!/bin/bash

# ============================================================
# Script mejorado para generar listas de APs WiFi
# ============================================================

set -euo pipefail

# Colores para output
RED='\033[1;31m'
GREEN='\033[1;32m'
YELLOW='\033[1;33m'
BLUE='\033[1;34m'
RESET='\033[0m'

# Función para mostrar error y salir
error() {
    printf "${RED}[ERROR]${RESET} %s\n" "$1" >&2
    exit 1
}

# Función para mostrar advertencia
warning() {
    printf "${YELLOW}[ADVERTENCIA]${RESET} %s\n" "$1"
}

# Función para mostrar éxito
success() {
    printf "${GREEN}[OK]${RESET} %s\n" "$1"
}

# Función para validar entrada
validate_input() {
    local input="$1"
    local max_len="$2"
    local field_name="$3"
    
    # Verificar que no esté vacío
    if [[ -z "$input" ]]; then
        error "$field_name no puede estar vacío"
    fi
    
    # Verificar longitud máxima
    if [[ ${#input} -gt $max_len ]]; then
        error "$field_name no puede exceder $max_len caracteres (actual: ${#input})"
    fi
}

# Función para validar número
validate_number() {
    local num="$1"
    
    if ! [[ "$num" =~ ^[0-9]+$ ]]; then
        error "El valor debe ser un número entero positivo"
    fi
    
    if [[ $num -lt 1 ]]; then
        error "El número debe ser mayor a 0"
    fi
}

# Banner
printf "\n${BLUE}╔═══════════════════════════════════════════════════════════╗${RESET}\n"
printf "${BLUE}║${RESET}        ${YELLOW}Generador de Diccionarios WiFi${RESET}                   ${BLUE}║${RESET}\n"
printf "${BLUE}╚═══════════════════════════════════════════════════════════╝${RESET}\n\n"

# Entrada 1: Nombre del AP
read -p "$(printf '${GREEN}›${RESET} Nombre del AP (máx 16 caracteres): ')" AP_name
validate_input "$AP_name" 16 "Nombre del AP"

# Entrada 2: Número de APs
read -p "$(printf '${GREEN}›${RESET} Número de APs a generar (default: 100): ')" AP_count
AP_count="${AP_count:-100}"
validate_number "$AP_count"

# Entrada 3: Nombre del diccionario
read -p "$(printf '${GREEN}›${RESET} Nombre del archivo de salida: ')" wordlist_name
validate_input "$wordlist_name" 255 "Nombre del diccionario"

# Verificar si el archivo ya existe
if [[ -f "$wordlist_name" ]]; then
    warning "El archivo '$wordlist_name' ya existe"
    read -p "$(printf '${YELLOW}›${RESET} ¿Deseas sobrescribirlo? (s/n): ')" overwrite
    if [[ "$overwrite" != "s" && "$overwrite" != "S" ]]; then
        printf "${YELLOW}Operación cancelada${RESET}\n"
        exit 0
    fi
fi

# Verificar permisos de escritura
if [[ ! -w "$(pwd)" ]]; then
    error "No tienes permisos de escritura en el directorio actual"
fi

# Generar el diccionario
printf "\n${BLUE}Generando diccionario...${RESET}\n"

{
    for ((i=1; i<=AP_count; i++)); do
        echo "$AP_name-$i"
        
        # Mostrar progreso cada 10 items
        if (( i % 10 == 0 )); then
            printf "\r${GREEN}Generados: $i/$AP_count${RESET}"
        fi
    done
} > "$wordlist_name" || error "No se pudo crear el archivo de salida"

printf "\r${GREEN}Generados: $AP_count/$AP_count${RESET}\n\n"

# Verificar que el archivo se creó correctamente
if [[ ! -f "$wordlist_name" ]]; then
    error "El archivo de salida no se creó correctamente"
fi

# Estadísticas
file_size=$(du -h "$wordlist_name" | cut -f1)
line_count=$(wc -l < "$wordlist_name")

# Mostrar resumen
printf "${BLUE}╔═══════════════════════════════════════════════════════════╗${RESET}\n"
printf "${BLUE}║${RESET} ${GREEN}Diccionario creado exitosamente${RESET}\n"
printf "${BLUE}║${RESET}\n"
printf "${BLUE}║${RESET} ${YELLOW}Nombre del AP:${RESET} $AP_name\n"
printf "${BLUE}║${RESET} ${YELLOW}Total de entradas:${RESET} $line_count\n"
printf "${BLUE}║${RESET} ${YELLOW}Tamaño del archivo:${RESET} $file_size\n"
printf "${BLUE}║${RESET} ${YELLOW}Ubicación:${RESET} $(pwd)/$wordlist_name\n"
printf "${BLUE}╚═══════════════════════════════════════════════════════════╝${RESET}\n\n"

success "Proceso completado"
