-- Find the admin user
SELECT * FROM users WHERE is_admin = TRUE;

-- Add a place
INSERT INTO places (name, description, price, owner_id)
VALUES ('Cozy Cabin', 'A nice cabin in the woods', 150.00, 1);

-- Link an amenity
INSERT INTO place_amenity (place_id, amenity_id) VALUES (1, 1);

-- Verify join
SELECT places.name, amenities.name
FROM places
JOIN place_amenity ON places.id = place_amenity.place_id
JOIN amenities ON amenities.id = place_amenity.amenity_id;
