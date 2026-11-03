# Pitch-Project - AssaySim
**Automated Ref-vs-Ref Evaluator for Bioassays**

## 1. What are your names?
Carbone Pietro

## 2. Is it an online app or a start-up? What is its name?
AssaySym is an offline Python desktop application with a graphical user interface (GUI).

## 3. What problem in life sciences does it solve?
When introducing new reference materials for pharmaceutical bioassays, laboratories need to verify the quality of dose-response curves and assess whether new materials are comparable to established references.

## 4. What does the app do? What is its central idea?
AssaySym aims to automate quantitative curve-quality assessment and reference-versus-reference (Ref vs. Ref) comparisons. The GUI will visualize dose-response data, fitted curves, and quality indicators.

## 5. How does it solve the problem?
Individual curves are first assessed using symmetry and ratio analyses. Curves meeting the defined quality criteria can then be compared across old and new reference materials.

## 6. Which regression method will you use, and why?
The project will use **four-parameter logistic (4PL) nonlinear regression**, because bioassay dose-response relationships are typically sigmoidal. The fitted curve will be used for subsequent quality assessment.

**Course clarification needed:** The assignment explicitly lists linear, multiple linear, Poisson, and binomial regression. We need to confirm whether 4PL is accepted or whether an additional course-listed model is required.

## 7. What data will you simulate? How large will the dataset be, what do rows and columns represent, and how will you choose the parameters?
The demo for the App will have 20 simulated curves.**3 established** (old) and **20 new** reference materials.

For each simulation, 3 x 12 drug concentration points will be derived from a base sigmoid curve. To simulate measurement variability, an Ornstein–Uhlenbeck process will generate a stochastic mean-reverting series. Every 100th value will be sampled as a deviation from the theoretical response.
Each simulation will have the drug concentration (ng/mL) **X** and potency-related response **Y** (generally absorbance or luminescence). A true scale of the Y axis will not be used for the simulation, since no true readings are provided.

## 8. How will you apply regression to the simulated data, and how does it support your idea?
A **4PL curve will be fitted to the noisy simulated measurements**, rather than using the original theoretical curve as the result. AssaySym will evaluate the fitted curves through symmetry and ratio analyses and support comparison between established and new reference materials.

## 9. AI Use
The whole matplolib plotting and logic was made with the help of ChatGPT
