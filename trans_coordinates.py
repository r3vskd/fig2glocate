import requests
from colorama import Fore, Style, init

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

def main():
    ip_address = '189.172.4.36'
    api_key = '0b402b1742cfb1'

    try:
        ip_info = get_ip_info(ip_address, api_key)
        location = ip_info.get('loc')
        if location:
            latitude, longitude = location.split(',')
            google_maps_url = generate_google_maps_url(latitude, longitude)
            print(Fore.GREEN +"Urban Areas: In cities and densely populated areas, the precision can be quite high, often within a few kilometers (3-20 km). This is because IP blocks are often allocated more granularly in these areas."+ Style.RESET_ALL)
            print(f"Google Maps URL: {google_maps_url}")
        else:
            print("Location information not available for this IP address.")
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()
