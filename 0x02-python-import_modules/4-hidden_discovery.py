#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    list = dir(hidden_4)
    for i in range(len(list)):
        if(list[i][0] != '_' and list[i][1] != '_'):
            print('{}'.format(list[i]))
