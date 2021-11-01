import yaml

with open('/subscribili/env.yml', 'r') as efile:
    _env = yaml.safe_load(efile)


def read_env(cfg=_env):
    return cfg
