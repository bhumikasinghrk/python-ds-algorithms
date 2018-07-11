#Find the number of elements that would need to be added so that each array value is separated by one.
#[1,2,3,5] -> 1 #4 needs to be added to the array
def makeArrayConsecutive(statues):
    length = len(statues)
    statuesNeeded = 0

    if length <= 1:
        return statuesNeeded

    sortedStatues = sorted(statues)
    print(sortedStatues)

    for i in range(1, length):
        statuesNeeded += (sortedStatues[i] - sortedStatues[i - 1]) - 1

    return statuesNeeded

def test_makeArrayConsecutive():
    a = [6, 2, 3, 8]
    assert makeArrayConsecutive(a) == 3

# Test
print(makeArrayConsecutive([6, 2, 3, 8]))