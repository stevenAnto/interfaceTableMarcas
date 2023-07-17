INSERT INTO gzz_empleado (EmpCod, EmpNom, EstRegCod) VALUES
(1, 'Juan Pérez', 'A'),
(2, 'María Gómez', 'A'),
(3, 'Pedro Ramírez', 'A'),
--(4, 'Ana López', 'A'),
---(5, 'Carlos Rodríguez', 'A');

INSERT INTO gzz_zona (ZonCod, ZonDes, ZonEstReg) VALUES
(1, 'Norte', 'A'),
(2, 'Sur', 'A'),
(3, 'Este', 'A'),
(4, 'Oeste', 'A'),
(5, 'Centro', 'A');

INSERT INTO gzz_unidad_medida (UniMedCod, UniMedNom, EstRegCod) VALUES
(1, 'CAJ', 'A'),
(2, 'UND', 'A'),
(3, 'PAQUE', 'A'),
(4, 'BARR', 'A'),
(5, 'MILL', 'A');

INSERT INTO gzz_marca(MarCod,MarNom,MarEstReg) VALUES
 (1,'Faber-Castell','A'),
 (2,'Surco','A'),
 (3,'Maped','A'),
 (4,'Stabilo','A'),
 (5,'Pelikan','A'),
 (6,'Staedtler','A'),
 (7,'Pilot','A'),
 (8,'Pentel','A'),
 (9,'Uni-Ball','A'),
 (10,'Zebra','A'),
 (11,'Sharpie','A'),
 (12,'Crayola','A'),
 (13,'Giotto','A'),
 (14,'Scribe','A'),
 (15,'Oxford','A'),
 (16,'Rhodia','A'),
 (17,'Carioca','A'),
 (18,'Giotto','A'),
 (19,'Standford','A'),
 (20,'Alpha','A'),
 (21,'loro','A'),
 (22,'Norma','A'),
 (23,'Justus','A'),
 (24,'Minerva','A'),
 (25,'Layconsa','A'),
 (26,'Ricon','A'),
 (27,'Ove','A'),
 (28,'Artline','A'),
 (29,'David','A'),
 (30,'Millenium','A');


INSERT INTO l1m_proveedor (ProCod,ProNom,ProFecInsProAño,ProFecInsProMes,ProFecInsProDia,ProDir,ProZon,ProEstReg)VALUES (1,'Tai-Heng',2019,12,15,'Fro Velazco 106',1,'A');

INSERT INTO l1m_cliente (CliCod,CliNom,CliFecInsAño,CliFecInsMes,CliFecInsDia,CliDir,CliZon,CliEstReg)VALUES
(1,'Juan Perez',2023,20,19,206,1,'A'),
(2,'Maria Rodríguez',2023,20,19,306,2,'A'),
(3,'Pedor Gomez',2023,20,19,105,4,'A'),
(4,'Luisa Martinez',2023,20,19,210,1,'A'),
(5,'Calos Sanchez',2023,20,19,206,5,'A'),
(6,'Noah Johnson',2023,20,19,206,2,'A'),
(7,'Emma Williams',2023,20,19,206,2,'A'),
(8,'Liam Brown',2023,20,19,206,3,'A'),
(9,'Elijah Davis',2023,20,19,206,3,'A'),
(10,'Ava Jones',2023,20,19,206,4,'A'),
(11,'Oliver Wilson',2023,20,19,206,4,'A'),
(12,'Isabella taylos',2023,20,19,206,5,'A'),
(13,'Lucas Anderson',2023,20,19,206,4,'A'),
(14,'Aiden Thompson',2023,20,19,206,4,'A'),
(15,'Mia Martinez',2023,20,19,206,1,'A'),
(16,'Amelia Garcia',2023,20,19,206,2,'A'),
(17,'Cadena Hernandez',2023,20,19,206,1,'A'),
(18,'Harper Lopez',2023,20,19,206,1,'A'),
(19,'Grayson Gonzales',2023,20,19,206,3,'A'),
(20,'Evely Perez',2023,20,19,206,2,'A'),
(21,'Michael Robinson',2023,20,19,206,2,'A'),
(22,'Abigail Lewis',2023,20,19,206,3,'A'),
(23,'Mason Lee',2023,20,19,206,4,'A'),
(24,'Emily Scott',2023,20,19,206,2,'A'),
(25,'Alexander King',2023,20,19,206,3,'A'),
(26,'Charlotte Wright',2023,20,19,206,2,'A'),
(27,'Ethan White',2023,20,19,206,1,'A'),
(28,'Antony Aco',2023,20,19,206,5,'A'),
(29,'Bryan Hancco',2:e023,20,19,206,3,'A'),
(30,'Lorenzo Wolverine',2023,20,19,206,3,'A');


