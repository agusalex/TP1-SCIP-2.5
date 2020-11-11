# TP1-SCIP-2.5
Paquetes requeridos: PySCIPOpt el siguiente script los instala y todo lo que se necesita para ejecutarse
## Ubuntu 18/20
Download https://www.scipopt.org/download.php?fname=SCIPOptSuite-7.0.1-Linux.deb

    sudo dpkg -i SCIPOptSuite-7.0.1-Linux.deb
    sudo apt-get install python3-pip python3-venv
    python3 -m venv venv
    source venv/bin/activate
    python3 -m pip install --upgrade pip
    pip install -r requirements.txt
    python main.py

## Next time
    source venv/bin/activate
## Docs
https://pypi.org/project/PySCIPOpt/
