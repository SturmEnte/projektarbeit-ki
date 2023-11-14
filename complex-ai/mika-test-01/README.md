# AI Example

## Introduction

This is a tensorflow keras based AI example for recognizing digits from 0 to 9.
As this model was trained with example data included in the tensorflow library, testing it with your own images might not work so well.
However, I have provided a way to test the model with self drawn images.

## The Model

The model is using black and white images with a size of 28 x 28 pixels.
The hidden layer consists of two dense layers with 128 neurons each.
The output layer is made of 10 neurons; one for every possible digit.

## Installation

To be able to use this model, you need to have python 3 installed on your machine.
If you are on linux and your python version happens to be close enough to mine, you can use the *install_venv.sh* file.
Otherwise just install the libraries *tensorflow* and *opencv-python* with pip.

On the school laptops the file *install_school_laptop.bat* can be executed to install everything necessary.

## tensorflow_train.py

This file creates, trains and saves a model. It needs to be run before you can use it to test it.

## tensorflow_predict.py

This file loads the previously trained model and tests it with the provided test data of the tensorflow library.
The variable *i* can be changed to use a different sample.

## tensorflow_draw.py

This file is the **most exciting** one in this repository.
Here you can draw an image of a digit yourself!
Once you are done drawing hit *enter* on your keyboard and it will try to guess what you drew.

As stated earlier, this might not work that well, because the training data is different to the data you input in many ways.