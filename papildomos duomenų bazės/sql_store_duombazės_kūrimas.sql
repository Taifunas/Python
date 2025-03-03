-- sql_store

DROP DATABASE IF EXISTS `sql_store`;
CREATE DATABASE `sql_store`;
USE `sql_store`;

DROP TABLE IF EXISTS `products`;
CREATE TABLE `products` (
  `product_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `quantity_in_stock` int(11) NOT NULL,
  `unit_price` decimal(6,2) NOT NULL,
  PRIMARY KEY (`product_id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
INSERT INTO `products` VALUES (1,'Mikrobangų krosnelė',70,103.02);
INSERT INTO `products` VALUES (2,'Elektrinis virdulyss',49,42.10);
INSERT INTO `products` VALUES (3,'Sulčiaspaudė, Heart',38,35.00);
INSERT INTO `products` VALUES (4,'Virtuvinis kombainas',90,135.98);
INSERT INTO `products` VALUES (5,'Elektrinė pjaustyklė',94,65.65);
INSERT INTO `products` VALUES (6,'Trintuvas',14,33.72);
INSERT INTO `products` VALUES (7,'Kokteilinė',98,27.99);
INSERT INTO `products` VALUES (8,'Plakiklis',26,24.99);
INSERT INTO `products` VALUES (9,'Skrudintuvas',67,39.26);
INSERT INTO `products` VALUES (10,'Vaflinė',6,28.25);

DROP TABLE IF EXISTS `shippers`;
CREATE TABLE `shippers` (
  `shipper_id` smallint(6) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`shipper_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
INSERT INTO `shippers` VALUES (1,'Sklaida');
INSERT INTO `shippers` VALUES (2,'Produktai Visiems');
INSERT INTO `shippers` VALUES (3,'Elektroninė Parduotuvė');
INSERT INTO `shippers` VALUES (4,'Pirk Pirk Pirk');
INSERT INTO `shippers` VALUES (5,'Prekyba ir KO');

DROP TABLE IF EXISTS `customers`;
CREATE TABLE `customers` (
  `customer_id` int(11) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(50) NOT NULL,
  `last_name` varchar(50) NOT NULL,
  `birth_date` date DEFAULT NULL,
  `phone` varchar(50) DEFAULT NULL,
  `address` varchar(50) NOT NULL,
  `city` varchar(50) NOT NULL,
  `state` char(30) NOT NULL,
  `points` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`customer_id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
INSERT INTO `customers` VALUES (1,'Giedrė','Randomaitė','1986-03-28','37060001000','K. Donelaičio g. 73','Kaunas','Kauno apskritis',2273);
INSERT INTO `customers` VALUES (2,'Antanas','Pavardžius','1986-04-13','37061112223','Saulėtekio al. 11','Vilnius','Vilniaus apskritis',947);
INSERT INTO `customers` VALUES (3,'Gediminas','Mantainis','1985-02-07','37069998877','Vytauto g. 1A','Prienai','Kauno apskritis',2967);
INSERT INTO `customers` VALUES (4,'Joana','Sprigtukienė','1974-04-14','37068764532','Liepų g. 5','Klaipėda','Klaipėdos apskritis',457);
INSERT INTO `customers` VALUES (5,'Amelija','Puškutė','1993-11-07',NULL,'Savanorių g. 17','Alytus','Alytaus apskritis',3675);
INSERT INTO `customers` VALUES (6,'Donatas','Skardžius','1991-09-04','37061155555','Smėlio g. 9','Utena','Utenos apskritis',3073);
INSERT INTO `customers` VALUES (7,'Rasa','Antanienė','1964-08-30','37069912345','Laukų g. 24','Ukmergė','Vilniaus apskritis',1672);
INSERT INTO `customers` VALUES (8,'Arminas','Vaitiekūnas','1993-07-17','37062235854','Nemuno g. 18','Panevėžys','Panevėžio apskritis',205);
INSERT INTO `customers` VALUES (9,'Romualdas','Klėvišas','1992-05-23','37063422288','Lakūnų g. 4','Šiauliai','Šiaulių apskritis',1486);
INSERT INTO `customers` VALUES (10,'Daina','Ugnienė','1969-10-13','37062244531','Ligoninės g. 12','Alytus','Alytaus apskritis',796);


DROP TABLE IF EXISTS `order_statuses`;
CREATE TABLE `order_statuses` (
  `order_status_id` tinyint(4) NOT NULL,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`order_status_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
INSERT INTO `order_statuses` VALUES (1,'Paruoštas');
INSERT INTO `order_statuses` VALUES (2,'Išsiųstas');
INSERT INTO `order_statuses` VALUES (3,'Pristatytas');


DROP TABLE IF EXISTS `orders`;
CREATE TABLE `orders` (
  `order_id` int(11) NOT NULL AUTO_INCREMENT,
  `customer_id` int(11) NOT NULL,
  `order_date` date NOT NULL,
  `status` tinyint(4) NOT NULL DEFAULT '1',
  `comments` varchar(2000) DEFAULT NULL,
  `shipped_date` date DEFAULT NULL,
  `shipper_id` smallint(6) DEFAULT NULL,
  PRIMARY KEY (`order_id`),
  KEY `fk_orders_customers_idx` (`customer_id`),
  KEY `fk_orders_shippers_idx` (`shipper_id`),
  KEY `fk_orders_order_statuses_idx` (`status`),
  CONSTRAINT `fk_orders_customers` FOREIGN KEY (`customer_id`) REFERENCES `customers` (`customer_id`) ON UPDATE CASCADE,
  CONSTRAINT `fk_orders_order_statuses` FOREIGN KEY (`status`) REFERENCES `order_statuses` (`order_status_id`) ON UPDATE CASCADE,
  CONSTRAINT `fk_orders_shippers` FOREIGN KEY (`shipper_id`) REFERENCES `shippers` (`shipper_id`) ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
INSERT INTO `orders` VALUES (1,6,'2019-01-30',1,NULL,NULL,NULL);
INSERT INTO `orders` VALUES (2,7,'2018-08-02',2,NULL,'2018-08-03',4);
INSERT INTO `orders` VALUES (3,8,'2017-12-01',1,NULL,NULL,NULL);
INSERT INTO `orders` VALUES (4,2,'2017-01-22',1,NULL,NULL,NULL);
INSERT INTO `orders` VALUES (5,5,'2017-08-25',2,'','2017-08-26',3);
INSERT INTO `orders` VALUES (6,10,'2018-11-18',1,'Prašau pristatyti siuntinį darbo valandomis',NULL,NULL);
INSERT INTO `orders` VALUES (7,2,'2018-09-22',2,NULL,'2018-09-23',4);
INSERT INTO `orders` VALUES (8,5,'2018-06-08',1,'Atsiimsiu jūsų parduotuvėje Kaune',NULL,NULL);
INSERT INTO `orders` VALUES (9,10,'2017-07-05',2,'Išsiųskite sąskaitą faktūrą elektroniniu paštu','2017-07-06',1);
INSERT INTO `orders` VALUES (10,6,'2018-04-22',2,NULL,'2018-04-23',2);

DROP TABLE IF EXISTS `order_items`;
CREATE TABLE `order_items` (
  `order_id` int(11) NOT NULL AUTO_INCREMENT,
  `product_id` int(11) NOT NULL,
  `quantity` int(11) NOT NULL,
  `unit_price` decimal(6,2) NOT NULL,
  PRIMARY KEY (`order_id`,`product_id`),
  KEY `fk_order_items_products_idx` (`product_id`),
  CONSTRAINT `fk_order_items_orders` FOREIGN KEY (`order_id`) REFERENCES `orders` (`order_id`) ON UPDATE CASCADE,
  CONSTRAINT `fk_order_items_products` FOREIGN KEY (`product_id`) REFERENCES `products` (`product_id`) ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
INSERT INTO `order_items` VALUES (1,4,4,'140.00');
INSERT INTO `order_items` VALUES (2,1,2,104.50);
INSERT INTO `order_items` VALUES (2,4,4,142.15);
INSERT INTO `order_items` VALUES (2,6,2,34.00);
INSERT INTO `order_items` VALUES (3,3,10,38.00);
INSERT INTO `order_items` VALUES (4,3,7,36.00);
INSERT INTO `order_items` VALUES (4,10,7,29.00);
INSERT INTO `order_items` VALUES (5,2,3,44.50);
INSERT INTO `order_items` VALUES (6,1,4,105.20);
INSERT INTO `order_items` VALUES (6,2,4,43.10);
INSERT INTO `order_items` VALUES (6,3,4,35.00);
INSERT INTO `order_items` VALUES (6,5,1,69.99);
INSERT INTO `order_items` VALUES (7,3,7,37.70);
INSERT INTO `order_items` VALUES (8,5,2,68.50);
INSERT INTO `order_items` VALUES (8,8,2,26.99);
INSERT INTO `order_items` VALUES (9,6,5,33.90);
INSERT INTO `order_items` VALUES (10,1,10,105.40);
INSERT INTO `order_items` VALUES (10,9,9,41.99);

DROP TABLE IF EXISTS `order_item_notes`;
CREATE TABLE `sql_store`.`order_item_notes` (
  `note_id` INT NOT NULL,
  `order_Id` INT NOT NULL,
  `product_id` INT NOT NULL,
  `note` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`note_id`));

INSERT INTO `order_item_notes` (`note_id`, `order_Id`, `product_id`, `note`) VALUES ('1', '1', '4', 'pirma pastaba');
INSERT INTO `order_item_notes` (`note_id`, `order_Id`, `product_id`, `note`) VALUES ('2', '2', '6', 'antra pastaba');