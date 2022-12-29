# T: O(n)
def insert(intervals, newInterval):
    res = []

    for i in range(len(intervals)):
        if newInterval[1] < intervals[i][0]:
            res.append(newInterval)
            return res + intervals[i::]
        elif newInterval[0] > intervals[i][1]:
            res.append(newInterval)
        else:
            newInterval = [min(newInterval[0], intervals[i][0]),
                           max(newInterval[1], intervals[i][1])]

    res.append(newInterval)

    return res


print(insert([[1, 3], [6, 9]], [2, 5]))  # Output: [[1, 5], [6, 9]]