INSERT INTO l1t_stock_entrada_cab(StoEntCabCod,StoEntCabFecInsAño,StoEntCabFecInsMes,StoEntCabFecInsDia,StoEntCabPro,StoEntCanEstReg,EmpCod)VALUES
(101,2023,10,20,1,'A',3),
(102,2023,10,21,1,'A',1),
(103,2023,10,22,1,'A',2),
(104,2023,10,23,1,'A',3),
(105,2023,10,24,1,'A',3),
(106,2023,10,25,1,'A',1),
(107,2023,10,26,1,'A',1);

INSERT INTO l1m_articulo(ArtCod,ArtNom,ArtCan,ArtDes,ArtEstReg,ArtMar,UniMedCod)VALUES
(1,'Cuaderno A-4 c 80h',0,'Cuaderno','A',2,2),
(2,'Cuaderno A-4 a 80h',0,'Cuaderno','A',2,2),
(3,'Cuaderno A-4 e 80h',0,'Cuaderno','A',2,2),
(4,'Cuaderno A-4 c 160h',0,'Cuaderno','A',2,2),
(5,'Cuaderno A-4 a 160h',0,'Cuaderno','A',2,2),
(6,'Cuaderno A-4 c 110h',0,'Cuaderno','A',2,2),
(7,'Cuaderno A-4 a 110h',0,'Cuaderno','A',2,2),
(8,'Cuaderno A-4 e 110h',0,'Cuaderno','A',2,2),
(9,'Cuaderno A-5 c 80h',0,'Cuaderno','A',2,2),
(10,'Cuaderno A-5 a 80h',0,'Cuaderno','A',2,2),
(11,'Cuaderno A-5 e 80h',0,'Cuaderno','A',2,2),
(12,'Cuaderno A-5 c 160h',0,'Cuaderno','A',2,2),
(13,'Cuaderno A-5 a 160h',0,'Cuaderno','A',2,2),
(14,'Cuaderno A-5 c 110h',0,'Cuaderno','A',2,2),
(15,'Cuaderno A-5 a 110h',0,'Cuaderno','A',2,2),
(16,'Cuaderno A-5 e 110h',0,'Cuaderno','A',2,2),
(17,'Cuaderno A-4 c 80h',0,'Cuaderno','A',15,2),
(18,'Cuaderno A-4 a 80h',0,'Cuaderno','A',15,2),
(19,'Cuaderno A-4 e 80h',0,'Cuaderno','A',15,2),
(20,'Cuaderno A-4 c 160h',0,'Cuaderno','A',15,2),
(21,'Cuaderno A-4 a 160h',0,'Cuaderno','A',15,2),
(22,'Cuaderno A-4 c 110h',0,'Cuaderno','A',15,2),
(23,'Cuaderno A-4 a 110h',0,'Cuaderno','A',15,2),
(24,'Cuaderno A-4 e 110h',0,'Cuaderno','A',15,2),
(25,'Cuaderno A-5 c 80h',0,'Cuaderno','A',15,2),
(26,'Cuaderno A-5 a 80h',0,'Cuaderno','A',15,2),
(27,'Cuaderno A-5 e 80h',0,'Cuaderno','A',15,2),
(28,'Cuaderno A-5 c 160h',0,'Cuaderno','A',15,2),
(29,'Cuaderno A-5 a 160h',0,'Cuaderno','A',15,2),
(30,'Cuaderno A-5 c 110h',0,'Cuaderno','A',15,2),
(31,'Cuaderno A-5 a 110h',0,'Cuaderno','A',15,2),
(32,'Cuaderno A-5 e 110h',0,'Cuaderno','A',15,2);

INSERT INTO l1t_stock_entrada_det(StoEntCabSec,StoEntDetCan,StoEntCabCod,StoEntDetArt,StoEntCabEstReg) VALUES
(1,20,101,1,'A'),
(2,20,101,2,'A'),
(3,20,101,3,'A'),
(4,20,101,4,'A'),
(5,20,101,5,'A'),
(6,20,101,6,'A'),
(7,20,102,1,'A'),
(8,20,102,2,'A'),
(9,20,102,3,'A'),
(10,20,102,4,'A'),
(11,20,102,5,'A'),
(12,20,102,6,'A'),
(13,20,103,7,'A'),
(14,20,103,8,'A'),
(15,20,103,9,'A'),
(16,20,103,10,'A'),
(17,20,103,11,'A'),
(18,20,103,12,'A'),
(20,20,104,13,'A'),
(21,20,104,14,'A'),
(22,20,104,15,'A'),
(23,20,104,16,'A'),
(24,20,104,17,'A'),
(25,20,104,18,'A'),
(26,20,105,19,'A'),
(27,20,105,20,'A'),
(28,20,105,21,'A'),
(29,20,105,22,'A'),
(30,20,106,23,'A'),
(31,20,106,24,'A'),
(32,20,106,25,'A'),
(33,20,107,26,'A'),
(34,20,107,27,'A'),
(35,20,107,29,'A');

