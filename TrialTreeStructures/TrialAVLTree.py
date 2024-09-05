from Node import Node
from TrialTree import TrialTree
from TrialTreeStructures.AVLNode import AVLNode


class TrialAVLTree(TrialTree):
    __targetNode: AVLNode = None
    __previousNode: AVLNode = None
    __headNode: AVLNode = None
    __isbalanced: bool = True
    firstNode: AVLNode = None
    lastNode: AVLNode = None

    def __init__(self):
        self.__headNode = None
        self.firstNode = None
        self.lastNode = None
        self.__previousNode = None
        self.__targetNode: AVLNode = None
        self.__isbalanced: bool = True

    def Add(self, *values):
        for value in values:
            if self.__headNode is None:
                self.__headNode = AVLNode(value)
            self.AddNode(self.__headNode, value)
        self.CheckBalanced()




    def AddNode(self, CurrentNode: AVLNode, value):
        self.__previousNode = CurrentNode
        if value > CurrentNode.value:

            if CurrentNode.rightNode is None:
                CurrentNode.rightNode = AVLNode(value)
                CurrentNode.rightNode.upNode = self.__previousNode

            CurrentNode.BalanceFactorDecraament()
            self.AddNode(CurrentNode.rightNode, value)

        elif value < CurrentNode.value:

            if CurrentNode.leftNode is None:
                CurrentNode.leftNode = AVLNode(value)
                CurrentNode.leftNode.upNode = self.__previousNode

            CurrentNode.BalanceFactorIncrament()
            self.AddNode(CurrentNode.leftNode, value)

    def CheckBalanced(self, newAddedNode: AVLNode):
        upNode: AVLNode = newAddedNode.upNode

        if upNode.GetBalanceFactor() >= 2:
            self.__isbalanced = False
            self.__previousNode = upNode

        else:
            upNode = upNode.upNode

            if upNode.GetBalanceFactor() >= 2:
                self.__isbalanced = False
            else:
                self.__isbalanced = True


    def RegainBalance(self):
        if not self.__isbalanced:
            firstNode: AVLNode
            SecondNode: AVLNode
            ThirdNode: AVLNode
            self.__targetNode.value