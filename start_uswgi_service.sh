#!/usr/bin/env bash
cp site/site.service /etc/systemd/system/site.service
sudo systemctl start site
sudo systemctl enable site