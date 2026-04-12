import random
import time
import sys
import argparse
import statistics
import matplotlib.pyplot as plt

# הגבלת עומק הרקורסיה במערכים גדולים
sys.setrecursionlimit(2000000)


def insertion_sort(arr):
    size = len(arr)
    for i in range(1, size):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def merge_sort(arr, start, end):
    if start < end:
        mid = (start + end) // 2
        merge_sort(arr, start, mid)
        merge_sort(arr, mid + 1, end)
        merge(arr, start, mid, end)


def merge(arr, start, mid, end):
    L = arr[start: mid + 1]
    R = arr[mid + 1: end + 1]
    i = j = 0
    k = start
    while i < len(L) and j < len(R):
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


# --- פונקציות עזר לניסויים ---

def generate_array(size, exp_type):
    if exp_type == 0:  # Random
        return [random.randint(0, size * 10) for _ in range(size)]

    # Nearly Sorted (חלק ג')
    arr = sorted([random.randint(0, size * 10) for _ in range(size)])
    noise_percent = 5 if exp_type == 1 else 20
    num_swaps = int(size * (noise_percent / 100))
    for _ in range(num_swaps):
        idx1 = random.randint(0, size - 1)
        idx2 = random.randint(0, size - 1)
        arr[idx1], arr[idx2] = arr[idx2], arr[idx1]
    return arr


def run_experiments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--algorithms", nargs='+', type=int,
                        help="3-Insertion, 4-Merge, 5-Quick")
    parser.add_argument("-s", "--sizes", nargs='+', type=int, help="Array sizes")
    parser.add_argument("-e", "--exp_type", type=int, default=1, help="0-Random, 1-5%% Noise, 2-20%% Noise")
    parser.add_argument("-r", "--repetitions", type=int, default=5, help="Number of repetitions")
    args = parser.parse_args()

    # מיפוי מספרים לפונקציות ושמות
    algo_map = {

        3: ("Insertion Sort", lambda a: insertion_sort(a)),
        4: ("Merge Sort", lambda a: merge_sort(a, 0, len(a) - 1)),
        5: ("Quick Sort", lambda a: quick_sort(a, 0, len(a) - 1))
    }


    experiment(args.algorithms, args.sizes, 0, args.repetitions, algo_map) # חלק B במטלה
    experiment(args.algorithms, args.sizes, args.exp_type, args.repetitions, algo_map) ##כאן יש בחירה בין 5% רעש ל20% רעש (חלק C במטלה)



def experiment(algorithms_to_run, sizes, exp_type, repetitions, algo_map):
    results = {algo_id: {"avg": [], "std": []} for algo_id in algorithms_to_run}

    for size in sizes:
        for algo_id in algorithms_to_run:
            times = []
            for _ in range(repetitions):
                arr = generate_array(size, exp_type)

                start_time = time.perf_counter()
                algo_map[algo_id][1](arr)
                times.append(time.perf_counter() - start_time)

            # חישוב ממוצע וסטיית תקן
            avg = sum(times) / repetitions
            std = statistics.stdev(times) if repetitions > 1 else 0

            results[algo_id]["avg"].append(avg)
            results[algo_id]["std"].append(std)

            print(f"Algo: {algo_map[algo_id][0]}, Size: {size}, Avg: {avg:.4f}s")
    plot_results(results, algorithms_to_run, sizes, exp_type, algo_map)


def plot_results(results, algorithms_to_run, sizes, exp_type, algo_map):
    plt.figure(figsize=(10, 6))

    for algo_id in algorithms_to_run:
        name = algo_map[algo_id][0]
        avgs = results[algo_id]["avg"]
        stds = results[algo_id]["std"]

        # ציור הקו המרכזי
        plt.plot(sizes, avgs, label=name, marker='o')

        # הוספת ההצללה של סטיית התקן
        plt.fill_between(
            sizes,
            [a - s for a, s in zip(avgs, stds)],
            [a + s for a, s in zip(avgs, stds)],
            alpha=0.2
        )
    if exp_type ==1:
        string = "Nearly Sorted,noise=5%"
    elif exp_type ==2:
        string = "Nearly Sorted,noise=20%"
    else:
        string = "Random"
    plt.title(f"Runtime Comparison("+string+")")
    plt.xlabel("Array Size (n)")
    plt.ylabel("Runtime (seconds)")
    plt.legend()
    plt.grid(True)

    # הצגת הגרפים

if __name__ == "__main__":
    run_experiments()
    plt.show()