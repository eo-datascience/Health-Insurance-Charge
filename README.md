🏥 Health Insurance Cost Prediction App

An interactive machine learning web app that predicts a person’s health insurance cost based on input features like age, BMI, smoking status, and region.
The model was trained using Gradient Boosting Regressor (GBR) and deployed with Streamlit Cloud for real-time predictions.

⸻

🚀 Live Demo

👉 Click here to use the app (https://your-streamlit-cloud-link.streamlit.app/)

⸻

✨ Features
 • 💡 Predicts insurance cost in real-time
 • 🧠 Powered by Gradient Boosting Regressor (GBR)
 • 🧩 Handles categorical variables with pd.get_dummies()
 • 💾 Loads pre-trained model with Joblib
 • 🌈 Clean, intuitive Streamlit interface

⸻

🧰 Tech Stack

Category Tools / Libraries
Language Python
Framework Streamlit
Data Handling Pandas, NumPy
Machine Learning Scikit-learn
Model Saving Joblib
Visualization Matplotlib, Seaborn


⸻

⚙️ Installation & Setup

Follow these steps to run the app locally or on Streamlit Cloud.

1. Clone the repository

git clone https://github.com/your-username/health-insurance-prediction.git
cd health-insurance-prediction

2. Install dependencies

pip install -r requirements.txt

3. Run the app locally

streamlit run app.py


⸻

☁️ Deploying on Streamlit Cloud
 1. Push your project to a GitHub repository.
 2. Visit Streamlit Cloud. (https://streamlit.io/cloud)
 3. Click “New App” → Connect your GitHub account.
 4. Select your repo and branch.
 5. In “Main file path,” enter:

app.py


 6. Streamlit Cloud will automatically install dependencies from requirements.txt.

✅ Tip: Ensure the following files are in your repo root:
 • app.py
 • gbr_model.pkl
 • model_columns.pkl
 • requirements.txt
 • README.md

⸻

🧮 How It Works
 1. User inputs age, BMI, region, and smoker status.
 2. Input data is converted to a DataFrame and encoded using get_dummies().
 3. The new data is reindexed to match the model’s training columns.
 4. The pre-trained GBR model predicts the insurance cost.
 5. Streamlit displays the prediction dynamically.

⸻

📂 Project Structure

health-insurance-prediction/
│
├── app.py                # Streamlit web app
├── gbr_model.pkl         # Trained Gradient Boosting model
├── model_columns.pkl     # Columns used during model training
├── requirements.txt      # Dependencies
└── README.md             # Documentation


⸻

📈 Model Performance

Metric Value
R² Score 0.83
MAE (e.g.) 2500.45
RMSE (e.g.) 4300.12

The model was evaluated using cross-validation to ensure robust performance across unseen data.

⸻

👨🏾‍💻 Author

Your Name
📧 your.email@example.com
🌐 Your LinkedIn or Portfolio (https://linkedin.com/in/your-profile)
🐦 @your_twitter (https://twitter.com/your_twitter)

⸻

🪪 License

This project is licensed under the MIT License — feel free to modify and reuse with attribution.

⸻

Would you like me to add an optional screenshot preview section (with placeholders like “App Screenshot Here”) to make your README more visual for GitHub?