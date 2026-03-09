INSERT INTO User (id, first_name, last_name, email, password, is_admin)
VALUES (
    '36c9050e-ddd3-4c3b-9731-9f487208bbc1',
    'Admin',
    'HBnB',
    'admin@hbnb.io',
    '$2b$12$izmWKHa56KHJfLxBXhj6R.znnnyy10Crqm.URRuVfRwSe6xsfVlb6',
    TRUE
);

INSERT INTO Amenity (id, name) VALUES
    ('90c50757-a3e2-4a14-a744-1b4b59cbfa15', 'WiFi'),
    ('ed5cd7ba-c1a6-4f07-8d62-68eab173b6e0', 'Piscine'),
    ('d8870ea5-67cf-4cbf-bd99-940ed7d568f9', 'Climatisation');
