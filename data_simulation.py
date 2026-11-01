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

            triplicates = []

            for j in range(3):

                error_points = self.random_mean_reverting(0, 1000, 0.15)

                #Take every 100th point
                y_error = error_points[:1000:100]

                #Inject the error in the sigmoid curve and save
                y_list_err = self.std_sigmoid(x_list) + y_error

                triplicates.append(y_list_err)
            
            simulated_data.append(triplicates)

        return x_list, np.array(simulated_data)

if __name__ == "__main__":

    import matplotlib.pyplot as plt

    simulation = RandomResponseCurves()
    x, data = simulation.generate_simulation(1)

    print("Array-Form: ", data.shape)

    for i, triplicates in enumerate(data):
        plt.figure()

        for j, y in enumerate(triplicates):
            plt.plot(x, y, "o", label=f"Triplikat {j + 1}")

        plt.xlabel("Drug Dosis")
        plt.ylabel("Antwort")
        plt.title(f"Simulation {i + 1}")
        plt.legend()
        plt.grid(alpha=0.3)

    plt.show()






