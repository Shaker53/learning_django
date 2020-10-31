sudo /etc/init.d/mysql start
mysql -uroot -e "CREATE DATABASE stepic_web;"
mysql -uroot -e "GRANT ALL ON stepic_web.* TO 'box'@'localhost' WITH GRANT OPTION;"
python3 ~/web/ask/manage.py makemigrations
python3 ~/web/ask/manage.py migrate

sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo rm -rf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
cd web/
sudo gunicorn -b 0.0.0.0:8000 hello:app&
cd ask/
sudo gunicorn -b 0.0.0.0:8080 ask.wsgi:application&