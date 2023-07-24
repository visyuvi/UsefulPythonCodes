def largestRange(arr):
    numbers = {x: 0 for x in arr}
    left = right = 0

    for number in arr:
        if numbers[number] == 0:

            left_count = number - 1
            right_count = number + 1
            while left_count in numbers: # O(1)
                numbers[left_count] = 1
                left_count -= 1
            left_count += 1

            while right_count in numbers:  # O(1)
                numbers[right_count] = 1
                right_count += 1
            right_count -= 1

            if (right - left) <= (right_count - left_count):
                right = right_count
                left = left_count

    return [left, right]


arr = [1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]
print(largestRange(arr))
