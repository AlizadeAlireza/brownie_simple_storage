from brownie import SimpleStorage, accounts, config


def read_contract():
    # print(SimpleStorage[0])  # this object work seems an array
    simple_storage = SimpleStorage[-1]  # 0 index give us the first deployment
    # ABI
    # ADDRESS
    print(simple_storage.retrieve())


def main():
    read_contract()
