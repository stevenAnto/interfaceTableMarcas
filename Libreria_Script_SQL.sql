CREATE DATABASE  IF NOT EXISTS `control_stock_libreria` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `control_stock_libreria`;
-- MySQL dump 10.13  Distrib 8.0.33, for Win64 (x86_64)
--
-- Host: localhost    Database: control_stock_libreria
-- ------------------------------------------------------
-- Server version	8.0.33

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
-- Table structure for table `gzz_empleado`
--

DROP TABLE IF EXISTS `gzz_empleado`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `gzz_empleado` (
  `EmpCod` int NOT NULL,
  `EmpNom` char(80) DEFAULT NULL,
  `EstRegCod` char(1) DEFAULT NULL,
  PRIMARY KEY (`EmpCod`),
  KEY `IX_Relationship21` (`EstRegCod`),
  CONSTRAINT `Relationship21` FOREIGN KEY (`EstRegCod`) REFERENCES `gzz_estado_registro` (`EstRegCod`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;



--
-- Table structure for table `gzz_estado_registro`
--

DROP TABLE IF EXISTS `gzz_estado_registro`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `gzz_estado_registro` (
  `EstRegCod` char(1) NOT NULL,
  `EstRegDes` char(40) DEFAULT NULL,
  `EstRegEstReg` char(1) DEFAULT NULL,
  PRIMARY KEY (`EstRegCod`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `gzz_estado_registro`
--

LOCK TABLES `gzz_estado_registro` WRITE;
/*!40000 ALTER TABLE `gzz_estado_registro` DISABLE KEYS */;
INSERT INTO `gzz_estado_registro` VALUES ('A','Activo','A'),('I','Inactivo','A'),('*','Eliminado','A');
/*!40000 ALTER TABLE `gzz_estado_registro` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `gzz_marca`
--

DROP TABLE IF EXISTS `gzz_marca`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `gzz_marca` (
  `MarCod` int NOT NULL,
  `MarNom` char(60) DEFAULT NULL,
  `MarEstReg` char(1) DEFAULT NULL,
  PRIMARY KEY (`MarCod`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;


--
-- Table structure for table `gzz_unidad_medida`
--

DROP TABLE IF EXISTS `gzz_unidad_medida`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `gzz_unidad_medida` (
  `UniMedCod` int NOT NULL,
  `UniMedNom` char(20) DEFAULT NULL,
  `EstRegCod` char(1) DEFAULT NULL,
  PRIMARY KEY (`UniMedCod`),
  KEY `IX_Relationship20` (`EstRegCod`),
  CONSTRAINT `Relationship20` FOREIGN KEY (`EstRegCod`) REFERENCES `gzz_estado_registro` (`EstRegCod`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;


--
-- Table structure for table `gzz_zona`
--

DROP TABLE IF EXISTS `gzz_zona`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `gzz_zona` (
  `ZonCod` int NOT NULL,
  `ZonDes` char(40) DEFAULT NULL,
  `ZonEstReg` char(1) DEFAULT NULL,
  PRIMARY KEY (`ZonCod`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;



--
-- Table structure for table `l1m_articulo`
--

DROP TABLE IF EXISTS `l1m_articulo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `l1m_articulo` (
  `ArtCod` int NOT NULL,
  `ArtNom` char(60) DEFAULT NULL,
  `ArtCan` int DEFAULT NULL,
  `ArtDes` char(60) DEFAULT NULL,
  `ArtEstReg` char(1) DEFAULT NULL,
  `ArtMar` int DEFAULT NULL,
  `UniMedCod` int DEFAULT NULL,
  PRIMARY KEY (`ArtCod`),
  KEY `IX_Relationship18` (`ArtEstReg`),
  KEY `IX_Relationship19` (`ArtMar`),
  KEY `IX_Relationship23` (`UniMedCod`),
  CONSTRAINT `Relationship18` FOREIGN KEY (`ArtEstReg`) REFERENCES `gzz_estado_registro` (`EstRegCod`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `Relationship19` FOREIGN KEY (`ArtMar`) REFERENCES `gzz_marca` (`MarCod`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `Relationship23` FOREIGN KEY (`UniMedCod`) REFERENCES `gzz_unidad_medida` (`UniMedCod`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;


--
-- Table structure for table `l1m_cliente`
--

DROP TABLE IF EXISTS `l1m_cliente`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `l1m_cliente` (
  `CliCod` int NOT NULL,
  `CliNom` char(60) DEFAULT NULL,
  `CliFecInsAño` int DEFAULT NULL,
  `CliFecInsMes` int DEFAULT NULL,
  `CliFecInsDia` int DEFAULT NULL,
  `CliDir` int DEFAULT NULL,
  `CliZon` int DEFAULT NULL,
  `CliEstReg` char(1) DEFAULT NULL,
  PRIMARY KEY (`CliCod`),
  KEY `IX_Relationship9` (`CliZon`),
  KEY `IX_Relationship10` (`CliEstReg`),
  CONSTRAINT `Relationship10` FOREIGN KEY (`CliEstReg`) REFERENCES `gzz_estado_registro` (`EstRegCod`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `Relationship9` FOREIGN KEY (`CliZon`) REFERENCES `gzz_zona` (`ZonCod`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;


--
-- Table structure for table `l1m_proveedor`
--

DROP TABLE IF EXISTS `l1m_proveedor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `l1m_proveedor` (
  `ProCod` int NOT NULL,
  `ProNom` char(60) DEFAULT NULL,
  `ProFecInsProAño` int DEFAULT NULL,
  `ProFecInsProMes` int DEFAULT NULL,
  `ProFecInsProDia` int DEFAULT NULL,
  `ProDir` char(20) DEFAULT NULL,
  `ProZon` int DEFAULT NULL,
  `ProEstReg` char(1) DEFAULT NULL,
  PRIMARY KEY (`ProCod`),
  KEY `IX_Relationship2` (`ProZon`),
  KEY `IX_Relationship4` (`ProEstReg`),
  CONSTRAINT `Relationship2` FOREIGN KEY (`ProZon`) REFERENCES `gzz_zona` (`ZonCod`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `Relationship4` FOREIGN KEY (`ProEstReg`) REFERENCES `gzz_estado_registro` (`EstRegCod`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;


--
-- Table structure for table `l1t_stock_entrada_cab`
--

DROP TABLE IF EXISTS `l1t_stock_entrada_cab`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `l1t_stock_entrada_cab` (
  `StoEntCabCod` int NOT NULL,
  `StoEntCabFecInsAño` int DEFAULT NULL,
  `StoEntCabFecInsMes` int DEFAULT NULL,
  `StoEntCabFecInsDia` int DEFAULT NULL,
  `StoEntCabPro` int DEFAULT NULL,
  `StoEntCanEstReg` char(1) DEFAULT NULL,
  `EmpCod` int DEFAULT NULL,
  PRIMARY KEY (`StoEntCabCod`),
  KEY `IX_Relationship3` (`StoEntCabPro`),
  KEY `IX_Relationship5` (`StoEntCanEstReg`),
  KEY `IX_Relationship22` (`EmpCod`),
  CONSTRAINT `Relationship22` FOREIGN KEY (`EmpCod`) REFERENCES `gzz_empleado` (`EmpCod`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `Relationship3` FOREIGN KEY (`StoEntCabPro`) REFERENCES `l1m_proveedor` (`ProCod`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `Relationship5` FOREIGN KEY (`StoEntCanEstReg`) REFERENCES `gzz_estado_registro` (`EstRegCod`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;


--
-- Table structure for table `l1t_stock_entrada_det`
--

DROP TABLE IF EXISTS `l1t_stock_entrada_det`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `l1t_stock_entrada_det` (
  `StoEntCabSec` int NOT NULL,
  `StoEntDetCan` int DEFAULT NULL,
  `StoEntCabCod` int DEFAULT NULL,
  `StoEntDetArt` int DEFAULT NULL,
  `StoEntCabEstReg` char(1) DEFAULT NULL,
  PRIMARY KEY (`StoEntCabSec`),
  KEY `IX_Relationship6` (`StoEntCabCod`),
  KEY `IX_Relationship7` (`StoEntDetArt`),
  KEY `IX_Relationship8` (`StoEntCabEstReg`),
  CONSTRAINT `Relationship6` FOREIGN KEY (`StoEntCabCod`) REFERENCES `l1t_stock_entrada_cab` (`StoEntCabCod`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `Relationship7` FOREIGN KEY (`StoEntDetArt`) REFERENCES `l1m_articulo` (`ArtCod`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `Relationship8` FOREIGN KEY (`StoEntCabEstReg`) REFERENCES `gzz_estado_registro` (`EstRegCod`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;


--
-- Table structure for table `l1t_stock_salida_cab`
--

DROP TABLE IF EXISTS `l1t_stock_salida_cab`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `l1t_stock_salida_cab` (
  `StoSalCabCod` int NOT NULL,
  `StoSalCabFecInsStoAño` int DEFAULT NULL,
  `StoSalCabFecInsStoMes` int DEFAULT NULL,
  `StoSalCabFecInsStoDia` int DEFAULT NULL,
  `StoSalCabCli` int DEFAULT NULL,
  `StoSalCabEstReg` char(1) DEFAULT NULL,
  `EmpCod` int DEFAULT NULL,
  PRIMARY KEY (`StoSalCabCod`),
  KEY `IX_Relationship11` (`StoSalCabCli`),
  KEY `IX_Relationship12` (`StoSalCabEstReg`),
  KEY `IX_Relationship24` (`EmpCod`),
  CONSTRAINT `Relationship24` FOREIGN KEY (`EmpCod`) REFERENCES `gzz_empleado` (`EmpCod`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `Relationship11` FOREIGN KEY (`StoSalCabCli`) REFERENCES `l1m_cliente` (`CliCod`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `Relationship12` FOREIGN KEY (`StoSalCabEstReg`) REFERENCES `gzz_estado_registro` (`EstRegCod`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;


--
-- Table structure for table `l1t_stock_salida_det`
--

DROP TABLE IF EXISTS `l1t_stock_salida_det`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `l1t_stock_salida_det` (
  `StoSalDetSec` int NOT NULL,
  `StoSalDetCan` int DEFAULT NULL,
  `StoSalCabCod` int DEFAULT NULL,
  `StoSalDetArt` int DEFAULT NULL,
  `StoSalCabEstReg` char(1) DEFAULT NULL,
  PRIMARY KEY (`StoSalDetSec`),
  KEY `IX_Relationship13` (`StoSalCabCod`),
  KEY `IX_Relationship14` (`StoSalDetArt`),
  KEY `IX_Relationship15` (`StoSalCabEstReg`),
  CONSTRAINT `Relationship13` FOREIGN KEY (`StoSalCabCod`) REFERENCES `l1t_stock_salida_cab` (`StoSalCabCod`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `Relationship14` FOREIGN KEY (`StoSalDetArt`) REFERENCES `l1m_articulo` (`ArtCod`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `Relationship15` FOREIGN KEY (`StoSalCabEstReg`) REFERENCES `gzz_estado_registro` (`EstRegCod`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;


--
-- Dumping routines for database 'control_stock_libreria'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-07-09 14:34:05
