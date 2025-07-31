document.addEventListener('DOMContentLoaded', () => {
  const reviewForm = document.getElementById('review-form');
  const token = checkAuthentication();
  const placeId = getPlaceIdFromURL();

  if (reviewForm) {
    reviewForm.addEventListener('submit', async (event) => {
      event.preventDefault();

      const comment = document.getElementById('review-comment').value;
      const rating = document.getElementById('review-rating').value;

      try {
        const response = await submitReview(token, placeId, comment, rating);
        if (response.ok) {
          alert('Review submitted successfully!');
          reviewForm.reset();
        } else {
          const err = await response.json();
          alert('Failed to submit review: ' + (err.message || 'Unknown error'));
        }
      } catch (error) {
        console.error('Error submitting review:', error);
        alert('An unexpected error occurred.');
      }
    });
  }
});

function checkAuthentication() {
  const token = getCookie('token');
  if (!token) {
    window.location.href = 'index.html';
  }
  return token;
}

function getCookie(name) {
  const value = `; ${document.cookie}`;
  const parts = value.split(`; ${name}=`);
  if (parts.length === 2) return parts.pop().split(';').shift();
  return null;
}

function getPlaceIdFromURL() {
  const params = new URLSearchParams(window.location.search);
  return params.get('id');
}

async function submitReview(token, placeId, comment, rating) {
  return await fetch('http://127.0.0.1:5000/api/v1/reviews', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${token}`
    },
    body: JSON.stringify({
      place_id: placeId,
      comment: comment,
      rating: parseInt(rating)
    })
  });
}
