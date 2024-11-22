import streamlit as st

# DELTA to STAR function
def DELTA_STAR(R12, R23, R31):
    total_resistance = R12 + R23 + R31
    R1 = (R12 * R13) / total_resistance
    R2 = (R12 * R23) / total_resistance
    R3 = (R23 * R31) / total_resistance
    return R1, R2, R3

# Title of the app
st.title("2305A21L22-PS5")

# Input fields for Delta resistances
st.header("Input Delta Resistances")
R13 = st.number_input("R12 (Ohms)", min_value=0.0, value=100.0)
R23 = st.number_input("R23 (Ohms)", min_value=0.0, value=100.0)
R31 = st.number_input("R31 (Ohms)", min_value=0.0, value=100.0)

# Compute STAR resistances
if st.button("Compute"):
    R1, R2, R3 = DELTA_STAR(R13, R23, R31)
    st.header("STAR Resistances")
    st.write(f"R1 = {R1:.2f} Ohms")
    st.write(f"R2 = {R2:.2f} Ohms")
    st.write(f"R3 = {R3:.2f} Ohms")