import random, time
from random_word import RandomWords

int_list = []
float_list = []
str_list = []

w = RandomWords()

for i in range(0, 5000):
    int_list.append(random.randint(0, 1000))
    float_list.append(random.uniform(0.1, 100.0))
    str_list.append(w.get_random_word())


def partitions (nums, low, hight):
    pivot = nums[(low + hight) // 2]
    i = low - 1
    j = hight + 1
    while True:
        i += 1
        while nums[i] < pivot:
            i += 1

        j -= 1
        while nums[j] > pivot:
            j -= 1

        if i >= j:
            return j

        nums[i], nums[j] = nums[j], nums[i]

def quick_sort(nums):
    def _quick_sort(items, low, high):
        if low < high:
            split_index = partitions(items, low, high)
            _quick_sort(items, low, split_index)
            _quick_sort(items, split_index + 1, high)
    _quick_sort(nums, 0, len(nums) - 1)

def average_quick_sort_time(arr, iterations):
    total_time = 0

    for _ in range(iterations):

        start_time = time.time()
        quick_sort(arr)
        end_time = time.time()

        total_time += end_time - start_time

    average_time = total_time / iterations

    return average_time


iterations = 10

average_time = average_quick_sort_time(int_list, iterations)
print(f"Среднее время работы быстрой сортировки int_list: {average_time} секунд")
average_time = average_quick_sort_time(float_list, iterations)
print(f"Среднее время работы быстрой сортировки float_list: {average_time} секунд")
average_time = average_quick_sort_time(str_list, iterations)
print(f"Среднее время работы быстрой сортировки str_list: {average_time} секунд")