from random import random
import gym
import operator
from copy import copy

class Agent(object):
    def __init__(self, env_name, q=None, actions=None, learning_rate=0, eps=0, discount_rate=0):
        self.env = gym.make(env_name)
        self.action_space = self.env.action_space
        self.observation_space = self.env.observation_space

        self.learning_rate = learning_rate
        self.eps = eps
        self.discount_rate = discount_rate

        self.q = [copy(q) for _ in range(self.observation_space.n)]
        self.action_dict = actions


    def run_env(self, ep_len, ep_count):
        env = self.env
        total_reward = 0

        for episode in xrange(ep_count):
            print "Starting episode #", episode
            observation = env.reset()
            env.render()
            for _ in xrange(ep_len):
                action = self.select_action(observation)
                observation, reward, done, _ = env.step(action)
                env.render()
                total_reward += reward

                if done:
                    break

        print "Average reward: ", float(total_reward) / float(ep_count) 

    def run_env_with_learning(self, ep_len, ep_count, debug=False, choose_max_neighbor=True):
        env = self.env
        total_reward = 0
        reward_list = []
        delta = (self.eps - 0.005) / float(ep_count)
        env.monitor.start('/tmp/FrozenLake_test0', force=True)

        for episode in xrange(ep_count):
            print episode
            position = env.reset()
            #env.render()
            action = self.select_action(position, debug)
            for _ in xrange(ep_len):
                new_position, reward, done, info = env.step(action)
                next_action = self.select_action(new_position, debug)

                if choose_max_neighbor:
                    self.update_q(position, action, new_position, reward)
                else:
                    self.update_q(position, action, new_position, reward, next_action)
                
                action = next_action
                position = new_position
                total_reward += reward

                if done:
                    break
            
            #reward_list.append(total_reward / float(episode+1))

            ### Uncomment for taxi ###
            reward_list.append(total_reward) 
            print total_reward
            total_reward = 0
            
            self.eps -= delta

        env.monitor.close()
        #gym.upload('/tmp/FrozenLake_test0', api_key='sk_FqhrkckbSkKZ5ScFyoZ7JQ')
        return self.q, reward_list


    def select_action(self, position):
        curr_q_dict = self.q[position]
        q_sum = sum(curr_q_dict.itervalues())

        p_south = curr_q_dict['s'] / q_sum
        p_west = (curr_q_dict['w'] / q_sum) + p_south
        p_east = (curr_q_dict['e'] / q_sum) + p_west
        p_north = (curr_q_dict['n'] / q_sum) + p_east

        p_rand = random() 
        if p_rand <= p_south: return self.action_dict['s']
        if p_rand <= p_west: return self.action_dict['w']
        if p_rand <= p_east: return self.action_dict['e']
        if p_rand <= p_north: return self.action_dict['n']


    def update_q(self, old_position, action, new_position, reward, next_action=None):
        curr_q_dict = self.q[old_position]
        action_dir = (list((self.action_dict).keys())[list((self.action_dict).values()).index(action)])
        neighbor_dict = self.q[new_position]

        if next_action == None:
            neighbor_q = max(neighbor_dict.itervalues())
        else:
            next_action_dir = (list((self.action_dict).keys())[list((self.action_dict).values()).index(next_action)])
            neighbor_q = neighbor_dict[next_action_dir]

        added_value = self.learning_rate * (reward + self.discount_rate * neighbor_q - curr_q_dict[action_dir])
        curr_q_dict[action_dir] += added_value


class Greedy_Agent(Agent):
    def select_action(self, position, debug=False):
        direction = max((self.q[position]).iteritems(), key=operator.itemgetter(1))[0]
        p_rand = random()
        if p_rand < self.eps:
            return self.action_space.sample()
        else:
            return self.action_dict[direction]



class Random_Agent(Agent):
    def select_action(self, position):
        return self.action_space.sample()

