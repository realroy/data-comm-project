#!/usr/bin/python
from ip_scanner import IPScanner


def main():
    ### App configuration ###
    start = 0
    limit = 20
    host_ip = '10.2.0.0'
    subnet_mask = '255.255.192.0'
    retry = 1
    max_thread = 4
    #########################
    ip_scanner = IPScanner(
        start=start,
        limit=limit,
        host_ip=host_ip,
        subnet_mask=subnet_mask,
        retry=retry,
        max_thread=max_thread
    )
    print("Start scaning from {0} to {1}".format(ip_scanner.hosts[0], ip_scanner.hosts[-1]))
    total_time, available_hosts = ip_scanner.run()
    print('Total time: ', total_time, ' sec.')
    for host in available_hosts: print(host['ip_addr'], host['mac_addr'])

if __name__ == "__main__":
    main()
