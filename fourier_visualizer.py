import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

# --- Streamlit UI setup ---
st.set_page_config(page_title="Fourier Series Visualizer", layout="wide")
st.title("Interactive Fourier Series Visualizer")
st.markdown("Explore how complex waveforms can be built from simple sine waves using Fourier Series.")

# --- User Inputs ---
signal_type = st.selectbox(
    "Choose a signal type:",
    ["Square Wave", "Triangle Wave", "Sawtooth Wave"]
)
num_harmonics = st.slider("Number of Harmonics:", 1, 50, 10)

# --- Define time axis ---
t = np.linspace(0, 2*np.pi, 1000)

# --- Generate original signal ---
if signal_type == "Square Wave":
    original = np.sign(np.sin(t))
elif signal_type == "Triangle Wave":
    original = 2*np.arcsin(np.sin(t)) / np.pi
elif signal_type == "Sawtooth Wave":
    original = 2*(t/ (2*np.pi)) - 1
    original = 2*(original - np.floor(0.5 + original))

# --- Fourier Series Approximation ---
reconstructed = np.zeros_like(t)

if signal_type == "Square Wave":
    for n in range(1, num_harmonics*2, 2):
        reconstructed += (4/np.pi)*(np.sin(n*t)/n)

elif signal_type == "Triangle Wave":
    for n in range(1, num_harmonics*2, 2):
        reconstructed += (8/(np.pi**2)) * ((-1)**((n-1)//2) / (n**2)) * np.sin(n*t)

elif signal_type == "Sawtooth Wave":
    for n in range(1, num_harmonics + 1):
        reconstructed += (-2/np.pi) * ((-1)**n / n) * np.sin(n*t)

# --- Plot Results ---
fig, ax = plt.subplots(2, 1, figsize=(10, 6))

ax[0].plot(t, original, 'k', label="Original Signal", linewidth=2)
ax[0].set_title("Original Signal")
ax[0].grid(True)
ax[0].set_ylim(-1.5, 1.5)

ax[1].plot(t, reconstructed, 'r', label="Reconstructed Signal", linewidth=2)
ax[1].set_title(f"Reconstructed Signal with {num_harmonics} Harmonics")
ax[1].grid(True)
ax[1].set_ylim(-1.5, 1.5)

st.pyplot(fig)

st.markdown("""
### 📘 How It Works
- The Fourier series expresses a periodic signal as a sum of sine waves of different frequencies and amplitudes.
- Increasing the number of harmonics improves the accuracy of reconstruction.

Project Made By:
- Aditya Mohan (202310101030002)

""")
