import sys

sys.stdin = open("input.txt", "rt")


def binary_search(search_list, find_data):
    if search_list[0] == find_data:
        return 0
    elif search_list[len(search_list)-1] == find_data:
        return len(search_list) - 1

    medium = len(search_list) // 2

    if search_list[medium] == find_data:
        return medium
    elif search_list[medium] > find_data:
        return binary_search(search_list[:medium], find_data)
    elif search_list[medium] < find_data:
        return binary_search(search_list[medium:], find_data) + medium


N, M = map(int, input().split())
search_list = list(map(int, input().split()))
search_list.sort()
answer = binary_search(search_list, M)
print(answer+1)
