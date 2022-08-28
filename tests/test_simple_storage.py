from brownie import SimpleStorage, accounts


def test_deploy():
    # arrange
    account = accounts[0]  # we can actually make contracts
    # act
    simple_storage = SimpleStorage.deploy({"from": account})  # deploy
    starting_value = simple_storage.retrieve()  # call and see start value
    expected = 0
    # assert
    assert starting_value == expected


def test_update_storage():
    # arrange
    account = accounts[0]
    # in this one arranging is also going to be deploying our smart contract
    simple_storage = SimpleStorage.deploy({"from": account})
    # act
    expected = 15
    simple_storage.store(
        expected, {"from": account}
    )  # we want to store 15 in our contract
    # assert
    assert expected == simple_storage.retrieve()
