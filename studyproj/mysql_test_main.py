#-*- coding: utf-8 -*-

import os
import pymysql

if __name__ == "__main__":
    print('=======================================')
    print('==============PROJECT START============')
    print('=======================================')

    # MySQL Connection 연결
    conn = pymysql.connect(host='192.168.255.193', user='root', password='2358', db='bsp_stat', charset='utf8')
    # Connection 으로부터 Cursor 생성
    curs = conn.cursor()
    time_table_sql = 'call make_intervals(\'2018-03-07 00:00\',\'2018-03-08 00:00\',1,\'MINUTE\'); '
    curs.execute(time_table_sql)

    work_root = 'E:\\UserData\\insoft\\Documents\\네이블\\BPP_SQL\\nable_sql\\'
    full_sql = work_root + 'full_sql.info'
    full_sql_file = open(full_sql, 'w', encoding='UTF8')

    for filename in os.listdir(work_root):
        if filename[-3:] != "sql":
            continue
        full_sql_file.write('\n\ntee /root/nable_sql/%s.result\n\n' % filename)
        full_path = work_root + filename
        sql_file = open(full_path, 'r', encoding='UTF8')
        read_lines = sql_file.read().split('============================================================================================')

        for idx, sql_line in enumerate(read_lines):
            if idx > 0:
                full_sql_file.write(sql_line)

        full_sql_file.write('\n\nnotee\n\n')

    conn.close()