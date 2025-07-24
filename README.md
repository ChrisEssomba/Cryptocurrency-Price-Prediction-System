# 📈 Crypto Price Prediction System

This project aims to develop a complete system for **predicting the short-term price of cryptocurrencies** using real-time data and machine learning. It combines data engineering, model training, and web deployment into a seamless, production-ready solution.

---

## 🚀 Project Overview

In a highly volatile market like cryptocurrency, being able to forecast price movements, even in the short term, can provide valuable insights for investors and analysts. This project leverages machine learning to predict crypto price trends and provides an interactive web interface for users to view forecasts in real-time.

### 🔧 Main Features

- **Automated Data Collection**: Real-time price data is continuously collected using a REST API and fed into the prediction pipeline.
- **ML Model Training**: A powerful `XGBoost` regression model is trained and fine-tuned to capture patterns in crypto price movements.
- **Web Application**: The FastAPI framework is used to create a lightweight and efficient RESTful API interface for predictions.
- **Containerization**: The entire app is containerized using Docker for portability and reproducibility.
- **Cloud Deployment**: The application is deployed on Microsoft Azure with Kubernetes orchestration for scalability.
- **CI/CD Integration**: GitHub Actions ensures automated testing and deployment with every push.

---

## 🧪 Tech Stack

- **Languages & Frameworks**: Python, FastAPI
- **Machine Learning**: XGBoost, Scikit-Learn
- **DevOps & Cloud**: Docker, Kubernetes, Azure, GitHub Actions
- **Other**: REST APIs, Automated Testing

---

## 📁 Project Structure

```
├── .github/
│   └── workflows/            # CI/CD pipelines (Azure deployment)
│
├── containerization/         # Docker/Kubernetes config files
├── dash_scripts/             # Dashboard-related scripts
├── manifests/                # Kubernetes manifests
├── reports/                  # Analysis/output reports
├── tests/                    # Test scripts
├── web_application/          # Web app source code
│
├── .coverage                 # Test coverage data
├── .dockerignore             # Docker ignore rules
├── .gitignore                # Git ignore rules
├── README.md                 # Project documentation
└── requirements.txt          # Python dependencies
```


---

## 🧠 Model Choice

We evaluated several models for time series prediction and found that `XGBoost` delivered the best performance in terms of short-term accuracy and generalization on unseen data. Its ability to handle non-linear relationships and missing values makes it particularly well-suited for real-world crypto data.

---

## 💻 How to Run Locally

1. **Clone the repository**  
   ```bash
   git clone https://github.com/your-username/crypto-price-predictor.git
   cd crypto-price-predictor
   ```

2. **Create a virtual environment and install dependencies**  
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Run the application**  
   ```bash
   uvicorn App:app --reload
   ```

4. **Access the API**  
   Go to `http://localhost:8000/docs` for the Swagger documentation.

---

## ☁️ Deployment

- Dockerized with a `Dockerfile`
- Deployed to **Azure Kubernetes Service**
- CI/CD handled through GitHub Actions in `.github/workflows/`

---

## 📬 Contact

If you have any questions or suggestions, feel free to reach out!

---

## 📜 License

This project is licensed under the MIT License.

