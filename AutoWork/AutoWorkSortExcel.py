#-*- coding: utf-8 -*-

import configparser, os, re, datetime, time
import logging.handlers
from AutoWorkLib import *

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
'''
로직 순서
1. 주어진 엑셀 파일에서 F 컬럼 7번째 로우 부터 모두 읽는다.
2. 읽은 데이타에서 "날짜" 단어로 구분한다.
  * XXXXXXXX구간:제주→김포,날짜:2/1 (목),시간:09:05-1개 -->날짜:2/1 (목),시간:09:05-1개
3. 날짜를 기준으로 정렬한다.
4. 정렬된 row를 F 컬럼부터 하나씩 읽어서 result 시트에 저장한다.
'''
if __name__ == "__main__":
    logger.info('=======================================')
    logger.info('Autowork sort excel')
    logger.info('=======================================')

    config = configparser.ConfigParser()
    if os.path.exists('.\config.txt'):
        config.read('.\config.txt')

    # 설정 파일 확인
    file_path = 'E:\\UserData\\insoft\\Documents\\카카오톡 받은 파일\\SomSaleEndListExcel.xlsx'
    start_row = 7
    column = 5
    sheet_name = 'Sheet'

    #엑셀 파일에서 주어진 컬럼의 값을 모두 읽는다.
    basicfunction = AutoWorkLibExcel()
    column_data_list = basicfunction.LoadColumn(file_path, sheet_name, column, start_row)



    # "날짜"를 구분자로해서 나눠주고 날짜 부분을 맨앞으로 옮겨준다.
    # "날짜"로 구분된 토큰이 1/1 이라면 01/01 로 변경한다.
    sorted_list = []
    month = 1
    day =1
    hour = 0
    min = 0
    for idx, column_data in enumerate(column_data_list):
        date_string = column_data.split('날짜')[1]

        print(date_string)

        p_date = re.compile('[0-9]{1,2}/[0-9]{1,2} ')
        match_date = p_date.search(date_string)
        if match_date :
            month = int(match_date.group().split('/')[0])
            day = int(match_date.group().split('/')[1])


        p_time = re.compile('[0-9]{2}:[0-9]{2}')
        match_time = p_time.search(date_string)
        if match_time:
            hour = int(match_time.group().split(':')[0])
            min = int(match_time.group().split(':')[1])

        sort_key = datetime.datetime(2018, month, day, hour, min)
        sorted_list.append( (str(sort_key), idx + start_row) )

    sorted_list.sort()
    print(sorted_list)


    #리스트 확인
    #print(len(pnr_code_list))
    #print(option_list)
    wb = openpyxl.load_workbook(file_path)
    ws_result = wb.create_sheet('result')
    ws_data = wb[sheet_name]

    col_range = 'FGHIJKLMNOPQRSTUVW'

    # A ~ W 까지
    for idx, option in enumerate(sorted_list) :
        row_index = option[1]
        for idx_col, arg in enumerate(col_range):
            if idx_col == 0:
                temp = ws_data[arg + str(row_index)].value.split('구간')[1]
                ws_result.cell(row=idx + start_row, column=1, value='구간' + temp)
            ws_result.cell(row=idx + start_row, column=idx_col + 2, value=ws_data[arg + str(row_index)].value)

    wb.save(file_path)
    wb.close()
