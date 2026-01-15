AI vs. Human Essay Detector
This project uses a Random Forest Classifier to distinguish between student-written essays and AI-generated text. The model currently achieves a 97.7% accuracy on unseen test data.

The model identifies AI-generated text by looking for specific linguistic patterns. Based on feature importance analysis, the top indicators include:

Formal Transitions: High frequency of words like “additionally,” “moreover,” and “consequently.”

Academic Adjectives: Frequent use of "low-risk" descriptors such as “essential,” “potential,” and “important.”

Contraction Usage: Currently, the model effectively uses the absence of contractions (e.g., "do not" vs "don't") as a strong signal for AI origin.

Model Performance - 

Testing Accuracy: 97.77%

Sensitivity: 95%
Specificity: 99%

How to Use - 

Clone the repository (ensure you have Git LFS installed to pull the full dataset).

Run the preprocessing script to clean the text data.

Execute the training script to generate the model and feature importance plots.

Use the predict_essay() function to test your own text samples.