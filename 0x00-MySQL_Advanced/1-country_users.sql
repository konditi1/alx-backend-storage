-- script that creates a table users with an attribute country
CREATE TABLE IF NOT EXISTS users (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(256),
    country ENUM('US', 'CO', 'TN') NOT NULL DEFAULT 'US'
    );
    