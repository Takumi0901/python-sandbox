from time import sleep
from threading import Thread

target_time = 10

def up_timer(secs):
  for i in range(0, secs):
    print(i)
    sleep(1)
  print("finish up!")

def down_timer(secs):
  for i in range(secs, -1, -1):
    print(i)
    sleep(1)
  print("finish down!")

thread_1 = Thread(target=up_timer,args=(target_time,))
thread_2 = Thread(target=down_timer,args=(target_time,))

thread_1.start()
thread_2.start()