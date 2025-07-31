document.addEventListener('DOMContentLoaded', () => {
    const loginForm = document.querySelector('.login-form');

    if (loginForm) {
      loginForm.addEventListener('submit', async (envent) => {
        envent.preventDefault();

        const email = document.getElementById('email').value;
        const password = document.getElementById('password').value;

        try {
            const response = await fetch('http://127.0.0.1:5000', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ email, password })
            });

            if (response.ok) {
                const data = await response.json();
                document.cookie = `token=${data.token}; path=/`;
                window.location.href = 'index.html';
            } else {
                const errorData = await response.json();
                alert('Login failed: ' + ( errorData.message || response.statusText));
            }
        } catch (error) {
            console.error('Error during login:', error);
            alert('An unexpected error occurred.');
        }
      });
    }
});
