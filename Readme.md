# Simple TCP Port Scanner

A minimal Python script that checks which TCP ports in the range **1–1023** (the "well-known" ports) are open on a target host, using only the standard library.

## Features

- Scans ports 1 to 1023
- Uses plain TCP connect scanning (`connect_ex`)
- No external dependencies
- Short and easy to read, good for learning how sockets work

## Requirements

- Python 3.6 or newer (f-strings are used)
- No third-party packages

## Usage

1. Save the script as `port_scanner.py`.
2. Run it:

   ```bash
   python port_scanner.py
   ```

3. When prompted, enter the IP address or hostname of the target:

   ```
   Enter target: 127.0.0.1
   ```

### Example output

```
Enter target: 127.0.0.1
Port 22: Got connected !
Port 80: Got connected !
```

Only open ports are printed. If nothing is printed, no port in the range accepted a connection.

## How it works

For each port from 1 to 1023, the script:

1. Creates a TCP socket (`AF_INET`, `SOCK_STREAM`)
2. Sets a 5-second timeout
3. Calls `connect_ex((target_ip, port))`, which returns `0` if the connection succeeds
4. Prints the port if it is open
5. Closes the socket

## Code

```python
import socket

target_ip = input("Enter target: ")

for port in range(1, 1024):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(5)

    result = s.connect_ex((target_ip, port))

    if result == 0:
        print(f"Port {port}: Got connected !")

    s.close()
```

## Limitations

- **Sequential scanning:** ports are checked one at a time. With a 5-second timeout, scanning a host that drops packets can take a very long time. Lower the timeout (e.g. `0.5`) or use threading for speed.
- **TCP only:** UDP ports are not scanned.
- **No service detection:** the script reports open ports but not what is running on them.
- **Limited range:** only ports 1–1023 are checked. Change `range(1, 1024)` to scan more.
- **Firewalls/IDS:** firewalls may block or log connection attempts.

## Possible improvements

- Accept a port range as input or command-line arguments (`argparse`)
- Add multithreading for faster scans
- Resolve hostnames and handle invalid input
- Grab service banners
- Save results to a file

## Legal & ethical notice

Only scan systems that you **own** or have **explicit written permission** to test. Unauthorized port scanning may be illegal in your jurisdiction and may violate network or service provider policies. This project is intended for **educational purposes** and authorized network administration only. The author takes no responsibility for misuse.

## License

Released under the MIT License. Feel free to use, modify, and share.
