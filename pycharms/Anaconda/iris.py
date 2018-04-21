import numpy as np
from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
from datetime import datetime


def get_test_train_split(X, y, seed=None, split_percentage=0.1):

    seed = seed or datetime.now().microsecond
    np.random.seed(seed)

    len_X = len(X)
    indicies = np.random.permutation(len_X)
    test_partition_index = int(-len_X * split_percentage)

    X_train = X[indicies[:test_partition_index]]
    y_train = y[indicies[:test_partition_index]]
    X_test = X[indicies[test_partition_index:]]
    y_test = y[indicies[test_partition_index:]]

    return (X_train, y_train, X_test, y_test)


def main():
    iris = datasets.load_iris()
    iris_X = iris.data
    iris_y = iris.target

    iris_X_train, iris_y_train, iris_X_test, iris_y_test = get_test_train_split(iris_X, iris_y, split_percentage=0.15)

    knn_model = KNeighborsClassifier()

    knn_model.fit(iris_X_train, iris_y_train)

    predictions = list(enumerate(knn_model.predict(iris_X_test)))
    actual_values = list(enumerate(iris_y_test))

    discrepancies = ((pos, prediction, iris_y_test[pos]) for pos, prediction in predictions
                     if prediction != iris_y_test[pos])
    for pos, prediction, actual in discrepancies:
        print(f"predicited {prediction} at position {pos} but was actually {actual}")

    print(f"predicted\t = {predictions}\nactual\t\t = {actual_values}")


if __name__ == "__main__":
    main()
