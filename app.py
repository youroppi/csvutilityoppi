import streamlit as st
import pandas as pd

# Function to fill the user-id column
def fill_user_id(df):
    df['user-id'].fillna(method='ffill', inplace=True)
    return df

# Streamlit app
st.title('User-ID Auto-fill App')

st.write("Upload a CSV file and the app will auto-fill the 'user-id' column with the appropriate values.")

# File uploader
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    # Read the uploaded file into a DataFrame
    df = pd.read_csv(uploaded_file)
    
    st.write("Original Data:")
    st.write(df.head())
    
    # Fill down the 'user-id' column
    df_filled = fill_user_id(df)
    
    st.write("Updated Data:")
    st.write(df_filled.head())
    
    # Option to download the modified CSV file
    st.download_button(
        label="Download Updated CSV",
        data=df_filled.to_csv(index=False).encode('utf-8'),
        file_name='updated_ranking_questions.csv',
        mime='text/csv',
    )
