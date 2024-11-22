import streamlit as st

# DELTA_STAR function as defined above
def DELTA_STAR(R12, R23, R31):
    R1 = (R12 * R31) / (R12 + R23 + R31)
    R2 = (R12 * R23) / (R12 + R23 + R31)
    R3 = (R31 * R23) / (R12 + R23 + R31)
    
    return R1, R2, R3

# Streamlit UI elements
st.title('DELTA to STAR Resistance Calculator')

# Get user input for DELTA resistances (R12, R23, R31)
R12 = st.number_input('Enter Resistance R12 (Ohms)', min_value=0.0, step=0.1)
R23 = st.number_input('Enter Resistance R23 (Ohms)', min_value=0.0, step=0.1)
R31 = st.number_input('Enter Resistance R31 (Ohms)', min_value=0.0, step=0.1)

# When the user clicks the button, calculate the STAR resistances
if st.button('Calculate STAR Resistances'):
    if R12 > 0 and R23 > 0 and R31 > 0:
        # Get STAR resistances
        R1, R2, R3 = DELTA_STAR(R12, R23, R31)
        
        # Convert to kiloohms
        R1_kΩ = R1 / 1000
        R2_kΩ = R2 / 1000
        R3_kΩ = R3 / 1000
        
        st.subheader('Calculated STAR Resistances (in Kiloohms):')
        st.write(f'R1 = {R1_kΩ:.3f} kΩ')
        st.write(f'R2 = {R2_kΩ:.3f} kΩ')
        st.write(f'R3 = {R3_kΩ:.3f} kΩ')
    else:
        st.error("Please enter valid positive resistance values for R12, R23, and R31.")