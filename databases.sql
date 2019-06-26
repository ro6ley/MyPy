-- CREATE DATABASE
CREATE DATABASE IF NOT EXISTS `safaricom_home_demo`;

USE `safaricom_home_demo`;

-- ---------------------------------------------------------------------------

---
-- CREATE TABLES
---

-- Agents table
CREATE TABLE IF NOT EXISTS `agents` (
  `agent_id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `agent_first_name` VARCHAR(30) NULL,
  `agent_last_name` VARCHAR(30) NULL,
  `agent_email` VARCHAR(30) NULL,
  `agent_phone` VARCHAR(30) NULL
);


-- Regions table
CREATE TABLE IF NOT EXISTS `regions` (
  `region_id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `region_name` VARCHAR(30) NULL,
  `region_county_id` INT
);

-- Customer Info table
CREATE TABLE IF NOT EXISTS `customers` (
	`cust_id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	`cust_first_name` VARCHAR(30) NULL,
	`cust_last_name` VARCHAR(30) NULL,
	`cust_phone` VARCHAR(30) NULL,
	`cust_email` VARCHAR(30) NULL,
	`cust_address` VARCHAR(30) NULL,
  `cust_agent_id` INT,
  `cust_region_id` INT,
  FOREIGN KEY (`cust_agent_id`) REFERENCES `agents`(`agent_id`),
  FOREIGN KEY (`cust_region_id`) REFERENCES `regions`(`region_id`)
);

-- Packages table
CREATE TABLE IF NOT EXISTS `packages` (
  `package_id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `package_name` VARCHAR(30) NULL,
  `package_speed` VARCHAR(4) NULL,
  `package_cost` DECIMAL(6,2) NOT NULL DEFAULT 0.00
);

