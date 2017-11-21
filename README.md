# GUI IP Scanner
* only Windows support!

## Member
| Name | StudentID|
|------|----------|
|Akarachai Passavoranan|5810545505|
|Khanutchon Ammawong|810546609|
|Roiboon Chaiyachit|5810546005|

## How to use
```bash
    # Example
    main.py 255.255.192.0 10.2.0.0 10.2.0.1 20 1 4 csv_filename
```
Arguments
1. Subnet Mask
2. Default Gateway
3. Start IP
4. Limit
5. Retry
6. Max Thread
7. Output filename 

## Features
- [Done] Show all active device information IP, MAC Address and Manufacturer.
- [Done] Export results to CSV format.
- [Done] Multi-threading support.
- [Not Done] Notify when new MAC Address found in network or manually specify by user.
- [Not Done] Graphic User Interface.