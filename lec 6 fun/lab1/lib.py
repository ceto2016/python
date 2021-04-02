def setBit(num, bit):
    # num is 0010 in dec == 2
    # we want to set bit 2
    # move 1 to the bit we wnat to set
    #  1 << 2 == 0100
    # we will use or to set
    # 0010 | 0100 == 0110
    x = 1 << bit
    print("number after setting bit" + str(bit) + " is : ", num | x)


def clearBit(num, bit):
    # 1- num is 0010 in dec == 2
    # 2- we want to clear bit 2
    # 3- move 1 to the bit we wnat to clear
    # 4-  1 << 2 == 0100
    # 5- we will use and to clear
    # 6- 0010 and 0100 == 0000 wrong !!!
    # 7- before we use and we should use not on 1 after step 4
    # so ~(0100) == 1011
    # now we use and ----> 0010 & 1011 ==  0010 because bit 2 is 0 and still 0
    x = 1 << bit
    print("number after clear bit " + str(bit) + " is : ", num & ~x)


def toggleBit(num, bit):
    # 1- num is 0010 in dec == 2
    # 2- we want to clear bit 2
    # 3- move 1 to the bit we wnat to clear
    # 4-  1 << 2 == 0100
    # 5- we use xor to toggle the bit
    # 6- 0010 ^ 0100 == 0110
    x = 1 << bit
    print("number after toggle bit " + str(bit) + " is : ", num ^ x)


def getBit(num, bit):
    #  1- move the bit you want to get to bit 0 num >> bit
    #  2- num = 0110 you want to read bit 1 so 0110 >> 1 == 0011
    #  3- use and  with 0001 to clear all other bits 0011 & 0001 == 0001
    # 4- you now have bit 1
    x = num >> bit
    print("bit is : ", 1 & x)
