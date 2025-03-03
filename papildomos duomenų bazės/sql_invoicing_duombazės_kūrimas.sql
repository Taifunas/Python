-- sql_invoicing

DROP DATABASE IF EXISTS `sql_invoicing`;
CREATE DATABASE `sql_invoicing`; 
USE `sql_invoicing`;

SET NAMES utf8 ;
SET character_set_client = utf8mb4 ;


DROP TABLE IF EXISTS `payment_methods`;
CREATE TABLE `payment_methods` (
  `payment_method_id` tinyint(4) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`payment_method_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
INSERT INTO `payment_methods` VALUES (1,'Kredito kortelė');
INSERT INTO `payment_methods` VALUES (2,'Grynieji pinigai');
INSERT INTO `payment_methods` VALUES (3,'Elektroninė bankininkystė');
INSERT INTO `payment_methods` VALUES (4,'Bankinis pavedimas');


DROP TABLE IF EXISTS `clients`;
CREATE TABLE `clients` (
  `client_id` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `address` varchar(50) NOT NULL,
  `city` varchar(50) NOT NULL,
  `state` char(30) NOT NULL,
  `phone` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`client_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
INSERT INTO `clients` VALUES (1,'Vintukai','Saulės g. 15','Vilnius','Vilniaus','37060001234');
INSERT INTO `clients` VALUES (2,'Pirkimai ir KO','Vytauto g. 24','Kaunas','Kauno','37064421312');
INSERT INTO `clients` VALUES (3,'Tiesus tiekimas','Saulėgrąžų g. 77','Klaipėda','Klaipėdos','37063377554');
INSERT INTO `clients` VALUES (4,'Blyksnis','Pieninės g. 44','Šiauliai','Šiaulių','37064455111');
INSERT INTO `clients` VALUES (5,'Topinis','Šaltuko g. 82','Panevėžys','Panevėžio','37067585213');


DROP TABLE IF EXISTS `invoices`;
CREATE TABLE `invoices` (
  `invoice_id` int(11) NOT NULL,
  `number` varchar(50) NOT NULL,
  `client_id` int(11) NOT NULL,
  `invoice_total` decimal(9,2) NOT NULL,
  `payment_total` decimal(9,2) NOT NULL DEFAULT '0.00',
  `invoice_date` date NOT NULL,
  `due_date` date NOT NULL,
  `payment_date` date DEFAULT NULL,
  PRIMARY KEY (`invoice_id`),
  KEY `FK_client_id` (`client_id`),
  CONSTRAINT `FK_client_id` FOREIGN KEY (`client_id`) REFERENCES `clients` (`client_id`) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
INSERT INTO `invoices` VALUES (1,'91-953-3396',2,1010.79,0.00,'2019-03-09','2019-03-29',NULL);
INSERT INTO `invoices` VALUES (2,'03-898-6735',5,1750.32,800.18,'2019-06-11','2019-07-01','2019-02-12');
INSERT INTO `invoices` VALUES (3,'20-228-0335',5,1470.99,0.00,'2019-07-31','2019-08-20',NULL);
INSERT INTO `invoices` VALUES (4,'56-934-0748',3,1520.21,0.00,'2019-03-08','2019-03-28',NULL);
INSERT INTO `invoices` VALUES (5,'87-052-3121',5,1690.36,0.00,'2019-07-18','2019-08-07',NULL);
INSERT INTO `invoices` VALUES (6,'75-587-6626',1,1570.78,740.55,'2019-01-29','2019-02-18','2019-01-03');
INSERT INTO `invoices` VALUES (7,'68-093-9863',3,1330.87,0.00,'2019-09-04','2019-09-24',NULL);
INSERT INTO `invoices` VALUES (8,'78-145-1093',1,1890.12,0.00,'2019-05-20','2019-06-09',NULL);
INSERT INTO `invoices` VALUES (9,'77-593-0081',5,1720.17,0.00,'2019-07-09','2019-07-29',NULL);
INSERT INTO `invoices` VALUES (10,'48-266-1517',1,1590.50,0.00,'2019-06-30','2019-07-20',NULL);
INSERT INTO `invoices` VALUES (11,'20-848-0181',3,1260.15,350.00,'2019-01-07','2019-01-27','2019-01-11');
INSERT INTO `invoices` VALUES (13,'41-666-1035',5,1350.01,870.44,'2019-06-25','2019-07-15','2019-01-26');
INSERT INTO `invoices` VALUES (15,'55-105-9605',3,1670.29,800.31,'2019-11-25','2019-12-15','2019-01-15');
INSERT INTO `invoices` VALUES (16,'10-451-8824',1,1620.02,0.00,'2019-03-30','2019-04-19',NULL);
INSERT INTO `invoices` VALUES (17,'33-615-4694',3,1260.38,680.10,'2019-07-30','2019-08-19','2019-01-15');
INSERT INTO `invoices` VALUES (18,'52-269-9803',5,1800.17,420.77,'2019-05-23','2019-06-12','2019-01-08');
INSERT INTO `invoices` VALUES (19,'83-559-4105',1,1340.47,0.00,'2019-11-23','2019-12-13',NULL);


DROP TABLE IF EXISTS `payments`;
CREATE TABLE `payments` (
  `payment_id` int(11) NOT NULL AUTO_INCREMENT,
  `client_id` int(11) NOT NULL,
  `invoice_id` int(11) NOT NULL,
  `date` date NOT NULL,
  `amount` decimal(9,2) NOT NULL,
  `payment_method` tinyint(4) NOT NULL,
  PRIMARY KEY (`payment_id`),
  KEY `fk_client_id_idx` (`client_id`),
  KEY `fk_invoice_id_idx` (`invoice_id`),
  KEY `fk_payment_payment_method_idx` (`payment_method`),
  CONSTRAINT `fk_payment_client` FOREIGN KEY (`client_id`) REFERENCES `clients` (`client_id`) ON UPDATE CASCADE,
  CONSTRAINT `fk_payment_invoice` FOREIGN KEY (`invoice_id`) REFERENCES `invoices` (`invoice_id`) ON UPDATE CASCADE,
  CONSTRAINT `fk_payment_payment_method` FOREIGN KEY (`payment_method`) REFERENCES `payment_methods` (`payment_method_id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
INSERT INTO `payments` VALUES (1,5,2,'2019-02-12',800.18,1);
INSERT INTO `payments` VALUES (2,1,6,'2019-01-03',740.55,3);
INSERT INTO `payments` VALUES (3,3,11,'2019-01-11',350.00,3);
INSERT INTO `payments` VALUES (4,5,13,'2019-01-26',870.44,3);
INSERT INTO `payments` VALUES (5,3,15,'2019-01-15',800.31,1);
INSERT INTO `payments` VALUES (6,3,17,'2019-01-15',680.10,2);
INSERT INTO `payments` VALUES (7,5,18,'2019-01-08',320.77,1);
INSERT INTO `payments` VALUES (8,5,18,'2019-01-08',100.00,2);