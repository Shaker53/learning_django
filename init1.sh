sudo apt update
sudo apt-get install -y lynx #debug
sudo apt install -y python3.5
sudo apt-get install -y python3.5-dev
sudo rm /usr/bin/python3
sudo ln -s /usr/bin/python3.5 /usr/bin/python3
sudo pip3 install --upgrade pip
sudo -H pip3 install --upgrade django==2.0.1
sudo -H pip3 install --upgrade gunicorn
sudo -H pip3 install --upgrade mysqlclient