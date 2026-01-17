# 📧 Spam Mail Detection using Machine Learning

This project is a **Spam Mail Detection system** built using **Machine Learning (Logistic Regression)** and deployed using **Flask** with a clean HTML & CSS user interface.

---

## 🚀 Features

* Detects whether an email is **Spam** or **Ham (Not Spam)**
* Uses **Logistic Regression**
* Text vectorization using **TF-IDF / Count Vectorizer**
* Simple and user-friendly web interface
* Refresh button to test multiple emails

---

## 🧠 Machine Learning Model

* Algorithm: Logistic Regression
* Labels:

  * **0 → Ham (Not Spam)**
  * **1 → Spam**
* Trained on email/text data
* Model and vectorizer saved using `joblib`

---

## 🛠️ Technologies Used

* Python
* Scikit-learn
* Flask
* HTML
* CSS
* Joblib

---

## 📁 Project Structure

```
spam-mail-detection/
│
├── app.py
├── LR_Spam.pkl
├── feature_extraction.pkl
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
└── README.md
```

---

## ▶️ How to Run the Project

1. Clone the repository

```bash
git clone https://github.com/your-username/spam-mail-detection.git
```

2. Navigate to the project folder

```bash
cd spam-mail-detection
```

3. Install required libraries

```bash
pip install flask scikit-learn joblib
```

4. Run the Flask app

```bash
python app.py
```

5. Open your browser and go to:

```
http://127.0.0.1:5000/
```

---

## 🧪 Sample Test Inputs

**Spam**

```
Congratulations! You have won a free prize. Click now to claim.
```

**Ham**

```
Hi, please find the meeting agenda attached.
```
---

## 👨‍💻 Author

**Sujal Mondal**
