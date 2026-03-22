# 💳 BankFlow – Predictive Credit Scorecard System

## 📌 Overview
**BankFlow** is a full-stack fintech application simulating a **banking credit risk assessment system**.  

It allows users to:
- Input financial details  
- Generate a **real-time credit score**  
- Visualize results using interactive charts  
- Track past credit evaluations  

The system mimics real-world banking workflows by combining **risk scoring, OTP verification, and historical tracking**.

---

## 🚀 Core Features

### 📊 Credit Risk Prediction
- Score range: **300 – 850**
- Rule-based scoring model
- Instant decision output:
  - ✅ Approved (Low Risk)
  - ⚠️ Review Required (Medium Risk)
  - ❌ Rejected (High Risk)

### 📈 Interactive Visualization
- Dynamic **doughnut chart (Chart.js)**  
- Real-time score display  
- Visual risk meter with pointer indicator  

### 📜 Scoring History Tracking
- Stores all applications in MySQL  
- Displays applicant name, credit score, decision, and date  
- Color-coded decisions for better readability  

### 🔐 OTP Authentication (Demo)
- Generates and verifies OTP  
- Simulated verification flow before accessing credit analysis

### 🖥️ User Interface
- Dashboard with risk categories & FAQs  
- Analysis page for score generation  
- History page for past records  
- OTP verification page  

---

## 🧠 Credit Score Formula


Score = 380
+ (Income × 0.0015)
+ (Age × 0.8)
+ (Credit History × 1.5)
- (Debt × 0.003)


---

## 📊 Risk Classification

| Score Range | Category      | Decision        |
|------------|--------------|----------------|
| ≥ 750      | Excellent     | Approved       |
| 650–749    | Fair          | Review Required|
| < 650      | High Risk     | Rejected       |

---

## 🛠️ Tech Stack

- **Backend:** Flask (Python)  
- **Frontend:** HTML, CSS, JavaScript  
- **Visualization:** Chart.js  
- **Database:** MySQL  

### Libraries Used:
- Flask  
- Flask-MySQLdb  
- Flask-CORS  
- mysqlclient  

---

## 📁 Project Structure


├── app.py
├── templates/
│ ├── dashboard.html
│ ├── analysis.html
│ ├── history.html
│ ├── otp.html
├── static/
│ └── style.css
├── requirements.txt
└── README.md


---

## ⚙️ Setup Instructions

### 1️⃣ Clone Repository
```bash
git clone https://github.com/darshanadalvi39/credit-default-scorecard-bankflow.git
cd credit-default-scorecard-bankflow
2️⃣ Install Dependencies
pip install -r requirements.txt
3️⃣ Setup MySQL Database
CREATE DATABASE banking_db;

CREATE TABLE credit_applicants (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    income FLOAT,
    age INT,
    credit_history_months INT,
    debt FLOAT,
    credit_score INT,
    decision VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
4️⃣ Configure Database

Update credentials in app.py:

app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'your_password'
5️⃣ Run the Application
python app.py

Open in browser:

http://127.0.0.1:5000/
🔌 API Endpoints
Endpoint	Method	Description
/predict	POST	Generate credit score
/send_otp	POST	Send OTP
/verify_otp	POST	Verify OTP
/get_history	GET	Fetch scoring history
🔮 Future Improvements
Integrate Machine Learning models (Logistic Regression, XGBoost)
Use real SMS OTP service (Twilio)
Deploy on cloud (Render / Vercel)
Add advanced analytics dashboard
Implement secure authentication system
⚠️ Disclaimer

This project is intended for educational purposes only and should not be used for real financial decisions.

👤 Author

Your Name
GitHub: https://github.com/darshanadalvi39

⭐ Contributing

Contributions are welcome! Feel free to fork and improve the project.