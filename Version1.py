from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException


# Node is credentials
rpc_user = "username"
rpc_password = "password"

# Connection Node tan
rpc_connection = AuthServiceProxy("http://%s:%s@127.0.0.1:8332" % (rpc_user, rpc_password))

# es sheqmnis yveala axal userze axal address-s
get_new_address = rpc_connection.getnewaddress()
