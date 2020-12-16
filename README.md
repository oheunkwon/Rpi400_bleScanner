# Rpi 400 Blescanner  
### Ble scanner (Bluetooth device scanner) using Raspberry pi 400.  
***  
### **Directory** 
/home/pi/projects/blescanner/
### Run command     
 1. sudo python3 /home/pi/projects/blescanner/blescanner.py
 (It needs "sudo" because of the bluetooth activation thing..)
  
### source code explanation
* **log.py** : log formatting source code  
* **scanner.py** : scanning bluetooth devices around rpi 400 (main)  
* **activateble.py** : make raspberry pi into a beacon.
* **scan_func.py** : scan function source code
* **del_log.sh** : delete file the day exceeds 30 days after created  
* **zip_log.sh** : compresses(.zip) file the day exceeds 10 days after created  


***
### Run project

#### ERROR
* If "9.bad file descripter" ERROR occurs,
it means you did not activated rpi's bluetooth functions. 
you can activate bluetooth function by conducting following commands.
**![](https://lh4.googleusercontent.com/dwDBWjsVjN3vFrxu0RXdwHxNu9dgJk_lJOkZuRqfk8EmlzdXwi_87-LdB5CZ85_QYB-FAXJ9XzFZe88mVv-CWkUmrQxLHdjwDiK8-3gYbd272Qw0mTSkvwFYzi1vFNTvUj9TUtGZ)**

```
> systemctl status hciuart.service
> sudo systemctl start hciuart.service
> systemctl status hciuart.service
> hcitool dev # bluetooth alive check
```


**![](https://lh6.googleusercontent.com/mfw4l9cGWe1WAQGJ4IlJ5wRQS3LlniMC0PhqNzqbinOPPFbSQecDGSb5skrRtq6eM_Kdk4DJdW9b3R2VOlwcm3ZJT04UVzEmxjzpVdsvYmx8N-reBZMarUY_Y2NcigAx0tKLzYqH)**