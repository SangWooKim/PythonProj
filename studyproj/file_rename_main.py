#-*- coding: utf-8 -*-

import configparser
import logging.handlers
import os

logdir = '{0}\\log'.format(os.getcwd())

if not os.path.exists(logdir):
    os.makedirs(logdir)

logger = logging.getLogger('auto_task_log')
fileHandler = logging.FileHandler('{0}/autotask.log'.format(logdir))
streamHandler = logging.StreamHandler()

logger.addHandler(fileHandler)
logger.addHandler(streamHandler)
logger.setLevel(logging.DEBUG)


if __name__ == "__main__":
    logger.info('=======================================')
    logger.info('File rename')
    logger.info('=======================================')


    config = configparser.ConfigParser()
    if os.path.exists('.\config.txt'):
        config.read('.\config.txt')

    root_path = "C:\\IN-SOFT\\OpenManager3.0\\log\\"

    '''
    #파일명 변경하기
    for filename in os.listdir(root_path):
        if filename[-3:] == "log":
            full_path = root_path + filename
            target_path = full_path.replace('.log', '.txt')
            os.rename(full_path, target_path)
    '''


    for filename in os.listdir(root_path):
        if filename[-3:] == "txt":
            full_path = root_path + filename
            target_path = full_path.replace('.txt', '.sql')

            source_file = open(full_path, 'r', encoding='UTF8')
            target_file = open(target_path, 'w', encoding='UTF8')
            while True:
                line = source_file.readline()
                if not line: break
                if line[0] != '[':
                    target_file.write(line)

            source_file.close()
            target_file.close()
