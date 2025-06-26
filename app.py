import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load your cleaned CSV file
df = pd.read_csv("cleaned_books_data.csv")

st.title("📚 Book Data Explorer")

# Show raw data
if st.checkbox("Show raw data"):
    st.write(df)

# Rating distribution
st.subheader("Rating Distribution")
fig1, ax1 = plt.subplots()
sns.countplot(data=df, x="Rating", order=df["Rating"].value_counts().index, ax=ax1)
st.pyplot(fig1)

# Price distribution
st.subheader("Price Distribution")
fig2, ax2 = plt.subplots()
sns.histplot(df["Price"], bins=10, kde=True, ax=ax2)
st.pyplot(fig2)



