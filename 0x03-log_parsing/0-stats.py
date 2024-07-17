#!/usr/bin/python3
""" Log Parsing
"""
import sys
import signal

# Initialize variables
total_size = 0
status_codes_count = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}
line_count = 0


def print_stats():
    """ Print the current statistics """
    print(f"File size: {total_size}")
    for code in sorted(status_codes_count.keys()):
        if status_codes_count[code] > 0:
            print(f"{code}: {status_codes_count[code]}")

def signal_handler(sig, frame):
    """ Signal handler for keyboard interruption (CTRL + C) """
    print_stats()
    sys.exit(0)

# Register the signal handler
signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        line_count += 1

        parts = line.split()
        if len(parts) < 7:
            continue

        ip, _, _, date, method, path, protocol, status_code, file_size = parts[0], parts[1], parts[2], parts[3], parts[4], parts[5], parts[6], parts[8], parts[9]

        if method != '"GET' or path != '/projects/260' or protocol != 'HTTP/1.1"':
            continue

        # Update total file size
        try:
            total_size += int(file_size)
        except ValueError:
            continue

        # Update status code count
        if status_code in status_codes_count:
            status_codes_count[status_code] += 1

        # Print stats after every 10 lines
        if line_count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    print_stats()
    sys.exit(0)

# Print final stats if the script finishes normally
print_stats()

