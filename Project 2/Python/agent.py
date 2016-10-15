from random import random
import gym
import operator

class Agent(object):
    def __init__(self, env_name):
        self.env = gym.make(env_name)
        self.action_space = self.env.action_space
        self.observation_space = self.env.observation_space

    def select_action(self, position):
        raise NotImplementedError

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

    def run_env_with_learning(self, ep_len, ep_count, debug=False):
        env = self.env
        total_reward = 0
        reward_list = []
        #env.monitor.start('/tmp/FrozenLake_test0', force=True)

        for episode in xrange(ep_count):
            print episode
            position = env.reset()
            #env.render()
            for _ in xrange(ep_len):
                action = self.select_action(position, debug)
                new_position, reward, done, info = env.step(action)
                self.update_q(position, action, new_position, reward)
                #env.render()
                position = new_position
                total_reward += reward

                if done:
                    break
            
            reward_per_episode = float(total_reward) / float(ep_count)
            reward_list.append(reward_per_episode)

        #env.monitor.close()
        #gym.upload('/tmp/FrozenLake_test0', api_key='sk_FqhrkckbSkKZ5ScFyoZ7JQ')
        return self.q, reward_list


class Lake_Agent(Agent):
    def __init__(self, q=None, learning_rate=0, eps=0, discount_rate=0):
        self.env = gym.make("FrozenLake-v0")
        self.action_space = self.env.action_space
        self.observation_space = self.env.observation_space

        self.learning_rate = learning_rate
        self.eps = eps
        self.discount_rate = discount_rate

        if q == None:
            self.q = [{'s': 0, 'w': 0, 'e': 0, 'n': 0} for _ in xrange(16)]
        else:
            self.q = q

        self.action_dict = {'s': 1, 'w': 0, 'e': 2, 'n': 3}


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

    
    def update_q(self, old_position, action, new_position, reward):
        curr_q_dict = self.q[old_position]
        action_dir = (list((self.action_dict).keys())[list((self.action_dict).values()).index(action)])
        neighbor_dict = self.q[new_position]
        best_neighbor_q = max(neighbor_dict.itervalues())

        added_value = self.learning_rate * (reward + self.discount_rate * best_neighbor_q - curr_q_dict[action_dir])
        curr_q_dict[action_dir] += added_value


class Greedy_Lake_Agent(Lake_Agent):
    def select_action(self, position, debug=False):
        direction = max((self.q[position]).iteritems(), key=operator.itemgetter(1))[0]
        p_rand = random()
        if p_rand < self.eps:
            action = self.action_space.sample()
        else:
            action = self.action_dict[direction]
        """
        if debug:
            print self.q[position]
            print direction
            print action
            raw_input()
        """
        return action

class Random_Agent(Agent):
    def select_action(self, position):
        return self.action_space.sample()

