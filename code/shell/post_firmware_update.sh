#!/bin/bash

if [ `whoami` != 'root' ]; then
	echo 'Must be run as root'
	exit 1
fi

set -e

echo '--- save and edit cmdline.txt'
rm /boot/cmdline.txt
cp /boot/cmdline.txt.save /boot/cmdline.txt

echo '--- adding line to config.txt'
sed -i 's|dtparam=pi3-disable-bt|#dtparam=pi3-disable-bt|' /boot/config.txt

echo '--- enabling hciuart'
systemctl enable hciuart

echo '--- enabling serial'
systemctl start serial-getty@ttyAMA0.service
systemctl enable serial-getty@ttyAMA0.service
systemctl start serial-getty@ttyS0.service
systemctl enable serial-getty@ttyS0.service

echo '--- all done'
exit 0