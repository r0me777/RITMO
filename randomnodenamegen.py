import random
import string

def name_gen():
    '''
    Uses Uppercase letters, lowercase letters, numbers, and symbols.
    At least 6 to 7 characters in length.
    Randomly Generated
    Used to randomly gen node/drone names
    '''

    x = string.printable #all strings
    x = list(x)

    lengname = random.randint(6,7) #length of node/drone
    newname = []

    for i in range(lengname):
       namechoicer = random.randint(0, 99) #randomly selects num
       newname.append(x[namechoicer])

    newname = "".join(newname)
    return newname #node/drone name

def point_gen(numofp):
    """
    This function, creates multiple (x,y) coords on a v
    virtual invisible map the drones/nodes "move" too
    :param numofp:
    :return: pointlist
    """
    randomList = []
    randomList1 = []
    pointlist = []
    for i in range(1000):  #This is overkill and could be accomplished with neater code but it works.
       r=random.randint(1,100)
       r1=random.randint(1,100)
       if r not in randomList:
          randomList.append(r)
       if r1 not in randomList1:
           randomList1.append(r1)
    while len(randomList1) > numofp:
        randomList1.pop()
    while len(randomList) > numofp:
        randomList.pop()

    for i in range(0, len(randomList)):
        insidelist = []
        insidelist.append(randomList[i]) #X
        insidelist.append(randomList1[i]) #Y
        pointlist.append(insidelist) #creats massive point list.

    return pointlist

def break_list_into_sublists(input_list, min_length, max_length):
    """
    # Breaks up the long lists of coords int randomized
    segments ranging from min_length to max_length
    to be put into node/drones
    :param input_list:
    :param min_length:
    :param max_length:
    :return: result
    """
    result = []

    while input_list:
        sublist_length = random.randint(min_length, max_length) #Gen random num
        if sublist_length > len(input_list):
            sublist_length = len(input_list)

        selected_elements = input_list[:sublist_length]
        result.append(selected_elements) #Splice section
        input_list = input_list[sublist_length:]

    return result



if __name__ == '__main__':
    print("This is the Random Password Program!")
    print("Passwords range from 12 to 14 characters")
    print("Rerun for a different password")
    #print(name_gen())
    print("non-repeating random numbers are:")
    x = point_gen(16)
    print(x)
    y = break_list_into_sublists(x,3,7)
    for i, y in enumerate(y):
        print(f"Sublist {i + 1}: {y}")

    my_list = [10, 20, 30, 40, 50]
    random_index = random.randint(0, len(my_list) - 1)


