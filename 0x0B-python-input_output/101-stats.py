#!/usr/bin/python3
import sys
from collections import defaultdict
"""Reads from standard input and computes metrics.

After every ten lines or the input of a keyboard interruption (CTRL + C),
prints the following statistics:
    - Total file size up to that point.
    - Count of read status codes up to that point.
"""


def print_stats(size, status_codes):
    """Print accumulated metrics.

    Args:
        size (int): The accumulated read file size.
        status_codes (dict): The accumulated count of status codes.
    """
    # Define the status codes to track
    status_codes = [200, 301, 400, 401, 403, 404, 405, 500]

    # Initialize variables to store metrics
    total_size = 0
    status_code_counts = defaultdict(int)
    line_count = 0

    try:
        for line in sys.stdin:
            # Split the input line into parts
            parts = line.strip().split()
            if len(parts) >= 8:
                status_code = int(parts[-2])
                file_size = int(parts[-1])

                # Update metrics
                total_size += file_size
                status_code_counts[status_code] += 1
                line_count += 1

                # Check if it's time to print the statistics
                if line_count % 10 == 0:
                    print("Total file size: File size:", total_size)
                    for code in sorted(status_codes):
                        if status_code_counts[code] > 0:
                            print(f"{code}: {status_code_counts[code]}")
    except KeyboardInterrupt:
        # Handle keyboard interruption (CTRL + C)
        print("Keyboard interruption detected. Printing current statistics:")
        print("Total file size: File size:", total_size)
        for code in sorted(status_codes):
            if status_code_counts[code] > 0:
                print(f"{code}: {status_code_counts[code]}")
