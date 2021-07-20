#!/bin/bash
# set USE_VIRTUAL_ENV as 'true' or 'false'
USE_VIRTUAL_ENV=false

echo "starting"
python_path=python3
# check if python3 is present
if [ -z $(command -v $python_path) ]; then
    echo "python3 not found, aborting...";
    exit 1;
else
    echo "python3 is present.";
fi

if [ $USE_VIRTUAL_ENV == "true" ]; then
    echo "Using virtual environment"
    if [ -d env ];then
        echo "Virtual environment exists."
    else
        echo "Creating new virtual environment."
        $python_path -m venv env
    fi
    source env/bin/activate
fi

echo "Installing dependencies."
pip3 install -r requirements.txt
if [ $? == 0 ]; then
    echo "Installed the dependencies."
else
    echo "ERROR: Dependencies are not installed. Please try to install them manually."
fi

# create directories 'out' and 'encr-decr/out'
if [ ! -d "out" ]; then
    mkdir "out"
fi
if [ ! -d "encr-decr/out" ]; then
    mkdir "encr-decr/out"
fi

echo "setup completed"
