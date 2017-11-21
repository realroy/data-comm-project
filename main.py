#!/usr/bin/python
import sys
from ip_scanner import IPScanner


def main():
    ### App configuration ###
    start_ip = '10.2.0.1'
    limit = 20
    default_gateway = '10.2.0.0'
    subnet_mask = '255.255.192.0'
    retry = 1
    max_thread = 4
    #########################
    ip_scanner = IPScanner()
    ip_scanner.config(
        subnet_mask=str(sys.argv[1]),
        default_gateway=str(sys.argv[2]),
        start_ip=str(sys.argv[3]),
        limit=int(sys.argv[4]),
        retry=int(sys.argv[5]),
        max_thread=int(sys.argv[6])
    )
    total_time, available_hosts = ip_scanner.run()
    print("Start scanning from {0} to {1}".format(ip_scanner.hosts[0], ip_scanner.hosts[-1]))
    print('Total time: ', total_time, ' sec.')
    for host in available_hosts: print(host)
    ip_scanner.save_to_csv('', sys.argv[7])

if __name__ == "__main__":
    main()
