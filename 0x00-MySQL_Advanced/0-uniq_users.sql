-- script that creates a table users
CREATE TABLE IF NOT EXISTS users (
    id INT UNIQUE NOT NULL AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(256)
    
    );
    