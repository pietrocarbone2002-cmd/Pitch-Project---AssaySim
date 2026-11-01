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

        values = [start]

        for i in range (1, steps + 1):
            x_curr = values[i -1]

            mean = x_curr * np.e ** (-theta * dt) + mu * (1 - np.e ** (-theta * dt))
            var = sigma**2/(2 * theta) * (1 - np.e ** (-2* theta * dt))
            sd = np.sqrt(var)

            x_next = np.random.normal(loc = mean, scale = sd)
            x_curr = x_next

            values.append(x_next)

        return np.array(values)

    #Generate Human-like Potency Scatter

    def generate_simulation(self, n):

        n_simulations = n
        x_list = np.linspace(-15, 15, 10)
        simulated_data = []

        for i in range(n_simulations):

            error_points = self.random_mean_reverting(0, 1000, 0.15)

            #Take every 100th point
            y_error = error_points[:1000:100]

            #Inject the error in the sigmoid curve and save
            y_list_err = self.std_sigmoid(x_list) + y_error
            simulated_data.append([x_list, y_list_err])

        return np.array(simulated_data)

if __name__ == "__main__":

    import matplotlib.pyplot as plt

    simulation = RandomResponseCurves()
    data = simulation.generate_simulation(5)

    print("Array-Form: ", data.shape)

    for i, curve in enumerate(data):
        x = curve[0]
        y = curve[1]

        plt.plot(x,y, "o", label = f"Simulation {i + 1}")

    plt.xlabel("Drug Dosis")
    plt.ylabel("Reponse")
    plt.title("Simualted Bioassay Potency Curves")
    plt.legend()
    plt.grid(alpha = 0.3)
    plt.show()






