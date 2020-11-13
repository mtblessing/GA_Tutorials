import time
import os

for x in range(10, -1, -1):
    print("\r %d" % x, end="")
    time.sleep(1)