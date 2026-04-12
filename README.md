
# Sorting_Assignment
Sorting Assignment in Data Structures course in BGU
Noam Dahan
Tomer Amran
The selected algorithms: Insertion_Sort, Merge_Sort, Quick_Sort (3,4,5)
<img width="993" height="667" alt="Result2" src="https://github.com/user-attachments/assets/0dacf325-a797-444a-b7ea-d82f1a15fae4" />
<img width="991" height="668" alt="Result1" src="https://github.com/user-attachments/assets/639b7f49-1ce5-490a-a13e-94c5ee5cb88d" />

Insertion Sort: The biggest change observed is the sharp decline in Insertion Sort's runtime. While it was the slowest algorithm in the random experiment, it became much faster in this scenario. Insertion Sort is an adaptive algorithm. Its inner loop only executes when an element is out of order. Since most elements are already near their final positions, the algorithm performs very few swaps and comparisons, pushing its time complexity toward its best-case scenario.

Quick Sort: remained efficient, but depending on the pivot selection strategy (in this case, using the last element), its performance can slightly degrade on nearly sorted data. When the array is nearly sorted and the pivot is chosen poorly (e.g., the last element), the partitions become unbalanced. Instead of splitting the array into two equal halves, the partitions often result in a size of 1 and n-1. This increases the recursion depth and pushes the complexity closer to its worst-case of O(n^2), though it still remains relatively fast due to low constant overhead.

Merge Sort: Consistent Performance, without any major changes. The runtimes for Merge Sort remained almost identical to those in the first experiment, showing a very stable and predictable curve. Merge Sort is a non-adaptive algorithm. It follows a rigid "Divide and Conquer" structure, recursively splitting and merging the array regardless of the initial order of elements. Thus, it always performs O(nlog n) operations, making it highly consistent but unable to capitalize on pre-existing order.
