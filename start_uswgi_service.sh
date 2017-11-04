#!/usr/bin/env bash
cp ~/site/site.service /etc/systemd/system/site.service
sudo systemctl start site
sudo systemctl enable site

cp ~/site/nginx_config /etc/nginx/sites-available/site
sudo ln -s /etc/nginx/sites-available/site /etc/nginx/sites-enabled