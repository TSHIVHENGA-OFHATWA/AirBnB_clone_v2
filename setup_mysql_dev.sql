-- Step 1: Create the database if it does not exist
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Step 2: Create the user if it does not exist
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Step 3: Grant all privileges on the database hbnb_dev_db to the user hbnb_dev
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

-- Step 4: Grant SELECT privilege on the database performance_schema to the user hbnb_dev
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';

-- Step 5: Apply changes
FLUSH PRIVILEGES;
