import math

def linear_search(numbers, target, offset=0):
    comparisons = 0
    for i, num in enumerate(numbers):
        comparisons += 1
        if num == target:
            return i + offset, comparisons
    return -1, comparisons

def binary_search(numbers, target):
    comparisons = 0
    low, high = 0, len(numbers) - 1

    while low <= high:
        comparisons += 1
        mid = (low + high) // 2
        mid_element = numbers[mid]

        if mid_element == target:
            return mid, comparisons
        elif mid_element < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1, comparisons

def jump_search(numbers, target):
    n = len(numbers)
    m = int(math.sqrt(n))
    i = 0
    comparisons = 0

    while i < n and numbers[min(i + m, n) - 1] < target:
        comparisons += 1
        i += m
        if i >= n:
            return -1, comparisons
        
    current_block = numbers[i : min(i +m, n)]

    result_index, linear_comps = linear_search(current_block, target, offset=i)

    comparisons += linear_comps
    return result_index, comparisons

def interpolation_search(numbers, target):
    comparisons = 0
    low = 0
    high = len(numbers) - 1

    while low <= high and target >= numbers[low] and target <= numbers[high]:
        comparisons += 1
        # Avoid division by zero if all numbers in range are the same
        if numbers[high] == numbers[low]:
            if numbers[low] == target: return low, comparisons
            break

        pos = low + int(((float(high - low) / (numbers[high] - numbers[low])) * (target - numbers[low])))

        if numbers[pos] == target:
            return pos, comparisons
        if numbers[pos] < target:
            low = pos + 1
        else:
            high = pos - 1

    return -1, comparisons

def main():
    print("Enter a list of a minimum of 20 numbers, or more, and they should be in ascending or descending order. However, they do not need to be sequential.")
    user_input = input("> ")

    numbers = sorted([int(x) for x in user_input.split()])

    if len(numbers) < 20:
        print(f"You only entered {len(numbers)} numbers. Requires 20+.")

    target = int(input("Enter the target number to search for: "))

    lin_idx, lin_comp = linear_search(numbers, target)
    bin_idx, bin_comp = binary_search(numbers, target)
    jmp_idx, jmp_comp = jump_search(numbers, target)
    int_idx, int_comp = interpolation_search(numbers, target)

    # Display results in a formatted table
    print(f"{'Search Type':<25} | {'Index':<8} | {'Comparisons'}")
    print("-" * 55)
    print(f"{'Linear Search':<25} | {str(lin_idx):<8} | {lin_comp}")
    print(f"{'Binary Search':<25} | {str(bin_idx):<8} | {bin_comp}")
    print(f"{'Jump Search':<25} | {str(jmp_idx):<8} | {jmp_comp}")
    print(f"{'Interpolation Search':<25} | {str(int_idx):<8} | {int_comp}")

    print("\n-1 Index indicates the target was not found in the list.")

if __name__ == "__main__":
    main()