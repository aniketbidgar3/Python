import threading
import time

def fun(sec):
    print(f"Sleeping for {sec} seconds\n")
    time.sleep(sec)



# This Process Takes Total 12 Seconds

start=time.perf_counter()

fun(3)
fun(3)
fun(3)

end=time.perf_counter()
print("Serial : ",end-start)



# This Process Takes only 4 Seconds

start=time.perf_counter()

t1=threading.Thread(target=fun,args=[3])
t2=threading.Thread(target=fun,args=[3])
t3=threading.Thread(target=fun,args=[3])


t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

end=time.perf_counter()
print(end-start)