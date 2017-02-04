#!/bin/bash

if [ `whoami` != 'root' ]; then
	echo 'Must be run as root'
	exit 1
fi

set -e

echo '--- save and edit cmdline.txt'
cp /boot/cmdline.txt /boot/cmdline.txt.save
sed -i 's| console=ttyAMA0,115200||' /boot/cmdline.txt

echo '--- adding line to config.txt'
echo -e "\n\ndtparam=pi3-disable-bt\n\n" >> /boot/config.txt

echo '--- disabling hciuart'
systemctl disable hciuart

echo '--- disabling serial'
systemctl stop serial-getty@ttyAMA0.service
systemctl disable serial-getty@ttyAMA0.service
systemctl stop serial-getty@ttyS0.service
systemctl disable serial-getty@ttyS0.service

echo '--- all done'
exit 0