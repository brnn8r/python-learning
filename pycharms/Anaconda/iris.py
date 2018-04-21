
from sklearn import datasets

def main():

    iris = datasets.load_iris()
    digits = datasets.load_digits()

    print(iris)
    print(digits)

    print(digits.target)


if __name__ == "__main__":
    main()

