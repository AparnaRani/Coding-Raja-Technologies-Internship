-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: bot
-- ------------------------------------------------------
-- Server version	8.2.0

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
-- Table structure for table `que_table`
--

DROP TABLE IF EXISTS `que_table`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `que_table` (
  `QUESTION` char(200) DEFAULT NULL,
  `ANSWER` char(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `que_table`
--

LOCK TABLES `que_table` WRITE;
/*!40000 ALTER TABLE `que_table` DISABLE KEYS */;
INSERT INTO `que_table` VALUES ('What is the name of the parallel dimension inhabited by the Demogorgon?','The Upside Down'),('Who is Eleven\'s best friend and the first to encounter her in the Demogorgon?','Mike Wheeler'),('What is the name of the game that the kids play in the first season that helps them communicate with Will?','Dungeons & Dragons'),('What is the real name of the character known as \"Eleven\"?','Jane Hopper'),('Who is the police chef of Hawkins, Indiana, known for his dedication to finding Will Byers?','Jim Hopper'),('What does Will Byers use to communicate with his mother while trapped in the Upside Down?','Lights'),('Which character has the ability to move objects with their mind, known as telekinesis?','Eleven'),('What is the name of the monstrous creature that terrorizes the town of Hawkins in Season 1?','The Demogorgon'),('What is the name of the secretive government agency responsible for experiments on Eleven and the portal to the Upside Down?','Hawkins National Laboratory (HNL)'),('Which character is known for saying \"Friends don\'t lie\"?','Eleven');
/*!40000 ALTER TABLE `que_table` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-11-26  8:07:42
