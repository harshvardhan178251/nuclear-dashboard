# nuclear-dashboard
A predictive maintenance dashboard for nuclear plant safety using AI/ML and sensor data.
# ☢️ Nuclear Plant Predictive Maintenance Dashboard

This project is a predictive maintenance (PdM) dashboard for monitoring the health of nuclear plant components. It uses Python, Plotly Dash, and a machine learning model (LSTM) trained on the NASA Turbofan dataset to predict the Remaining Useful Life (RUL) of critical assets.

<img width="2874" height="676" alt="image" src="https://github.com/user-attachments/assets/d0d007f2-ae2e-410a-b3fa-4bda204b2dd0" />
screen shot

---

## 🛠️ Tech Stack

* **Python**: Core programming language.
* **Plotly Dash**: For the interactive web dashboard.
* **Dash Bootstrap Components**: For professional styling and layout.
* **Dash DAQ**: For the real-time gauges.
* **Pandas**: For data manipulation.
* **TensorFlow / Keras**: For building and running the LSTM (RUL prediction) model.
* **Scikit-learn**: For data scaling and preprocessing.
* **Numpy**: For numerical operations.

---

## ✨ Features

* **Real-time KPI Cards**: A high-level overview of plant status.
* **Interactive Controls**: Dropdown to select and analyze individual components.
* **Live Gauges**: Visual display of real-time temperature and pressure.
* **Historical Data Graphs**: Time-series charts for vibration and pressure trends.
* **AI-Driven Predictions**: A (simulated or real) prediction for component Remaining Useful Life (RUL).

---

## 🚀 How to Run This Project

Follow these steps to run the dashboard on your local machine.

### 1. Clone the Repository
```bash
git clone [https://github.com/harshvardhan178251/nuclear-dashboard.git](https://github.com/harshvardhan178251/nuclear-dashboard.git)
cd nuclear-dashboard
