import threading

class PrintThread(threading.Thread):
    def run(self):
        for i in range(1,26):
            print(f'PrintThread : {i}')


print(threading.current_thread())
t = PrintThread()
t.start()

for i in range(1, 26):
    print(f'MainThread : {i}')
