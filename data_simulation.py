import numpy as np

class RandomResponseCurves():

    #Create a Sigmoid Curve

    def std_sigmoid(self, x):
        
        y = 1 / (1 + np.e ** -x)
        return y

    #Create random points around 0 (Ornstein-Uhlenbeck Method)

    def random_mean_reverting(self, start, steps, sigma,
                            theta = 2, mu = 0):

        tau = 1/theta
        dt = 0.01 * tau
        y = start

        values = [y]

        for i in range (1, steps + 1):
            x_curr = values[i -1]

            mean = x_curr * np.e ** (-theta * dt) + mu * (1 - np.e ** (-theta * dt))
            var = sigma**2/(2 * theta) * (1 - np.e ** (-2* theta * dt))
            sd = np.sqrt(var)

            x_next = np.random.normal(loc = mean, scale = sd)
            x_curr = x_next

            values.append(x_next)

    #Generate Human-like Potency Scatter

    def generate_simulation(self, n):

        n_simulations = n
        x_list = np.linspace(-15, 15, 10)
        simulated_data = np.array([x_list, y_list_err])

        for i in range(n_simulations):

            error_points = list(self.random_mean_reverting(0, 1000, 1))
            y_error = error_points[::100]
            y_list_err = np.array([self.std_sigmoid(x_list) + y_error]).append(simulated_data)
            i += 1

        return simulated_data




