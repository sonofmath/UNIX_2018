#!/bin/bash


string=$(head -n 1 /dev/ttyACM0)


echo The initial water level is: $string

#for i in {1..5}; do
#	sleep 1
#	string=$(head -n 1 /dev/ttyACM0)
#	echo The $i time is $string
#done
# Sending Emails
if [ $string -eq 0 ]; then
	python /home/pi/Desktop/UNIXPROJECT/send.py "sonofmath3.14@gmail.com" "!!! CRITICAL !!!" "Water level is at $string and needs water immediately!"
elif [ $string -le 400 ] && [ $string -gt 0 ]; then
	python /home/pi/Desktop/UNIXPROJECT/send.py "sonofmath3.14@gmail.com" "!!! DANGER !!!" "Water level is at $string and getting dangerously low! Add water ASAP!"
elif [ $string -le 800 ] && [ $string -gt 400 ]; then
	python /home/pi/Desktop/UNIXPROJECT/send.py "sonofmath3.14@gmail.com" "!!! ALERT !!!" "Water level is at $string and and needs watering soon!"
fi


 







