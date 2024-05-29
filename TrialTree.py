from Node import Node


class TrialTree:
    __headNode: Node = None
    firstNode: Node = None
    lastNode: Node = None
    __targetNode: Node = None
    __previousNode: Node = None
    '''
    def __init__(self, listArg: list, listLenght: int) -> None:
        listArgIndex = 0
        self.__headNode = Node(listArg[0])
        while listArgIndex < listLenght:
            self.Add(listArg)
            listArgIndex += 1

        self.firstNode = None
        self.lastNode = None
    '''
    def __init__(self) -> None:
        self.__headNode = None
        self.__targetNode = None
        self.firstNode = None
        self.lastNode = None

    def Add(self, *values):
        for value in values:
            if self.__headNode is None:
                self.__headNode = Node(value)
            self.AddNode(self.__headNode, value)

    def AddNode(self, CurrentNode: Node, value):
        self.__previousNode = CurrentNode
        if value > CurrentNode.value:

            if CurrentNode.rightNode is None:
                CurrentNode.rightNode = Node(value)
                CurrentNode.rightNode.upNode = self.__previousNode
            self.AddNode(CurrentNode.rightNode, value)

        elif value < CurrentNode.value:
            if CurrentNode.leftNode is None:
                CurrentNode.leftNode = Node(value)
                CurrentNode.leftNode.upNode = self.__previousNode
            self.AddNode(CurrentNode.leftNode, value)

    def GetHeadNode(self) -> Node:
        return self.__headNode

    def FindMinValue(self):
        return self._FindMinValueNode(self.__headNode).value

    def _FindMinValueNode(self, CurrentNode: Node):
        self.__previousNode = CurrentNode
        if CurrentNode.leftNode is not None:
            self._FindMinValueNode(CurrentNode.leftNode)
        return self.__previousNode

    def _updateFirstNode(self, NodeArg: Node):
        self.firstNode = NodeArg
