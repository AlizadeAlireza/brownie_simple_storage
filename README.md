# brownie_simple_storage
this is https://github.com/AlizadeAlireza/Simple_Storage_web3.py and exactly worked like this,
but this time i'm work with brownie framework and writing tests for it.


don't want deploy a new contract every single time maybe we want to work with a contract that we've already deployed.
what if we want to work with a whole of bunch of different chains?
what if we want to work kovan, mainnet or ...
this is where brownie is going to come into  play

brownie : is currently the most popular smart contract development platform built base on python
brownie heavily relies on web3.py
install brownie via pipx
pipx install brownie in virtual environment and mekes it available directly from the command line 

after installing brownie: brownie init --force 

build directiory --> import low level information
interfaces --> it's going to track any interfaces that we're working with or deploying  
deployments --> across all of the different chains so we no longer have to manage that ourselves
and it's going to store all the compiled code from json

	--------- 	---------	--------	----------

contracts directory(outside of build dir) ---> we're going to put all of our contracts 

interfaces dir --- > is where we can save and store defferent interfaces 

reports dir --> are to save any type of report you run scripts or we can 

we can compile our code without compiler 


1 ) adding first brownie contract (simple storage . sol)
1,1 ) $brownie compile -----> build/contracs ---> create compile file 

	--------- 	---------	--------	----------
	
2 ) Deploy Script
2,1 ) new file in the scripts dir
# brownie defaults to always working with a local ganache cli

2,2) put all the logic of our deployment in its own function

	--------- 	---------	--------	----------

3 ) getting your address and privatekey into brownie

3,1 ) brownie has an account packages that actually natively understands how to work with accounts 

3,2 ) built-in local ganache accounts ----> account = accounts[0];print(account)

another way to add your account is use the commandline ---> brownie accounts new <name> --> alirez-account and then enter your p.k to it
see accounts ---> brownie accounts list 

3,3 ) we can work with our account in .py
account = accounts.load("account name")

	--------- 	---------	--------	----------

4) often time mix of working with the local ganache 
enviroment variable & brownie config

4,1 ) create .env file and ....

4,2) we can tell brownie to always pull from our env file a brownie-config.yaml
and write in dotenv: .env
this is telling brownie when you run scripts grab the enviroment variable from 
.env file

4,3 ) we can actually add more information that what wallets we want to use 
and when we want to use them
wallet:
	from_key: ${PRIVATE_KEY}
import config beside accounts 

automatically get transformed into the enviroment.

4,4 ) import our contract from brownie
SimpleStorage.deploy()
we always need to do a from and then say who to be deploying from

	--------- 	---------	--------	----------

5 ) recreating our web3.py script in browine ---> retrieve and 15 number
now we want to do this in brownie

5,1 ) stored_value = simple_storage.retrieve()

5,2 ) transaction = simple_storage.store(15)

but in brownie we always have to add who we're going to transact from
in our case going to do from account
and wait for a transaction to finish 
# it is just like befor deploy.py so it is in the brownie

	--------- 	---------	--------	----------

6 ) testing 
a way to actually automate that our contracts are doing what we want to do
we don't want to always have to manually check that all of our stuff is doing what
remix and solidity have tests too but is better in the python and brownie
create a file in tests dir and be sure it starts with "test"

6,1 ) testing in anything separated into three categories 

1. arrange
2. act
3. assert

and in the end we need to run ---> $brownie test
green dot means the test passed 

6,2) updating test with 5

6,3 ) when we have many func test
when we want test one func we need to write in commandline
---> $brownie test -k <func_name> ---> test_updating_storage

with -s if we have any print lines it would print the lines.

	--------- 	---------	--------	----------

7 ) deploy to a Testnet

7,1 ) brownie networks list
rpc url / http provider in brownie

dev networks are temporary but eth network can be tracked by brwonie

7,2 ) in .env --> WEB3_ INFURA_PROJECT_ID= ...

7,3 ) for deploying in test net
----> brownie run scripts/deploy.py --network <name> like kovan

7,4 ) get account function

if we're working on a development chain we'll use account zero
and if not we'll use the method that pulls from our config

* network is another keyword that allow us to contanct to another networks
deployments contract in ---> so you can always go back and say hmm where i did
i deploy that or what happend with that deployment

----> we can actually interact with contracts we've already deployed onto chain 
so let's go ahead and even add a new file in here called read value and read from 
a contract that we've already deployed we did this in web3.py with abi and address
----> do exact same way with the browni ----> in read value 

	--------- 	---------	--------	----------
	
8 ) readValue() --> is going to read directly from the rinkeby blockchain and it's going to read from 
a contract that we've already deployed 

	--------- 	---------	--------	----------

9 ) brownie console ---> $brownie console
if i run simple storage give me --> []
brownie console is python shell with all of our smart contract features already natively integrated 
