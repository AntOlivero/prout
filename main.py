from playsound import playsound
from pynput.keyboard import Listener
import threading

def honk() :
    while True :
        on_press(key)


class myThread(threading.Thread) :
    def __init__(self, name) :
        threading.Thread.__init__(self)
        self.name = name
    def run(self) :
        honk()

def on_press(key) :
    keyP = "{0}".format(key)
    if(keyP == '\'h\'') :
        playsound("honk-sound.mp3")

def main() :
    with Listener(on_press) as listener :
        listener.join()
    honkThread = myThread("honk")
    honkThread.start()


if __name__ == "__main__" :
    main()
