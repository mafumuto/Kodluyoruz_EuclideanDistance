# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from EuclideanDistance import EuclideanDistance
from TrialTree import TrialTree


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

    points = [(3, 4), (6, 8), (7, 24), (8, 6), (10, 10)]
    print("Points List: ", points)

    euclid = EuclideanDistance()

    distances = euclid.EuclideanDistanceInList(euclid, points)

    print("Distance list: ", distances)

    trialTree = TrialTree(distances[0])

    index = 0
    for item in distances:
        if index != 0:
            trialTree.Add(item)
        index += 1

    minDistance = trialTree.FindMinValue()

    # euclid.FindEuclideanDistance(points[0], points[1])

    print("Minimum Distance: ", minDistance)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
