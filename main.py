import random
from droneobject import Node
from randomnodenamegen import name_gen
from randomnodenamegen import point_gen
from randomnodenamegen import break_list_into_sublists

def check(list):
    return all(i == list[0] for i in list)

if __name__ == "__main__":
    Nodelist = [] #
    oldPointlist = []
    AmountofNodes = 5
    AmountofPoints = (AmountofNodes * 5) - 1
    oldPointlist = point_gen(AmountofPoints)
    newPointlist = break_list_into_sublists(oldPointlist, 3, 7)

    for i in range(0, AmountofNodes):
        Nodelist.append(Node(name_gen(), newPointlist[i - 1], 5))

    for node in Nodelist:
        node.monitor_the_queue_and_node_state()
        node.__str__()

    r = 0
    current_node_index = 0
    positions_filled = 0
    print(positions_filled)
    c =True
    while c:

        current_node = Nodelist[current_node_index]
        q = current_node.monitor_the_queue_and_node_state()
        z = current_node.queuemax()
        current_node.__str__()

        if q > z:
            task = current_node.taskmigration()
            g = True
            while g:
                random_node_index = random.randint(0, len(Nodelist) - 1)
                random_target_node = Nodelist[random_node_index]

                if random_target_node.queuemax() > len(random_target_node.tasklist):
                    random_target_node.taskallocation(task)
                    positions_filled += 1
                    #print(positions_filled)
                    g = False

        if r == 0:
            rq = q + 1
            if rq > z:
                task = current_node.taskmigration()
                z = True
                while z:
                    random_node_index = random.randint(0, len(Nodelist) - 1)
                    random_target_node = Nodelist[random_node_index]

                    if random_target_node.queuemax() > len(random_target_node.tasklist):
                        random_target_node.taskallocation(task)
                        positions_filled += 1
                        #print(positions_filled)
                        z = False

        if q != 0:
            current_node.move()
            positions_filled += 1

        if q <= 0:
            current_node_index = (current_node_index + 1) % len(Nodelist)

        # Print positions_filled here to check its value

    # If you want to check after the loop, print it here
        print(positions_filled)

        tasklistcheck = []
        for i in range(0,AmountofNodes):
            tasklistcheck.append(Nodelist[i].tasklist)

        trorf = check(tasklistcheck)
        if trorf == True:
            c = False
            print("EXIT")
        #if all(len(node.tasklist) == 0 for node in Nodelist):
        #    c = False
