-- sql_inventory

DROP DATABASE IF EXISTS `sql_inventory`;
CREATE DATABASE `sql_inventory`;
USE `sql_inventory`;

DROP TABLE IF EXISTS `products`;
CREATE TABLE `products` (
  `product_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `quantity_in_stock` int(11) NOT NULL,
  `unit_price` decimal(6,2) NOT NULL,
  PRIMARY KEY (`product_id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
INSERT INTO `products` VALUES (1,'Mikrobangų krosnelė',70,103.02);
INSERT INTO `products` VALUES (2,'Elektrinis virdulys',49,42.10);
INSERT INTO `products` VALUES (3,'Sulčiaspaudė, Heart',38,35.00);
INSERT INTO `products` VALUES (4,'Virtuvinis kombainas',90,135.98);
INSERT INTO `products` VALUES (5,'Elektrinė pjaustyklė',94,65.65);
INSERT INTO `products` VALUES (6,'Trintuvas',14,33.72);
INSERT INTO `products` VALUES (7,'Kokteilinė',98,27.99);
INSERT INTO `products` VALUES (8,'Plakiklis',26,24.99);
INSERT INTO `products` VALUES (9,'Skrudintuvas',67,39.26);
INSERT INTO `products` VALUES (10,'Vaflinė',6,28.25);