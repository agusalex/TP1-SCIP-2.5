# TP1-SCIP-2.5
download https://www.scipopt.org/download.php?fname=SCIPOptSuite-7.0.1-Linux.deb
dpkg -i SCIPOptSuite-7.0.1-Linux.deb
apt-get install python3-pip python3-venv
python3 -m venv venv
source venv/bin/activate
python3 -m pip install --upgrade pip
pip install -r requirements.txt


# every time you want to work on your project run:
source venv/bin/activate