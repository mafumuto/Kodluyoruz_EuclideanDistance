from Node import Node


class AVLNode(Node):
    __balancefactor: int = 0

    def __init__(self, value):
        super.__init__(value)

    def GetBalanceFactor(self):
        return self.__balancefactor

    def BalanceFactorIncrament(self):
        self.__balancefactor += 1
        if self.__balancefactor > 2:
            self.__balancefactor == 2

    def BalanceFactorDecraament(self):
        self.__balancefactor -= 1
        if self.__balancefactor < -2:
            self.__balancefactor == -2

