

def check_size(histogram, pos):
    size = histogram[pos]
    total = 0

    while pos < len(histogram):
        if histogram[pos] >= size:
            total += size
        pos = pos + 1
    print(total)
    return total


def largest_histogram(histogram):
    largest = 0

    for x, y in enumerate(histogram):
        size = check_size(histogram, x)

        if largest < size:
            largest = size

    return largest
    


if __name__ == "__main__":
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert largest_histogram([2, 1, 4, 5, 1, 3, 3]) == 8, "complex"
    assert largest_histogram([5]) == 5, "one is always the biggest"
    assert largest_histogram([5, 3]) == 6, "two are smallest X 2"
    assert largest_histogram([1, 1, 4, 1]) == 4, "vertical"
    assert largest_histogram([1, 1, 3, 1]) == 4, "horizontal"
    
    print("Done! Go check it!")
