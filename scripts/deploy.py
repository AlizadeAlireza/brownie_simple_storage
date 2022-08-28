from brownie import accounts, config, SimpleStorage, network


def deploye_simple_storage():
    # account = accounts[0]  # first in 10 fake accounts
    account = get_account()
    # account = accounts.load("alireza-account")
    # account = accounts.add(os.getenv("PRIVATE_KEY"))
    # account = accounts.add(config["wallets"]["from_key"])
    simple_storage = SimpleStorage.deploy({"from": account})
    stored_value = simple_storage.retrieve()
    print(stored_value)
    transaction = simple_storage.store(15, {"from": account})
    transaction.wait(1)  # how many block we want to wait
    # update
    update_stored_value = simple_storage.retrieve()
    print(update_stored_value)


def get_account():
    if (
        network.show_active() == "development"
    ):  # network another key word that brownie actually has
        return accounts[0]
    else:
        # we're going to pull directly from our config
        return accounts.add(config["wallets"]["from_key"])


def main():
    deploye_simple_storage()
