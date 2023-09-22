from telnetlib import IP
from flask import Flask
import ipcode

app = Flask(__name__) #app instance reference
@app.route("/")
def hello_world():
    result = ipcode.getIP()
    if not result["found_vpn_pool"]:
        return f'ip address {result["vpn_pool_ip"]} was not found in a known VPN pool.' + f' The Hostname {result["vpn_info"]} was not found in known VPN pool.'

    return f'vpn pool address: {result["vpn_pool_ip"]}' + f'\neip nat pool address: {result["eit_nat_pool_ip"]}' + f'\nnmnet nat pool address: {result["nmnet_nat_pool_ip"]}'  

if __name__ == "__main__":
    app.run(debug=True, port=3000) #makes flask run
