import random
import time

def choose_pivot(left, right):
    """
    Function to choose pivot point
    :param left: Left index of sub-list
    :param right: right-index of sub-list
    """

    # Pick 3 random numbers within the range of the list
    i1 = left + random.randint(0, right - left)
    i2 = left + random.randint(0, right - left)
    i3 = left + random.randint(0, right - left)

    # Return their median
    return max(min(i1, i2), min(max(i1, i2), i3))


def partition(data, left, right, drawData, timeTick, ):
    """
    Partition the list on the basis of pivot
    :param left: Left index of sub-list
    :param right: right-index of sub-list
    """

    pivot_index = choose_pivot(left, right)  # Index of pivot



    data[right], data[pivot_index] = data[pivot_index], data[right]  # put the pivot at the end

    pivot = data[right]  # Pivot
    i = left - 1  # All the elements less than or equal to the
    # pivot go before or at i
    drawData(data, colorArray(len(data), left, right, pivot, pivot))
    time.sleep(timeTick)

    for j in range(left, right):
        if data[j] <= pivot:
            i += 1  # increment the index
            drawData(data, colorArray(len(data), left, right, pivot, j, True))
            time.sleep(timeTick)
            data[i], data[j] = data[j], data[i]
        drawData(data, colorArray(len(data), left, right, pivot, j))
        time.sleep(timeTick)
    drawData(data, colorArray(len(data), left, right, pivot, right, True))
    time.sleep(timeTick)
    data[i + 1], data[right] = data[right], data[i + 1]  # Putting the pivot back in place
    return i + 1


def quick_sort(data, left, right, drawData, timeTick):
    """
    Quick sort function
    :param data: data of unsorted integers
    :param left: Left index of sub-list
    :param right: right-index of sub-list
    """

    if left < right:
        # pi is where the pivot is at
        pi = partition(data, left, right, drawData, timeTick)

        # Separately sort elements before and after partition
        quick_sort(data, left, pi - 1, drawData, timeTick)
        quick_sort(data, pi + 1, right, drawData, timeTick)


def colorArray(dataLen, left, right, border, currIdx, is_swapping=False):
    colorArray = []
    for i in range(dataLen):

        if i >= left and i <= right:
            colorArray.append("magenta")
        else:
            colorArray.append("DarkSlateGray2")

        if i == right:
            colorArray[i] = "orange"
        elif i == border:
            colorArray[i] = "OliveDrab4"
        elif i == currIdx:
            colorArray[i] = "yellow"

        if is_swapping:
            if i == border or i == currIdx:
                colorArray[i] = "blue"

    return colorArray