INSERT INTO l1t_stock_salida_cab(StoSalCabCod,StoSalCabFecInsStoAño,StoSalCabFecInsStoMes,StoSalCabFecInsStoDia,StoSalCabCli,StoSalCabEstReg,EmpCod)VALUES
(201,2023,10,27,9,'A',3),
(202,2023,10,28,11,'A',1),
(203,2023,10,29,10,'A',2),
(204,2023,10,30,15,'A',3),
(205,2023,10,31,1,'A',3),
(206,2023,11,1,18,'A',1),
(207,2023,11,1,18,'A',1);

INSERT INTO l1t_stock_salida_det(StoSalDetSec,StoSalDetCan,StoSalCabCod,StoSalDetArt,StoSalCabEstReg)VALUES
(1,1,201,1,'A'),
(2,2,201,2,'A'),
(3,2,201,3,'A'),
(4,2,201,4,'A'),
(5,3,201,5,'A'),
(6,4,201,6,'A'),
(7,2,202,1,'A'),
(8,1,202,2,'A'),
(9,1,202,3,'A'),
(10,1,202,4,'A'),
(11,2,202,5,'A'),
(12,6,202,6,'A'),
(13,12,203,7,'A'),
(14,5,203,8,'A'),
(15,3,203,9,'A'),
(16,2,203,10,'A'),
(17,12,203,11,'A'),
(18,12,203,12,'A'),
(20,1,204,13,'A'),
(21,12,204,14,'A'),
(22,6,204,15,'A'),
(23,6,204,16,'A'),
(24,1,204,17,'A'),
(25,6,204,18,'A'),
(26,5,205,19,'A'),
(27,3,205,20,'A'),
(28,12,205,21,'A'),
(29,6,205,22,'A'),
(30,12,206,23,'A'),
(31,12,206,24,'A'),
(32,6,206,25,'A'),
(33,1,207,26,'A'),
(34,1,207,27,'A'),
(35,2,207,29,'A');
--Otros--
--Script para mostrar tabla detalle, pero con el nombre del articulo
SELECT l1t_stock_salida_det.StoSalDetSec,l1t_stock_salida_det.StoSalDetCan,StoSalCabCod,l1m_articulo.ArtNom,StoSalCabEstReg
FROM l1m_articulo
INNER JOIN l1t_stock_salida_det
ON l1m_articulo.ArtCod=l1t_stock_salida_det.StoSalDetArt;

--Ver cliente por zonas
SELECT l1m_cliente.CliCod,l1m_cliente.CliNom,gzz_zona.ZonDes,l1m_cliente.CliEstReg
FROM l1m_cliente
INNER JOIN gzz_zona
ON l1m_cliente.CliZon=gzz_zona.ZonCod;

--Hacer un join de tres tablas
CREATE VIEW STOCK AS
SELECT l1m_articulo.ArtCod,l1m_articulo.ArtNom,l1m_articulo.ArtCan,l1m_proveedor.ProNom
FROM l1m_articulo
JOIN l1m_proveedor
ON





--Se creo vista de aritculos con proveedores
CREATE VIEW STOCKR AS
SELECT l1m_articulo.ArtCod,l1m_articulo.ArtNom,l1m_articulo.ArtCan,l1m_proveedor.ProNom
FROM l1m_articulo
JOIN l1m_proveedor
JOIN l1t_stock_entrada_cab
ON l1t_stock_entrada_cab.StoEntCabPro=l1m_proveedor.ProCod;

--Vista de Productos con proveedores
CREATE VIEW STOCK_PRO AS
SELECT DISTINCT ArtCod,ArtNom,ArtCan,ProNom
FROM STOCKR;

--Vista De total entradas
CREATE VIEW TOTAL_ENTRADA AS
SELECT StoEntDetArt, SUM(StoEntDetCan) AS Total_Ingresado
FROM l1t_stock_entrada_det
GROUP BY StoEntDetArt;
--Vista de total entradas con nombre
CREATE VIEW TOTAL_ENTRADA_NOM AS
SELECT TOTAL_ENTRADA.StoEntDetArt,l1m_articulo.ArtNom,TOTAL_ENTRADA.Total_Ingresado
FROM TOTAL_ENTRADA
JOIN l1m_articulo
ON TOTAL_ENTRADA.StoEntDetArt=l1m_articulo.ArtCod;
