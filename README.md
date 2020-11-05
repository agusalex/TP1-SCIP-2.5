# TP1-SCIP-2.5
## Ubuntu 18/20
Download https://www.scipopt.org/download.php?fname=SCIPOptSuite-7.0.1-Linux.deb

    dpkg -i SCIPOptSuite-7.0.1-Linux.deb
    apt-get install python3-pip python3-venv
    python3 -m venv venv
    source venv/bin/activate
    python3 -m pip install --upgrade pip
    pip install -r requirements.txt
    python main.py

## Next time

    source venv/bin/activate
