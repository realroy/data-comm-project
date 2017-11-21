#!/usr/bin/python
from ip_scanner import IPScanner


def main():
    ### App configuration ###
    start = 90
    limit = 20
    subnet = '192.168.8.'
    retry = 1
    max_thread = 4
    #########################
    ip_scanner = IPScanner(
        start=start,
        limit=limit,
        subnet=subnet,
        retry=retry,
        max_thread=max_thread
    )
    result = ip_scanner.run()

if __name__ == "__main__":
    main()
