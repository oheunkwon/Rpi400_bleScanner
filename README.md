# Rpi 400 Blescanner  
### 라즈베리 파이를 이용한 (Rpi 400) Ble scanner 구현.  
***  
### **디렉토리(라즈베리파이 내부)** 
/home/pi/projects/blescanner/
### 사용법(실행)     
 1. sudo python3 blescanner.py
  
### 코드 별 구현 기능  
* **log.py** : 로그 포맷 지정 파일  
* **scanner.py** : 주변에서 쏘는 비콘 신호로 비콘 스캔 (main)  
* **scan_func.py** : 비콘 스캔 함수
***
### 실행 화면


* 9.bad file descripter 에러 발생시
다음 명령어 순차적으로 실행하여 블루투스 활성화 후 프로그램 재 시작.

**![](https://lh4.googleusercontent.com/dwDBWjsVjN3vFrxu0RXdwHxNu9dgJk_lJOkZuRqfk8EmlzdXwi_87-LdB5CZ85_QYB-FAXJ9XzFZe88mVv-CWkUmrQxLHdjwDiK8-3gYbd272Qw0mTSkvwFYzi1vFNTvUj9TUtGZ)**

```
> systemctl status hciuart.service
> sudo systemctl start hciuart.service
> systemctl status hciuart.service
> hcitool dev # bluetooth alive check
```


**![](https://lh6.googleusercontent.com/mfw4l9cGWe1WAQGJ4IlJ5wRQS3LlniMC0PhqNzqbinOPPFbSQecDGSb5skrRtq6eM_Kdk4DJdW9b3R2VOlwcm3ZJT04UVzEmxjzpVdsvYmx8N-reBZMarUY_Y2NcigAx0tKLzYqH)**