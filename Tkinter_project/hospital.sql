-- MySQL dump 10.13  Distrib 8.0.23, for Win64 (x86_64)
--
-- Host: localhost    Database: hospital
-- ------------------------------------------------------
-- Server version	8.0.23

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
-- Table structure for table `info`
--

DROP TABLE IF EXISTS `info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `info` (
  `id` varchar(50) NOT NULL,
  `name` varchar(45) NOT NULL,
  `phone` varchar(45) NOT NULL,
  `address` varchar(100) NOT NULL,
  `admit` varchar(45) NOT NULL,
  `days` varchar(45) NOT NULL,
  `discharge` varchar(45) NOT NULL,
  `dname` varchar(45) DEFAULT NULL,
  `dvisitcharge` varchar(45) DEFAULT NULL,
  `tablet` varchar(45) DEFAULT NULL,
  `ward` varchar(45) DEFAULT NULL,
  `discriptions` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`,`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `info`
--

LOCK TABLES `info` WRITE;
/*!40000 ALTER TABLE `info` DISABLE KEYS */;
INSERT INTO `info` VALUES ('34','asfg','7463476','dfe\n','5/25/21','76','5/25/21','Sdqe','56','zdfg','Sed','WEed\n'),('76','cgh','7875645632','rdtyfui\n','6/2/21','7','6/17/21','dfty','700','fgd','9099','cdtfgdt\n'),('99','zshtdy','zfs','srfgfs\n','5/27/21','sers','5/27/21','uyi','tye5y','fghfy','uiy','tryt\n');
/*!40000 ALTER TABLE `info` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `log`
--

DROP TABLE IF EXISTS `log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `log` (
  `username` varchar(50) DEFAULT NULL,
  `password` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `log`
--

LOCK TABLES `log` WRITE;
/*!40000 ALTER TABLE `log` DISABLE KEYS */;
INSERT INTO `log` VALUES ('admin','123');
/*!40000 ALTER TABLE `log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `log1`
--

DROP TABLE IF EXISTS `log1`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `log1` (
  `username` varchar(50) DEFAULT NULL,
  `password` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `log1`
--

LOCK TABLES `log1` WRITE;
/*!40000 ALTER TABLE `log1` DISABLE KEYS */;
INSERT INTO `log1` VALUES ('sofi','123'),('admin','123'),('admin','123');
/*!40000 ALTER TABLE `log1` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `logg`
--

DROP TABLE IF EXISTS `logg`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `logg` (
  `username` varchar(50) DEFAULT NULL,
  `password` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `logg`
--

LOCK TABLES `logg` WRITE;
/*!40000 ALTER TABLE `logg` DISABLE KEYS */;
INSERT INTO `logg` VALUES ('pims','123'),('jipmer','123'),('rajiv gandhi hospital','123'),('admin','123');
/*!40000 ALTER TABLE `logg` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `management`
--

DROP TABLE IF EXISTS `management`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `management` (
  `name` varchar(50) NOT NULL,
  `location` varchar(50) DEFAULT NULL,
  `address` varchar(50) DEFAULT NULL,
  `date` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `management`
--

LOCK TABLES `management` WRITE;
/*!40000 ALTER TABLE `management` DISABLE KEYS */;
INSERT INTO `management` VALUES ('','','',''),('','','',''),('aerftw','adrfAE','ASDF','12/05/2021'),('aerftw','adrfAE','ASDF','12/05/2021'),('dsa','as','yuhi\n','5/22/21'),('srm','chennai','chennai,\n600032\n','5/11/21'),('ete','fgs','xfg\n','5/6/21'),('rfedtry','ghfryt','tydtr\n','5/7/21'),('srm','chennai','srrg\n','5/25/21'),('srm','chennai','east costal,\nchennai,\n6000005.\n','6/2/21'),('sd','wqed','wqe\n','6/11/21'),('sd','wqed','wqe\n','6/11/21'),('pims','puducherry','puducherry\n','6/12/21'),('pims','puducherry','kalapet,\npududcherry,\n605014.\n','6/12/21'),('pims','puducherry','kalapet,\npuducherry,\n605014.\n','6/12/21'),('pims','puducherry','kalapet,puducherry,\n605014.\n','6/12/21'),('xxx','chennai','no.25, ECR,\nChennai\n','7/23/21'),('pims','puducheery','nill\n','10/8/21'),('sss','puducherry','nil\n','10/1/21'),('sxy','puducherry','nil\n','10/8/21');
/*!40000 ALTER TABLE `management` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pat`
--

DROP TABLE IF EXISTS `pat`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pat` (
  `id` varchar(50) NOT NULL,
  `name` varchar(50) DEFAULT NULL,
  `contact` varchar(50) DEFAULT NULL,
  `dob` varchar(50) DEFAULT NULL,
  `gender` varchar(50) DEFAULT NULL,
  `blood` varchar(50) DEFAULT NULL,
  `aadhar` varchar(50) NOT NULL,
  `address` varchar(100) DEFAULT NULL,
  `disease` varchar(50) DEFAULT NULL,
  `date` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`,`aadhar`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pat`
--

LOCK TABLES `pat` WRITE;
/*!40000 ALTER TABLE `pat` DISABLE KEYS */;
INSERT INTO `pat` VALUES ('','','','','','','','','',''),('00','xx','6812763894','7/9/21','Female','b+ve','68912370`29','dsf\n','sdzfxawd\n','7/23/21'),('22','jhjgtyr','75453658989','5/22/21','male','b+ve','5786098956334','tystrst\n','tugfrty\n','5/7/21'),('23','jhjgtyr','75453658989','5/22/21','male','b+ve','5786098956334','tystrst\n','tugfrty\n','5/7/21'),('44','asrfgf','253765t45','5/24/21','trty','sfg','asrg','arg\n','srg\n','5/24/21'),('45','xxx','76883988455','5/25/21','male','b+ve','38976897235','rwsgtet\n','setrf\n','5/24/21'),('56','dty','7890654321','6/3/21','Female','b+ve','78906434216','puducherry\n','dtrftyf\n','6/3/21'),('65','bjhgdf','6789054321','5/25/21','male','b','7689053321','frrw\n','hfaeui\n','5/25/21'),('66','xxx','9807654321','10/8/21','Male','a+ve','89078655343','puducherry','xxx\n','10/8/21');
/*!40000 ALTER TABLE `pat` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-12-30 13:18:43
