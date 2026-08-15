# Customer Churn Prediction

A Machine Learning based web application that predicts whether a customer is likely to churn based on their information.

## 📌 Project Overview

Customer churn prediction helps businesses identify customers who are likely to leave their service.

This project uses Machine Learning techniques to analyze customer information and predict whether a customer is likely to churn.

The trained Machine Learning model is integrated with a Streamlit web application, allowing users to enter customer details and get a churn prediction through an interactive interface.

## 🎯 Objectives

- Predict whether a customer is likely to churn.
- Analyze important customer characteristics.
- Build a Machine Learning model for churn prediction.
- Create an interactive web interface using Streamlit.
- Help businesses identify customers who may leave their service.

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Pickle
- Machine Learning

## 📂 Project Structure

```text
Customer-Churn-Prediction/
│
├── app.py
├── Telco-Customer-Churn.csv
├── customer_churn_model.pkl
├── requirements.txt
├── README.md
└── LICENSE
```

## 📊 Dataset

The project uses the Telco Customer Churn dataset.

The dataset contains customer-related information such as:

- Gender
- Senior Citizen
- Partner
- Dependents
- Tenure
- Phone Service
- Internet Service
- Contract
- Payment Method
- Monthly Charges
- Total Charges
- Churn Status

## 🤖 Machine Learning

The project uses a Machine Learning model trained on customer data to predict churn.

The trained model is saved as:

`customer_churn_model.pkl`

The Streamlit application loads the trained model and uses it to generate predictions for new customer information.

## ✨ Features

- Customer churn prediction
- Interactive web application
- Customer information input
- Machine Learning based prediction
- Simple and user-friendly interface
- Trained model integration

## 🚀 How to Run the Project

### 1. Clone the Repository

```bash
git clone https://github.com/Karthik-commits07/Customer-Churn-Prediction.git
```

### 2. Navigate to the Project Folder

```bash
cd Customer-Churn-Prediction
```

### 3. Install Required Libraries

```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit Application

```bash
streamlit run app.py
```

The application will open in your browser.

## 📈 Prediction Output

The application predicts whether a customer is likely to:

- Stay with the company
- Churn from the company

## 🔮 Future Improvements

The project can be further improved by adding:

- Multiple Machine Learning models
- Hyperparameter tuning
- Model comparison
- Churn probability prediction
- Feature importance visualization
- Interactive analytics dashboard
- Better UI/UX
- Online deployment
- Real-time prediction
- Explainable AI features

## 👨‍💻 Author

**M. Murali Karthik**

B.Tech CSE (Data Science & Artificial Intelligence)

## 📄 License

This project is licensed under the MIT License.
