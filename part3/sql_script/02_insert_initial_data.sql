-- Insert an admin user (hash this password in Python!)
INSERT INTO users (first_name, last_name, email, password, is_admin)
VALUES ('Admin', 'User', 'admin@example.com', '<hashed_password_here>', TRUE);

-- Insert some amenities
INSERT INTO amenities (name) VALUES ('WiFi');
INSERT INTO amenities (name) VALUES ('Parking');
INSERT INTO amenities (name) VALUES ('Pool');
