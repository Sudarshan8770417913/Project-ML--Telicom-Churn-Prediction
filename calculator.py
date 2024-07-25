import streamlit as st

# Set page title
st.set_page_config(page_title="Calculator")

# Title
st.title("Create a Calculator By Using Streamlit")

# Input fields for numbers
num1 = st.number_input("Enter the first number:")
num2 = st.number_input("Enter the second number:")

# Select operation
operation = st.selectbox(
    "Select an operation",
    ("Addition", "Subtraction", "Multiplication", "Division")
)

# Perform selected operation
if st.button("Calculate"):
    if operation == "Addition":
        result = num1 + num2
        st.success(f"The result of {num1} + {num2} is {result}")
    elif operation == "Subtraction":
        result = num1 - num2
        st.success(f"The result of {num1} - {num2} is {result}")
    elif operation == "Multiplication":
        result = num1 * num2
        st.success(f"The result of {num1} * {num2} is {result}")
    elif operation == "Division":
        if num2 != 0:
            result = num1 / num2
            st.success(f"The result of {num1} / {num2} is {result}")
        else:
            st.error("Division by zero is not allowed")
