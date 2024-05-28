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

    euclid = EuclideanDistance()

    distances = euclid.EuclideanDistanceInList(euclid, points)

    print("Distance list: ", distances)

    Deneme = TrialTree(7.1)
    Deneme.Add(10.88888888)
    Deneme.Add(5.5555555555)
    Deneme.Add(4.4444444444)
    Deneme.Add(6.0)
    Deneme.Add(4.1555555555)
    Deneme.Add(6.4555555555)
    Deneme.Add(3.5444444444)
    Deneme.Add(4.2333333333)
    Deneme.Add(2.4444444444)
    Deneme.Add(2.8888888888)
    Deneme.Add(3.8888888888)
    Deneme.Add(4.8888888888)
    Deneme.Add(5.8888888888)
    Deneme.Add(6.8888888888)
    Deneme.Add(7.8888888888)
    Deneme.Add(9.8888888888)
    Deneme.Add(10.8888888888)
    Deneme.Add(11.8888888888)
    Deneme.Add(0.8888888888)
    Deneme.Add(12.8888888888)
    Deneme.Add(0.68888888888)
    Deneme.Add(14.8888888888)
    Deneme.Add(1.48888888888)
    Deneme.Add(0.78888888888)
    Deneme.Add(22.8888888888)
    Deneme.Add(135.8888888888)
    Deneme.Add(0.48888888888)
    for i in range(1, 1000):
        Deneme.Add(i)

    print("Head value: ", Deneme.GetHeadNode().value)
    print("head.right value: ", Deneme.GetHeadNode().rightNode.value)
    print("head.right.up value: ", Deneme.GetHeadNode().rightNode.upNode.value)
    minDistance1 = Deneme.FindMinValue()
    print("Minimum Distance: ", minDistance1)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
