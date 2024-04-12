#!/bin/bash
echo -n "Updating system libraries..."
sudo apt update  # To get the latest package lists

echo -n "Checking dependencies..."

bash_packages = "wine python3 python3-pip firefox"
python_packages = "schedule"

for dependencyName in $bash_packages
do
    if dpkg -l $dependencyName > /dev/null
    then 
        echo -n "$depencyName is installed. Proceeding to the next dependency..."
    else 
        echo -n "$dependencyName is NOT installed. Beggining installation..."
        sudo apt install $dependencyName -y
        echo -n "Instalation Complete: $depencyName is installed."
    fi
done

for dependencyName in $linux_packages
do
    if
    then
    else
        echo -n "$dependencyName is NOT installed. Beggining installation..."
        pip install $dependencyName
        echo -n "Instalation Complete: $depencyName is installed."
done