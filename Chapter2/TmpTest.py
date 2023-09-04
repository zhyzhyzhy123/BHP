import sys
import time

if __name__ == "__main__":
    print("Start Listen")
    buffer = sys.stdin.read()
    time.sleep(3)
    print("End")
    print(buffer.encode())