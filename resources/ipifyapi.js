document.addEventListener('DOMContentLoaded', (event) => {
    const ipDisplay = document.getElementById('ip-address');

    fetch('https://api.ipify.org?format=json')
        .then(response => response.json())
        .then(data => {
            ipDisplay.textContent = `Your IP Address is: ${data.ip}`;
        })
        .catch(error => {
            ipDisplay.textContent = 'Could not retrieve IP address';
            console.error('Error fetching IP address:', error);
        });
});
