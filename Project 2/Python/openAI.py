from agent import *
import matplotlib.pyplot as plt

### Parameters ###
episode_count = 100
episode_length = 100
q = {'s': 1.0, 'w': .5, 'n': .5, 'e': .5} 
lake_actions = {'w': 0, 's': 1, 'e': 2, 'n': 3}
eps = .01
learning_rate = .2
discount_rate = .99

### Problem 1 ###
#random_lake_agent = Random_Agent("FrozenLake-v0")
#random_taxi_agent = Random_Agent("Taxi-v1")
#random_lake_agent.run_env(episode_length, episode_count)
#random_taxi_agent.run_env(episode_length, episode_count)


### Problem 2a ###
#lake_agent = Agent("FrozenLake-v0", q=q, actions=lake_actions)
#lake_agent.run_env(episode_length, episode_count)


### Problem 2b ###
#greedy_lake_agent = Lake_Agent(q=q)
#greedy_lake_agent.run_env(episode_length, episode_count)


### Problem 2c ###
#greedy_lake_agent = Lake_Agent(q=q, eps=.1)
#greedy_lake_agent.run_env(episode_length, episode_count)


### Problem 3 ###
#lake_agent = Lake_Agent(learning_rate=learning_rate, eps=eps, discount_rate=discount_rate)
#q, rewards, last_reward = lake_agent.run_env_with_learning(episode_length, episode_count)
#print q
#print rewards[-1]
#improved_agent = Lake_Agent(q=q, learning_rate=learning_rate, eps=0, discount_rate=discount_rate)
#_, rewards = improved_agent.run_env_with_learning(1000, 100, True)
#print last_reward
#plt.plot([i for i in range(1, episode_count+1)], rewards)
#plt.axis([0, episode_count+1, 0, 1])
#plt.show()
