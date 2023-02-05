def merge_interval(arr1, arr2):
    return [min(arr1[0], arr2[0]), arr2[1]]


def non_overlapping_intervals(intervals):
    result = []

    i = 0
    while i < len(intervals) - 1:
        secondValueOfFirstInter = intervals[i][1]
        firstValueOfSecondInter = intervals[i + 1][0]
        if firstValueOfSecondInter <= secondValueOfFirstInter:
            result.append(merge_interval(intervals[i], intervals[i + 1]))
            i += 1
        else:
            result.append(intervals[i])

        i += 1

    if i == len(intervals) - 1:
        result.append(intervals[i])  # Edge case: handle last element

    return result


print(non_overlapping_intervals([[1, 3], [2, 6], [8, 10], [15, 18]]))  # [[1, 6], [8, 10], [15, 18]]
