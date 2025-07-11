import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

# Load cleaned data
df = pd.read_csv("HR_Analytics.csv")  # use your pre-cleaned dataset

# Title
st.title("HR Analytics Dashboard 📊")
st.markdown("Explore Attrition, Satisfaction, and Workforce Trends")

# Sidebar Filters
travel_filter = st.sidebar.selectbox("Select Business Travel Type", df['BusinessTravel'].unique())
gender_filter = st.sidebar.selectbox("Select Gender", df['Gender'].unique())

# Filtered Data
filtered = df[(df['BusinessTravel'] == travel_filter) & (df['Gender'] == gender_filter)]

# Show Data
if st.checkbox("Show Data"):
    st.write(filtered)

# Attrition by Job Satisfaction
st.subheader("Attrition by Job Satisfaction")
fig = px.histogram(filtered, x='JobSatisfaction', color='Attrition', barmode='group')
st.plotly_chart(fig)

# Attrition by Environment Satisfaction
st.subheader("Environment Satisfaction vs Attrition")
fig2 = px.box(filtered, x='Attrition', y='EnvironmentSatisfaction', color='Attrition')
st.plotly_chart(fig2)

# Age vs Attrition
st.subheader("Age Group vs Attrition")
df['AgeGroup'] = pd.cut(df['Age'], bins=[18,30,40,60], labels=['<30','30-40','40+'])
fig3 = px.histogram(df, x='AgeGroup', color='Attrition', barmode='group')
st.plotly_chart(fig3)
