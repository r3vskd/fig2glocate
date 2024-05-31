from flask import Flask, request
from pyngrok import ngrok
import requests
import ipaddress

app = Flask(__name__)

def get_public_ip():
    
    try:
        response = requests.get("https://api.ipify.org?format=json")
        response.raise_for_status()
        ip_data = response.json()
        return ip_data['ip']
    except requests.RequestException as e:
        print(f"Error retrieving public IP address: {e}")
        return "Error retrieving public IP address"

@app.route('/')
def log_ip():
    user_ip = request.remote_addr
    
    try:
        
        public_ip = get_public_ip()
        ipv4_ip = ipaddress.ip_address(public_ip)
        if ipv4_ip.version == 4:
            print(f"Visitor public IP address (IPv4): {ipv4_ip}")
            return f"Your public IP address (IPv4) is: {ipv4_ip}"
        else:
            return "No IPv4 address found."
    except ValueError as e:
        print(f"Error converting to IPv4: {e}")
        return "Error converting IP address."

if __name__ == '__main__':
    
    public_url = ngrok.connect(5000)
    print(f"ngrok http --domain=enabled-daily-garfish.ngrok-free.app 80")
    
    app.run(port=5000)