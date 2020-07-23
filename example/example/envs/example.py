import gym
from gym import error, spaces, utils
from gym.utils import seeding


class Example(gym.Env):
    """Custom Environment that follows gym interface"""
    metadata = { 'render.modes': ['human'] }

    def __init__(self):
        # Define action and observation space
        # They must be gym.spaces objects
        ...
        print('init Example')
        raise NotImplementedError
    
    def step(self, action):
        """Run one timestep of the environment's dynamics. When end of
        episode is reached, you are responsible for calling `reset()`
        to reset this environment's state."""
        ...
        print('step')
        raise NotImplementedError
        #return observation, reward, done, info
    
    def reset(self):
        """Resets the state of the environment and returns an initial observation."""
        ...
        print('reset')
        raise NotImplementedError
        #return observation  # reward, done, info can't be included

    def render(self, mode='human'):
        """Renders the environment.
        Args:
            mode (str): the mode to render with"""
        ...
        print('render')
        raise NotImplementedError

    def close(self):
        """Override close in your subclass to perform any necessary cleanup."""
        ...
        print('close')
        raise NotImplementedError