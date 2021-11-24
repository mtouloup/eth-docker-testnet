 
# Generating Traffic in the Network (Python Implementation)
The scripts in this repository are responsible to generate traffic, meaning generating and submitting transactions within our Geth private network.

## Prerequisites
In order to run the traffic generator you need to have installed Python3, Pip3 and Git on your system.    
Moreover, you need to define the Host IP and Port of the Geth RPC node in the ```config.ini``` file.    

## Run it for the first time

```git clone https://github.com/mtouloup/eth-docker-testnet.git```    
```cd geth-traffic-gen```    
```pip3 install -r requirements.txt```    
```python3 main.py <number_of_transactions>```    

This command will generate 1 new wallet account and will send 0xE8D4A51000 ETH with each transaction.    
The amount of ETH is in hexadecimal format and if converted to Decimal equals to 1000000000000 WEI --> 0.000001 ETH    

The amount of ETH that are tranfered while generating transactions are covered by the Genesis account which is created during the deployment of our GETH private network.    
Also, this account is configured to gain all rewards when a new block is mined.    
