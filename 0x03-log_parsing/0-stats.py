#!/usr/bin/python3
"""
Script that reads stdin line by line and computes metrics
"""

import sys

if __name__ == '__main__':

    filesize, count = 0, 0
    codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
    stats = {key: 0 for key in codes}

    def print_stat(stats: dict, file_size: int) -> None:
        print("File size: {:d}".format(filesize))
        for key, val in sorted(stats.items()):
            if val:
                print("{}: {}".format(key, val))

    try:
        for line in sys.stdin:
            count += 1
            data = line.split()
            try:
                status_code = data[-2]
                if status_code in stats:
                    stats[status_code] += 1
            except BaseException:
                pass
            try:
                filesize += int(data[-1])
            except BaseException:
                pass
            if count % 10 == 0:
                print_stat(stats, filesize)
        print_stat(stats, filesize)
    except KeyboardInterrupt:
        print_stat(stats, filesize)
        raise
