from gym.envs.registration import register

register(
    id='example-v0',
    entry_point='example.envs:Example',
)