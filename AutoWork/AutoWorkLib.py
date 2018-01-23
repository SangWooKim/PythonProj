#-*- coding: utf-8 -*-
import logging
import openpyxl
import win32api, win32con, time
from AutoWorkDefine import VK_CODE


class AutoWorkLibExcel(object):

    def __init__(self):
        self.mylogger = logging.getLogger('auto_work_log')
        return

    '''주어진 xlsx파일의 sheet에서 선택한 컬럼을 읽고 row index를 저장한다.'''
    def LoadColumn(self, file_path, sheet_name, column, row =0):
        ret_column_list = []
        wb = openpyxl.load_workbook(file_path)
        ws = wb[sheet_name]

        for r in ws.rows:
            row_index = r[0].row
            if row_index < int(row):
                continue

            ret_column_list.append(r[column].value)

        wb.close()
        return ret_column_list

    ##AutoWorkLibExcel END
    ############

class AutoworkLibKeyboardMouse(object):
    def __init__(self):
        self.mylogger = logging.getloger('auto_work_log')
        return

    '''주어진 text를 한글자씩 키보드 이벤트를 발생한다.'''
    def inputText(self, text):
        for arg in text:
            win32api.keybd_event(VK_CODE[arg], 0, 0, 0)
            time.sleep(0.01)

            win32api.keybd_event(VK_CODE[arg], 0, win32con.KEYEVENTF_KEYUP, 0)
        return

    '''방향키 홈키와 같은 특수키를 눌렀다가 뗀다.'''
    def inputKey(self, keyName):
        win32api.keybd_event(VK_CODE[keyName], 0, 0, 0)
        time.sleep(0.01)
        win32api.keybd_event(VK_CODE[keyName], 0, win32con.KEYEVENTF_KEYUP, 0)
        return

    '''주어진 키를 누르고 있는다.'''
    def holdKey(self, keyName):
        win32api.keybd_event(VK_CODE[keyName], 0, 0, 0)
        return

    '''눌려진 키를 뗀다.'''
    def releaseKey(self, keyName):
        win32api.keybd_event(VK_CODE[keyName], 0, win32con.KEYEVENTF_KEYUP, 0)
        return

    '''pos로 주어진 위치에 마우스를 클릭한다.'''
    def leftClick(self, pos):
        pos_x = int(pos[0])
        pos_y = int(pos[1])
        win32api.SetCursorPos((pos_x, pos_y))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, pos_x, pos_y, 0, 0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, pos_x, pos_y, 0, 0)
        return

    '''pos로 주어진 위치에 마우스를 더블 클릭한다.'''
    def doubleClick(self, pos):
        pos_x = int(pos[0])
        pos_y = int(pos[1])
        win32api.SetCursorPos((pos_x, pos_y))  # set the cursor to where you wanna click
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, pos_x, pos_y, 0, 0)  # generate a mouse event
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, pos_x, pos_y, 0, 0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, pos_x, pos_y, 0, 0)  # generate a mouse event
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, pos_x, pos_y, 0, 0)
        return

    ##AutoworkLibKeyboardMouse END
    ############



