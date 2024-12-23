# Importing necessary libraries
import streamlit as st
import math

# Title
st.title("Scientific Calculator")

# Instructions
st.write("Enter values and choose an operation to perform calculations.")

# Input fields
num1 = st.number_input("Enter the first number:", value=0.0, format="%.5f")
num2 = st.number_input("Enter the second number (if applicable):", value=0.0, format="%.5f")

# Dropdown for operations
operation = st.selectbox(
    "Choose an operation:",
    [
        "Addition (+)",
        "Subtraction (-)",
        "Multiplication (*)",
        "Division (/)",
        "Exponentiation (x^y)",
        "Square Root (√x)",
        "Logarithm (log base 10)",
        "Natural Logarithm (ln)",
        "Sine (sin)",
        "Cosine (cos)",
        "Tangent (tan)",
    ]
)

# Calculate button
if st.button("Calculate"):
    try:
        if operation == "Addition (+)":
            result = num1 + num2
            st.success(f"Result: {result}")
        elif operation == "Subtraction (-)":
            result = num1 - num2
            st.success(f"Result: {result}")
        elif operation == "Multiplication (*)":
            result = num1 * num2
            st.success(f"Result: {result}")
        elif operation == "Division (/)":
            if num2 != 0:
                result = num1 / num2
                st.success(f"Result: {result}")
            else:
                st.error("Error: Division by zero!")
        elif operation == "Exponentiation (x^y)":
            result = math.pow(num1, num2)
            st.success(f"Result: {result}")
        elif operation == "Square Root (√x)":
            if num1 >= 0:
                result = math.sqrt(num1)
                st.success(f"Result: {result}")
            else:
                st.error("Error: Square root of a negative number!")
        elif operation == "Logarithm (log base 10)":
            if num1 > 0:
                result = math.log10(num1)
                st.success(f"Result: {result}")
            else:
                st.error("Error: Logarithm of non-positive numbers is undefined!")
        elif operation == "Natural Logarithm (ln)":
            if num1 > 0:
                result = math.log(num1)
                st.success(f"Result: {result}")
            else:
                st.error("Error: Natural logarithm of non-positive numbers is undefined!")
        elif operation == "Sine (sin)":
            result = math.sin(math.radians(num1))
            st.success(f"Result: {result}")
        elif operation == "Cosine (cos)":
            result = math.cos(math.radians(num1))
            st.success(f"Result: {result}")
        elif operation == "Tangent (tan)":
            result = math.tan(math.radians(num1))
            st.success(f"Result: {result}")
        else:
            st.error("Invalid operation selected!")
    except Exception as e:
        st.error(f"An error occurred: {e}")

