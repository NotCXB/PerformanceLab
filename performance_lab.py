# 🔍 Problem 1: Find Most Frequent Element
# Given a list of integers, return the value that appears most frequently.
# If there's a tie, return any of the most frequent.
#
# Example:
# Input: [1, 3, 2, 3, 4, 1, 3]
# Output: 3

def most_frequent(numbers):
    if not numbers:
        raise ValueError("numbers must not be empty")

    counts = {}
    for item in numbers:
        counts[item] = counts.get(item, 0) + 1
    return max(counts, key=counts.get)

"""
Time and Space Analysis for problem 1:
- Best-case: O(n), since every input element must be counted.
- Worst-case: O(n^2) with pathological dictionary hash collisions;
  O(n) under the usual constant-time dictionary operation assumption.
- Average-case: O(n).
- Space complexity: O(k), where k is the number of distinct values.
- Why this approach? A dictionary counts each value in one pass, and
  max() finds the value with the largest count. Ties return the first seen.
- Could it be optimized? Tracking the most frequent value while counting
  avoids the final O(k) scan, but average time remains O(n).
"""


# 🔍 Problem 2: Remove Duplicates While Preserving Order
# Write a function that returns a list with duplicates removed but preserves order.
#
# Example:
# Input: [4, 5, 4, 6, 5, 7]
# Output: [4, 5, 6, 7]

def remove_duplicates(nums):
    if not nums:
        raise ValueError("numbers must not be empty")
    seen = set()
    result = []
    for item in nums:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

"""
Time and Space Analysis for problem 2:
- Best-case: O(n), since every element is checked.
- Worst-case: O(n^2) with pathological hash collisions; otherwise O(n).
- Average-case: O(n), assuming constant-time set operations.
- Space complexity: O(k), where k is the number of distinct values.
- Why this approach? A set makes membership checks fast, and the result
  list keeps first occurrences in their original order.
- Could it be optimized? list(dict.fromkeys(nums)) is shorter but has
  the same average time and space complexity.
"""


# 🔍 Problem 3: Return All Pairs That Sum to Target
# Write a function that returns all unique pairs of numbers in the list that sum to a target.
# Order of output does not matter. Assume input list has no duplicates.
#
# Example:
# Input: ([1, 2, 3, 4], target=5)
# Output: [(1, 4), (2, 3)]

def find_pairs(nums, target):
    if not nums:
        raise ValueError("numbers must not be empty")
    seen = set()
    # Optimization: unique inputs mean each matching pair is found only once.
    # Append directly to a list to avoid hashing result tuples and converting
    # a result set to a list. Both versions average O(n) time and use O(n)
    # space, but this version removes the extra result set and conversion.
    pairs = []
    for num in nums:
        complement = target - num
        if complement in seen:
            pairs.append((min(num, complement), max(num, complement)))
        seen.add(num)
    return pairs

"""
Time and Space Analysis for problem 3:
- Best-case: O(n), since every number is checked.
- Worst-case: O(n^2) with pathological hash collisions; otherwise O(n).
- Average-case: O(n), assuming constant-time set operations.
- Space complexity: O(n) for seen numbers and matching pairs.
- Why this approach? Checking each complement in a set avoids comparing
  every possible pair. With unique inputs, each pair is found only when
  its second member is encountered, so a result set is unnecessary.
- Could it be optimized? This refactor stores matching pairs directly in
  the returned list. It relies on the prompt's no-duplicate-input rule.
"""

# Refactor comparison (n input numbers, p matching pairs):
# Original: average O(n + p) time; hashes each pair and copies p references
# from the result set into a new list. Space is O(n + p), with both the
# result set and returned list present during conversion.
# Refactored: average O(n + p) time; appends pairs directly to the returned
# list, avoiding tuple hashing and the final O(p) conversion. Space remains
# O(n + p), but avoids result-set overhead and duplicate reference storage.
# Since p <= n / 2 for unique inputs, both simplify to O(n) time and space.


# 🔍 Problem 4: Simulate List Resizing (Amortized Cost)
# Create a function that adds n elements to a list that has a fixed initial capacity.
# When the list reaches capacity, simulate doubling its size by creating a new list
# and copying all values over (simulate this with print statements).
#
# Example:
# add_n_items(6) → should print when resizing happens.

def add_n_items(n):
    if n < 0:
        raise ValueError("n must be non-negative")

    capacity = 2
    items = [None] * capacity
    size = 0
    for value in range(n):
        if size == capacity:
            new_capacity = capacity * 2
            print(f"Resizing from {capacity} to {new_capacity}; copying {size} items")
            new_items = [None] * new_capacity
            for index in range(size):
                new_items[index] = items[index]
            items = new_items
            capacity = new_capacity
        items[size] = value
        size += 1
    return items[:size]

"""
Time and Space Analysis for problem 4:
- When do resizes happen? Before inserting into a full list at sizes
  2, 4, 8, 16, and so on. Initial capacity is 2.
- What is the worst-case for a single append? O(k) to resize and copy
  k existing items. An insertion without resizing costs O(1).
- What is the amortized time per append overall? O(1), with O(n) total
  insertion time. Returning the final slice also takes O(n).
- Space complexity: O(n), including temporary storage during resizing.
- Why does doubling reduce the cost overall? The copied item counts
  form a geometric series (2 + 4 + 8 + ...), totaling less than 2n.
  Spreading this O(n) cost over n insertions gives O(1) amortized cost.
"""


# 🔍 Problem 5: Compute Running Totals
# Write a function that takes a list of numbers and returns a new list
# where each element is the sum of all elements up to that index.
#
# Example:
# Input: [1, 2, 3, 4]
# Output: [1, 3, 6, 10]
# Because: [1, 1+2, 1+2+3, 1+2+3+4]

def running_total(nums):
    total = 0
    result = []
    for num in nums:
        total += num
        result.append(total)
    return result

# Testing

print (most_frequent([1, 3, 2, 3, 4, 1, 3]))  # Output: 3
print (remove_duplicates([4, 5, 4, 6, 5, 7]))  # Output: [4, 5, 6, 7]
print (find_pairs([1, 2, 3, 4], 5))            # Output: [(1, 4), (2, 3)]
print (add_n_items(6))                          # Resizes at sizes 2 and 4
print (running_total([1, 2, 3, 4]))            # Output: [1, 3, 6, 10]

"""
Time and Space Analysis for problem 5:
- Best-case: O(n).
- Worst-case: O(n).
- Average-case: O(n), assuming constant-time numeric addition.
- Space complexity: O(n) for the result and O(1) auxiliary space.
- Why this approach? Keeping a running sum processes each number once,
  avoiding O(n^2) work from repeatedly summing earlier elements.
- Could it be optimized? O(n) time is optimal because all inputs must
  be read. A generator could use O(1) auxiliary space if a returned list
  were not required.
"""
