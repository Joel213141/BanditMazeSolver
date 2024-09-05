# Multi-Arm Bandit and Maze Solver

This project implements a multi-arm bandit problem and explores action selection (exploration/exploitation) to solve a maze using reinforcement learning and Q-learning.

## Project Overview

### Multi-Arm Bandit Problem
- **Objective:** Identify the optimal arm among three options after 1000 trials using an epsilon-greedy strategy.
- **Approach:** The agent uses the Q-learning update rule to estimate the value of each arm and balances exploration and exploitation based on the epsilon parameter.

### Maze Solver
- **Objective:** Train an agent to solve a 5x5 maze using Q-learning.
- **Environment:** Utilizes Gym’s `gym-maze` environment.
- **Approach:** The agent learns the optimal policy by updating a Q-table based on the rewards received from the environment.

## Requirements

Ensure you have Python 3 installed. Install the dependencies using:

```bash
pip install -r requirements.txt