-- Accounts table
CREATE TABLE IF NOT EXISTS `accounts` (
  `account_id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `account_subscription_status` BOOLEAN DEFAULT FALSE,
  `account_payment_due_date` DATE NOT NULL,
  `account_balance` DECIMAL(6,2) NOT NULL DEFAULT 0.00,
  `account_connection_date` DATE NULL,
  `account_region_id` INT,
  `account_package_type` INT,
  `account_cust_id` INT,
  FOREIGN KEY (`account_region_id`) REFERENCES `regions`(`region_id`),
  FOREIGN KEY (`account_package_type`) REFERENCES `packages`(`package_id`),
  FOREIGN KEY (`account_cust_id`) REFERENCES `customers`(`cust_id`) ON DELETE CASCADE
);

-- ---------------------------------------------------------------------------

--
-- INSERT DATA
--

-- Insert into packages
INSERT INTO `packages` 
  (`package_name`, `package_speed`, `package_cost`) 
VALUES 
  ('BRONZE', '2', 2500.00),
  ('SILVER', '5', 4000.00),
  ('GOLD', '10', 7000.00),
  ('PLATINUM', '20', 10000.00);

-- Insert into regions
INSERT INTO `regions` 
  (`region_name`, `region_county_id`)
VALUES
  ('Nairobi CBD', 47),
  ('Westlands', 47),
  ('South B', 47),
  ('Ongata Rongai', 44),
  ('Ruaka', 20),
  ('Nakuru CBD', 32),
  ('Mombasa CBD', 1),
  ('Nyali', 1);

-- Insert into agents
INSERT INTO `agents` 
  (`agent_first_name`, `agent_last_name`, `agent_email`, `agent_phone`)
VALUES 
  ('Jar Jar', 'Binks', 'jarjar@binks.com', '01234567'),
  ('Luke', 'Skywalker', 'luke@skywalker.com', '12345670'),
  ('Leah', 'Skywalker', 'leah@skywalker.com', '23456701'),
  ('Darth', 'Vader', 'darth@vader.com', '34567012'),
  ('Master', 'Yoda', 'master@yoda.com', '45670123'),
  ('Chew', 'Bacca', 'chew@bacca.com', '56701234'),
  ('Obi-Wan', 'Kenobi', 'obiwan@kenobi.com', '67012345'),
  ('Han', 'Solo', 'han@solo.com', '70123456');

-- Insert into customers
INSERT INTO `customers` 
  (`cust_first_name`, `cust_last_name`, `cust_phone`, `cust_email`, `cust_address`, `cust_agent_id`, `cust_region_id`)
VALUES
  ('Jon', 'Snow', '0987654321', 'jon@snow.com', 'Winterfell', 1, 2),
  ('Daenerys', 'Targaryen', '9876543210', 'danny@targaryen.com', 'Dragon Stone', 1, 2),
  ('Tyrion', 'Lannister', '8765432109', 'tyrion@lannister.com', 'Dragon Stone', 2, 2),
  ('Arya', 'Stark', '7654321098', 'arya@stark.com', 'Winterfell', 3, 2),
  ('Cersei', 'Lannister', '6543210987', 'cersei@lannister.com', 'King\'s Landing', 3, 2),
  ('Euron', 'Greyjoy', '5432109876', 'euron@greyjoy.com', 'Iron Islands', 3, 2),
  ('Night', 'King', '4321098765', 'night@king.com', 'The Wall', 8, 2),
  ('Samuel', 'Tarly', '3210987654', 'samuel@tarly.com', 'The Citadel', 6, 2);

-- Insert into accounts
INSERT INTO `accounts` 
  (`account_subscription_status`, `account_payment_due_date`, `account_balance`, `account_connection_date`, `account_region_id`, `account_package_type`, `account_cust_id`)
VALUES
  (FALSE, '2019-04-12', 0.00, '2019-03-12', 1, 8, 1),
  (TRUE, '2019-04-12', 0.00, '2019-03-12', 1, 7, 1),
  (FALSE, '2019-04-12', 0.00, '2019-03-12', 1, 5, 2),
  (TRUE, '2019-04-12', 0.00, '2019-03-12', 1, 8, 3),
  (FALSE, '2019-04-12', 0.00, '2019-03-12', 1, 6, 4),
  (TRUE, '2019-04-12', 0.00, '2019-03-12', 1, 5, 5),
  (FALSE, '2019-04-12', 0.00, '2019-03-12', 1, 5, 6),
  (TRUE, '2019-04-12', 0.00, '2019-03-12', 1, 7, 7),
  (TRUE, '2019-04-12', 0.00, '2019-03-12', 1, 8, 8),
  (TRUE, '2019-04-12', 0.00, '2019-03-12', 1, 5, 3),
  (FALSE, '2019-04-12', 0.00, '2019-03-12', 1, 5, 3);

-- ---------------------------------------------------------------------------
--
-- READ DATA
--

SELECT * FROM `packages`;

SELECT * FROM `regions`;

SELECT * FROM `customers`;

SELECT * FROM `accounts`;

-- ---------------------------------------------------------------------------
--
-- UPDATE DATA
--

-- Modify account balance
UPDATE `accounts` SET `account_balance`=1200.00 WHERE `account_id`=12;

-- Update user's package
UPDATE `accounts` SET `account_package_type`=8 WHERE `account_id`=14;
 
-- ---------------------------------------------------------------------------

--
-- DELETE DATA
--

-- Delete Accounts
DELETE FROM `accounts` WHERE `account_id`=22;

-- Delete Customers, with Cascade all accounts should be deleted
DELETE FROM `customers` WHERE `cust_id`=8;

-- ---------------------------------------------------------------------------

--
-- ALTER COLUMNS
--

-- Update number of digits before decimal to 8
ALTER TABLE `packages` MODIFY COLUMN `package_cost` DECIMAL(10,2);

-- Rename Column
-- ALTER TABLE `packages` RENAME COLUMN `packages_cost` TO `packages_new_cost`;

-- Add Column
-- ALTER TABLE `packages` ADD COLUMN `users_count` INT AFTER `package_cost`;

-- Delete Column
-- ALTER TABLE `packages` DROP COLUMN `users_count`;

-- Delete a row
-- DELETE FROM `packages` WHERE `package_id`=10;

-- ---------------------------------------------------------------------------

-- READ: ORDER BY

-- Order by Package Type
SELECT * FROM `accounts` ORDER BY `account_package_type`;

-- Order by Customer Id
SELECT * FROM `accounts` ORDER BY `account_cust_id`;

-- READ: GROUP BY

-- Group by Region
SELECT `account_region_id`, COUNT(`account_region_id`) FROM `accounts` GROUP BY `account_region_id`;

-- Group by Package Type
SELECT `account_package_type`, COUNT(`account_package_type`) FROM `accounts` GROUP BY `account_package_type`;

-- ---------------------------------------------------------------------------

--
-- READ: COUNT
--

-- Count number of accounts on the Bronze Package
SELECT `account_package_type`, COUNT(`account_package_type`) `Bronze Users` FROM `accounts` WHERE `account_package_type`=5;

-- Count number of account in Mombasa
SELECT `account_region_id`, COUNT(`account_region_id`) `Msa Accounts` FROM `accounts` WHERE `account_region_id`=7;

-- ---------------------------------------------------------------------------

--
-- EXISTS COMMAND
--
-- Select agents that have at least one customer
SELECT `agent_first_name`, `agent_last_name`, `agent_email` FROM `agents`
  WHERE  EXISTS
  (SELECT * from `customers` WHERE `cust_agent_id` = `agent_id`);

-- ---------------------------------------------------------------------------

-- JOINS

--
-- INNER JOIN
--

-- Select all accounts with their package information
SELECT * FROM `accounts`
  INNER JOIN `packages` ON `account_package_type` = `package_id`;

--
-- LEFT JOIN
--

-- Select all customers with their agent information
SELECT * FROM `customers`
  LEFT JOIN `agents` ON `cust_agent_id` = `agent_id`;

--
-- RIGHT JOIN
--

-- Select all agents that have customers alongside their clients information
SELECT * FROM `agents`
  RIGHT JOIN `customers` ON `agent_id` = `cust_agent_id`;

--
-- FULL OUTER JOIN
--

/*
There are no Full Joins on MySQL so we emulate them using 
  a UNION on a LEFT and RIGHT JOIN
*/

-- Select all accounts and their regions, even regions that have no customers
SELECT * FROM `accounts` 
  LEFT JOIN `regions` ON `account_region_id` = `region_id`
UNION
SELECT * FROM `accounts` 
  RIGHT JOIN `regions` ON `account_region_id` = `region_id`;

-- ---------------------------------------------------------------------------

--
-- CREATE VIEW
--

-- View of all customers with Platinum packages
CREATE VIEW `platinum_customers` AS
  SELECT DISTINCT `cust_first_name`, `cust_last_name`, `cust_email`, `cust_phone`, `account_subscription_status` 
  FROM `customers`
  INNER JOIN `accounts` ON `cust_id` = `account_cust_id`
  INNER JOIN `packages` ON `account_package_type` = 8;

SELECT * FROM `platinum_accounts`;

-- ---------------------------------------------------------------------------

--
-- CREATE CLUSTERD INDEX
--

/*
Syntax:
CREATE UNIQUE INDEX index_name
  ON table_name (column ASC)

MySQL Creates a Clustered Index called PRIMARY when you define a primary key
  in your table.
*/
CREATE UNIQUE INDEX `clustered_index` ON ``(``);

--
-- CREATE NONCLUSTERED INDEX
--

/*
Syntax:
CREATE INDEX index_name
  ON table_name(column_1 ASC, column_2 ASC, ...column_n ASC)
*/
-- Composite Index: Index using more than one column
CREATE INDEX `cust_names` ON `customers`(`cust_first_name`, `cust_last_name`);

SHOW INDEX FROM `customers`;

/*
When I run the following query now:
 EXPLAIN SELECT cust_first_name, cust_last_name FROM customers;

+----+-------------+-----------+------------+-------+---------------+------------+---------+------+------+----------+-------------+
| id | select_type | table     | partitions | type  | possible_keys | key        | key_len | ref  | rows | filtered | Extra       |
+----+-------------+-----------+------------+-------+---------------+------------+---------+------+------+----------+-------------+
|  1 | SIMPLE      | customers | NULL       | index | NULL          | cust_names | 246     | NULL |    8 |   100.00 | Using index |
+----+-------------+-----------+------------+-------+---------------+------------+---------+------+------+----------+-------------+
1 row in set, 1 warning (0.00 sec)

Under keys we can see that MySQL used the index we created above to fetch the data.

An index can be created to sort first names in ascending order and increase the lookup time
  for this particular arrangement of the table:
CREATE INDEX `asc_first_name_index` ON `customers`(`cust_first_name` ASC);
*/

CREATE INDEX `region_names` ON `regions`(`region_name` ASC);

SHOW INDEX FROM `regions`;

-- Deleting an index
-- DROP INDEX index_name ON table_name

-- ---------------------------------------------------------------------------

-- PPARTITIONING

--
-- CREATE HORIZONTAL PARTITION
--

/*
MySQL does not yet support Foreign Keys in conjuction with horizontal partitioning
*/
-- Hash Partitioning
ALTER TABLE `accounts` 
  PARTITION BY HASH(`account_id`) 
  PARTITIONS 2;

-- Range Partitioning
ALTER TABLE `regions` PARTITION BY RANGE (`region_id`)
  (
    PARTITION p1 VALUES LESS THAN (3),
    PARTITION p2 VALUES LESS THAN MAXVALUE 
  );

/*
MySQL 8 does not support vertical partitioning.
*/

-- ---------------------------------------------------------------------------

--
-- DEFINE STORED PROCEDURE
--
/*
We change the delimiter to $$ to avoid issues when our procedures have many statements.

The Stored Procedure will end at the delimiter while any statements within it,
  will end with the original delimter (;)
*/
DELIMITER $$

CREATE PROCEDURE `create_new_package`
  (
    IN package_name VARCHAR(30), 
    IN package_speed VARCHAR(4),
    IN package_cost DECIMAL(8,2)
  )
BEGIN
  INSERT INTO `packages`
    (`package_name`, `package_speed`, `package_cost`)
  VALUES
    (package_name, package_speed, package_cost);
  SELECT * FROM `packages`;
END $$

DELIMITER ;

--
-- USE DEFINED STORED PROCEDURE
--
CALL `create_new_package`(
  'RED', '100', 20000.00
);

-- ---------------------------------------------------------------------------
