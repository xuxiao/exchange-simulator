#!/usr/bin/python3
import os
import json

import yaml


class Token:

    def __init__(self, token, address, decimals):
        self.token = token
        self.address = address
        self.decimals = decimals

    def __str__(self):
        return self.token

    def __repr__(self):
        return self.token


def get_int(hex_str):
    return int(hex_str, 16)


MODE = os.environ.get('KYBER_ENV', 'dev')
this_dir, this_filename = os.path.split(__file__)
env_file = os.path.join(this_dir, 'env.yaml')
with open(env_file, 'r') as f:
    env = yaml.load(f)
    DEPOSIT_DELAY = env[MODE]['deposit_delay']
    BLOCKCHAIN_URL = env[MODE]['blockchain_url']

    with open(env[MODE]['addresses'], 'r') as f:
        cfg = json.loads(f.read())
        LIQUI_ADDRESS = get_int(cfg['exchanges']['liqui'])
        BANK_ADDRESS = get_int(cfg['bank'])
        SUPPORTED_TOKENS = {}
        for name, token in cfg['tokens'].items():
            SUPPORTED_TOKENS[name.lower()] = Token(
                name.lower(), get_int(token['address']), token['decimals'])

LOGGER_NAME = "simulator"

EXCHANGE_NAME = "liqui"

DEFAULT_API_KEY = "s7kwmscu-u6myvpjh-47evo234-y2uxw61t-raxby17f"
