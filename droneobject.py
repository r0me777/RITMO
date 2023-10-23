import random

class Node:
    def __init__(self, namofnode, curtasks, quesizemax):
        self.q = 0 #number of current tasks
        self.nodeN = namofnode #name of the node
        self.tasklist = curtasks  #list of tasks in Node
        self.z = quesizemax #Queue size threshold
        self.mirgratedtask = []
        self.position = []

    def positionlength(self):
        x = len(self.position)
        return x
    def move(self):
        if self.q > 0:
            self.q -= 1
            a1 = self.tasklist.pop()
            self.position.append(a1)
            return self.position
            print("     Task moved     ")
        else:
            print("The tasklist is empty. Nothing to pop.")
            return None
    def taskallocation(self,task):
         self.tasklist.append(task)
         self.q += 1
         print("     Task Allocation   ")
    def queuemax(self):
        z = self.z
        return z
    def monitor_the_queue_and_node_state(self):
        self.q = 0
        for i in self.tasklist:
            self.q += 1
        print("Node Monitored:", self.nodeN, "Queue Size:", self.q)
        return self.q

    def taskmigration(self):
        if self.q > 0:
            x = self.tasklist.pop()
            self.mirgratedtask.append(x)
            self.q -= 1
            return [x]  # Return the migrated task as a list
        else:
            print("The tasklist is empty. Nothing to pop.")
            return []

    def __str__(self):
        nodename = "Name:" + str(self.nodeN) + " Current tasks: " + str(self.q)
        nodename += " list of tasks: " + str(self.tasklist) + " queue size threshold: " + str(self.z)
        nodename += " position: " + str(self.position) + "\n    "
        print(nodename)

if __name__ == "__main__":
    pass