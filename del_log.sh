#! /bin/bash

LOG_HOME="/home/pi/projects/blescanner/logs"

find ${LOG_HOME} -type f -name "*gz" -ctime +30 -exec rm -f {}
