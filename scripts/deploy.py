from brownie import accounts, config, SimpleStorage, network


def deploye_simple_storage():
    # account = accounts[0]  # first in 10 fake accounts
    account = get_account()
    # account = accounts.load("alireza-account")
    # account = accounts.add(os.getenv("PRIVATE_KEY"))
    # account = accounts.add(config["wallets"]["from_key"]) ---> use in get account function

    # default transactin

    # deploy contract
    simple_storage = SimpleStorage.deploy({"from": account})
    # with view function we don't have to add from account
    stored_value = simple_storage.retrieve()
    print("it's the default value: ", stored_value)

    # store function transaction

    # deploy contract
    storing_num = int(input("enter your number for storing in favorite number: "))
    transaction = simple_storage.store(storing_num, {"from": account})
    # how many block we want to wait
    transaction.wait(1)
    # update and call the retrieve function again
    updated_stored_value = simple_storage.retrieve()
    print("update stored value: ", updated_stored_value)

    # add person transaction
    print("add person transaction")

    name = input("enter your name: ")
    number = int(input("enter your number: "))

    add_transaction = simple_storage.addPerson(name, number)
    add_transaction.wait(1)
    print(
        f"your entry value: {simple_storage.people(0)},\n\n tracing by mapping with the name of {name} the number is: {simple_storage.nameToFavoriteNumber(name)}\n\n"
    )


def get_account():
    """
    if we're working on a development chain we'll use account zero.
    and if not we'll use the method that pulls from our config.
    """
    if (
        network.show_active() == "development"
    ):  # network another key word that brownie actually has
        return accounts[0]
    else:
        # we're going to pull directly from our config
        return accounts.add(config["wallets"]["from_key"])


def main():
    deploye_simple_storage()
