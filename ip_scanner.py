import csv, time
from queue import Queue
from ipaddress import IPv4Address, ip_network

from ping_thread import PingThread


class IPScanner:
    def __init__(self):
        self.start_ip = IPv4Address('0.0.0.0')
        self.limit = 0
        self.work_queue = Queue()
        self.available_hosts = list()
        self.subnet_mask = '/24'
        self.hosts = []
        self.total_task = 0
        self.retry = 1
        self.max_thread = 1
        self.default_gateway = IPv4Address('0.0.0.0')

    def config(self, subnet_mask, default_gateway, start_ip, limit, retry, max_thread):
        self.start_ip = IPv4Address(start_ip)
        self.subnet_mask = self.figure_out_subnet_mask(subnet_mask)
        self.default_gateway = IPv4Address(default_gateway)
        start_index = (int(self.start_ip) - 1) - int(self.default_gateway)
        last_index = start_index + limit
        all_hosts = ip_network('{0}{1}'.format(self.default_gateway, self.subnet_mask)).hosts()
        self.hosts = list(all_hosts)[start_index: last_index]
        self.total_task = len(self.hosts)
        self.retry = retry
        self.max_thread = max_thread


    def run(self):
        start_time = time.time()

        # Create queue of IP that want to ping
        for host in self.hosts: self.work_queue.put(host)

        # Create list of thread by number of max thread
        threads = [PingThread(self.retry, self.work_queue, self.available_hosts, self.total_task) for thread in
                   range(self.max_thread)]

        # Starting all threads
        for t in threads: t.start()

        # Wait for every threads
        for t in threads: t.join()

        total_time = time.time() - start_time

        return total_time, self.available_hosts

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

    def save_to_csv(self, destination, name):
        with open('{0}.csv'.format(name), 'w', newline='') as csv_file:
            writer = csv.writer(csv_file, delimiter=',')
            writer.writerow(['IP', 'MAC Address', 'Manufacturer'])
            for host in self.available_hosts:
                writer.writerow([host['ip_addr'], host['mac_addr'], host['manufacturer']])
