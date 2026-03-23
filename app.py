from flask import Flask, render_template, request, jsonify
from flask_mysqldb import MySQL
from flask_cors import CORS
import MySQLdb.cursors
import random

app = Flask(__name__)
CORS(app)

# --- DATABASE CONFIGURATION ---
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Rudra@2921'
app.config['MYSQL_DB'] = 'banking_db'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)

# OTP STORE (temporary)
otp_store = {}

# ---------------- SCORING ---------------- #
def get_risk_assessment(score):
    if score >= 720: 
        return "APPROVED", "#27ae60", "Excellent"
    if score >= 620: 
        return "REVIEW REQUIRED", "#f1c40f", "Fair"
    return "REJECTED", "#e74c3c", "High Risk"


# ---------------- ROUTES ---------------- #
@app.route('/')
def index():
    return render_template('dashboard.html')


@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


@app.route('/analysis')
def analysis():
    return render_template('analysis.html')


@app.route('/history')
def history():
    return render_template('history.html')


@app.route('/otp')
def otp():
    return render_template('otp.html')


# ---------------- OTP ROUTES ---------------- #
@app.route('/send_otp', methods=['POST'])
def send_otp():
    data = request.get_json()
    phone = data.get('phone')
    if not phone:
        return jsonify({'error': 'Phone required'}), 400

    otp = str(random.randint(100000, 999999))
    otp_store[phone] = otp

    print(f"OTP for {phone}: {otp}")  # demo
    return jsonify({'otp': otp})


@app.route('/verify_otp', methods=['POST'])
def verify_otp():
    data = request.get_json()
    phone = data.get('phone')
    user_otp = data.get('otp')
    if otp_store.get(phone) == user_otp:
        return jsonify({'success': True})
    else:
        return jsonify({'success': False})


# ---------------- CREDIT PREDICTION ---------------- #
@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()

        name = data.get('name', 'Unknown')
        income = float(data.get('income', 0))
        age = int(data.get('age', 0))
        history = int(data.get('history_months', 0))
        debt = float(data.get('debt', 0))

        score_calc = 380 + (income * 0.0015) + (age * 0.8) + (history * 1.5) - (debt * 0.003)
        final_score = int(max(300, min(850, score_calc)))

        decision, color, status = get_risk_assessment(final_score)

        cur = mysql.connection.cursor()
        cur.execute("""
            INSERT INTO credit_applicants 
            (name, income, age, credit_history_months, debt, credit_score, decision) 
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (name, income, age, history, debt, final_score, decision))

        mysql.connection.commit()
        cur.close()

        return jsonify({
            'score': final_score,
            'decision': decision,
            'color': color,
            'status': status,
            'name': name
        })

    except Exception as e:
        print(e)
        return jsonify({'error': str(e)}), 500


@app.route('/get_history')
def get_history():
    try:
        cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cur.execute("SELECT * FROM credit_applicants ORDER BY created_at DESC")
        rows = cur.fetchall()
        cur.close()
        return jsonify(rows)
    except:
        return jsonify([])


if __name__ == '__main__':
    app.run(debug=True)
