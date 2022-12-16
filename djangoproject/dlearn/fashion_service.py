import numpy as np
import pandas as pd
import tensorflow as tf
from keras import Sequential
from keras.layers import Dense
from keras.saving.save import load_model
from matplotlib import pyplot as plt
from sklearn import datasets
from sklearn.preprocessing import OneHotEncoder
import os




class FashionService(object):
    def __init__(self):
        global class_names
        class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
                            'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']


    def service_model(self, i) -> []:
        model = load_model(os.path.join(os.path.abspath("dlearn\save"), "fashion_model.h5"))
        (train_images, train_labels), (test_images, test_labels) = tf.keras.datasets.fashion_mnist.load_data()
        predictions = model.predict(test_images)

        predictions_array, true_label, img = predictions[i], test_labels[i], test_images[i]
        predicted_label = np.argmax(predictions_array)
        print(f"예측 답: {predicted_label}")

        return (class_names[predicted_label], class_names[true_label])
    @staticmethod
    def plot_value_array(i, predictions_array, true_label):
        prediction_arrays, true_label = predictions_array[i], true_label[i]

        plt.grid(False)
        plt.xticks([])
        plt.yticks([])
        thisplot = plt.bar(range(10),
                           predictions_array,
                           color='#777777')
        plt.ylim([0,1])
        predicted_label = np.argmax(predictions_array)
        thisplot[predicted_label].set_color('red')
        thisplot[true_label].set_color('blue')




fashion_menu = ["Exit", #0
             "hook"] #1
fashion_lambda = {
    "1" : lambda x: x.service_model(10),
}
if __name__ == '__main__':
    fashion = FashionService()
    while True:
        [print(f"{i}. {j}") for i, j in enumerate(fashion_menu)]
        menu = input('메뉴선택: ')
        if menu == '0':
            print("종료")
            break
        else:
            try:
                fashion_lambda[menu](fashion)
            except KeyError as e:
                if 'some error message' in str(e):
                    print('Caught error message')
                else:
                    print("Didn't catch error message")