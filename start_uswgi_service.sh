#!/usr/bin/env bash
# https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-uwsgi-and-nginx-on-ubuntu-16-04
cp ~/site/site.service /etc/systemd/system/site.service
sudo systemctl start site
sudo systemctl enable site

cp ~/site/nginx_config /etc/nginx/sites-available/site
sudo ln -s /etc/nginx/sites-available/site /etc/nginx/sites-enabled

sudo systemctl restart nginx
