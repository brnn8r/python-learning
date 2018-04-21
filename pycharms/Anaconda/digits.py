import threading

import numpy as np
from sklearn import datasets
from sklearn import svm
import matplotlib.pyplot as plt


def plot_digit_async(digit_data, image_size):
    plt.figure(1, figsize=(image_size, image_size))
    plt.imshow(digit_data, cmap=plt.cm.gray_r, interpolation='nearest')
    plt.show()


def plot_digit(digit_data, image_size):
    t = threading.Thread(target=plot_digit_async, args=(digit_data, image_size))
    t.start()
    return t


def predicit_digit(digits, digit_pos=1, image_size=3):
    classifier = svm.SVC(gamma=0.001, C=100.0)

    data_list = np.concatenate((digits.data[:digit_pos], digits.data[digit_pos + 1:]))
    target_list = np.concatenate((digits.target[:digit_pos], digits.target[digit_pos + 1:]))

    classifier.fit(data_list, target_list)

    prediction = classifier.predict(digits.data[digit_pos:digit_pos + 1])

    plot_digit(digits.images[digit_pos], image_size)
    print(f"The image displayed is predicted to be {prediction}")


def main():
    digits = datasets.load_digits()

    predicit_digit(digits, digit_pos=88, image_size=4)


if __name__ == "__main__":
    main()
