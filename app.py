import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Streamlit App with Libraries")

# Contoh penggunaan pandas
df = pd.DataFrame({
    'x': [1, 2, 3, 4],
    'y': [10, 20, 30, 40]
})
st.write(df)

# Contoh penggunaan matplotlib
fig, ax = plt.subplots()
ax.plot(df['x'], df['y'])
st.pyplot(fig)
