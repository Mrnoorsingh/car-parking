# Car Parking Detection

## Overview

The project uses MRCNN model pre-trained on MS-COCO dataset to detect vehicles and OPENCV library to process(read & write) real time video frames.
To enable SMS alert, Twilio API is utilized to send the SMS on the user's phone

The problem for parking detection can be break down as follows

![alt text](/img/pipeline.png)
 
 ---
 
 ## Example

Recorded Video     | SMS Received
:-----------------:|:-----------------------:
![](/img/park.gif) | ![alt text](/img/Screenshot%20from%202019-08-07%2002-07-53.png)



![recorded video](/img/park.gif)  ![recieved SMS](/img/Screenshot%20from%202019-08-07%2002-07-53.png)
