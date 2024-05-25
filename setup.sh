#!/bin/bash
clear

echo -e "\e[32m
 __    _  _______  _______  __   __  ___   _______  _______  __    _ 
|  |  | ||       ||       ||  | |  ||   | |       ||       ||  |  | |
|   |_| ||    ___||   _   ||  | |  ||   | |    ___||    ___||   |_| |
|       ||   |___ |  | |  ||  |_|  ||   | |   | __ |   |___ |       |
|  _    ||    ___||  |_|  ||       ||   | |   ||  ||    ___||  _    |
| | |   ||   |___ |      | |       ||   | |   |_| ||   |___ | | |   |
|_|  |__||_______||____||_||_______||___| |_______||_______||_|  |__|


xploitLabs -> https://github.com/xploitLabs
\e[0m"

# Verificar si python3 o python está instalado
if command -v python3 &> /dev/null; then
    PYTHON=python3
elif command -v python &> /dev/null; then
    PYTHON=python
else
    echo -e "\e[1;31m[\e[34m+\e[1;31m] \e[0mThis system requires Python 3 or Python to be installed.\e[0m"
    exit 1
fi

current_directory=$(pwd)
echo "export PATH=\$PATH:$current_directory/src" >> ~/.bashrc

# Dar permiso de ejecución al archivo src/nequi
nequi_file="$current_directory/src/nequi"
if [ -e "$nequi_file" ]; then
    chmod +x "$nequi_file"
    echo -e "\e[1;32m[\e[34m+\e[1;32m] \e[0mPermissions set for $nequi_file."
else
    echo -e "\e[1;31m[\e[34m+\e[1;31m] \e[0m$nequi_file not found."
    exit 1
fi

# Instalar los requerimientos desde src/requirements.txt
requirements_file="$current_directory/src/requirements.txt"
if [ -e "$requirements_file" ]; then
    echo -e "\e[1;32m[\e[34m+\e[1;32m] \e[0mInstalling requirements..."
    $PYTHON -m pip install -r "$requirements_file"
else
    echo -e "\e[1;31m[\e[34m+\e[1;31m] \e[0mRequirements.txt file not found in the src directory."
    exit 1
fi

echo -e "\e[1;32m[\e[34m+\e[1;32m] \e[0mProcess finished, use the 'nequi' command."
bash