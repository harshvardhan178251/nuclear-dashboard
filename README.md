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
2. Create and Activate a Virtual Environment
Bash

# Create the environment
python -m venv venv

# Activate on Windows
.\venv\Scripts\activate

# Activate on macOS/Linux
source venv/bin/activate
3. Install Dependencies
Install all required libraries from the requirements.txt file.

Bash

pip install -r requirements.txt
4. Prepare the Data
(You only need to do this step once)

This script creates the sensor_data.csv file used by the dashboard.

Bash

python generate_data.py
(Note for Week 2+: You would also add python train_model.py here to train the AI).

5. Run the Dashboard
Bash

python app.py
The dashboard will now be running at: https://www.google.com/search?q=http://127.0.0.1:8050/

📊 Data Source
The AI model for RUL prediction was trained using the NASA C-MAPSS Turbofan Jet Engine Data Set.
