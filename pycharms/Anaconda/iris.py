import numpy as np
from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestRegressor
from sklearn import svm
from sklearn.model_selection import train_test_split
from datetime import datetime
from sklearn.metrics import accuracy_score

def main():
    iris = datasets.load_iris()
    iris_X = iris.data
    iris_y = iris.target

    iris_X_train, iris_X_test, iris_y_train, iris_y_test = train_test_split(iris_X, iris_y,
                                test_size=0.25, random_state=datetime.now().microsecond)

    #model = KNeighborsClassifier()
    #model = svm.SVC(kernel='poly', degree=5)
    model = svm.LinearSVC()

    model.fit(iris_X_train, iris_y_train)

    test_result = model.predict(iris_X_test)

    print(f"Model accuracy = {round(accuracy_score(test_result, iris_y_test)*100,2)}%")

    predictions = list(enumerate(test_result ))
    actual_values = list(enumerate(iris_y_test))

    discrepancies = ((pos, prediction, iris_y_test[pos]) for pos, prediction in predictions
                     if prediction != iris_y_test[pos])
    for pos, prediction, actual in discrepancies:
        print(f"predicited {prediction} at position {pos} but was actually {actual}")

    print(f"predicted\t = {predictions}\nactual\t\t = {actual_values}")


if __name__ == "__main__":
    main()
