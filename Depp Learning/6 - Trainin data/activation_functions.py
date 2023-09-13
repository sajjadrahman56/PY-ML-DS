# -*- coding: utf-8 -*-
"""activation-functions.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1w3lQ7DV7qOSCVWKjwfy30EbTDwEODRSl

# Activation functions
- use to introduce non-linearity into the model
-  It control the output of a neuron and enable the network to learn complex patterns from the input data.

#### Different Types of Activation Functions
- sigmoid   
-tanh
- ReLU (Rectified Linear Unit)
- Leaky ReLU,
- softmax (multi-class classification)
"""



# Binary Step Activation Function
#
# Return 0 or 1 ( > 0)

import numpy as np
import matplotlib.pyplot as plt

def binaryStep(x):
  return np.heaviside(x,1);

x = np.linspace(-10,10)
plt.plot(x,binaryStep(x))

plt.show()

# Linear Activation function
#
# It returns as like input

def linear(x):
  return x

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10,10)
plt.plot(x,linear(x))

plt.show()

# Sigmoid Activation function
#
# It returns 1/(1+exp(-x)) . either 0 or 1

import numpy as np
import matplotlib.pyplot as plt

def sigmoid(x):
  return 1/(1+np.exp(-x))

value = 1.0
print('Applying Sigmoid Activation on (%.1f) gives %.1f' % (value, sigmoid(value)))


x = np.linspace(-10, 10)
plt.plot(x, sigmoid(x))
plt.show()

# Tanh Activation function
#
# It returns (1-exp(-2x))/(1+exp(-2x)) . values lie -1 or 1

import numpy as np
import matplotlib.pyplot as plt

def tanh(x):
  return np.tanh(x)

plt.plot(x, tanh(x))
plt.show()

# Relu Activation function
#
# It returns 0 if input is < 0 otherwise input

import numpy as np
import matplotlib.pyplot as plt

def Relu(x):
  x1 = []
  for data in x:
    if data < 0:
      x1.append(0)
    else:
      x1.append(data)
  return x1

x = np.linspace(-50, 50)
plt.plot(x, Relu(x))

plt.show()

# Leaky Relu Activation function
#
# f(x) = 0.01x , x<0
#       = x,     x>=0

import numpy as np
import matplotlib.pyplot as plt

def leaky_relu(x):
  x1 = []
  for data in x:
    if data>0 :
      x1.append(data)
    else:
      x1.append(0.01 * data)

  return x1

x = np.linspace(-10, 30)
plt.plot(x, leaky_relu(x))
plt.show()

# Softmax Activation function
#
# the last linear layer of a multi-class classification neural network into probabilities
#

import numpy as np
import matplotlib.pyplot as plt

def softmax(x):
    ''' Compute softmax values for each sets of scores in x. '''
    return np.exp(x) / np.sum(np.exp(x))

x = np.linspace(-20, 10)

plt.plot(x, softmax(x))
plt.show()

# Tanh Activation function
#
# It returns (1-exp(-2x))/(1+exp(-2x)) . values lie -1 or 1

import numpy as np
import matplotlib.pyplot as plt



"""- collect
- https://www.nbshare.io/notebook/751082217/Activation-Functions-In-Python/

"""