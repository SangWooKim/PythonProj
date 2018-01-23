#-*- coding: utf-8 -*-

import configparser
import logging.handlers
import os
import AutoPNRLib
import openpyxl

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
    logger.info('Sale END')
    logger.info('=======================================')

    config = configparser.ConfigParser()
    if os.path.exists('.\config.txt'):
        config.read('.\config.txt')

    # 설정 파일 확인
    file_path = 'C:\\Users\\swkim\\Documents\\카카오톡 받은 파일\\SomSaleEndListExcel.xlsx'
    start_row = 7
    column = 5
    sheet_name = 'Sheet'



    #엑셀 파일에서 PNR 코드만 읽어서 리스트를 만들어 준다.
    basicfunction = AutoPNRLib.AutoPNRLib()
    option_list = basicfunction.LoadXLSXData(file_path, sheet_name, column, start_row)

    option_list.sort()
    print(option_list)


    #리스트 확인
    #print(len(pnr_code_list))
    #print(option_list)


    wb = openpyxl.load_workbook(file_path)
    ws_result = wb.create_sheet('result')
    ws_data = wb[sheet_name]

    col_range = 'ABCDEFGHIJKLMNOPQRSTUVW'


    # A ~ W 까지
    for idx, option in enumerate(option_list) :
        row_index = option[1]
        for idx_col, arg in enumerate(col_range):
            ws_result.cell(row=idx + start_row, column=idx_col+1, value=ws_data[arg + str(row_index)].value)

    wb.save(file_path)
    wb.close()