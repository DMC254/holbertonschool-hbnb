from .user_routes import api as user_api
from .amenity_routes import api as amenity_api
from .health_routes import api as health_api
from .place_routes import api as place_api
from .review_routes import api as review_api  # <--- Add this

namespaces = [user_api, amenity_api, health_api, place_api, review_api]
