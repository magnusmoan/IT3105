from agent import *

### Problem 1 ###
random_lake_agent = Random_Agent("FrozenLake-v0")
random_taxi_agent = Random_Agent("Taxi-v1")
#random_lake_agent.run_env(15,10)
#random_taxi_agent.run_env(15,10)


### Problem 2a ###
lake_agent = Lake_Agent({'s': 1.0, 'w': .5, 'n': .5, 'e': .5})
#lake_agent.run_env(20, 10)


### Problem 2b ###
greedy_lake_agent = Greedy_Lake_Agent({'s': 1.0, 'w': .5, 'n': .5, 'e': .5})
greedy_lake_agent.run_env(20,100)

