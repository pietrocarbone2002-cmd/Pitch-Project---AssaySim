import numpy as np
import matplotlib.pyplot as ppl
from scipy.optimize import curve_fit

#Create a Sigmoid Curve

def std_sigmoid(x):
    
    y = 1 / (1 + np.e ** -x)
    return y

x_list = np.linspace(-15, 15, 10)
y_sub = np.array([0, 0.05, -0.1, 0.11, -0.08, 0.1, 0.12, -0.1, 0, -0.1])
y_list = std_sigmoid(x_list)
y_list_err = std_sigmoid(x_list) + y_sub


ppl.plot(x_list, y_list, "--", color = "orange", label = "Example")
ppl.plot(x_list, y_list_err, "o", color = "green", label = "Error Function")
ppl.legend()
ppl.ylabel("Reponce")
ppl.xlabel("Drug Dosis")
ppl.grid()
ppl.show()
