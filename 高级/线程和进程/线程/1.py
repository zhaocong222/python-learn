from threading import Thread
import time

def test():
    print("-----hello world-----")
    time.sleep(1)

from i in range(5):
    t = Thread(target=test)
    t.start()
