[![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome) <img src="https://img.shields.io/badge/Python-3.8-blue"> <img src="https://img.shields.io/badge/Status-Beta-orange"> <img src="https://img.shields.io/badge/Version-1-red"> <img src="https://img.shields.io/badge/Licence-MIT-yellowgreen">

<img src = 'https://github.com/r3vskd/fig2glocate/blob/main/resources/Screenshot_1.png'></img>

:warning: This tool is only for educational purposes, use this responsibly. :warning:

## FIG2GLOCATE
This Python tool retrieves geographical information about a public IP address using the IPinfo API. It offers three main functionalities:

Generate Google Maps URL: Provides a link to Google Maps based on the IP address coordinates.
Retrieve Location Information: Displays the country, region, and city associated with the IP address.
Get Coordinates: Outputs the latitude and longitude of the IP address.
Capabilities
Public IP Validation: Ensures the input IP address is a valid public IP, avoiding private IP ranges.
Google Maps Integration: Generates a direct link to view the location on Google Maps.
Location Details: Fetches and displays detailed location information including country, region, and city.
Coordinate Extraction: Retrieves and prints the geographical coordinates of the IP address.
IPinfo API
The tool leverages the IPinfo API to gather detailed IP address data. By sending a request to IPinfo with an IP address and an API token, it retrieves a JSON response containing location-related information. This API is reliable for obtaining accurate geographic data for public IP addresses, which includes:

Country: The country where the IP address is located.
Region: The specific region within the country.
City: The city associated with the IP address.
Coordinates: Latitude and longitude of the IP address location.
This API is user-friendly and widely used for various networking and geolocation tasks, making it a valuable resource for IP address information retrieval.

## USAGE & INSTALLATION:
``` pip install -r requirements.txt ```
``` python trans_coordinates.py ```

## Donation

Loved the project? You can buy me a coffee:

<a href="https://www.buymeacoffee.com/r3vskd" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/default-orange.png" alt="Buy Me A Coffee" height="41" width="174"></a>
