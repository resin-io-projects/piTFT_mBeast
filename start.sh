#!/bin/bash

if [ "$DEVICE" == 'raspberrypi' ]; then
	if [ ! -c /dev/fb1 ]; then
	  echo "loading piTFT kernel module"
	  modprobe spi-bcm2708
	  modprobe fbtft_device name=pitft verbose=0 rotate=0

	  sleep 2

	  mknod /dev/fb1 c $(cat /sys/class/graphics/fb1/dev | tr ':' ' ')
	fi
fi

exec python /usr/src/app/show.py
