class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = self.rear = None

    def is_empty(self):
        return self.front == None

    def enqueue(self, data):
        new_node = Node(data)

        if self.front == None:
            self.front = self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        if self.is_empty():
            print('the Queue is empty!!')
            return
        tmp = self.front
        self.front = tmp.next

        if self.front == None:
            self.rear = None

q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
print(str(q.front.data),str(q.rear.data))
q.dequeue()
print(str(q.front.data),str(q.rear.data))

#lists
my_list=[]
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.pop(1)
print(my_list)
my_list.pop()
print(my_list)

#2ta module ham darim vase queue ha
from queue import Queue
q=Queue(maxsize=4)
q.put('a')
q.put(1)
q.put('b')
q.put(2)
#agar put be tanhayi estefade beshe bade full shodane queue error nemide
# q.put('c')
#vali age az put_nowait estefaade beshe error mide
# q.put_nowait('c')
# print(q.queue)
# print(q.full())
q.get()
q.get()
q.get()
q.get()
# print(q.full())
# print(q.empty())
#bad az empty shodane queue harcheghad ham get konim error nemide
# q.get()
# q.get()
# q.get()
#agar bekhaym error bede bade khali shodane queue bayad get_nowait bashe
#albate bayad havaset bashe age get ha bishtar az tedad bashe error nemide
# va app haminjoor open mimooone va dar hale ejra mimoone yejoorayi!!
# print(q.get_nowait())

#module 2
from collections import deque

d=deque()
d.append(10)
d.append(20)
d.append(40)
print(d)
d.popleft()
print(d)
d.pop()
print(d)
#agar pop() bashe az akhar ke add shodan pop mikone(raast) pas mishe hamoon
# stack ya poshte ;))