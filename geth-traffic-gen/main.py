import execute_tx as tx
import requests
import time
import sys

def main(n=None):
    # create persistent HTTP connection
    session = requests.Session()
    
    # Get the primary account
    primary_acc_method = 'eth_accounts'
    primary_acc_params = []
    primary_account=tx.geth_comm(session,primary_acc_method,primary_acc_params)['result'][0]
    print("Primary Account: " + primary_account)

    # Generate  a new account to transfer ETH to
    new_acc_method = 'personal_newAccount'
    new_acc_params = ["5uper53cr3t"]
    new_account=tx.geth_comm(session,new_acc_method,new_acc_params)['result']
    print("Newly Generated Account: " + new_account)

    # Unlock our primary account
    unlock_acc_method = 'personal_unlockAccount'
    unlock_acc_params = [primary_account, "iff_super_pass"]
    unlock_acc_resp=tx.geth_comm(session,unlock_acc_method,unlock_acc_params)['result']
    print("Primary Account Unlocked: " + str((unlock_acc_resp)))

    # Make transaction
    make_tx_method = 'eth_sendTransaction'
    make_tx_payload = {
                        "from": primary_account,
                        "to": new_account,
                        "value": "0xE8D4A51000"
                    }
    make_tx_params = [make_tx_payload]
    print("Making Transactions....")
    i=0
    # starting time
    start = time.time()
    while i < 10:
        tx_response=tx.geth_comm(session,make_tx_method,make_tx_params)['result']
        i=i+1
        print(tx_response)
    end = time.time()

    print(f"Finished in {end - start}")
    
if __name__ == "__main__":
    n = int(sys.argv[1])
    main(n)