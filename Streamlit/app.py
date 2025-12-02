# Import Streamlit
import numpy as np
import pandas as pd
import streamlit as st

# Check Streamlit version
st.__version__

# Basic Streamlit App Example

st.write("Hello, Streamlit!")

# Explanation:
# - import streamlit as st: Imports the Streamlit library.
# - st.write(): Displays text, data, or other objects in the app.

# Text and Markdown Examples

st.title("Streamlit App Title")
st.header("This is a header")
st.subheader("This is a subheader")
st.text("This is fixed-width text.")
st.markdown("**This text is bold using Markdown!**")

# Explanation:
# - Use st.title(), st.header(), st.subheader() for headings.
# - st.text() for plain text, st.markdown() for formatted text.

# Interactive Widgets Example
age = st.slider('Select your age', 0, 100, 25)
st.write(f'Your age: {age}')

if st.button('Say hello'):
    st.write('Hello!')

option = st.selectbox('Choose a color', ['Red', 'Green', 'Blue'])
st.write(f'You selected: {option}')

color = st.color_picker("Pick A Color", "#00f900")
st.write("The current color is", color)

sentiment_mapping = ["one", "two", "three", "four", "five"]
selected = st.feedback("stars")
if selected is not None:
    st.markdown(f"You selected {sentiment_mapping[selected]} star(s).")

df = pd.DataFrame(
    [
        {"command": "st.selectbox", "rating": 4, "is_widget": True},
        {"command": "st.balloons", "rating": 5, "is_widget": False},
        {"command": "st.time_input", "rating": 3, "is_widget": True},
    ]
)
edited_df = st.data_editor(df)

favorite_command = edited_df.loc[edited_df["rating"].idxmax()]["command"]
st.markdown(f"Your favorite command is **{favorite_command}**")
# Explanation:
# - st.slider() returns the selected value.
# - st.button() triggers an action when clicked.
# - st.selectbox() returns the selected option.

# DataFrames and Charts Example

data = pd.DataFrame({
    'A': np.random.randn(10),
    'B': np.random.randn(10)
})

st.dataframe(data)
st.line_chart(data['A'])
st.bar_chart(data['B'])

# Explanation:
# - st.dataframe() displays a DataFrame as an interactive table.
# - st.line_chart() and st.bar_chart() plot columns of data.
