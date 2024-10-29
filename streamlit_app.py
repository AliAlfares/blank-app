import streamlit as st

import pandas as pd
import matplotlib.pyplot as plt

st.image('logo.png')
st.header("إدارة التدريب والتطوير - التدريب الإكلينيكي")
st.header("Dashboard coming Soon!")

st.sidebar.title("القائمة")


# Create a DataFrame
data = {
    "Date": ["2023-1"] * 8,
    "Hospital": ["KFSH", "DMC", "QHN", "MCH", "SBCC", "Erada", "DESH", "JGH"],
    "Capacity": [0, 114, 62, 14, 19, 12, 2, 10],
    "Trainee_G": [0, 67, 129, 54, 1, 8, 1, 15],
    "Trainee_P": [1, 181, 191, 68, 20, 12, 3, 25],
    "Trainees": [1, 181, 191, 68, 20, 20, 3, 25],
    "Tamheer": [None] * 8,
    "Revenue": ["SAR 1,500", "SAR 120,500", "SAR 202,800", "SAR 80,500", 
                "SAR 1,500", "SAR 7,500", "SAR 2,000", "SAR 22,900"]
}

df = pd.DataFrame(data)
df['Revenue'] = df['Revenue'].replace({'SAR ': '', ',': ''}, regex=True).astype(float)

# Streamlit app layout
st.title('Hospital Trainee Dashboard')

# Display the data
st.subheader('Data Overview')
st.dataframe(df)

# Plotting Revenue by Hospital
st.subheader('Revenue by Hospital')
plt.figure(figsize=(10, 5))
plt.bar(df['Hospital'], df['Revenue'], color='skyblue')
plt.xlabel('Hospital')
plt.ylabel('Revenue (SAR)')
plt.title('Revenue by Hospital')
st.pyplot(plt)

# Plotting Trainees by Hospital
st.subheader('Number of Trainees by Hospital')
plt.figure(figsize=(10, 5))
plt.bar(df['Hospital'], df['Trainees'], color='lightgreen')
plt.xlabel('Hospital')
plt.ylabel('Number of Trainees')
plt.title('Number of Trainees by Hospital')
st.pyplot(plt)
