# UNIX_2018

Water Sensor Project
By: JR Mathson and Jeana Althea Altura

The main purpose of this project was to be able to detect changes in water level and to send alerts/notifications based on that information. This would then allow the notified person to be able to turn on a pump with just a click of a button.

To accomplish this, we used a Raspberry Pi 3, an Arduino, and a water sensor.

The first step was to program the Arduino to work with the water sensor (unix_watersensor.ino). Following this, a bash script (project.sh), ran by the Raspberry Pi, read in data from the Arduino and called upon a python script (send.py) to send out a specific email based on the water level. The bash script was paired together with a cron job that will have it run once a day for the made up scenario of needing to water a plant or fill up a dog's water bowl.

The sent out emails state the level of priority and also contain a button, that when clicked, will open a webpage. That webpage will then allow the user to turn on the water pump through the click of another button. In the background, the button from the webpage will send an email to the raspberry pi. Another cron job will run a python script (scan.py), every minute, that will check for an unread email with a specific subject line. Once it is found, a bash script (runpump.sh) is executed to give the signal to run the pump. However, due to the absence of a water pump, an led was used instead. The pump (led) would then turn off only when the water level has reached a safe level (unix_watersensor.ino). 

In using the school's wifi, there were some limitations in being able to have the webpage communicate with the raspberry pi. It was overcomed, however, by creating and using a web application (index.html & script.gs). JR created the python scripts while Jeana handled the web application. The rest was a collaborative effort. Overall, this was a fun and inspiring project to work on. 
