#-*- coding: utf-8 -*-

import configparser
import os
from AutoWorkLib import *



#control pos index
INDEX_INPUT = 0
INDEX_FLIGHT = 1
INDEX_RESULT_ROW =2
INDEX_DELETE_ALL =3
INDEX_ADD_BUTTON=4
INDEX_COMBO=5
INDEX_COMBO_OTHER=6
INDEX_LAST_NAME=7
INDEX_FIRST_NAME=8
INDEX_HOME=9
INDEX_SAVE_BUTTON=10

SLEEP_TIME=3
#로그 정의
logdir = '{0}\\log'.format(os.getcwd())

if not os.path.exists(logdir):
    os.makedirs(logdir)

logger = logging.getLogger('auto_pnr_log')
fileHandler = logging.FileHandler('{0}/autoPNR.log'.format(logdir))
streamHandler = logging.StreamHandler()

logger.addHandler(fileHandler)
logger.addHandler(streamHandler)
logger.setLevel(logging.DEBUG)

if __name__ == "__main__":
    logger.info('=======================================')
    logger.info('AUTO PNR START')
    logger.info('=======================================')

    config = configparser.ConfigParser()
    if os.path.exists('.\config.txt'):
        config.read('.\config.txt')

    # 설정 파일 확인
    file_path = config.get('AUTOPNR', 'file_path')
    start_row = config.get('AUTOPNR', 'row')
    column=config.get('AUTOPNR', 'col')
    column_index = ord(column.upper()) - ord('A') - 1

    logger.info('file path = ' + file_path + 'start row = ' + start_row + 'start column = ' + column)

    #설정 파일에서 버튼 위치를 얻는다.
    control_pos_tuple = ()
    control_pos = config.get('BUTTON_POS', 'input_box')
    input_box = control_pos.split(',')

    control_pos = config.get('BUTTON_POS', 'flight_info_box')
    flight_box = control_pos.split(',')

    control_pos = config.get('BUTTON_POS', 'result_row')
    result_row = control_pos.split(',')

    control_pos = config.get('BUTTON_POS', 'delete_all')
    delete_all = control_pos.split(',')

    control_pos = config.get('BUTTON_POS', 'add_button')
    add_button = control_pos.split(',')


    ########
    control_pos = config.get('BUTTON_POS', 'type_combo')
    type_combo = control_pos.split(',')

    control_pos = config.get('BUTTON_POS', 'type_combo_other')
    type_combo_other = control_pos.split(',')

    control_pos = config.get('BUTTON_POS', 'last_name')
    last_name = control_pos.split(',')

    control_pos = config.get('BUTTON_POS', 'first_name')
    first_name = control_pos.split(',')

    control_pos = config.get('BUTTON_POS', 'phone_home')
    phone_home = control_pos.split(',')

    control_pos = config.get('BUTTON_POS', 'save_button')
    save_button = control_pos.split(',')

    control_pos_tuple = tuple(input_box), tuple(flight_box), tuple(result_row), tuple(delete_all), tuple(add_button), tuple(type_combo), tuple(type_combo_other), tuple(last_name), tuple(first_name), tuple(phone_home), tuple(save_button)

    print(control_pos_tuple)


    #엑셀 파일에서 PNR 코드만 읽어서 리스트를 만들어 준다.
    basicfunction = AutoWorkLibExcel()
    pnr_code_list = basicfunction.LoadColumn(file_path, 'Sheet', column_index, start_row)

    #리스트 확인
    #print(len(pnr_code_list))
    #print(pnr_code_list)

    for pnrcode in pnr_code_list :

        #타이틀 클릭 후 초기화 화면에서 PNR 코드 입력
        basicfunction.leftClick((-836, 9))
        basicfunction.inputKey('F10')
        time.sleep(SLEEP_TIME)
        basicfunction.leftClick(control_pos_tuple[INDEX_INPUT])
        basicfunction.inputText(pnrcode)
        basicfunction.inputKey('enter')

        #조회 대기 후 결과 로우 더블클릭
        time.sleep(SLEEP_TIME)
        basicfunction.doubleClick(control_pos_tuple[INDEX_RESULT_ROW])

        #delete all 버튼
        time.sleep(SLEEP_TIME)
        basicfunction.leftClick(control_pos_tuple[INDEX_DELETE_ALL])

        #spacebar 입력
        time.sleep(SLEEP_TIME)
        basicfunction.inputKey('spacebar')

        #shift + F5
        time.sleep(SLEEP_TIME)
        basicfunction.shiftinputKey('F5')

        #add 버튼클릭
        time.sleep(SLEEP_TIME)
        basicfunction.leftClick(control_pos_tuple[INDEX_ADD_BUTTON])


        #type에서 other 선택 후 클릭
        time.sleep(SLEEP_TIME)
        basicfunction.leftClick(control_pos_tuple[INDEX_COMBO])
        time.sleep(0.2)
        basicfunction.leftClick(control_pos_tuple[INDEX_COMBO_OTHER])

        #last name, first name, home 입력
        time.sleep(1)
        basicfunction.leftClick(control_pos_tuple[INDEX_LAST_NAME])
        basicfunction.inputText('LASTNAME')
        time.sleep(1)
        basicfunction.leftClick(control_pos_tuple[INDEX_FIRST_NAME])
        basicfunction.inputText('FIRSTNAME')
        time.sleep(1)
        basicfunction.leftClick(control_pos_tuple[INDEX_HOME])
        basicfunction.inputText('1234')

        #save 버튼
        time.sleep(1)
        basicfunction.inputKey('enter')

        #f8 + enter + f8 + f8 + enter
        time.sleep(2)
        basicfunction.inputKey('F8')
        time.sleep(2)
        basicfunction.inputKey('enter')
        time.sleep(2)
        basicfunction.inputKey('F8')
        time.sleep(2)
        basicfunction.inputKey('F8')
        time.sleep(2)
        basicfunction.inputKey('enter')
        break