import numpy as np
import matplotlib.pyplot as ppl

class RandomResponseCurves():
#Create a Sigmoid Curve

    def std_sigmoid(x):
        
        y = 1 / (1 + np.e ** -x)
        return y

    #Create random points around 0 (Ornstein-Uhlenbeck Method)

    def random_mean_reverting(start, steps, sigma,
                            theta = 2, mu = 0):

        tau = 1/theta
        dt = 0.01 * tau
        y = start

        time = np.arange(steps + 1)
        values = [y]

        for i in range (1, steps + 1):
            x_curr = values[i -1]

            mean = x_curr * np.e ** (-theta * dt) + mu * (1 - np.e ** (-theta * dt))
            var = sigma**2/(2 * theta) * (1 - np.e ** (-2* theta * dt))
            sd = np.sqrt(var)

            x_next = np.random.normal(loc = mean, scale = sd)
            x_curr = x_next

            values.append(x_next)

        return time, values

#Generate Human-like Potency Scatter

n_simulations = 20
x_list = np.linspace(-15, 15, 10)

for i in range(1, n_simulations):

    data_list = np.array([])
    error_points = list(random_mean_reverting(0, 1000, 1))
    y_error = error_points[::100]
    y_list_err = np.array([std_sigmoid(x_list) + y_error]).append(data_list)
    i += 1



# ppl.plot(x_list, y_list_err, "o", color = "green", label = "Error Function")
# ppl.legend()
# ppl.ylabel("Reponce")
# ppl.xlabel("Drug Dosis")
# ppl.grid()
# ppl.show()
