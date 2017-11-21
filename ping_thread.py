from threading import Thread
from os import system
from subprocess import check_output

NOT_FOUND = b'No ARP Entries Found.\r\n'


class PingThread(Thread):
    def __init__(self, retry, work_queue, available_hosts, total_task):
        Thread.__init__(self)
        self.work_queue = work_queue
        self.retry = retry
        self.available_host = available_hosts
        self.total_task = total_task

    def run(self):
        while self.work_queue.qsize() != 0:
            progress = (self.total_task - self.work_queue.qsize()) + 1
            print('Progress => {0}/{1}'.format(progress, self.total_task))
            addr = self.work_queue.get()
            system('ping -n {0} {1}'.format(self.retry, addr))
            call_arp = 'arp -a {0}'.format(addr)
            output = check_output(call_arp)
            if (output != NOT_FOUND):
                result = []
                info = output.decode('utf-8').splitlines()[3].split(" ")
                for each in info:
                    if (len(each) > 0): result.append(each)
                self.available_host.append({'ip_addr': result[0], 'mac_addr': result[1]})
