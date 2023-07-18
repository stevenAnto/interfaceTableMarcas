--Otro
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

--total SALIDA
CREATE VIEW TOTAL_SALIDA AS
SELECT StoSalDetArt, SUM(StoSalDetCan) AS Total_Salida
FROM l1t_stock_salida_det
GROUP BY StoSalDetArt;
--Vista de total salidas con nombre
CREATE VIEW TOTAL_SALIDA_NOM AS
SELECT TOTAL_SALIDA.StoSalDetArt,l1m_articulo.ArtNom,TOTAL_SALIDA.Total_Salida
FROM TOTAL_SALIDA
JOIN l1m_articulo
ON TOTAL_SALIDA.StoSalDetArt=l1m_articulo.ArtCod;



--CREANDO TRIGGERS

--afectando entradas
DELIMITER //
CREATE TRIGGER ACTUALIZA_CANTIDAD_ENT
AFTER INSERT ON l1t_stock_entrada_det
FOR EACH ROW
BEGIN
  UPDATE l1m_articulo
  SET ArtCan = ArtCan + NEW.StoEntDetCan
  WHERE ArtCod = NEW.StoEntDetArt;
END;
//
DELIMITER ;

--afectando salidas
DELIMITER //
CREATE TRIGGER ACTUALIZA_CANTIDAD_SAL
AFTER INSERT ON l1t_stock_salida_det
FOR EACH ROW
BEGIN
  UPDATE l1m_articulo
  SET ArtCan = ArtCan - NEW.StoSalDetCan
  WHERE ArtCod = NEW.StoSalDetArt;
END;
//
DELIMITER ;

DELIMITER //
CREATE PROCEDURE VER_VENTAS_MAYOR(IN COTA INT)
BEGIN
  SELECT * FROM TOTAL_SALIDA_NOM
  WHERE Total_Salida > COTA
  ORDER BY Total_Salida DESC;
END//

DELIMITER ;

DELIMITER //
CREATE PROCEDURE VER_STOCK_MENOR(IN COTA INT)
BEGIN
  SELECT * FROM STOCK_PRO
  WHERE ArtCan <= COTA
  ORDER BY ArtCan DESC;
END//

DELIMITER ;

--Auxiliares
DELIMITER //
CREATE PROCEDURE VER_MAESTRAS()
BEGIN
  SELECT * FROM l1m_proveedor;
  SELECT * FROM l1m_cliente;
  SELECT * FROM l1m_articulo;
END//
DELIMITER ;

DELIMITER //
CREATE PROCEDURE VER_TRANSA()
BEGIN
  SELECT * FROM l1t_stock_entrada_cab;
  SELECT * FROM l1t_stock_entrada_det;
  SELECT * FROM l1t_stock_salida_cab;
  SELECT * FROM l1t_stock_salida_det;
END//

DELIMITER ;
