from math import exp, expm1, pow


def derivate1(listX, listY, linearFunctionParams):
    if len(listX) != len(listY):
        raise Exception("Wrong lenghts")
    else:
        listSize = len(listY)
        listOfSums = [-2*(listY[i]-(linearFunctionParams[0]*listX[i] +
                                    linearFunctionParams[1]))*listX[i] for i in range(listSize)]
        return float((sum(listOfSums)) / listSize)


def derivate2(listX, listY, linearFunctionParams):
    if len(listX) != len(listY):
        raise Exception("Wrong lenghts")
    else:
        listSize = len(listY)
        listOfSums = [-2*(listY[i]-(linearFunctionParams[0]*listX[i] +
                                    linearFunctionParams[1]))*1 for i in range(listSize)]
        return float((sum(listOfSums)) / listSize)


def lossFunction(listX, listY, linearFunctionParams):
    if len(listX) != len(listY):
        raise Exception("Wrong lenghts")
    else:
        listSize = len(listY)
        listOfSums = [pow((listY[i]-(linearFunctionParams[0]*listX[i] +
                                     linearFunctionParams[1])), 2) for i in range(listSize)]
        value = sum(listOfSums)
        return float(sum / listSize)


class SimpleLinearRegression:
    def __init__(self, learningRateAlfa=0.0001, iterationNumbers=10000):
        self.iterationNumbers = iterationNumbers
        self.learningRateAlfa = learningRateAlfa
        self.x1 = None
        self.x0 = None

    def fitWhenTraining(self, X, Y):
        if len(X) < 2 or len(X) != len(Y):
            raise Exception("Wrong lenghts")
        else:
            x1 = float((Y[-1]-Y[0]) / (X[-1]-X[0]))
            x0 = float(Y[0] - X[0]*x1)
            realX0 = x0
            realX1 = x1
            params = [realX0, realX1]
            for i in range(self.iterationNumbers):
                realX0 = min(realX0, realX0-self.learningRateAlfa *
                             derivate1(X, Y, params))
                realX1 = min(realX1, realX1-self.learningRateAlfa *
                             derivate2(X, Y, params))
            self.x1 = realX1
            self.x0 = realX0
            # return [realX1, realX0]

    def predict(self, X):
        try:
            #params = self.fitWhenTraining()
            return float(X*self.x1 + self.x0)
        except:
            raise Exception("{} is not a valid number".format(X))


x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
predicty = SimpleLinearRegression()
predicty.fitWhenTraining(x, y)
print(predicty.predict(11))
