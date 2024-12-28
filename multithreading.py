########## using time module to know the excution time for task ##########
# import time as t

# start = t.perf_counter()
# print(start)

# def do_something():
#     print("Sleeping 1 second...")
#     t.sleep(1)
#     print("Done sleeping...")   

# do_something()
# end = t.perf_counter()

# print(f'Finished in {round(end-start,2)} second(s)') 


####### Threading ########
# for only one thread(one process)

# import time
# import threading as T

# start = time.perf_counter()

# def do_something():
#     print("Sleeping 1 second...")
#     time.sleep(1)
#     print("Done sleeping...")   

# t1 = T.Thread(target = do_something) # we have created a thread object
# t1.start() # we have link the thread to the function
# t1.join() # we have executed the thread

# end = time.perf_counter()
# print(f'Finished in {round(end-start,4)} seconds(s)')


###################################################################################
# we can create multiple threads

import time
import threading as T

start = time.perf_counter()

def do_something():
    print("Sleeping 1 second...")
    time.sleep(1)
    print("Done sleeping...")   

threads = []
# creating and linking 10 threads
for _ in range(10):
    t = T.Thread(target = do_something)
    t.start()
    threads.append(t)

# we can excute all threads at once but one by one
for th in threads:
    th.join()# we have executed the threads

end = time.perf_counter()
print(f'Finished in {round(end-start,4)} seconds(s)')
