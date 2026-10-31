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
All measurements will be synthetic, covering **3 established** (old) and **20 new** reference materials.

Each observation will contain a reference-material identifier, the drug concentration **X** and potency-related response **Y** (generally absorbance or luminescence). The planned dataset size is approximately **10 concentration-response observations per material** (about **230–240 observations**), subject to implementation.

Responses will start from a theoretical sigmoid curve. To simulate measurement variability, an Ornstein–Uhlenbeck process will generate a stochastic mean-reverting series 1,100 values. Every 100th value will be sampled as a deviation from the theoretical response.

## 8. How will you apply regression to the simulated data, and how does it support your idea?
A **4PL curve will be fitted to the noisy simulated measurements**, rather than using the original theoretical curve as the result. AssaySym will evaluate the fitted curves through symmetry and ratio analyses and support comparison between established and new reference materials.
