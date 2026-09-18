# 1D Wave Propagation Simulator (NetLogo)

This project is an interactive, agent-based simulation of wave propagation in a 1D elastic medium, developed using **NetLogo**. 

As part of my exploration into multi-agent environments, I took an open-source foundational code for agent physics and heavily modified it to create a visualizer for driven harmonic oscillators. Instead of traditional array iterations, this model uses "turtles" acting as coupled oscillators that transfer energy to their neighbors, simulating a physical string.

![Wave Simulation Demo](./wave_demo.gif) *(Note: Upload a gif and uncomment this line!)*

## ⚙️ How it Works
* **The Driver:** A central agent (green) acts as the driver, oscillating according to a sine function: `y = amplitude * sin(frequency * time)`.
* **The Medium:** The rest of the agents (white) act as a coupled elastic medium. They calculate their vertical velocity based on the height difference with their immediate left and right neighbors, applying a damping/friction factor.

## 🎛️ Interesting Parameter Configurations

By tweaking the GUI sliders, the system can reach different steady states and resonance patterns. Here are some interesting configurations to try:

* **Standard String Vibration:**
  * `friction`: 38
  * `frequency`: 15
  * `amplitude`: 9

* **Rhomboid / Triangular Wave Pattern:**
  * `friction`: 12
  * `frequency`: 4
  * `amplitude`: 15

* **Bimodal / Cardioid Pattern (The "Peach" Wave):**
  * `friction`: 31
  * `frequency`: 19
  * `amplitude`: 8
  *(A curious resonance state where the wave visually resembles a cardioid shape).*

## Running the Simulation
1. Download and install [NetLogo](https://ccl.northwestern.edu/netlogo/).
2. Open `coupled_oscillators_wave.nlogo`.
3. Click `setup`, then `go`.
4. Adjust the sliders in real-time to observe phase changes and damping effects.
