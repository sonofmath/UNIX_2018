# UNIX_2018

Water Sensor Project
By: JR Mathson and Jeana Althea Altura

The main purpose of this project was to be able to detect changes in water level and to send alerts or notifications based on that information. This would then allow the notified person to be able to turn on a pump with just a click of a button.

To accomplish this, we used a Raspberry Pi 3, an Arduino, and a water sensor.

Our first step was to program the Arduino to work with the water sensor. Following this, we used a bash script, ran by the Raspberry Pi, to read in the data from the Arduino and based on the water level at a specific point in time, will send out an email if the water level is low. This script pairs together with a cron job that would have it run once a day for our made up scenario of needing to water a plant or fill up a dog's water bowl.
