-- Create the database if it doesn't exist
CREATE DATABASE IF NOT EXISTS banking_db;
USE banking_db;

-- Table structure for `applicants`
DROP TABLE IF EXISTS `applicants`;
CREATE TABLE `applicants` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL,
  `income` float DEFAULT NULL,
  `age` int DEFAULT NULL,
  `debt` float DEFAULT NULL,
  `score` int DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Table structure for `credit_applicants`
DROP TABLE IF EXISTS `credit_applicants`;
CREATE TABLE `credit_applicants` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL,
  `income` float DEFAULT NULL,
  `age` int DEFAULT NULL,
  `credit_history_months` int DEFAULT NULL,
  `debt` float DEFAULT NULL,
  `credit_score` int DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `decision` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4;
