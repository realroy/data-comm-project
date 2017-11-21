#!/usr/bin/python
import os, threading, time
from queue import Queue

from ping_thread import PingThread


class IPScanner:
    def __init__(self, start, limit, subnet, retry, max_thread):
        self.start = start
        self.limit = limit
        self.subnet = subnet
        self.retry = retry
        self.max_thread = max_thread

    def run(self):
        start_time = time.time()
        work_queue = Queue()
        result_queue = Queue()

        # Create queue of IP that want to ping
        for i in range(self.start, self.start + self.limit): work_queue.put('{0}{1}'.format(self.subnet, i))

        # Create list of thread by number of max thread
        threads = [PingThread(self.retry, work_queue, result_queue) for i in range(self.max_thread)]

        # Starting all threads
        for t in threads: t.start()

        # Wait for every threads
        for t in threads: t.join()

        total_time = time.time() - start_time
        display_result(total_time, result_queue)
        return { total_time: total_time, result_queue: result_queue }


def display_result(total_time, available_hosts):
    print('Done in', total_time, ' sec')
    if (available_hosts.qsize() == 0): return print('There\'s no available hosts.')
    print('Available Hosts')
    print('--------------')
    while available_hosts.qsize() != 0: print(available_hosts.get())
    print('--------------')
