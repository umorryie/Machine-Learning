from SimpleLinearRegresion import SimpleLinearRegression

if __name__ == "__main__":
    x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    y = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]
    z = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    predicty = SimpleLinearRegression()
    predicty.fitWhenTraining(x, z)
    print(predicty.predict(113))
