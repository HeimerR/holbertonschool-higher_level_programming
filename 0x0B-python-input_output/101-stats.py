#!/usr/bin/python3
import sys


#if __name__ == "__main__":
total_size = 0
status = ['200', '301', '400', '401', '403', '404', '405', '500']
times_status = [0, 0, 0, 0, 0, 0, 0, 0]
counter = 0
try:
    for line in sys.stdin: 
        line_list = line.split(" ")
        size = line_list[-1]
        code = line_list[-2]
        total_size += int(size)
        i = status.index(code)
        times_status[i] += 1
        counter += 1
        if counter == 10:
            print("File size: {:d}".format(total_size))
            for i in range(8):
                if times_status[i] != 0:
                    print("{:}: {:d}".format(status[i], times_status[i]))
            counter = 0
except KeyboardInterrupt:
    print("File size: {:d}".format(total_size))
    for i in range(8):
        if times_status[i] != 0:
            print("{:}: {:d}".format(status[i], times_status[i]))

