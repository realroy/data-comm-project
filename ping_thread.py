import threading, os


class PingThread(threading.Thread):
    def __init__(self, retry, work_queue, result_queue):
        threading.Thread.__init__(self)
        self.work_queue = work_queue
        self.retry = retry
        self.result_queue = result_queue

    def run(self):
        while True:
            if (self.work_queue.qsize() != 0):
                addr = self.work_queue.get()
                flag = os.system('ping -c {0} {1}'.format(self.retry, addr))
                if (flag == 0): self.result_queue.put(addr)
            else:
                break
