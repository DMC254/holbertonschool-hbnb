document.addEventListener('DOMContentLoaded', () => {
  const loginForm = document.querySelector('.login-form');
  if (loginForm) {
    loginForm.addEventListener('submit', async (event) => {
      event.preventDefault();

      const email = document.getElementById('email').value;
      const password = document.getElementById('password').value;

      try {
        const response = await fetch('http://127.0.0.1:5000/api/v1/login', {
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
          alert('Login failed: ' + (errorData.message || response.statusText));
        }
      } catch (error) {
        console.error('Error during login:', error);
        alert('An unexpected error occurred.');
      }
    });
  }

  const placesList = document.getElementById('places-list');
  if (placesList) {
    checkAuthentication();

    const priceFilter = document.getElementById('price-filter');
    if (priceFilter) {
      priceFilter.addEventListener('change', filterPlacesByPrice);
    }
  }
});


function getCookie(name) {
  const value = `; ${document.cookie}`;
  const parts = value.split(`; ${name}=`);
  if (parts.length === 2) return parts.pop().split(';').shift();
  return null;
}

function checkAuthentication() {
  const token = getCookie('token');
  const loginLink = document.getElementById('login-link');

  if (!token) {
    if (loginLink) loginLink.style.display = 'block';
  } else {
    if (loginLink) loginLink.style.display = 'none';
    fetchPlaces(token);
  }
}

let allPlaces = [];

async function fetchPlaces(token) {
  try {
    const response = await fetch('http://127.0.0.1:5000/api/v1/places', {
      method: 'GET',
      headers: {
        'Authorization': `Bearer ${token}`
      }
    });

    if (!response.ok) throw new Error('Failed to fetch places');

    const data = await response.json();
    allPlaces = data;
    displayPlaces(data);
  } catch (error) {
    console.error(error);
    alert('Unable to load places. Please try again.');
  }
}

function displayPlaces(places) {
  const placesList = document.getElementById('places-list');
  placesList.innerHTML = '';

  places.forEach(place => {
    const card = document.createElement('div');
    card.className = 'place-card';
    card.dataset.price = place.price_per_night;

    card.innerHTML = `
      <h3>${place.name}</h3>
      <p>$${place.price_per_night} per night</p>
      <button class="details-button" onclick="window.location.href='place.html?id=${place.id}'">View Details</button>
    `;

    placesList.appendChild(card);
  });
}

function filterPlacesByPrice() {
  const selected = document.getElementById('price-filter').value;
  const placesList = document.getElementById('places-list').children;

  for (let card of placesList) {
    const price = parseFloat(card.dataset.price);
    if (selected === 'all' || price <= parseFloat(selected)) {
      card.style.display = 'block';
    } else {
      card.style.display = 'none';
    }
  }
}
