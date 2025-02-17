import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Streamlit App
st.title("Income and Interest Growth Calculator")

# User Inputs
income = st.slider("Annual Income (amount added each year)", min_value=1000, max_value=100000, value=10000, step=1000)
years = st.slider("Number of Years", min_value=1, max_value=50, value=20, step=1)
interest_rate = st.slider("Annual Interest Rate (%)", min_value=0.0, max_value=20.0, value=5.0, step=0.1)

# Calculate Growth
total_income = []
total_interest = []
cumulative_amount = 0

for year in range(1, years + 1):
    cumulative_amount += income  # Add income
    interest = cumulative_amount * (interest_rate / 100)  # Calculate interest
    cumulative_amount += interest  # Update cumulative amount
    total_income.append(income * year)
    total_interest.append(cumulative_amount - (income * year))

# Create DataFrame
df = pd.DataFrame({
    "Year": np.arange(1, years + 1),
    "Total Income Added": total_income,
    "Total Interest Earned": total_interest
})

# Plot Data
fig, ax = plt.subplots()
ax.bar(df["Year"], df["Total Income Added"], label="Total Income Added", color="blue")
ax.bar(df["Year"], df["Total Interest Earned"], bottom=df["Total Income Added"], label="Total Interest Earned", color="orange")
ax.set_xlabel("Year")
ax.set_ylabel("Amount (£)")
ax.set_title("Income and Interest Growth Over Time")
ax.legend()

# Show Chart
st.pyplot(fig)

# Display Data
st.write("### Data Table")
st.dataframe(df)
