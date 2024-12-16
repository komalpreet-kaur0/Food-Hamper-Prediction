### Food Hamper Pickup Prediction App

---

## Project Overview

The **Food Hamper Pickup Prediction App** is an interactive Streamlit-based web application that predicts whether clients will pick up their food hampers based on various factors such as distance from the distribution center. It also provides visualizations, a Looker Studio dashboard integration, Explainable AI insights, and a chatbot for client-specific information.

---

## Features

1. **Prediction Module**: 
   - Predict whether clients will pick up their food hampers using a pre-trained XGBoost model.
   - Filter predictions by distance thresholds.

2. **Data Visualization**:
   - Interactive plots for analyzing dataset features.
   - Histogram visualizations of key metrics like age, number of dependents, and distance.

3. **Looker Studio Dashboard**:
   - Embedded dashboard for detailed insights.

4. **Explainable AI (XAI)**:
   - Preloaded visualizations explaining the model's predictions.

5. **Client Information Chatbot**:
   - Query specific details about clients, such as age, dependents, distance, and status.

---

## Prerequisites

### Software Requirements
- Python 3.8+
- Streamlit 1.2+
- XGBoost
- Pandas
- Matplotlib
- Seaborn
- Pillow

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/food-hamper-app.git
   cd food-hamper-app
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Ensure the following files are in the project directory:
   - `final_model.json`: Pre-trained XGBoost model.
   - `final_df.csv`: Dataset with client information.
   - Preloaded XAI images: `Unknown-13.png`, `Unknown-14.png`, `Unknown-15.png`.

---

## Running the App

1. Start the application:
   ```bash
   streamlit run app.py
   ```

2. Open your browser and navigate to `http://localhost:8501`.

---

## Application Tabs

### 1. **Prediction**
   - Upload a dataset (`final_df.csv`).
   - Adjust the distance slider to filter predictions.
   - View results with predicted pickup statuses.

### 2. **Visualization**
   - Select dataset features for analysis.
   - View histograms and distributions for features like `age`, `dependents_qty`, and `distance_km`.

### 3. **Looker Studio Dashboard**
   - Embedded iframe to explore additional insights via the Looker Studio dashboard.

### 4. **XAI (Explainable AI)**
   - Displays model decision explanations through preloaded visualizations.

### 5. **Chatbot**
   - Select a client ID to retrieve client details.
   - Query specific client information (e.g., age, dependents, status).

---

## Files in the Repository

1. **Code Files**:
   - `app.py`: Main Streamlit application script.
   - `requirements.txt`: List of Python dependencies.

2. **Model**:
   - `final_model.json`: Pre-trained XGBoost model.

3. **Dataset**:
   - `final_df.csv`: Client information dataset.

4. **Assets**:
   - Preloaded XAI visualizations: `Unknown-13.png`, `Unknown-14.png`, `Unknown-15.png`.

---

## Customization

- **Model**: Replace `final_model.json` with a different XGBoost model if needed. Ensure the features in your dataset match the model's expected features.
- **Dataset**: Modify `final_df.csv` as required. The dataset must include columns for `unique_client_id`, `distance_km`, and any features required by the model.
- **XAI Visualizations**: Update image files with new explanations if the model is retrained.

---

## Troubleshooting

1. **Model Loading Errors**:
   - Ensure `final_model.json` is in the project directory.
   - Check that the model's expected features match the dataset.

2. **Dataset Errors**:
   - Verify `final_df.csv` exists and contains the required columns.

3. **Image Not Found**:
   - Ensure the preloaded XAI images are in the project directory.

---

## Credits

Developed by **Komalpreet_Kaur** and team for predicting food hamper pickup behavior. 

For queries, contact: `kkaur44@gmail.com`.
