-- Step 1: Set the password policy to low temporarily
SET GLOBAL validate_password.policy=LOW;
SET GLOBAL validate_password.length=4;

-- Step 2: Create the database if it does not exist
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Step 3: Create the user if it does not exist
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Step 4: Grant all privileges on the database hbnb_dev_db to the user hbnb_dev
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

-- Step 5: Grant SELECT privilege on the database performance_schema to the user hbnb_dev
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';

-- Step 6: Apply changes
FLUSH PRIVILEGES;
