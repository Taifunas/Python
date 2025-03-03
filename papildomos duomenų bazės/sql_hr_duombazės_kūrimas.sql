-- sql_hr

DROP DATABASE IF EXISTS `sql_hr`;
CREATE DATABASE `sql_hr`;
USE `sql_hr`;

DROP DATABASE IF EXISTS `offices`;
CREATE TABLE `offices` (
  `office_id` int(11) NOT NULL,
  `address` varchar(50) NOT NULL,
  `city` varchar(50) NOT NULL,
  `state` varchar(50) NOT NULL,
  PRIMARY KEY (`office_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
INSERT INTO `offices` VALUES (1,'Aukštumos g. 20','Kaunas','Kauno');
INSERT INTO `offices` VALUES (2,'Aukštumos g. 22','Kaunas','Kauno');
INSERT INTO `offices` VALUES (3,'Pramonės g.202','Klaipėda','Klaipėdos');
INSERT INTO `offices` VALUES (4,'Žemaitės g. 42','Vilnius','Vilniaus');
INSERT INTO `offices` VALUES (5,'Aukštumos g. 24','Kaunas','Kauno');
INSERT INTO `offices` VALUES (6,'Pergalės g. 12','Alytus','Alytaus');



CREATE TABLE `employees` (
  `employee_id` int(11) NOT NULL,
  `first_name` varchar(50) NOT NULL,
  `last_name` varchar(50) NOT NULL,
  `job_title` varchar(50) NOT NULL,
  `salary` int(11) NOT NULL,
  `reports_to` int(11) DEFAULT NULL,
  `office_id` int(11) NOT NULL,
  PRIMARY KEY (`employee_id`),
  KEY `fk_employees_offices_idx` (`office_id`),
  KEY `fk_employees_employees_idx` (`reports_to`),
  CONSTRAINT `fk_employees_managers` FOREIGN KEY (`reports_to`) REFERENCES `employees` (`employee_id`),
  CONSTRAINT `fk_employees_offices` FOREIGN KEY (`office_id`) REFERENCES `offices` (`office_id`) ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
INSERT INTO `employees` VALUES (37270,'Dalia','Pargienė','Direktorius',76800,NULL,1);
INSERT INTO `employees` VALUES (33391,'Artūras','Nykštys','Direktoriaus pavaduotojas',54000,37270,1);
INSERT INTO `employees` VALUES (37851,'Žygimantas','Radavičius','Personalo skyriaus vadovas',50400,37270,1);
INSERT INTO `employees` VALUES (40448,'Saulė','Almaitė','Komunikacijos skyriaus vadovas',48800,37270,2);
INSERT INTO `employees` VALUES (56274,'Nijolė','Kauskienė','Teisės skyriaus vadovas',55200,37270,1);
INSERT INTO `employees` VALUES (63196,'Aurimas','Jurgilas','Komunikacijos skyriaus specialistas',32400,40448,2);
INSERT INTO `employees` VALUES (67009,'Petras','Garbavičius','Vidaus audito vadovas',49200,37270,1);
INSERT INTO `employees` VALUES (67370,'Normantas','Gomurys','Teisininkas',37200,56274,1);
INSERT INTO `employees` VALUES (76196,'Mindaugas','Janavičius','Finansų ir apskaitos skyriaus vadovas',49100,37270,4);
INSERT INTO `employees` VALUES (80529,'Lidija','Būgienė','Operacijų ir mokėjimų skyriaus vadovas',51800,37270,3);
INSERT INTO `employees` VALUES (68249,'Danutė','Urbonienė','Vyr Operacijų specialistas',36800,80529,3);
INSERT INTO `employees` VALUES (80679,'Arijus','Sakalas','Operacijų specialistas',29000,37270,3);
INSERT INTO `employees` VALUES (84791,'Patrikas','Tarberutas','Personalo skyriaus atrankų specialistas',33600,37851,1);
INSERT INTO `employees` VALUES (115357,'Danguolė','Likšienė','Finansų planavimo ir analizės skyriaus vadovas',52200,37270,3);
INSERT INTO `employees` VALUES (95213,'Aistė','Ženčienė','Vyr. Teisininkas',40050,56274,1);
INSERT INTO `employees` VALUES (72540,'Agata','Jakučionytė','Buhalteris',33000,76196,4);
INSERT INTO `employees` VALUES (72913,'Matas','Lastauskas','Finansininkas',35000,76196,4);
INSERT INTO `employees` VALUES (75900,'Gintautas','Grikinis','Analitikas',37050,115357,3);
INSERT INTO `employees` VALUES (96513,'Severija','Kanapeckienė','Vyr. Analitikas',39900,115357,3);
INSERT INTO `employees` VALUES (98374,'Tomas','Šalčius','Analitikas',36800,115357,3);