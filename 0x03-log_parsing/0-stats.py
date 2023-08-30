#!/usr/bin/env python3

import sys
import signal

# Initialize variables to store metrics
total_file_size = 0
status_code_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

def print_statistics():
    global total_file_size
    global status_code_counts

    print(f"File size: {total_file_size}")
    for code, count in sorted(status_code_counts.items()):
        if count > 0:
            print(f"{code}: {count}")
    print()

def signal_handler(sig, frame):
    print_statistics()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        parts = line.strip().split()
        if len(parts) != 9:  # Corrected to 9, which is the expected number of parts
            continue
        
        _, _, _, _, _, _, status_code, file_size = parts
        try:
            status_code = int(status_code)
            file_size = int(file_size)
        except ValueError:
            continue
        
        total_file_size += file_size
        if status_code in status_code_counts:
            status_code_counts[status_code] += 1
        line_count += 1
        
        if line_count % 10 == 0:
            print_statistics()

except KeyboardInterrupt:
    print_statistics()
    sys.exit(0)
