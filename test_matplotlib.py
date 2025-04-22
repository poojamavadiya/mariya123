import streamlit as st
import matplotlib
import sys

st.title("Matplotlib Test")

# Display Python and package versions
st.write("Python version:", sys.version)
st.write("Matplotlib version:", matplotlib.__version__)
st.write("Matplotlib backend:", matplotlib.get_backend())

try:
    import matplotlib.pyplot as plt
    st.success("Successfully imported matplotlib.pyplot")
    
    # Test plotting
    fig, ax = plt.subplots()
    ax.plot([1, 2, 3, 4], [1, 4, 9, 16])
    st.pyplot(fig)
except Exception as e:
    st.error(f"Error importing matplotlib.pyplot: {str(e)}") 