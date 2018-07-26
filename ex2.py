
from lib.queue import Queue


def hot_potato(name_list, num):
    q = Queue()

    for i in range(len(name_list)):
        q.enqueue(name_list[i])

    while num > 0 :
        if q.size() > 1:
            for i in range(num):
                q.enqueue(q.dequeue())
            q.dequeue()

        if q.size() == 1:
            remaining_person = q.dequeue()
            break    

    return remaining_person

hot_potato(["Susan", "Brad", "Kent", "David"], 6)           
hot_potato(["Bill", "David", "Susan", "Jane", "Kent", "Brad"], 7) 
