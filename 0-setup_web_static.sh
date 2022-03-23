#!/usr/bin/env bash
#  sets up your web servers for the deployment of web_static

sudo apt-get -y install nginx
mkdir -p /data
mkdir /data/web_static
mkdir /data/web_static/releases
mkdir /data/web_static/shared
mkdir /data/web_static/releases/test
touch /data/web_static/releases/test/index.html
rm -f /data/web_static/current && ln -s /data/web_static/releases/test/ /data/w>
chown -hR ubuntu:ubuntu /data
redirect="\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t>
sudo sed -i "50s|.*|$redirect|" /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart

