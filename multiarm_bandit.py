{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "f7c9e48d-2f08-464f-b0bd-fe60aff90fd6",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Final Q-values: [[0.89636952 0.7652429  0.90001889]]\n",
      "Number of times each arm was selected: [[ 58.  32. 910.]]\n",
      "Best arm is arm number: 3\n"
     ]
    }
   ],
   "source": [
    "# multiarm_bandit.py\n",
    "\n",
    "import numpy as np\n",
    "\n",
    "# Define the 'pull_arm' function\n",
    "def pull_arm(a, N):\n",
    "    if a == 0:\n",
    "        r = np.random.normal(0.9, 0.1)\n",
    "        N[0][0] += 1\n",
    "    elif a == 1:\n",
    "        r = np.random.normal(0.8, 0.1)\n",
    "        N[0][1] += 1\n",
    "    elif a == 2:\n",
    "        r = np.random.normal(0.9, 0.01)\n",
    "        N[0][2] += 1\n",
    "    return N, r\n",
    "\n",
    "def main():\n",
    "    N_trials = 1000\n",
    "    n_arms = 3  # 3 arms\n",
    "    epsilon = 0.1  # Exploration parameter\n",
    "    Q = np.zeros((1, n_arms))  # Initialize Q table\n",
    "    N = np.zeros((1, n_arms))  # Initialize count\n",
    "\n",
    "    for i in range(N_trials):\n",
    "        if np.random.random() < epsilon:\n",
    "            a = np.random.randint(n_arms)  # Explore\n",
    "        else:\n",
    "            a = np.argmax(Q[0])  # Exploit\n",
    "\n",
    "        N, R = pull_arm(a, N)  # Pull the arm\n",
    "\n",
    "        # Update the Q table\n",
    "        Q[0][a] = Q[0][a] + (1 / N[0][a]) * (R - Q[0][a])\n",
    "\n",
    "    print(\"Final Q-values:\", Q)\n",
    "    print(\"Number of times each arm was selected:\", N)\n",
    "    print(\"Best arm is arm number:\", np.argmax(Q[0]) + 1)\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    main()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8bfcea1a-64e5-4652-9db0-7da96bc4640d",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
