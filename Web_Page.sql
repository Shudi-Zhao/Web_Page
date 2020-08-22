-- MySQL dump 10.13  Distrib 8.0.19, for macos10.15 (x86_64)
--
-- Host: mydatabase.clslb5ktpqun.us-east-1.rds.amazonaws.com    Database: mydatabase
-- ------------------------------------------------------
-- Server version	5.7.30-log

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
SET @MYSQLDUMP_TEMP_LOG_BIN = @@SESSION.SQL_LOG_BIN;
SET @@SESSION.SQL_LOG_BIN= 0;

--
-- GTID state at the beginning of the backup 
--

SET @@GLOBAL.GTID_PURGED=/*!80000 '+'*/ '';

--
-- Table structure for table `Account`
--

DROP TABLE IF EXISTS `Account`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Account` (
  `Type` char(20) NOT NULL,
  `user_name` char(100) DEFAULT NULL,
  `email` varchar(100) NOT NULL,
  `password` char(100) DEFAULT NULL,
  `date` date DEFAULT NULL,
  PRIMARY KEY (`Type`,`email`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Account`
--

LOCK TABLES `Account` WRITE;
/*!40000 ALTER TABLE `Account` DISABLE KEYS */;
INSERT INTO `Account` VALUES ('Customer','aaa','aaa@gmail.com','$2b$12$jR6XQLtdH0L.zWqR9ul4W.7ZBn1/jBA0/s8sXentiFhSW8Z79iQsi','2020-08-14'),('Customer','abc','abc@gmail.com','$2b$12$YDgi1JxI3ld5nDiHjC4Al.ay8smmRdJjWotEgSRAyJirS7EKUpU/y','2020-08-14'),('Customer','Genghua','genghua@gmail.com','$2b$12$6r.bp0Plg00DRjA5q1/gOe5Yu3pkC00Of.lJ9ppSapVoju8cdEPZ2','2020-08-09'),('Customer','denial','hehe@gmail.com','$2b$12$qW6ZsPz.ubM8tPAD9qe6B.q69JLD2Fi3NpEOACI00lizxO80dWe4W','2020-08-14'),('Customer','michael','michael@shudiLooksLikeAMushroom.com','$2b$12$7ToPtAqRpW.6lpQ/hRBxLevgu.iDkayJmN.lkRvw1W.yCxRagmwfm','2020-08-14'),('Customer','Sam','Sam@gmail.com','$2b$12$ZUMvLuNVMCmcPZIqQ2zzJuYIyCt.xDLIIKM/T0HI.c29ercI0pTtO','2020-08-11'),('Customer','shudi','shudizhao923@gmail.com','$2b$12$yxM1Cte88eDxMizDDSMnreO1KwSb4qaHrCMj/4JNfk01Ikfo/g2bG','2020-07-02'),('Customer','Steve','steve@gmail.com','$2b$12$Lj.iNvWLLMNT918/Z9bWEucsbdG6d9Mkhh6bzVIr.GGhB/DjkixFG','2020-08-13'),('Customer','suman','suman.s@ntdtv.com','$2b$12$DVPQv3DT1IX4B/POO9aaTuKhN/ccB4gvz7MRHSmPiJcBY4a1FC9oe','2020-08-14'),('Customer','Tony','tony@gmail.com','$2b$12$hMDzi3S7NaWIDJTshP/.iuJB5LRK53T6Yw.WogwRaZb0t.jqQWDae','2020-08-12'),('Employee','Shudi','shudizhao923@gmail.com','$2b$12$X62Vq5Zn3qy9Rlll1hM74.Rjf5504dOrL5eO4tMzQPB3336pN19Hi','2020-07-28'),('Employee','Zeyu','zeyu@gmail.com','$2b$12$6P5qjJ5g3DoYoAydlAVeJuS6eiP8i4MUSH4CA.mxJ92W15pVF2Eyi','2020-08-12');
/*!40000 ALTER TABLE `Account` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Airports`
--

DROP TABLE IF EXISTS `Airports`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Airports` (
  `airport_id` char(20) NOT NULL,
  `name` char(100) DEFAULT NULL,
  `city` char(20) DEFAULT NULL,
  `Country` char(20) DEFAULT NULL,
  PRIMARY KEY (`airport_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Airports`
--

LOCK TABLES `Airports` WRITE;
/*!40000 ALTER TABLE `Airports` DISABLE KEYS */;
INSERT INTO `Airports` VALUES ('DFW','Dallas/Fort Worth International Airport','Dallas','United States'),('EWR','Newark Liberty International Airport','Newark','United States'),('LAX','Los Angeles International Airport','Los Angeles','United States'),('LGA','LaGuardia Airport','New York','United States'),('ORD','O\'Hare International Airport','Chicago','United the States');
/*!40000 ALTER TABLE `Airports` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Customer`
--

DROP TABLE IF EXISTS `Customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Customer` (
  `first_name` char(20) NOT NULL,
  `email` char(30) NOT NULL,
  `last_name` char(20) DEFAULT NULL,
  `Address` char(20) DEFAULT NULL,
  `city` char(20) DEFAULT NULL,
  `state` char(20) DEFAULT NULL,
  `zip_code` int(11) DEFAULT NULL,
  `credit_card` int(11) DEFAULT NULL,
  `telephone` int(11) DEFAULT NULL,
  PRIMARY KEY (`first_name`,`email`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Customer`
--

LOCK TABLES `Customer` WRITE;
/*!40000 ALTER TABLE `Customer` DISABLE KEYS */;
INSERT INTO `Customer` VALUES ('Shudi','shudizhao923@gmail.com','Zhao','14 Jason Pl','Middletown','NY',10940,2147483647,2147483647);
/*!40000 ALTER TABLE `Customer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Employee`
--

DROP TABLE IF EXISTS `Employee`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Employee` (
  `first_name` char(100) DEFAULT NULL,
  `last_name` char(100) DEFAULT NULL,
  `email` char(100) DEFAULT NULL,
  `SSN` char(100) NOT NULL,
  `Address` char(100) DEFAULT NULL,
  `city` char(100) DEFAULT NULL,
  `state` char(100) DEFAULT NULL,
  `zip_code` int(11) DEFAULT NULL,
  `telephone` int(11) DEFAULT NULL,
  `start_date` char(100) DEFAULT NULL,
  `hourly_rate` int(11) DEFAULT NULL,
  `password` char(20) DEFAULT NULL,
  PRIMARY KEY (`SSN`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Employee`
--

LOCK TABLES `Employee` WRITE;
/*!40000 ALTER TABLE `Employee` DISABLE KEYS */;
INSERT INTO `Employee` VALUES ('Shudi','Zhao','shudizhao923@gmail.com','000000001','14 Jason Pl','Middletown','NY',10940,2147483647,'2020-08-09',66,'123456'),('Zeyu','Guan','zeyu@gmail.com','000000003','Jason Pl','Middletown','NY',10940,1234567890,'2020-08-12',30,'123456');
/*!40000 ALTER TABLE `Employee` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Flight`
--

DROP TABLE IF EXISTS `Flight`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Flight` (
  `airline_id` char(20) NOT NULL,
  `flight_num` char(20) NOT NULL,
  `airlines` char(20) DEFAULT NULL,
  `num_seat` int(11) DEFAULT NULL,
  `day_of_week` int(11) DEFAULT NULL,
  PRIMARY KEY (`airline_id`,`flight_num`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Flight`
--

LOCK TABLES `Flight` WRITE;
/*!40000 ALTER TABLE `Flight` DISABLE KEYS */;
INSERT INTO `Flight` VALUES ('001','0001','United',NULL,NULL),('002','0002','Delta',NULL,NULL),('003','0003','American',NULL,NULL),('004','0231','United',NULL,NULL),('005','0563','Delta',NULL,NULL),('006','0671','American',NULL,NULL),('007','0021','United',NULL,NULL),('008','0031','Delta',NULL,NULL),('009','0012','American',NULL,NULL),('010','0049','United',NULL,NULL),('011','0056','Delta',NULL,NULL),('012','0078','American',NULL,NULL),('013','0220','United',NULL,NULL),('014','0327','Delta',NULL,NULL),('015','0578','American',NULL,NULL),('016','3451','United',NULL,NULL),('017','4512','Delta',NULL,NULL),('018','6894','American',NULL,NULL),('019','1257','United',NULL,NULL),('020','3468','Delta',NULL,NULL),('021','7612','American',NULL,NULL),('022','9745','United',NULL,NULL),('023','5347','Delta',NULL,NULL),('024','5721','American',NULL,NULL);
/*!40000 ALTER TABLE `Flight` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Reserve`
--

DROP TABLE IF EXISTS `Reserve`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Reserve` (
  `airport_id` char(20) NOT NULL,
  `airline_name` char(20) NOT NULL,
  `flight_num` char(20) NOT NULL,
  `meal` char(20) DEFAULT NULL,
  `seat` char(20) DEFAULT NULL,
  `user` char(100) DEFAULT NULL,
  `dep_date` date DEFAULT NULL,
  `arr_date` date DEFAULT NULL,
  `to_airport` char(20) DEFAULT NULL,
  `dep_time` time DEFAULT NULL,
  `arr_time` time DEFAULT NULL,
  `price` int(11) DEFAULT NULL,
  `seat_num` int(11) NOT NULL,
  PRIMARY KEY (`flight_num`,`airline_name`,`airport_id`,`seat_num`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Reserve`
--

LOCK TABLES `Reserve` WRITE;
/*!40000 ALTER TABLE `Reserve` DISABLE KEYS */;
INSERT INTO `Reserve` VALUES ('LGA','United','0001','sandwich','window','shudizhao923@gmail.com','2020-09-01','2020-09-01','ORD','12:20:00','15:10:00',323,1),('LGA','United','0001','lobster','middle','shudizhao923@gmail.com','2020-09-01','2020-09-01','ORD','12:20:00','15:10:00',323,2),('LGA','United','0001','sandwich','aisle','suman.s@ntdtv.com','2020-09-01','2020-09-01','ORD','12:20:00','15:10:00',323,3),('LGA','Delta','0002','lobster','aisle','shudizhao923@gmail.com','2020-09-01','2020-09-01','ORD','17:20:00','20:30:00',89,2),('LGA','Delta','0002','steak','window','Sam@gmail.com','2020-09-01','2020-09-01','ORD','17:20:00','20:30:00',89,3),('LGA','American','0003','salad','middle','genghua@gmail.com','2020-09-01','2020-09-01','ORD','09:45:00','13:00:00',189,2),('LGA','American','0003','lobster','window','shudizhao923@gmail.com','2020-09-01','2020-09-01','ORD','09:45:00','13:00:00',189,3),('LGA','United','0231','shirmp','window','Sam@gmail.com','2020-09-09','2020-09-09','ORD','12:20:00','15:10:00',303,2);
/*!40000 ALTER TABLE `Reserve` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Stop`
--

DROP TABLE IF EXISTS `Stop`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Stop` (
  `airport_id` char(20) NOT NULL,
  `dep_date` date DEFAULT NULL,
  `arr_date` date DEFAULT NULL,
  `airline_name` char(20) NOT NULL,
  `flight_num` char(20) NOT NULL,
  `from_airport` char(20) DEFAULT NULL,
  `to_airport` char(20) DEFAULT NULL,
  `dep_time` time DEFAULT NULL,
  `arr_time` time DEFAULT NULL,
  `price` int(11) DEFAULT NULL,
  `seat_num` int(11) NOT NULL,
  PRIMARY KEY (`airport_id`,`airline_name`,`flight_num`,`seat_num`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Stop`
--

LOCK TABLES `Stop` WRITE;
/*!40000 ALTER TABLE `Stop` DISABLE KEYS */;
INSERT INTO `Stop` VALUES ('DFW','2020-10-20','2020-10-20','American','5721','DFW','LAX','10:45:00','13:00:00',239,1),('DFW','2020-10-20','2020-10-20','American','5721','DFW','LAX','10:45:00','13:00:00',239,2),('DFW','2020-10-20','2020-10-20','American','5721','DFW','LAX','10:45:00','13:00:00',239,3),('DFW','2020-10-20','2020-10-20','American','5721','DFW','LAX','10:45:00','13:00:00',239,4),('DFW','2020-10-20','2020-10-20','American','5721','DFW','LAX','10:45:00','13:00:00',239,5),('DFW','2020-10-20','2020-10-20','American','5721','DFW','LAX','10:45:00','13:00:00',239,6),('DFW','2020-10-18','2020-10-18','American','7612','DFW','LAX','09:45:00','13:00:00',211,1),('DFW','2020-10-18','2020-10-18','American','7612','DFW','LAX','09:45:00','13:00:00',211,2),('DFW','2020-10-18','2020-10-18','American','7612','DFW','LAX','09:45:00','13:00:00',211,3),('DFW','2020-10-18','2020-10-18','American','7612','DFW','LAX','09:45:00','13:00:00',211,4),('DFW','2020-10-18','2020-10-18','American','7612','DFW','LAX','09:45:00','13:00:00',211,5),('DFW','2020-10-18','2020-10-18','American','7612','DFW','LAX','09:45:00','13:00:00',211,6),('DFW','2020-10-18','2020-10-18','Delta','3468','DFW','LAX','17:20:00','20:30:00',100,1),('DFW','2020-10-18','2020-10-18','Delta','3468','DFW','LAX','17:20:00','20:30:00',100,2),('DFW','2020-10-18','2020-10-18','Delta','3468','DFW','LAX','17:20:00','20:30:00',100,3),('DFW','2020-10-18','2020-10-18','Delta','3468','DFW','LAX','17:20:00','20:30:00',100,4),('DFW','2020-10-18','2020-10-18','Delta','3468','DFW','LAX','17:20:00','20:30:00',100,5),('DFW','2020-10-18','2020-10-18','Delta','3468','DFW','LAX','17:20:00','20:30:00',100,6),('DFW','2020-10-20','2020-10-20','Delta','5347','DFW','LAX','17:20:00','20:30:00',133,1),('DFW','2020-10-20','2020-10-20','Delta','5347','DFW','LAX','17:20:00','20:30:00',133,2),('DFW','2020-10-20','2020-10-20','Delta','5347','DFW','LAX','17:20:00','20:30:00',133,3),('DFW','2020-10-20','2020-10-20','Delta','5347','DFW','LAX','17:20:00','20:30:00',133,4),('DFW','2020-10-20','2020-10-20','Delta','5347','DFW','LAX','17:20:00','20:30:00',133,5),('DFW','2020-10-20','2020-10-20','Delta','5347','DFW','LAX','17:20:00','20:30:00',133,6),('DFW','2020-10-18','2020-10-18','United','1257','DFW','LAX','12:20:00','15:10:00',548,1),('DFW','2020-10-18','2020-10-18','United','1257','DFW','LAX','12:20:00','15:10:00',548,2),('DFW','2020-10-18','2020-10-18','United','1257','DFW','LAX','12:20:00','15:10:00',548,3),('DFW','2020-10-18','2020-10-18','United','1257','DFW','LAX','12:20:00','15:10:00',548,4),('DFW','2020-10-18','2020-10-18','United','1257','DFW','LAX','12:20:00','15:10:00',548,5),('DFW','2020-10-18','2020-10-18','United','1257','DFW','LAX','12:20:00','15:10:00',548,6),('DFW','2020-10-20','2020-10-20','United','9745','DFW','LAX','12:20:00','15:10:00',666,1),('DFW','2020-10-20','2020-10-20','United','9745','DFW','LAX','12:20:00','15:10:00',666,2),('DFW','2020-10-20','2020-10-20','United','9745','DFW','LAX','12:20:00','15:10:00',666,3),('DFW','2020-10-20','2020-10-20','United','9745','DFW','LAX','12:20:00','15:10:00',666,4),('DFW','2020-10-20','2020-10-20','United','9745','DFW','LAX','12:20:00','15:10:00',666,5),('DFW','2020-10-20','2020-10-20','United','9745','DFW','LAX','12:20:00','15:10:00',666,6),('LAX','2020-09-20','2020-09-20','American','0578','LAX','DFW','09:45:00','13:00:00',416,1),('LAX','2020-09-20','2020-09-20','American','0578','LAX','DFW','09:45:00','13:00:00',416,2),('LAX','2020-09-20','2020-09-20','American','0578','LAX','DFW','09:45:00','13:00:00',416,3),('LAX','2020-09-20','2020-09-20','American','0578','LAX','DFW','09:45:00','13:00:00',416,4),('LAX','2020-09-20','2020-09-20','American','0578','LAX','DFW','09:45:00','13:00:00',416,5),('LAX','2020-09-20','2020-09-20','American','0578','LAX','DFW','09:45:00','13:00:00',416,6),('LAX','2020-09-23','2020-09-23','American','6894','LAX','DFW','09:45:00','13:00:00',246,1),('LAX','2020-09-23','2020-09-23','American','6894','LAX','DFW','09:45:00','13:00:00',246,2),('LAX','2020-09-23','2020-09-23','American','6894','LAX','DFW','09:45:00','13:00:00',246,3),('LAX','2020-09-23','2020-09-23','American','6894','LAX','DFW','09:45:00','13:00:00',246,4),('LAX','2020-09-23','2020-09-23','American','6894','LAX','DFW','09:45:00','13:00:00',246,5),('LAX','2020-09-23','2020-09-23','American','6894','LAX','DFW','09:45:00','13:00:00',246,6),('LAX','2020-09-20','2020-09-20','Delta','0327','LAX','DFW','17:20:00','20:30:00',125,1),('LAX','2020-09-20','2020-09-20','Delta','0327','LAX','DFW','17:20:00','20:30:00',125,2),('LAX','2020-09-20','2020-09-20','Delta','0327','LAX','DFW','17:20:00','20:30:00',125,3),('LAX','2020-09-20','2020-09-20','Delta','0327','LAX','DFW','17:20:00','20:30:00',125,4),('LAX','2020-09-20','2020-09-20','Delta','0327','LAX','DFW','17:20:00','20:30:00',125,5),('LAX','2020-09-20','2020-09-20','Delta','0327','LAX','DFW','17:20:00','20:30:00',125,6),('LAX','2020-09-23','2020-09-23','Delta','4512','LAX','DFW','17:20:00','20:30:00',53,1),('LAX','2020-09-23','2020-09-23','Delta','4512','LAX','DFW','17:20:00','20:30:00',53,2),('LAX','2020-09-23','2020-09-23','Delta','4512','LAX','DFW','17:20:00','20:30:00',53,3),('LAX','2020-09-23','2020-09-23','Delta','4512','LAX','DFW','17:20:00','20:30:00',53,4),('LAX','2020-09-23','2020-09-23','Delta','4512','LAX','DFW','17:20:00','20:30:00',53,5),('LAX','2020-09-23','2020-09-23','Delta','4512','LAX','DFW','17:20:00','20:30:00',53,6),('LAX','2020-09-20','2020-09-20','United','0220','LAX','DFW','12:20:00','18:10:00',566,1),('LAX','2020-09-20','2020-09-20','United','0220','LAX','DFW','12:20:00','18:10:00',566,2),('LAX','2020-09-20','2020-09-20','United','0220','LAX','DFW','12:20:00','18:10:00',566,3),('LAX','2020-09-20','2020-09-20','United','0220','LAX','DFW','12:20:00','18:10:00',566,4),('LAX','2020-09-20','2020-09-20','United','0220','LAX','DFW','12:20:00','18:10:00',566,5),('LAX','2020-09-20','2020-09-20','United','0220','LAX','DFW','12:20:00','18:10:00',566,6),('LAX','2020-09-23','2020-09-23','United','3451','LAX','DFW','12:20:00','15:10:00',674,1),('LAX','2020-09-23','2020-09-23','United','3451','LAX','DFW','12:20:00','15:10:00',674,2),('LAX','2020-09-23','2020-09-23','United','3451','LAX','DFW','12:20:00','15:10:00',674,3),('LAX','2020-09-23','2020-09-23','United','3451','LAX','DFW','12:20:00','15:10:00',674,4),('LAX','2020-09-23','2020-09-23','United','3451','LAX','DFW','12:20:00','15:10:00',674,5),('LAX','2020-09-23','2020-09-23','United','3451','LAX','DFW','12:20:00','15:10:00',674,6),('LGA','2020-09-01','2020-09-01','American','0003','LGA','ORD','09:45:00','13:00:00',189,1),('LGA','2020-09-01','2020-09-01','American','0003','LGA','ORD','09:45:00','13:00:00',189,4),('LGA','2020-09-01','2020-09-01','American','0003','LGA','ORD','09:45:00','13:00:00',189,5),('LGA','2020-09-01','2020-09-01','American','0003','LGA','ORD','09:45:00','13:00:00',189,6),('LGA','2020-09-09','2020-09-09','American','0671','LGA','ORD','09:45:00','13:00:00',168,1),('LGA','2020-09-09','2020-09-09','American','0671','LGA','ORD','09:45:00','13:00:00',168,2),('LGA','2020-09-09','2020-09-09','American','0671','LGA','ORD','09:45:00','13:00:00',168,3),('LGA','2020-09-09','2020-09-09','American','0671','LGA','ORD','09:45:00','13:00:00',168,4),('LGA','2020-09-09','2020-09-09','American','0671','LGA','ORD','09:45:00','13:00:00',168,5),('LGA','2020-09-09','2020-09-09','American','0671','LGA','ORD','09:45:00','13:00:00',168,6),('LGA','2020-09-01','2020-09-01','Delta','0002','LGA','ORD','17:20:00','20:30:00',89,1),('LGA','2020-09-01','2020-09-01','Delta','0002','LGA','ORD','17:20:00','20:30:00',89,4),('LGA','2020-09-09','2020-09-09','Delta','0563','LGA','ORD','17:20:00','20:30:00',76,1),('LGA','2020-09-09','2020-09-09','Delta','0563','LGA','ORD','17:20:00','20:30:00',76,2),('LGA','2020-09-09','2020-09-09','Delta','0563','LGA','ORD','17:20:00','20:30:00',76,3),('LGA','2020-09-09','2020-09-09','Delta','0563','LGA','ORD','17:20:00','20:30:00',76,4),('LGA','2020-09-09','2020-09-09','Delta','0563','LGA','ORD','17:20:00','20:30:00',76,5),('LGA','2020-09-01','2020-09-01','United','0001','LGA','ORD','12:20:00','15:10:00',323,4),('LGA','2020-09-09','2020-09-09','United','0231','LGA','ORD','12:20:00','15:10:00',303,1),('LGA','2020-09-09','2020-09-09','United','0231','LGA','ORD','12:20:00','15:10:00',303,3),('LGA','2020-09-09','2020-09-09','United','0231','LGA','ORD','12:20:00','15:10:00',303,4),('LGA','2020-09-09','2020-09-09','United','0231','LGA','ORD','12:20:00','15:10:00',303,5),('LGA','2020-09-09','2020-09-09','United','0231','LGA','ORD','12:20:00','15:10:00',303,6),('ORD','2020-09-13','2020-09-13','American','0012','ORD','LGA','09:45:00','13:00:00',189,1),('ORD','2020-09-13','2020-09-13','American','0012','ORD','LGA','09:45:00','13:00:00',189,2),('ORD','2020-09-13','2020-09-13','American','0012','ORD','LGA','09:45:00','13:00:00',189,3),('ORD','2020-09-13','2020-09-13','American','0012','ORD','LGA','09:45:00','13:00:00',189,4),('ORD','2020-09-13','2020-09-13','American','0012','ORD','LGA','09:45:00','13:00:00',189,5),('ORD','2020-09-15','2020-09-15','American','0078','ORD','LGA','09:45:00','15:00:00',189,1),('ORD','2020-09-15','2020-09-15','American','0078','ORD','LGA','09:45:00','15:00:00',189,2),('ORD','2020-09-15','2020-09-15','American','0078','ORD','LGA','09:45:00','15:00:00',189,3),('ORD','2020-09-15','2020-09-15','American','0078','ORD','LGA','09:45:00','15:00:00',189,4),('ORD','2020-09-15','2020-09-15','American','0078','ORD','LGA','09:45:00','15:00:00',189,5),('ORD','2020-09-15','2020-09-15','American','0078','ORD','LGA','09:45:00','15:00:00',189,6),('ORD','2020-09-13','2020-09-13','Delta','0031','ORD','LGA','17:20:00','20:30:00',99,1),('ORD','2020-09-13','2020-09-13','Delta','0031','ORD','LGA','17:20:00','20:30:00',99,2),('ORD','2020-09-13','2020-09-13','Delta','0031','ORD','LGA','17:20:00','20:30:00',99,3),('ORD','2020-09-13','2020-09-13','Delta','0031','ORD','LGA','17:20:00','20:30:00',99,4),('ORD','2020-09-13','2020-09-13','Delta','0031','ORD','LGA','17:20:00','20:30:00',99,5),('ORD','2020-09-13','2020-09-13','Delta','0031','ORD','LGA','17:20:00','20:30:00',99,6),('ORD','2020-09-15','2020-09-15','Delta','0056','ORD','LGA','17:20:00','20:30:00',99,1),('ORD','2020-09-15','2020-09-15','Delta','0056','ORD','LGA','17:20:00','20:30:00',99,2),('ORD','2020-09-15','2020-09-15','Delta','0056','ORD','LGA','17:20:00','20:30:00',99,3),('ORD','2020-09-15','2020-09-15','Delta','0056','ORD','LGA','17:20:00','20:30:00',99,4),('ORD','2020-09-15','2020-09-15','Delta','0056','ORD','LGA','17:20:00','20:30:00',99,5),('ORD','2020-09-15','2020-09-15','Delta','0056','ORD','LGA','17:20:00','20:30:00',99,6),('ORD','2020-09-13','2020-09-13','United','0021','ORD','LGA','12:20:00','15:10:00',465,1),('ORD','2020-09-13','2020-09-13','United','0021','ORD','LGA','12:20:00','15:10:00',465,2),('ORD','2020-09-13','2020-09-13','United','0021','ORD','LGA','12:20:00','15:10:00',465,3),('ORD','2020-09-13','2020-09-13','United','0021','ORD','LGA','12:20:00','15:10:00',465,4),('ORD','2020-09-13','2020-09-13','United','0021','ORD','LGA','12:20:00','15:10:00',465,5),('ORD','2020-09-15','2020-09-15','United','0049','ORD','LGA','12:20:00','15:10:00',465,0),('ORD','2020-09-15','2020-09-15','United','0049','ORD','LGA','12:20:00','15:10:00',465,1),('ORD','2020-09-15','2020-09-15','United','0049','ORD','LGA','12:20:00','15:10:00',465,2),('ORD','2020-09-15','2020-09-15','United','0049','ORD','LGA','12:20:00','15:10:00',465,3),('ORD','2020-09-15','2020-09-15','United','0049','ORD','LGA','12:20:00','15:10:00',465,4),('ORD','2020-09-15','2020-09-15','United','0049','ORD','LGA','12:20:00','15:10:00',465,5);
/*!40000 ALTER TABLE `Stop` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping events for database 'mydatabase'
--

--
-- Dumping routines for database 'mydatabase'
--
SET @@SESSION.SQL_LOG_BIN = @MYSQLDUMP_TEMP_LOG_BIN;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-08-22 12:25:30
