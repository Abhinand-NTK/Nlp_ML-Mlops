import streamlit as st
import pandas as pd
import numpy as np

#Title
st.title("Hello stream lit")

# display a simple test

st.write("This is the example of the Simple test")

# Create a simple dataframe

df = pd.DataFrame({
    'first_column':[1,2,3,4,5],
    'second_column':[10,20,30,40,50]
})

# Display Dataframe

st.write("Here is teh dataframe")
st.write(df)

# Create a linechart
chart_data = pd.DataFrame(
    np.random.randn(20,3),columns=['a','b','c']
)
st.line_chart(chart_data)