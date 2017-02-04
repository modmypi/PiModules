#!/bin/bash

if [ `whoami` != 'root' ]; then
	echo 'Must be run as root'
	exit 1
fi

set -e

echo '--- update'
apt-get update
echo '--- install some packages'
apt-get install -y python-dev python-pip python-serial python-smbus python-jinja2 wiringpi

echo '--- pip install psutil'
pip install psutil

echo '--- pip install xmltodict'
pip install xmltodict

echo '--- installing & enabling daemon'
cd PiModules/code/python/package
python setup.py install
cd ../upspico/picofssd
python setup.py install
systemctl enable picofssd.service

echo '--- adding line to config.txt'
echo -e "\n\ndtoverlay=i2c-rtc,ds1307\n\n" >> /boot/config.txt
echo -e "\n\nenable_uart=1\n\n" >> /boot/config.txt

echo '--- adding lines to /etc/modules'
echo -e "\n\ni2c-bcm2708\ni2c-dev\rtc-ds1307\n\n" >> /etc/modules

echo '--- removing fake-hwclock'
apt-get -y remove fake-hwclock && sudo update-rc.d -f fake-hwclock remove

echo '--- all done'
exit 0
