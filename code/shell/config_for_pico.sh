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

echo '--- save and edit cmdline.txt'
cp /boot/cmdline.txt /boot/cmdline.txt.save
sed -i 's| console=serial0,115200 console=tty1||' /boot/cmdline.txt

echo '--- save and edit config.txt'
cp /boot/config.txt /boot/config.txt.save
sed -i 's|#dtparam=i2c_arm=on|dtparam=i2c_arm=on|' /boot/config.txt


echo '--- adding line to config.txt'
echo -e "\n\ndtparam=pi3-disable-bt\n\n" >> /boot/config.txt

echo '--- adding lines to /etc/modules'
echo -e "\n\ni2c-bcm2708\ni2c-dev\n\n" >> /etc/modules

echo '--- disabling hciuart'
systemctl disable hciuart

echo '--- all done'
exit 0

