from agent import *
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

### Parameters ###
episode_count = 15000
episode_length = 100
q = {'s': 1.0, 'w': .5, 'n': .5, 'e': .5} 
lake_actions = {'w': 0, 's': 1, 'e': 2, 'n': 3}
taxi_actions = {'w': 3, 's': 0, 'e': 2, 'n': 1, 'd': 5, 'p': 4}
eps = .01
learning_rate = .25
discount_rate = .99

### Helper method ###
def exp_func(x, a, b, c):
    return a*np.exp(-b*x)+c

while True:
    task = raw_input('Enter exercise number (1, 2a, 2b, 2c, 3, 7): ')
    
    ### Problem 1 ###
    if task == '1':
        random_lake_agent = Random_Agent("FrozenLake-v0")
        random_taxi_agent = Random_Agent("Taxi-v1")
        random_lake_agent.run_env(episode_length, 1000)
        raw_input("Press any key to run taxi")
        random_taxi_agent.run_env(20, 100)
    
    
    ### Problem 2a ###
    elif task == '2a':
        lake_agent = Agent("FrozenLake-v0", q=q, actions=lake_actions)
        lake_agent.run_env(episode_length, 1000)
    
    
    ### Problem 2b ###
    elif task == '2b':
        greedy_lake_agent = Greedy_Agent("FrozenLake-v0", q=q, actions=lake_actions)
        greedy_lake_agent.run_env(episode_length, 1000)
    
    
    ### Problem 2c ###
    elif task == '2c':
        greedy_lake_agent = Greedy_Agent("FrozenLake-v0", q=q, actions=lake_actions, eps=.1)
        greedy_lake_agent.run_env(episode_length, 1000)
    
    
    ### Problem 3 ###
    elif task == '3':
        q = {'w': 0, 's': 0, 'e': 0, 'n': 0}
        lake_agent = Greedy_Agent("FrozenLake-v0", q=q, actions=lake_actions, 
                learning_rate=learning_rate, eps=eps, discount_rate=discount_rate)
        q, rewards = lake_agent.run_env_with_learning(episode_length, 
                episode_count)
        plt.plot([i for i in range(1, episode_count+1)], rewards, lw=2)
        plt.axis([0, episode_count+1, -0.1, 1.1])
        plt.xlabel("Episode number")
        plt.ylabel("Episode reward")
        plt.title("Epsiode reward against episode")
        plt.show()
    
    ### Problem 4 ###
    elif task == '4':
        q = {'w': 0, 's': 0, 'e': 0, 'n': 0}
        lake_agent = Greedy_Agent("FrozenLake-v0", q=q, actions=lake_actions, 
                learning_rate=.2, eps=.1, discount_rate=discount_rate)
        q, rewards = lake_agent.run_env_with_learning(episode_length, 
                episode_count, choose_max_neighbor=False)
        plt.plot([i for i in range(1, episode_count+1)], rewards)
        plt.axis([0, episode_count+1, 0, 1])
        plt.show()
    
    ### Problem 7 ###
    elif task == '7':
        episode_count = 1500
        episode_length = 50
        q = {'w': 0, 's': 0, 'e': 0, 'n': 0, 'd': 0, 'p': 0}
        lake_agent = Greedy_Agent("Taxi-v1", q=q, actions=taxi_actions, 
                learning_rate=learning_rate, eps=0.1, discount_rate=discount_rate)
        q, rewards = lake_agent.run_env_with_learning(episode_length, 
                episode_count, choose_max_neighbor=False)
        
        
        x_values = np.array([i for i in range(1, episode_count+1)])
        rewards = np.array(rewards)
        
        popt, pcov = curve_fit(exp_func, x_values, rewards, p0=(1, 1e-6, 1))
        plt.plot(x_values, rewards, 'o', color=(0.9,0.9,0.9))
        plt.plot(x_values, exp_func(x_values, *popt), color='r', lw=3)
        plt.axis([0, episode_count+1, -300, 20])
        plt.xlabel('Episode number')
        plt.ylabel('Episode reward')
        plt.title('Episode reward against episode number\n')
        plt.show()
    
    elif task == 'exit' or task == 'quit' or len(task) == 0:
        break

    else:
        print("Invalid exercise number")
    print("\n --------------- \n")
