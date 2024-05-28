class EuclideanDistance:

    @staticmethod
    def FindEuclideanDistance(coordinatePoint1: tuple[int, int], coordinatePoint2: tuple[int, int]) -> float:
        try:
            x_1, y_1 = coordinatePoint1
            x_2, y_2 = coordinatePoint2

            l2Norm = ((x_2 - x_1) ** 2 + (y_2 - y_1) ** 2) ** 0.5

            return l2Norm

        except ValueError or TypeError:
            print("Invalid Type {parameter1} or {parameter2} \n\
              {parameter1} and {parameter2} must be (integer, integer) Tuple. \n\
              For example {parameter1}=(3,4), {parameter2}=(6,8)".format(parameter1=coordinatePoint1,
                                                                         parameter2=coordinatePoint2))

        except Exception as exc:
            print("An exception occurred {e}. \n\
              {parameter1} and {parameter2} must be (integer, integer) Tuple. \n\
              For example {parameter1}=(3,4), {parameter2}=(6,8)".format(e=exc, parameter1=coordinatePoint1,
                                                                         parameter2=coordinatePoint2))

    @staticmethod
    def ListLenght(listArg: list) -> int:
        try:
            lenght = 0
            for item in listArg:
                lenght += 1

            print("List lenght is %(lenght)x" % {"lenght": lenght})
            return lenght

        except Exception as exc:
            print("An exception occurred: %s" % {exc})

    @staticmethod
    def Combination(number1: int, number2: int):
        # result = 0
        try:
            if number1 < number2:
                print("First parameter value must be high than second value")

            result = number1

            while number2 > 1:
                result *= (number1 - 1)
                result /= number2
                number1 -= 1
                number2 -= 1
            return result
        except Exception as exc:
            print("An exception occurred: %s" % {exc})

    @staticmethod
    def EuclideanDistanceInList(self, points: list) -> list:
        choiceAmount = 2
        listIndex = 0
        listTargetIndex = listIndex + 1
        distanceListIndex = 0
        distanceListLenght: int = 0
        listTargetIndex: int = listIndex + 1

        pointsListLenght = self.ListLenght(points)
        distanceListLenght = self.Combination(pointsListLenght, choiceAmount)

        distances = [0] * int(distanceListLenght)

        while listIndex < pointsListLenght:
            while listTargetIndex < pointsListLenght:
                distance = self.FindEuclideanDistance(points[listIndex], points[listTargetIndex])
                print("%(1)x. and %(2)x. point between euclid distance: %(dist)f " % {"1": listIndex,
                                                                                      "2": listTargetIndex,
                                                                                      "dist": distance})
                distances[distanceListIndex] = distance

                distanceListIndex += 1
                listTargetIndex += 1

            listIndex += 1
            listTargetIndex = listIndex + 1

        return distances
