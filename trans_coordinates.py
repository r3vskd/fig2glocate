import requests
from colorama import Fore, Style, init
import ipaddress

init(autoreset=True)

def get_ip_info(ip_address, api_key):
    url = f"https://ipinfo.io/{ip_address}/json?token={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error fetching data from IPinfo API: {response.status_code}")

def generate_google_maps_url(latitude, longitude):
    return f"https://www.google.com/maps?q={latitude},{longitude}"

def is_public_ip(ip):
    # Funfion para convertir el valor string en formato IPv4 valido
    ip_addr = ipaddress.ip_address(ip)
    
    # Definiendo los rangos de direcciones ip
    private_ranges = [
        ipaddress.ip_network('10.0.0.0/8'),
        ipaddress.ip_network('172.16.0.0/12'),
        ipaddress.ip_network('192.168.0.0/16')
    ]
    
    # Checar si la direccion ip esta en alguno de los rangos de direcciones privadas
    for private_range in private_ranges:
        if ip_addr in private_range:
            return False
    return True

def main():
    ip_address = input("Ingresa la direccion ip: ")
    if is_public_ip(ip_address):
        print(f"{ip_address} is a valid ip address")
    else:
        print(f"{ip_address} is not a public IP address, Please enter a valid public ip address.")
        
    api_key = '0b402b1742cfb1' ###################### Aqui vas tu api key que debes crear en https://ipinfo.io/ ##########################

    try:
        ip_info = get_ip_info(ip_address, api_key)
        location = ip_info.get('loc')
        if location:
            latitude, longitude = location.split(',')
            google_maps_url = generate_google_maps_url(latitude, longitude)
            print(Fore.GREEN +"En ciudades y areas densamente pobladas, la precision de las coordenadas puede verse algo afectada, en un radio de 3 a 20 km como maximo."+ Style.RESET_ALL)
            print(f"Google Maps URL: {google_maps_url}") 
        else:
            print("Location information not available for this IP address.")
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()
