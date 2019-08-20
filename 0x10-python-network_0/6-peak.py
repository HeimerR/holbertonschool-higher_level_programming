#!/usr/bin/python3
""" finds a peak in a list of unsorted integers. """


def find_peak2(numbers, size, start, end):
    middle = int(start + (end - start) / 2)

    # Compare middle element with its
    # neighbours (if neighbours exist)
    if ((middle == 0 or numbers[middle - 1] <= numbers[middle]) and
       (middle == size - 1 or numbers[middle + 1] <= numbers[middle])):
        return numbers[middle]

    # If middle element is not peak and
    # its left neighbour is greater
    # than it, then left half must
    # have a peak element
    elif (middle > 0 and numbers[middle - 1] > numbers[middle]):
        return find_peak2(numbers, size, start, (middle - 1))

    # If middle element is not peak and
    # its right neighbour is greater
    # than it, then right half must
    # have a peak element
    else:
        return find_peak2(numbers, size, middle + 1, end)


def find_peak(list_of_integers):
    if len(list_of_integers) == 0:
        return None
    if len(list_of_integers) == 1:
        return list_of_integers[0]
    if len(list_of_integers) == 2:
        return (list_of_integers[0] if list_of_integers[0] >
                list_of_integers[1] else list_of_integers[1])
    return (find_peak2(list_of_integers, len(list_of_integers), 0,
            len(list_of_integers) - 1))
