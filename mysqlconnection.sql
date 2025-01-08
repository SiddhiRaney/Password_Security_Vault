SELECT * FROM hints;
SELECT * FROM passwords;
SELECT * FROM users;
SELECT * FROM login_history;


CREATE TABLE hints (
    id INT AUTO_INCREMENT PRIMARY KEY,
    account_name VARCHAR(255) NOT NULL,
    hint_question VARCHAR(255) NOT NULL,
    hint_answer VARCHAR(255) NOT NULL
);



CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    emergency_contact VARCHAR(255)
);


CREATE TABLE passwords (
    id INT AUTO_INCREMENT PRIMARY KEY,
    account_name VARCHAR(255) NOT NULL,
    username_email VARCHAR(255) NOT NULL,
    unhashed_passwords VARCHAR(255) NOT NULL,
    date_added TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE login_history (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    login_time DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (username) REFERENCES users(username)
);




DELETE FROM hints WHERE id > 0;
SET sql_safe_updates = 0;





