#! /bin/bash
LOG_HOME="/home/pi/projects/blescanner/logs"
GZIP_INTERVAL=10

find ${LOG_HOME} -type f -mtime +${GZIP_INTERVAL} -exec gzip {} +