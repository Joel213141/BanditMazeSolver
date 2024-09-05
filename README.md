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
```

### Running the Project
Clone this repository:
```bash
git clone https://github.com/your-username/MultiarmBanditMaze.git
```
Navigate to the project directory:
```bash
cd MultiarmBanditMaze
```
Install the required packages:
```bash
pip install -r requirements.txt
```
Running the Multi-Arm Bandit Simulation
Execute the multiarm_bandit.py script:

```bash
python multiarm_bandit.py
```
Running the Maze Solver
Execute the maze_solver.py script:

```bash
python maze_solver.py
```
Note: The maze solver will display the maze in the console. Ensure your terminal or IDE supports rendering.

Expected Output
Multi-Arm Bandit
The script will output the final Q-values for each arm, the number of times each arm was selected, and identify the best arm.

Maze Solver
Training Phase: The script will print the total reward after every 100 episodes.
Testing Phase: The agent will attempt to solve the maze using the learned Q-table, rendering each step.
