#-*- coding: utf-8 -*-

import random

#로또 번호 5개를 생성하는데, 45개의 숫자가 중복되지 않은 숫자로 5게임을 만든다.
if __name__ == "__main__":
    #지난주 당첨 번호는 제외 하자 아니면 그냥 맘에 안드는 숫자라든가..
    except_number = [6, 7, 18, 19, 30, 38]

    lotto_base = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                 1, 1, 1, 1, 1]



    #지난주 당첨 번호를 제외 한다.
    for lott_number in except_number:
        lotto_base[lott_number] = 0

    game_result = []

    #랜덤한 숫자를 생성 꺼내서 게임결과에 넣어준다.
    game_single = []
    while len(game_result) != 5 :
        random_number = random.randrange(1, 45)
        if lotto_base[random_number] == 1 :
            lotto_base[random_number] = 0
            game_single.append(random_number)
            if len(game_single) == 6 :
                game_single.sort()
                game_result.append(game_single)
                game_single = []

    for mygame in game_result:
        print ("%17s" % (mygame))

    print(random)