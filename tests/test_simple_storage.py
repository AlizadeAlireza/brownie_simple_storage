from brownie import SimpleStorage, accounts


def test_deploy():
    """
    in this section we want to get default value and see
    is it equal to 0 or not?!
    """
    # arrange
    account = accounts[0]

    # act
    simple_storage = SimpleStorage.deploy({"from": account})

    # expected to be zero
    starting_value = simple_storage.retrieve()
    expected = 0
    assert starting_value == expected


def test_updating_storage():
    """
    in this section we want to set a value and see
    is it equal to expected number or not?!
    """
    # arrange
    account = accounts[0]

    # act
    simple_storage = SimpleStorage.deploy({"from": account})

    # expected to be the given number
    expected = 5
    simple_storage.store(expected, {"from": account})

    # assert
    assert simple_storage.retrieve() == expected


def test_add_person():
    """
    in this section we want to set a value and owner of the value
    and see is the owner name equal to the owner number or not?!
    """
    # arrange
    account = accounts[0]

    # act
    simple_storage = SimpleStorage.deploy({"from": account})

    expected_number = 15
    simple_storage.addPerson("alireza", expected_number)

    # assert
    assert simple_storage.nameToFavoriteNumber("alireza") == expected_number
