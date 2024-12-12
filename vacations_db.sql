-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: localhost    Database: second_project_db
-- ------------------------------------------------------
-- Server version	8.0.36

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `countries`
--

DROP TABLE IF EXISTS `countries`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `countries` (
  `countryId` int NOT NULL AUTO_INCREMENT,
  `countryName` varchar(100) NOT NULL,
  PRIMARY KEY (`countryId`)
) ENGINE=InnoDB AUTO_INCREMENT=194 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `countries`
--

LOCK TABLES `countries` WRITE;
/*!40000 ALTER TABLE `countries` DISABLE KEYS */;
INSERT INTO `countries` VALUES (1,'Afghanistan'),(2,'Albania'),(3,'Algeria'),(4,'Andorra'),(5,'Angola'),(6,'Antigua and Barbuda'),(7,'Argentina'),(8,'Armenia'),(9,'Australia'),(10,'Austria'),(11,'Azerbaijan'),(12,'Bahamas'),(13,'Bahrain'),(14,'Bangladesh'),(15,'Barbados'),(16,'Belarus'),(17,'Belgium'),(18,'Belize'),(19,'Benin'),(20,'Bhutan'),(21,'Bolivia'),(22,'Bosnia and Herzegovina'),(23,'Botswana'),(24,'Brazil'),(25,'Brunei'),(26,'Bulgaria'),(27,'Burkina Faso'),(28,'Burundi'),(29,'Cabo Verde'),(30,'Cambodia'),(31,'Cameroon'),(32,'Canada'),(33,'Central African Republic'),(34,'Chad'),(35,'Chile'),(36,'China'),(37,'Colombia'),(38,'Comoros'),(39,'Congo (Congo-Brazzaville)'),(40,'Costa Rica'),(41,'Croatia'),(42,'Cuba'),(43,'Cyprus'),(44,'Czechia (Czech Republic)'),(45,'Democratic Republic of the Congo'),(46,'Denmark'),(47,'Djibouti'),(48,'Dominica'),(49,'Dominican Republic'),(50,'Ecuador'),(51,'Egypt'),(52,'El Salvador'),(53,'Equatorial Guinea'),(54,'Eritrea'),(55,'Estonia'),(56,'Eswatini (fmr. \"Swaziland\")'),(57,'Ethiopia'),(58,'Fiji'),(59,'Finland'),(60,'France'),(61,'Gabon'),(62,'Gambia'),(63,'Georgia'),(64,'Germany'),(65,'Ghana'),(66,'Greece'),(67,'Grenada'),(68,'Guatemala'),(69,'Guinea'),(70,'Guinea-Bissau'),(71,'Guyana'),(72,'Haiti'),(73,'Holy See'),(74,'Honduras'),(75,'Hungary'),(76,'Iceland'),(77,'India'),(78,'Indonesia'),(79,'Iran'),(80,'Iraq'),(81,'Ireland'),(82,'Israel'),(83,'Italy'),(84,'Jamaica'),(85,'Japan'),(86,'Jordan'),(87,'Kazakhstan'),(88,'Kenya'),(89,'Kiribati'),(90,'Kuwait'),(91,'Kyrgyzstan'),(92,'Laos'),(93,'Latvia'),(94,'Lebanon'),(95,'Lesotho'),(96,'Liberia'),(97,'Libya'),(98,'Liechtenstein'),(99,'Lithuania'),(100,'Luxembourg'),(101,'Madagascar'),(102,'Malawi'),(103,'Malaysia'),(104,'Maldives'),(105,'Mali'),(106,'Malta'),(107,'Marshall Islands'),(108,'Mauritania'),(109,'Mauritius'),(110,'Mexico'),(111,'Micronesia'),(112,'Moldova'),(113,'Monaco'),(114,'Mongolia'),(115,'Montenegro'),(116,'Morocco'),(117,'Mozambique'),(118,'Myanmar (formerly Burma)'),(119,'Namibia'),(120,'Nauru'),(121,'Nepal'),(122,'Netherlands'),(123,'New Zealand'),(124,'Nicaragua'),(125,'Niger'),(126,'Nigeria'),(127,'North Korea'),(128,'North Macedonia (formerly Macedonia)'),(129,'Norway'),(130,'Oman'),(131,'Pakistan'),(132,'Palau'),(133,'Panama'),(134,'Papua New Guinea'),(135,'Paraguay'),(136,'Peru'),(137,'Philippines'),(138,'Poland'),(139,'Portugal'),(140,'Qatar'),(141,'Romania'),(142,'Russia'),(143,'Rwanda'),(144,'Saint Kitts and Nevis'),(145,'Saint Lucia'),(146,'Saint Vincent and the Grenadines'),(147,'Samoa'),(148,'San Marino'),(149,'Sao Tome and Principe'),(150,'Saudi Arabia'),(151,'Senegal'),(152,'Serbia'),(153,'Seychelles'),(154,'Sierra Leone'),(155,'Singapore'),(156,'Slovakia'),(157,'Slovenia'),(158,'Solomon Islands'),(159,'Somalia'),(160,'South Africa'),(161,'South Korea'),(162,'South Sudan'),(163,'Spain'),(164,'Sri Lanka'),(165,'Sudan'),(166,'Suriname'),(167,'Sweden'),(168,'Switzerland'),(169,'Syria'),(170,'Tajikistan'),(171,'Tanzania'),(172,'Thailand'),(173,'Timor-Leste'),(174,'Togo'),(175,'Tonga'),(176,'Trinidad and Tobago'),(177,'Tunisia'),(178,'Turkey'),(179,'Turkmenistan'),(180,'Tuvalu'),(181,'Uganda'),(182,'Ukraine'),(183,'United Arab Emirates'),(184,'United Kingdom'),(185,'United States of America'),(186,'Uruguay'),(187,'Uzbekistan'),(188,'Vanuatu'),(189,'Venezuela'),(190,'Vietnam'),(191,'Yemen'),(192,'Zambia'),(193,'Zimbabwe');
/*!40000 ALTER TABLE `countries` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `likedvacations`
--

DROP TABLE IF EXISTS `likedvacations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `likedvacations` (
  `userId` int NOT NULL,
  `vacationId` int NOT NULL,
  KEY `userId_idx` (`userId`),
  KEY `vacationId_idx` (`vacationId`),
  CONSTRAINT `userId` FOREIGN KEY (`userId`) REFERENCES `users` (`userId`),
  CONSTRAINT `vacationId` FOREIGN KEY (`vacationId`) REFERENCES `vacations` (`vacationId`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `likedvacations`
--

LOCK TABLES `likedvacations` WRITE;
/*!40000 ALTER TABLE `likedvacations` DISABLE KEYS */;
/*!40000 ALTER TABLE `likedvacations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `roles`
--

DROP TABLE IF EXISTS `roles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `roles` (
  `roleId` int NOT NULL AUTO_INCREMENT,
  `roleName` varchar(45) NOT NULL,
  PRIMARY KEY (`roleId`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `roles`
--

LOCK TABLES `roles` WRITE;
/*!40000 ALTER TABLE `roles` DISABLE KEYS */;
INSERT INTO `roles` VALUES (1,'Admin'),(2,'User');
/*!40000 ALTER TABLE `roles` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `userId` int NOT NULL AUTO_INCREMENT,
  `firstName` varchar(45) NOT NULL,
  `lastName` varchar(45) NOT NULL,
  `email` varchar(100) NOT NULL,
  `password` varchar(150) NOT NULL,
  `roleId` int NOT NULL,
  PRIMARY KEY (`userId`),
  KEY `roleId_idx` (`roleId`),
  CONSTRAINT `roleId` FOREIGN KEY (`roleId`) REFERENCES `roles` (`roleId`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (21,'Jonathan','Zamanski','jonathan.zamanski@gmail.com','9f86b380d0943e9c4b15627e09e19a82944304e58e35147a3328f8b7c3bb2d6d65e3afd866d13593ede01a98351fd06ac6f4c28d51b3ad5fdb3786628df647e6',1),(22,'Wade','Wilson','wade@yahoo.com','cf0c2163a9477da3cd85bed2135434f03cfe693310b4a8f8c084e5571423ea735f568917be0aaa3566dea87381b7ba41975356b4578a02b87d25beae9a2d0c30',2),(23,'Fiona','Gallahger','fifi@gmail.com','520eb5a653c5490b7db2306d6b9c9003e92890395e4a1257df584601f181047f597658cb9d75ec01c43bf6e187ca9cd84477e20c0f5c469e60b09f5336b26459',2),(24,'Brian','Griffin','brain123543@yahoo.co.il','e8afd32c33f11d371a2854366fc6d8f3e78e1a3637a6354b5a12e59b77dd3384ecfecc64c7500802d5a9866da9f54f85c17a83bb56e092cd5f87f8020d05fea8',2),(25,'Bobby','Peanut','bobby.peanut@gmail.com','beab2c435cc9c398c43ac07bb9d5f327404be9d0cef9aefa34f79c091b6669d7637f244e24a6191e71d3a09ba9215b60120445ad550d6c988f4620c0742bc232',2);
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vacations`
--

DROP TABLE IF EXISTS `vacations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `vacations` (
  `vacationId` int NOT NULL AUTO_INCREMENT,
  `countryId` int NOT NULL,
  `vacationDescription` varchar(800) NOT NULL,
  `vacationStartDate` date NOT NULL,
  `vacationEndDate` date NOT NULL,
  `vacationPrice` int NOT NULL,
  `photoFileName` varchar(255) NOT NULL,
  PRIMARY KEY (`vacationId`),
  KEY `countryId_idx` (`countryId`),
  CONSTRAINT `countryId` FOREIGN KEY (`countryId`) REFERENCES `countries` (`countryId`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE=InnoDB AUTO_INCREMENT=45 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vacations`
--

LOCK TABLES `vacations` WRITE;
/*!40000 ALTER TABLE `vacations` DISABLE KEYS */;
INSERT INTO `vacations` VALUES (2,72,'Relax and unwind on a luxury cruise through the crystal-clear waters of the Caribbean, visiting multiple islands along the way.','2026-04-17','2026-04-17',1230,'7ec3b08b-d902-41fd-b7a7-fd926e37ec1f.jpg'),(3,167,'Come visit the royal palace with a chance to win a signed sword from the swedish king Carl XVI Gustaf! And that\'s not all! Abba is in town and whoemever gets the sword can expirience a free concert with all the original members in a private concert at the Radisson Blu Waterfront Hotel! Afterwords a session of autographs and a Q&A with the band and the best quality of local food! Will you be the one to be crowned with an abba concert? Only one way to find out! come to sweden today!','2026-06-05','2026-06-12',8666,'677d2a93-b0ec-41a1-b311-9060ccedd11d.png'),(5,32,'Hit the slopes in world-renowned ski resorts such as Whistler Blackcomb in British Columbia or Banff in Alberta.','2026-10-10','2026-10-17',2700,'e38bdc4b-d137-4966-8368-410fb0940cce.png'),(7,44,'Wander through the charming streets of Prague, visiting historic landmarks such as Prague Castle and Charles Bridge.','2029-06-01','2029-07-01',1500,'99aa0880-b5c8-4fd5-9070-61a454421f05.png'),(9,136,'Explore the ancient ruins of Machu Picchu, hike the Inca Trail, and discover the vibrant culture of Peru.','2027-06-05','2027-06-12',3442,'4308732e-eec0-40f0-8517-a354ff47d5ac.png'),(10,123,'Embark on an epic road trip across New Zealand, exploring stunning landscapes, fjords, and Maori culture.','2027-08-20','2027-08-27',2800,'4c797a6f-ec7c-4656-b0ef-90c82a4230e1.jpg'),(11,78,'Rejuvenate your mind, body, and soul with yoga, meditation, and spa treatments in the tranquil surroundings of Bali.','2025-10-10','2025-10-17',3200,'f94408fb-7887-444e-b498-b6379d010409.jpg'),(12,129,'Sail through breathtaking fjords, admire cascading waterfalls, and witness the stunning natural beauty of Norway.','2028-01-15','2028-01-22',2700,'4ef619f1-88d6-4db0-acff-eddaf8f03b2b.jpg'),(35,168,'Experience the country with beautiful cold landscapes, fresh rivers and the best chocolate in the world!','2024-10-02','2024-10-29',6190,'07cd1407-31a3-4764-8da6-ed7759863586.png'),(37,76,'Explore the otherworldly landscapes of Iceland, including waterfalls, glaciers and the greenest landscape you\'ve ever seen! Experience the beautiful sights of the aurora borealis in a once in a lifetime expirience at the Reykjavik northen lights show! Meet our wonderfull snowboarding experts that can show you a once in a lifetime pinguin snowboarding show! And that\'s not all! Try unique dishes like Hakarl and Plokkfiskur with the freshest fish you will ever eat at prices that are guaranteed to be cheaper than home!','2024-08-30','2024-08-31',598,'169d7d9c-9ca8-4e01-96e3-d621522aa3c2.png'),(41,9,'Come visit the famous Sydney Opera House to see the world famous Phantom of the Opera with the original cast!','2027-07-29','2027-08-11',1461,'281858d8-eae5-4140-9bac-b39ebb717ca6.png'),(44,137,'come for an underground river tour through a mesmerizing cave system, complete with audio guides and the chance to spot wildlife amidst stunning mountain scenery. Enjoy serene boat rides and natural wonders.','2024-11-29','2024-12-06',1736,'2f9a950c-ca77-40ee-a8e3-3d3c47986174.jpg');
/*!40000 ALTER TABLE `vacations` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-08-27 12:57:35
