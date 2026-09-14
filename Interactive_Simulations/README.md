# 🎮 Interactive Simulations & Game Physics

A space dedicated to real-time interactive physics, game-loop architecture, and graphics programming using Python.

---

## 🕹️ Classic Pong: Real-Time 2D Kinematics Engine

### 💡 Inspiration & Motivation
To truly understand how game engines and real-time graphics work under the hood, I wanted to go back to the origins of the medium and rebuild the mechanics of the game that launched the industry: **Pong (1972)**.

Driven by curiosity to explore the `pygame` library, this project was developed as a hands-on exploration of real-time event handling, frame-rate-independent physics loops, and 2D kinematics, developed through an iterative coding workflow assisted by AI tools for scaffolding and debugging.

---

## Physics & Technical Concepts Implemented

* **The Core Game Loop:** Managing the continuous sequence of **Event Polling $\rightarrow$ State Update $\rightarrow$ Screen Render** at a fixed frame rate (FPS).
* **2D Kinematics:** Discrete time-stepping position updates for moving entities:
  $$\vec{r}(t + \Delta t) = \vec{r}(t) + \vec{v}\Delta t$$
* **Elastic Collision Mechanics:** 
  * Inversion of velocity components upon impact with top/bottom boundaries ($v_y \rightarrow -v_y$).
  * Momentum reflection and response mechanics when the ball contacts the player and opponent paddles ($v_x \rightarrow -v_x$).
* **State & Score Tracking:** Bounding-box detection for scoring zones and automated ball respawn with reset velocity vectors.

---

## Tech Stack
* **Language:** Python
* **Library:** `pygame`

---

## How to Run the Game

1. **Install dependencies:**
   ```bash
   pip install pygame
