def geth_comm(session=None, method=None, params=None):
    headers = {'Content-type': 'application/json'}

    payload= {
                "jsonrpc":"2.0",
                "method":method,
                "params":params,
                "id":4
            }
    
    response = session.post('http://10.10.70.21:8545', json=payload, headers=headers)
      
    return response.json()




