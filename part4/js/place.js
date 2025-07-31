document.addEventListener('DOMContentLoaded', () => {
  const placeId = getPlaceIdFromURL();
  const token = getCookie('token');

  checkAuthentication(token);
  fetchPlaceDetails(token, placeId);
});

// Extract ?id= from URL
function getPlaceIdFromURL() {
  const params = new URLSearchParams(window.location.search);
  return params.get('id');
}

// Get cookie value
function getCookie(name) {
  const value = `; ${document.cookie}`;
  const parts = value.split(`; ${name}=`);
  if (parts.length === 2) return parts.pop().split(';').shift();
  return null;
}

// Check token and show/hide review form
function checkAuthentication(token) {
  const reviewSection = document.getElementById('add-review');
  const loginLink = document.getElementById('login-link');

  if (!token) {
    reviewSection.style.display = 'none';
    loginLink.style.display = 'block';
  } else {
    reviewSection.style.display = 'block';
    loginLink.style.display = 'none';
  }
}

// Fetch place details from API
async function fetchPlaceDetails(token, placeId) {
  try {
    const response = await fetch(`http://127.0.0.1:5000/api/v1/places/${placeId}`, {
      method: 'GET',
      headers: {
        'Authorization': token ? `Bearer ${token}` : ''
      }
    });

    if (!response.ok) throw new Error('Failed to fetch place details');

    const place = await response.json();
    displayPlaceDetails(place);
  } catch (err) {
    console.error(err);
    alert('Error loading place details.');
  }
}

// Inject data into DOM
function displayPlaceDetails(place) {
  const details = document.getElementById('place-details');
  const reviews = document.getElementById('reviews');

  details.innerHTML = `
    <div class="place-info">
      <h2>${place.name}</h2>
      <p><strong>Host:</strong> ${place.host}</p>
      <p><strong>Price:</strong> $${place.price_per_night}</p>
      <p><strong>Description:</strong> ${place.description}</p>
      <p><strong>Amenities:</strong> ${place.amenities.join(', ')}</p>
    </div>
  `;

  reviews.innerHTML = '<h3>Reviews:</h3>';
  if (place.reviews && place.reviews.length > 0) {
    place.reviews.forEach((r) => {
      const reviewCard = document.createElement('div');
      reviewCard.classList.add('review-card');
      reviewCard.innerHTML = `
        <p><strong>${r.user}:</strong> ${r.comment}</p>
        <p>Rating: ${r.rating}/5</p>
      `;
      reviews.appendChild(reviewCard);
    });
  } else {
    reviews.innerHTML += '<p>No reviews yet.</p>';
  }
}
