
import streamlit as st

import pickle
# Provide the full paths to the files
pipeline_path = 'C:/Users/HP/Desktop/Data Science Capstone Project/car_price_pipeline.pkl'
model_path = 'C:/Users/HP/Desktop/Data Science Capstone Project/car_price_model.pkl'

# Load the pipeline
with open(pipeline_path, 'rb') as file:
    pipeline = pickle.load(file)

print("Pipeline loaded successfully.")

# Load the model
with open(model_path, 'rb') as model_file:
    model = pickle.load(model_file)


example_features = {
    'year': 2018,
    'km_driven': 25000,
    'fuel': 'Diesel',
    'seller_type': 'Dealer',
    'transmission': 'Manual',
    'owner': 'First Owner'
}

# Predict button
if st.button("Predict Selling Price"):
    # Create a DataFrame from user input
    input_data = pd.DataFrame(
        [[year, km_driven, fuel, seller_type, transmission, owner]],
        columns=['year', 'km_driven', 'fuel', 'seller_type', 'transmission', 'owner']
    )
    
    # Use the pipeline to predict
    prediction = pipeline.predict(input_data)
    
    # Display the predicted price
    st.success(f"Predicted Selling Price: ₹{prediction[0]:,.2f}")


