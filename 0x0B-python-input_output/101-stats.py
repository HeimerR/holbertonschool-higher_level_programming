#!/usr/bin/python3
"""check stdin"""
import sys


total_size = 0
status = ['200', '301', '400', '401', '403', '404', '405', '500']
times_status = [0, 0, 0, 0, 0, 0, 0, 0]
counter = 0
try:
    for line in sys.stdin:
        line_list = line.split(" ")
        if len(line_list) > 2:
            size = line_list[-1]
            code = line_list[-2]
            if code in status:
                i = status.index(code)
                times_status[i] += 1
            total_size += int(size)
            counter += 1
        if counter == 10:
            print("File size: {:d}".format(total_size))
            for i in range(8):
                if times_status[i] != 0:
                    print("{:}: {:d}".format(status[i], times_status[i]))
            counter = 0
except Exception:
    pass
finally:
    print("File size: {:d}".format(total_size))
    for i in range(8):
        if times_status[i] != 0:
            print("{:}: {:d}".format(status[i], times_status[i]))
