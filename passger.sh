#!/bin/bash


###

# Define colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
BLUE='\033[0;34m'
MAGENTA='\033[0;35m'
CYAN='\033[0;36m'
WHITE='\033[0;37m'
BOLD='\033[1m'
UNDERLINE='\033[4m'
NC='\033[0m' # No Color

# Define the dashboard banner with a modern hacking theme
echo -e "${CYAN}${BOLD}"
echo -e "         ============================================================="
echo -e "${MAGENTA}
            ██████╗  █████╗ ███████╗███████╗ ██████╗ ███████╗██████╗ 
            ██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝ ██╔════╝██╔══██╗
            ██████╔╝███████║███████╗███████╗██║  ███╗█████╗  ██████╔╝   ${CYAN}" 
echo -e "            ██╔═══╝ ██╔══██║╚════██║╚════██║██║   ██║██╔══╝  ██╔══██╗
            ██║     ██║  ██║███████║███████║╚██████╔╝███████╗██║  ██║
            ╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝
            "
            
echo -e "         =============================================================
                     𝕍𝕖𝕣𝕤𝕚𝕠𝕟 : 𝟙.𝟘     𝕋𝕨𝕚𝕥𝕥𝕖𝕣 : anishalx7          
         ============================================================="
echo -e "${WHITE}${BOLD}Features:${NC}"
echo -e "  ${GREEN}- Add and retrieve passwords securely."
echo -e "  ${GREEN}- Uses SHA-256 hashing for password security."
echo -e "  ${GREEN}- Simple text-based interface."
echo -e "${WHITE}${BOLD}Usage:${NC}"
echo -e "  ${GREEN}- Add your master password to secure the passger"
echo -e "  ${GREEN}- [NOTE:- This password you have to remember to access your passger]"
echo -e "  ${YELLOW}1.${WHITE} Please choose an option: 1"
echo -e "     ${CYAN}Enter Website Name: example.com
     Enter Username: user@example.com
     Enter Password: my_secure_password"
echo -e "  ${YELLOW}2.${WHITE} Please choose an option: 2"
echo -e "     ${CYAN}Enter Website Name: example.com"
echo -e "${WHITE}${BOLD}License:${NC} MIT License"
echo -e "${WHITE}${BOLD}Contact:${NC} anishalx7@gmail.com"
echo -e "         ============================================================="
echo -e "${NC}"

###


# Path to the Python script
PYTHON_SCRIPT="passy.py"

# Ensure the Python script is executable
if [ ! -x "$PYTHON_SCRIPT" ]; then
    chmod +x "$PYTHON_SCRIPT"
fi

# Run the Python script using Python3
python3 "$PYTHON_SCRIPT"

