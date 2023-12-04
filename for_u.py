# 1
isEven = lambda x: x % 2 == 0  # на мой взгляд, основное преимущество лямбда-функций - это краткость кода
# 2
# 3

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]
        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Так же есть быстрая сортировка, однако с отсортированным массивом, она работает не эффективно, а сортировка слиянием работает стабильней за log(n)n
