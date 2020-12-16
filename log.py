import logging
import os
import time
from logging.handlers import TimedRotatingFileHandler


def get_log(name):
    # 로그 저장할 폴더 생성
    log_dir = '/home/pi/projects/blescanner/logs'
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    # 로거 생성
    logger = logging.getLogger(name)
    if len(logger.handlers) > 0:
        return logger
    # host_name = os.popen('hostname').read().replace('\n', '')
    # ip = os.popen('hostname -I').read().replace(' \n', '')
    # host_ip = host_name + '(' + ip + ')'

    formatter_str = '%(asctime)s %(levelname)s [%(filename)s:%(lineno)d] %(message)s'
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter(formatter_str, "%Y-%m-%d %H:%M:%S")
    # 로거에 핸들러 추가
    # 자정마다 한 번씩 로테이션
    file_handler = logging.handlers.TimedRotatingFileHandler(
        # filename='%s/subscribeLog.log' % log_dir, when='midnight', interval=1, encoding='utf-8'
        filename='%s/eg.log' % log_dir, when='midnight', interval=1, encoding='utf-8'
    )

    file_handler.suffix = '%Y%m%d'  # 로그 파일명 날짜 기록 부분 포맷 지정
    file_handler.setFormatter(formatter)  # 핸들러에 로깅 포맷 할당
    logger.addHandler(file_handler)
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    logger.addHandler(console_handler)
    return logger
