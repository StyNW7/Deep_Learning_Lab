import tensorflow as tf
import keras
import numpy as np
from sklearn.model_selection import train_test_split
from keras.utils import plot_model
import matplotlib.pyplot as plt

print("✅ TensorFlow:", tf.__version__)
print("✅ Keras:", keras.__version__)
print("✅ NumPy:", np.__version__)
print("✅ GPU:", tf.config.list_physical_devices('GPU'))