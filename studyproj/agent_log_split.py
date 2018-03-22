#-*- coding: utf-8 -*-

import operator

if __name__ == "__main__":
    agent_service_log_path  = 'E:\\UserData\\insoft\\Downloads\\NGFAgent\\log\\service_20180316.log'
    handler_dictionary = {}
    single_line_char = {}

    source_file = open(agent_service_log_path, 'r', encoding='UTF8')
    read_lines  = source_file.read().splitlines()
    source_file.close()

    '''

    output_file = open('C:\\IN-SOFT\\OpenManager3.0\\log\\formet_sql.txt', 'r', encoding='UTF8')
    output_file2 = open(agent_service_log_path + '.output2', 'w', encoding='UTF8')    

    output_lines = output_file.read().splitlines()
    for idx, line in enumerate(output_lines):
        if ';============================================================================================' in line :
            line = line.replace(';============================================================================================', ';')
            output_file2.write(line + '\n')
            output_file2.write('============================================================================================\n')
        else :
            output_file2.write(line + '\n')
    '''

    
    #로그에서 특정 키워드를 가지는 내용을 뺴서 파일로 만들어 준다.
    output_file = open(agent_service_log_path + '.output', 'w', encoding='UTF8')
    output_line = []
    for idx, line in enumerate(read_lines):
        if '[ERRPT]' in line:
            output_line.append(line)

    #중복 아이템 제거
    output_line = list(set(output_line))
    for wline in output_line:
        output_file.write(wline + '\r\n')

    output_file.close()




    #로그에서 핸들러별 요청/응답의 갯수를 센다.
    for idx, line in enumerate(read_lines):

        if len(line) > 999 :
            single_line_char[str(idx)] = len(line)

        split_line = line.split(' ')

        if len(split_line) > 3:
            if '[REQ]' == split_line[3] or '[RSP]' == split_line[3] or '[RES]' == split_line[3]:
                handler_key = '{0}-{1}'.format(split_line[2], split_line[3])
                if not handler_key in handler_dictionary :
                    handler_dictionary[handler_key] = 0

                handler_dictionary[handler_key] += 1

    print('############# HANDER COUNTER INFO #############')
    sorted_handler = sorted(handler_dictionary.items(), key=operator.itemgetter(0))
    for sorted_item in sorted_handler:
        print('%25s : %5d' % (sorted_item[0], sorted_item[1]))

    print('############# SINGLE LINE LENGTH #############')
    sorted_handler = sorted(single_line_char.items(), key=operator.itemgetter(0))
    for sorted_item in sorted_handler:
        print('%25s : %5d' % (sorted_item[0], sorted_item[1]))
        


    print('############FINISH################')