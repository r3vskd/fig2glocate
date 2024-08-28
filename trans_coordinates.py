import requests
from colorama import Fore, Style, init
import ipaddress

init(autoreset=True)

def display_banner():
    print(Fore.RED + '''   
███████╗██╗ ██████╗ ██████╗  ██████╗ ██╗      ██████╗  ██████╗ █████╗ ████████╗███████╗
██╔════╝██║██╔════╝ ╚════██╗██╔════╝ ██║     ██╔═══██╗██╔════╝██╔══██╗╚══██╔══╝██╔════╝
█████╗  ██║██║  ███╗ █████╔╝██║  ███╗██║     ██║   ██║██║     ███████║   ██║   █████╗  
██╔══╝  ██║██║   ██║██╔═══╝ ██║   ██║██║     ██║   ██║██║     ██╔══██║   ██║   ██╔══╝  
██║     ██║╚██████╔╝███████╗╚██████╔╝███████╗╚██████╔╝╚██████╗██║  ██║   ██║   ███████╗
╚═╝     ╚═╝ ╚═════╝ ╚══════╝ ╚═════╝ ╚══════╝ ╚═════╝  ╚═════╝╚═╝  ╚═╝   ╚═╝   ╚══════╝                                                                      
 Author: r3vskd                
 Warning: It was created for educational purposes. Please don't misuse it for illegal activities. 
          ''' + Style.RESET_ALL)

##################################aqui va tu api key que debes crear en https://ipinfo.io/ ##########################
api_key = 'your_api_key'

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
    # Convertir a formato ipv4 las direcciones ip para que lo entienda la API
    ip_addr = ipaddress.ip_address(ip)
    
    # Define private IP ranges
    private_ranges = [
        ipaddress.ip_network('10.0.0.0/8'),
        ipaddress.ip_network('172.16.0.0/12'),
        ipaddress.ip_network('192.168.0.0/16')
    ]
    
    # Checar si la direccion ip esta en algunos de los rangos de direcciones privadas
    for private_range in private_ranges:
        if ip_addr in private_range:
            return False
    return True

def main():
    print(Fore.GREEN + '''
           [01] ===> Retrieve the google maps url from a public IP address
           [02] ===> Retrieve the country/province/city from a public IP address 
           [03] ===> Retrieve the coordinates from a public IP address
           [04] ===> Exit
           ''' + Style.RESET_ALL)
    
    option = input(Fore.GREEN + '''Select an option: ''' + Style.RESET_ALL)
    
    if option == '1' or option == '2' or option == '3': # validacion de respuestas en el menu de opciones
        ip_address = input(Fore.GREEN + '''Enter a public IP address: ''' + Style.RESET_ALL)
        if not is_public_ip(ip_address):
            print(f"{ip_address} isn't a valid public IP address. Please enter a valid public IP address.")
            return
    
        try:
            ip_info = get_ip_info(ip_address, api_key) # variable para usar la ip que se ingrese asi como la api key posteriormente
            if option == '1':
                location = ip_info.get('loc')
                if location:
                    latitude, longitude = location.split(',') # generar variables para signar las coordenadas
                    google_maps_url = generate_google_maps_url(latitude, longitude) # crear variable para alojar las variables de las coordenadas dentro de la url de google maps
                    print(Fore.GREEN + "En ciudades y áreas densamente pobladas, la precisión de las coordenadas puede verse algo afectada, en un radio de 3 a 20 km como máximo." + Style.RESET_ALL)
                    print(f"Google Maps URL: {google_maps_url}")  # mostrando en pantalla la url final
                else:
                    print("Location information not available for this IP address.")
            elif option == '2':
                print(f"Country: {ip_info.get('country')}, Region: {ip_info.get('region')}, City: {ip_info.get('city')}") # mostrando en pantalla la informacion a cerca de la ubicacion de la direccion ip solicitada
            elif option == '3':
                location = ip_info.get('loc')
                if location:
                    print(f"Coordinates: {location}") # mostrando en pantalla las coordenadas en un radio aproximado de las direccion ip solicitada
                else:
                    print("Location information not available for this IP address.")
        except Exception as e:
            print(str(e))
    elif option == '4': 
        print("Exiting...")
    else:
        print("Error: Invalid option. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    display_banner()
    main()
