import numpy as np
from scipy.optimize import curve_fit

class RandomResponseCurves():

    #Create a Sigmoid Curve

    def std_sigmoid(self, x):
        
        y = 1 / (1 + np.e ** (-0.7*x))
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
        log_dosis = np.linspace(-15, 15, 12)
        x_list = np.exp(log_dosis)
        simulated_data = []

        #Pontecy Curves normally use triplicates before fitting a 4PL curve

        #This first loop creates the simulation
        for i in range(n_simulations):

            triplicates = []

            #This second loop creates the triplicates for each simulation
            for j in range(3):

                error_points = self.random_mean_reverting(0, 1200, 0.08)

                #Take every 100th point
                y_error = error_points[:1200:100]

                #Inject the error in the sigmoid curve and save
                y_list_err = self.std_sigmoid(log_dosis) + y_error

                triplicates.append(y_list_err)
            
            simulated_data.append(triplicates)

        return x_list, np.array(simulated_data)

    #Create the 4PL Regression
    #A = lower asymptote , B = slope middle-point, C = EC50 , D = higher asymptote
    def four_pl_fit(self, x, a, b, c, d):

        potency_curve = a + (d - a) / (1 + (c / x) ** b)
        return potency_curve

    def fit_4pl_simulation(self, x, triplicates):

        x_data = np.tile(x, len(triplicates))
        y_data = np.asarray(triplicates).ravel()

        mean_reponse = np.mean(triplicates, axis=0)

        a_start = np.min(mean_reponse)
        d_start = np.max(mean_reponse)

        half_reponse = (a_start + d_start) / 2
        midpoint_index = np.argmin(np.abs(mean_reponse - half_reponse))

        c_start = x[midpoint_index]

        params, covar = curve_fit(self.four_pl_fit, x_data, y_data,
                                    p0=[a_start, 1.0, c_start, d_start],
                                    bounds=([-np.inf, 0.01, np.min(x), -np.inf],
                                          [np.inf, 10.0, np.max(x), np.inf]
                                    ),
                                    maxfev=20000      
                                  )
        
        return params, covar

    

if __name__ == "__main__":
    import matplotlib.pyplot as plt

    simulation = RandomResponseCurves()
    x, data = simulation.generate_simulation(6)

    n_simulations = len(data)
    n_cols = min(3, n_simulations)
    n_rows = (n_simulations + n_cols - 1) // n_cols

    fig, axes = plt.subplots(
        n_rows,
        n_cols,
        figsize=(5 * n_cols, 4 * n_rows),
        sharex=False,
        sharey=False,
        squeeze=False,
    )

    fig.canvas.manager.set_window_title("Potency Curve Simulation")

    for i, triplicates in enumerate(data):
        ax = axes.flat[i]

        #Triplicates
        for j, y in enumerate(triplicates):
            ax.plot(x, y, ".", label=f"Triplicate {j + 1}")

        #Fit the 4PL regression
        try:
            parameters, covariance = simulation.fit_4pl_simulation(x, triplicates)

            a, b, c, d = parameters

            x_fit = np.geomspace(np.min(x), np.max(x), 300)
            y_fit = simulation.four_pl_fit(x_fit, *parameters)

            ax.plot(x_fit, y_fit, "-.", label=r"$f(x) = a + \frac{d-a}{1+(c/x)^b}$", color = "blue", linewidth = 0.7)

            parameter_text = (
                f"A = {a:.3g}\n"
                f"B = {b:.3g}\n"
                f"C = {c:.3g}\n"
                f"D = {d:.3g}"
            )

            ax.text(0.97, 0.05, parameter_text, transform=ax.transAxes, fontsize=10,
            ha="left", va="bottom", bbox=dict(
                boxstyle="round",
                facecolor="white",
                edgecolor="gray",
                alpha=0.85,
                )
            )


        except RuntimeError:
            print(f"Fit for simulation {i + 1} failed.")

        ax.set_xscale("log")
        ax.set_xlabel("Drug Dosis [ng/mL]")
        ax.set_ylabel("Potency Responce")
        ax.set_title(f"Simulation {i + 1}")
        ax.legend()
        ax.grid(alpha=0.3)

    for ax in list(axes.flat)[n_simulations:]:
        ax.set_visible(False)

    fig.tight_layout()
    plt.show()





