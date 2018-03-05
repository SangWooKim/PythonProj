#-*- coding: utf-8 -*-

import operator

if __name__ == "__main__":

    agent_service_log_path  = 'E:\\UserData\\insoft\\Downloads\\NGFAgent\\log\\service_20180302.log'
    handler_dictionary = {}

    source_file = open(agent_service_log_path, 'r', encoding='UTF8')
    read_lines  = source_file.read().splitlines()

    for line in read_lines:

        split_line = line.split(' ')

        if '[REQ]' == split_line[3] or '[RSP]' == split_line[3] or '[RES]' == split_line[3]:
            handler_key = '{0}-{1}'.format(split_line[2], split_line[3])
            if not handler_key in handler_dictionary :
                handler_dictionary[handler_key] = 0

            handler_dictionary[handler_key] += 1

    sorted_handler = sorted(handler_dictionary.items(), key=operator.itemgetter(0))

    print('############# HANDER COUNTER INFO #############')

    for handler_item in sorted_handler:
        print('%25s : %5d' % (handler_item[0], handler_item[1]))

    source_file.close()


    print('############FINISH################')