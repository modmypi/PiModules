#!/bin/bash

if [ `whoami` != 'root' ]; then
	echo 'Must be run as root'
	exit 1
fi

set -e

echo '--- update'
apt-get update
echo '--- install some packages'
apt-get install -y python3-dev python3-pip python3-serial python3-smbus python3-jinja2 python3-rpi.gpio # wiringpi

echo '--- pip install psutil'
pip3 install psutil

echo '--- pip install xmltodict'
pip3 install xmltodict

echo '--- save and edit cmdline.txt'
cp /boot/cmdline.txt /boot/cmdline.txt.save
sed -i 's| console=serial0,115200 console=tty1||' /boot/cmdline.txt

echo '--- save and edit config.txt'
config="/boot/config.txt"
cp $config /boot/config.txt.save

echo '--- enable i2c'
if grep -R "dtparam=i2c_arm=on" $config
then
        sed -i 's|#dtparam=i2c_arm=on|dtparam=i2c_arm=on|' $config
else
        echo 'dtparam=i2c_arm=on' $config
fi

echo '--- enable uart'
raspiuart=`cat $config | grep -R "enable_uart"`
if [ "$raspiuart" == "#enable_uart=1" ]; then
        sed -i "s,$raspiuart,enable_uart=1," $config
elif [ "$raspiuart" == "#enable_uart=0" ]; then
        sed -i "s,$raspiuart,enable_uart=1," $config
elif [ "$raspiuart" == "enable_uart=0" ]; then
        sed -i "s,$raspiuart,enable_uart=1," $config
else
        sh -c "echo 'enable_uart=1' >> $config"
fi

echo '--- enable rtc'
### Checking if rtc dtoverlay module is loaded which doesn't work on older kernels
rtcmodule=`cat $config | grep -R "dtoverlay=i2c-rtc,ds1307"`
if [ "$rtcmodule" == "#dtoverlay=i2c-rtc,ds1307" ]; then
        sed -i -e 's/#dtoverlay=i2c-rtc,ds1307/dtoverlay=i2c-rtc,ds1307/g' $config
else
        sh -c "echo 'dtoverlay=i2c-rtc,ds1307' >> $config"
fi
sleep 1


echo '--- disabling hciuart'
systemctl disable hciuart

echo '--- disable hwclock enable ds1307'
apt-get -y remove fake-hwclock
update-rc.d -f fake-hwclock remove
systemctl disable fake-hwclock

sed -i ':a;N;$!ba;s/if \[ -e \/run\/systemd\/system \] ; then\n    exit 0\nfi/#if \[ -e \/run\/systemd\/system \] ; then\n#    exit 0\n#fi/g' /lib/udev/hwclock-set
sed -i -e 's/  \/sbin\/hwclock --rtc=$dev --systz --badyear/  #\/sbin\/hwclock --rtc=$dev --systz --badyear/g' /lib/udev/hwclock-set
sed -i -e 's/  \/sbin\/hwclock --rtc=$dev --systz/  #\/sbin\/hwclock --rtc=$dev --systz/g' /lib/udev/hwclock-set
#do later in fabfile
#hwclock -w

echo '--- all done'
exit 0
