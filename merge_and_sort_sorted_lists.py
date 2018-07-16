# Task : Return a new sorted merged list from K sorted lists, each with size N.
# For example, if we had [[10, 15, 30], [12, 15, 20], [17, 20, 32]], the result should be [10, 12, 15, 15, 17, 20, 20, 30, 32].

import heapq


def merge_and_sort_sorted_lists(lists):
    result = []

    heap = [(lst[0], i, 0) for i, lst in enumerate(lists)]
    heapq.heapify(heap)

    while heap:
        smallest = heapq.heappop(heap)

        result.append(smallest[0])

        next_index = smallest[2] + 1
        if next_index < len(lists[smallest[1]]):
            next_tuple = (lists[smallest[1]][next_index], smallest[1],
                          next_index)
            heapq.heappush(heap, next_tuple)

    return result
