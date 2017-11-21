#!/usr/bin/python
import os, threading, time
from queue import Queue
from ipaddress import ip_network

from ping_thread import PingThread


class IPScanner:
    def __init__(self, start, limit, host_ip, subnet_mask, retry, max_thread):
        self.subnet_mask = self.figure_out_subnet_mask(subnet_mask)
        self.retry = retry
        self.max_thread = max_thread
        self.hosts = list(ip_network('{0}{1}'.format(host_ip, self.subnet_mask)).hosts())[start: start + limit]


    def run(self):
        start_time = time.time()
        work_queue = Queue()
        available_hosts = list()
        total_task = len(self.hosts)

        # Create queue of IP that want to ping
        # for i in range(self.start, self.start + self.limit): work_queue.put('{0}{1}'.format(self.subnet, i))
        for host in self.hosts: work_queue.put(host)

        # Create list of thread by number of max thread
        threads = [PingThread(self.retry, work_queue, available_hosts, total_task) for thread in range(self.max_thread)]

        # Starting all threads
        for t in threads: t.start()

        # Wait for every threads
        for t in threads: t.join()

        total_time = time.time() - start_time

        return total_time, available_hosts

    def figure_out_subnet_mask(self, subnet_mask):
        if (subnet_mask[0] == '/'): return subnet_mask
        count_one = 0
        for i in subnet_mask.split('.'):
            if (i == '255'):
                count_one += 8
            else:
                count_one += format(int(i), 'b').count('1')
                break

        return '/{0}'.format(count_one)
