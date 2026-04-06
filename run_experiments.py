# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random
import time
import matplotlib.pyplot as plt


def give_arr(size):
    arr = [random.randint(0, size) for _ in range(size)]
    return arr


def merge(arr, start, mid, end):
    L = arr[start: mid + 1]
    R = arr[mid + 1: end + 1]
    i, j = 0, 0
    k = start
    while (i < len(L)) and (j < len(R)):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1
    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1


def merge_sort(arr, start, end):
    if start < end:
        mid = (start + end) // 2
        merge_sort(arr, start, mid)
        merge_sort(arr, mid + 1, end)
        merge(arr, start, mid, end)

# quick sort
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)


def insertion_sort(arr, size):
    for i in range(1, size):
        key = arr[i]
        j = i-1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j = j-1
        arr[j+1] = key


def run_benchmark():
    # sizes of Arrays we will check
    sizes = [100, 500, 1000, 5000, 25000, 125000, 600000, 1000000]
    iterations = 5
    merge_avg_times = []
    quick_avg_times = []
    insertion_avg_times = []

    for size in sizes:
        m_times, q_times, i_times = [], [], []

        for _ in range(iterations):
            original_list = [random.randint(0, size) for _ in range(size)]

            # Merge Sort
            list_m = original_list.copy()
            s = time.perf_counter()
            merge_sort(list_m, 0, len(list_m) - 1)
            m_times.append(time.perf_counter() - s)

            # Quick Sort
            list_q = original_list.copy()
            s = time.perf_counter()
            quick_sort(list_q, 0, len(list_q) - 1)
            q_times.append(time.perf_counter() - s)

            # Insertion Sort
            if size <= 125000:
                list_i = original_list.copy()
                s = time.perf_counter()
                insertion_sort(list_i, len(list_i) - 1)
                i_times.append(time.perf_counter() - s)

        merge_avg_times.append(sum(m_times) / iterations)
        quick_avg_times.append(sum(q_times) / iterations)
        if size <= 125000:
            insertion_avg_times.append(sum(i_times) / iterations)
        print(f"Size {size} - Merge: {merge_avg_times[-1]:.4f}s, Quick: {quick_avg_times[-1]:.4f}s,"
              f" Insertion: {insertion_avg_times[-1]:.4f}")

    # graph plot

    plt.figure(figsize=(10, 6))
    plt.plot(sizes, merge_avg_times, label="Merge Sort", marker='o', color='blue')
    plt.plot(sizes, quick_avg_times, label="Quick Sort", marker='s', color='red')
    plt.plot(sizes[:len(insertion_avg_times)], insertion_avg_times, label="Insertion Sort", marker='s', color='green')
    plt.title("Average Execution Time vs. Array Size", fontsize=14)
    plt.xlabel("Array Size (n)", fontsize=10)
    plt.ylabel("Average Time (seconds)", fontsize=10)
    plt.legend()
    plt.grid()

    plt.show()


if __name__ == "__main__":
    run_benchmark()

