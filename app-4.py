import streamlit as st
import xgboost as xgb
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image

# Load the trained model with error handling
try:
    model = xgb.Booster()
    model.load_model("final_model.json")
    expected_features = model.feature_names
except Exception as e:
    st.error(f"Error loading model: {e}")
    st.stop()

# Define the prediction function
def predict(data):
    # Ensure input data has all required features
    for col in expected_features:
        if col not in data.columns:
            data[col] = 0  # Add missing features with default values

    # Align input features with the model
    dmatrix = xgb.DMatrix(data[expected_features])
    predictions = model.predict(dmatrix)
    return ["Pickup" if pred >= 0.5 else "No Pickup" for pred in predictions]

# Configure Streamlit page layout
st.set_page_config(
    page_title="Food Hamper Pickup Prediction",
    page_icon="🎯",
    layout="wide"
)

# Create tabs for pages
tab1, tab2, tab3, tab4, tab5 = st.tabs(["Prediction", "Visualization", "Looker Studio", "XAI", "ChatBot🤖"])

# ----------------------------------------
# Tab 1: Prediction
# ----------------------------------------
with tab1:
    st.title("Food Hamper Pickup Prediction 🎯")
    st.write("Predict whether clients will pick up their food hampers based on distance.")

    # Load dataset for unique IDs and distances
    try:
        final_df = pd.read_csv("final_df.csv")  # Replace with your dataset
        unique_ids_df = final_df[["unique_client_id", "distance_km"]].drop_duplicates()
    except Exception as e:
        st.error(f"Error loading dataset: {e}")
        st.stop()

    # Distance slider to filter unique IDs
    max_distance = unique_ids_df["distance_km"].max()
    distance_threshold = st.slider(
        "Filter by Distance (km)", min_value=0.0, max_value=max_distance, value=5.0, step=0.1
    )

    # Filter dataset based on slider value
    filtered_df = unique_ids_df[unique_ids_df["distance_km"] <= distance_threshold]

    if not filtered_df.empty:
        # Predict for the filtered dataset
        try:
            input_data = filtered_df.copy()
            input_data["distance_km"] = filtered_df["distance_km"]  # Ensure required column exists
            predictions = predict(input_data)
            filtered_df["Prediction"] = predictions

            st.subheader("Prediction Results:")
            st.write(filtered_df)
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("No clients found within the selected distance.")

# ----------------------------------------
# Tab 2: Visualization
# ----------------------------------------
with tab2:
    st.title("Data Visualizations 📊")
    st.write("Explore the relationships in your dataset with interactive visualizations.")

    # Feature to plot
    feature = st.selectbox(
        "Select Feature to Visualize",
        ["age", "dependents_qty", "distance_km", "quarter_period"]
    )

    # Visualization
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.histplot(data=final_df, x=feature, kde=True, bins=20, ax=ax)
    ax.set_title(f"Distribution of {feature.capitalize()}")

    st.pyplot(fig)

# ----------------------------------------
# Tab 3: Looker Studio
# ----------------------------------------
with tab3:
    st.title("Looker Studio Dashboard Integration 🔗")
    st.write("View the dashboard for detailed insights directly below:")

    # Embed Looker Studio dashboard
    st.components.v1.html(
        """
        <iframe
            src="https://lookerstudio.google.com/embed/reporting/194825f4-ef9b-40ad-8c84-f92de0fcf3c0/page/2KjKE"
            width="100%" height="800" style="border: none;">
        </iframe>
        """,
        height=800,
    )

# ----------------------------------------
# Tab 4: XAI (Explainable AI)
# ----------------------------------------
with tab4:
    st.title("Explainable AI (XAI) 📸")
    st.write("Preloaded visualizations explaining your model's decisions:")

    # Display pre-uploaded images
    image_files = ["Unknown-13.png", "Unknown-14.png", "Unknown-15.png"]
    for image_file in image_files:
        try:
            image = Image.open(image_file)
            st.image(image, caption=image_file, use_column_width=True)
        except FileNotFoundError:
            st.warning(f"Image {image_file} not found. Ensure it's uploaded to the project directory.")

# ----------------------------------------
# Tab 5: Chatbot
# ----------------------------------------
with tab5:
    st.title("Client Information Chatbot 🤖")
    st.write("Select a client ID to get details about the client.")

    # Client ID dropdown
    unique_ids = final_df["unique_client_id"].unique()
    selected_client_id = st.selectbox("Select Client ID", unique_ids)

    # Display details for the selected client
    client_details = final_df[final_df["unique_client_id"] == selected_client_id]

    if not client_details.empty:
        st.subheader("Client Details:")
        st.write(client_details)

        # Chatbot input
        user_query = st.text_input("Ask a question about this client:")

        if user_query:
            # Basic chatbot responses
            if "age" in user_query.lower():
                st.write(f"Age: {client_details['age'].values[0]}")
            elif "dependents" in user_query.lower():
                st.write(f"Number of Dependents: {client_details['dependents_qty'].values[0]}")
            elif "distance" in user_query.lower():
                st.write(f"Distance (km): {client_details['distance_km'].values[0]}")
            elif "status" in user_query.lower():
                st.write(f"Status: {client_details['status'].values[0]}")
            else:
                st.write("Sorry, I don't understand your query. Please ask about age, dependents, distance, or status.")
    else:
        st.warning("No details found for the selected client ID.")