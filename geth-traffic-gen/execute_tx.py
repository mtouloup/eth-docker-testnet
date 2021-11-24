import os
import configparser


def geth_comm(session=None, method=None, params=None):
    path_current_directory = os.path.dirname(__file__)
    path_config_file = os.path.join(path_current_directory, 'config.ini')
    config = configparser.ConfigParser()
    config.read(path_config_file)

    host = config['GETH_TESTNET']['geth_host']
    port = config['GETH_TESTNET']['geth_port']

    
    headers = {'Content-type': 'application/json'}

    payload= {
                "jsonrpc":"2.0",
                "method":method,
                "params":params,
                "id":4
            }
    
    response = session.post('http://'+host+':'+port, json=payload, headers=headers)
      
    return response.json()




