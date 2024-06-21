# running a function in another thread
from time import sleep, ctime
from threading import Thread

#a custom funtion tat blocks for a moment
def task():
    #block for a moment
    sleep(1)
    # display a message
    print(f'{ctime()}this is from another thread')

# create a thread
thread = Thread(target=task)
#run the thread
thread.start()
#wait for the thread of finish
print(f'{ctime()}Waiting for the thread...')
thread.join()