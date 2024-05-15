from random import randint as rd


def roll(msg):
    """Base function for rolling dices"""
    success = 0
    result = []
    for i in range(int(msg[1])):
        tmp = rd(1, int(msg[2]))
        result.append(tmp)
        if tmp >= int(msg[3]):
            success += 1
        elif tmp == 1:
            success -= 1
        if success < 0:
            success = 0
    return result, success


def rollone(msg):
    """Function for rolling one dice at a time"""
    tmp = rd(1, int(msg[2]))
    result = [tmp]
    success = 0
    if tmp > int(msg[3]):
        success = 1
    elif tmp == 1:
        success = -1
    if tmp == int(msg[2]):
        reroll = rollone(msg)
        tmp1, tmp2 = [j for j in reroll]
        success += tmp2
        result.append(tmp1)
    return result, success


def rollV3(msg):
    """Fuction for rolling dices according to the rules of Revised Edition"""
    success = 0
    result = []
    for i in range(int(msg[1])):
        tmp = rd(1, int(msg[2]))
        result.append(tmp)
        if tmp >= int(msg[3]):
            success += 1
        elif tmp == 1:
            success -= 1
        if tmp == int(msg[2]):
            reroll = rollone(msg)
            tmp1, tmp2 = [j for j in reroll]
            success += tmp2
            result.append(tmp1)
    if success < 0:
        success = 0
    return result, success


def rollV4(msg):
    """Fuction for rolling dices according to the rules of 20th Edition"""
    success = 0
    result = []
    for i in range(int(msg[1])):
        tmp = rd(1, int(msg[2]))
        result.append(tmp)
        if int(msg[3]) <= tmp < int(msg[2]):
            success += 1
        elif tmp == 1:
            success -= 1
        elif tmp == int(msg[2]):
            success += 2
    if success < 0:
        success = 0
    return result, success
