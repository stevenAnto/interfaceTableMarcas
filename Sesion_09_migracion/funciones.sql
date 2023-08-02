SELECT l1t_stock_salida_det.StoSalDetSec,l1t_stock_salida_det.StoSalDetCan,StoSalCabCod,l1m_articulo.ArtNom,StoSalCabEstReg
FROM l1m_articulo
INNER JOIN l1t_stock_salida_det
ON l1m_articulo.ArtCod=l1t_stock_salida_det.StoSalDetArt;


SELECT l1m_cliente.CliCod,l1m_cliente.CliNom,gzz_zona.ZonDes,l1m_cliente.CliEstReg
FROM l1m_cliente
INNER JOIN gzz_zona
ON l1m_cliente.CliZon=gzz_zona.ZonCod;

CREATE VIEW STOCKR AS
    SELECT 
        l1m_articulo.ArtCod,l1m_articulo.ArtNom,l1m_articulo.ArtCan,l1m_proveedor.ProNom
    FROM 
        (l1m_articulo JOIN l1t_stock_entrada_det on l1t_stock_entrada_det.stoentdetart = l1m_articulo.artcod)
        JOIN 
        (l1t_stock_entrada_cab join l1m_proveedor ON l1t_stock_entrada_cab.StoEntCabPro = l1m_proveedor.ProCod)
        ON l1t_stock_entrada_det.stoentcabcod = l1t_stock_entrada_cab.stoentcabcod;
        
CREATE VIEW STOCK_PRO AS
    SELECT DISTINCT ArtCod,ArtNom,ArtCan,ProNom
    FROM STOCKR;

CREATE VIEW TOTAL_ENTRADA AS
SELECT StoEntDetArt, SUM(StoEntDetCan) AS Total_Ingresado
FROM l1t_stock_entrada_det
GROUP BY StoEntDetArt;

CREATE VIEW TOTAL_ENTRADA_NOM AS
SELECT TOTAL_ENTRADA.StoEntDetArt,l1m_articulo.ArtNom,TOTAL_ENTRADA.Total_Ingresado
FROM TOTAL_ENTRADA
JOIN l1m_articulo
ON TOTAL_ENTRADA.StoEntDetArt=l1m_articulo.ArtCod;


CREATE VIEW TOTAL_SALIDA AS
SELECT StoSalDetArt, SUM(StoSalDetCan) AS Total_Salida
FROM l1t_stock_salida_det
GROUP BY StoSalDetArt;

CREATE VIEW TOTAL_SALIDA_NOM AS
SELECT TOTAL_SALIDA.StoSalDetArt,l1m_articulo.ArtNom,TOTAL_SALIDA.Total_Salida
FROM TOTAL_SALIDA
JOIN l1m_articulo
ON TOTAL_SALIDA.StoSalDetArt=l1m_articulo.ArtCod;

create or replace NONEDITIONABLE TRIGGER ACTUALIZA_CANTIDAD_ENT
    AFTER INSERT ON l1t_stock_entrada_det FOR EACH ROW
    DECLARE
    BEGIN
        UPDATE l1m_articulo
        SET ArtCan = ArtCan + :NEW.StoEntDetCan
        WHERE ArtCod = :NEW.StoEntDetArt;
    END;

create or replace NONEDITIONABLE TRIGGER ACTUALIZA_CANTIDAD_SAL
    AFTER INSERT ON l1t_stock_salida_det
    FOR EACH ROW
    BEGIN
    UPDATE l1m_articulo
    SET ArtCan = ArtCan - :NEW.StoSalDetCan
    WHERE ArtCod = :NEW.StoSalDetArt;
    END;


create or replace NONEDITIONABLE PROCEDURE VER_STOCK_MENOR(COTA IN INT)
    IS CURSOR c_stock IS
    select ARTNOM, ARTCAN from stock_pro where ARTCAN < cota;
    v_ARTNOM stock_pro.ARTNOM%TYPE;
    v_ARTCAN stock_pro.ARTCAN%TYPE;
    mensaje_concatenado CHAR(300);
BEGIN
    IF NOT c_stock%ISOPEN THEN
        OPEN c_stock;
    END IF;
    fetch c_stock into v_ARTNOM, v_ARTCAN;
    mensaje_concatenado := concat(v_ARTNOM, to_Char(v_ARTCAN));
    DBMS_OUTPUT.PUT_LINE(mensaje_concatenado);
    while c_stock%FOUND
    LOOP
        fetch c_stock into v_ARTNOM, v_ARTCAN;
        mensaje_concatenado := concat(v_ARTNOM, to_Char(v_ARTCAN));
        DBMS_OUTPUT.PUT_LINE(mensaje_concatenado);  
    END LOOP;
    CLOSE c_stock;
END;

create or replace NONEDITIONABLE PROCEDURE VER_VENTAS_MAYOR(COTA IN INT)
    IS CURSOR c_salida IS
    select STOSALDETART, ARTNOM, TOTAL_SALIDA from total_salida_nom where total_salida > cota;
    v_STOSALDETART total_salida_nom.stosaldetart%TYPE;
    v_ARTNOM total_salida_nom.ARTNOM%TYPE;
    v_TOTAL_SALIDA total_salida_nom.TOTAL_SALIDA%TYPE;
    mensaje_concatenado CHAR(300);
BEGIN
    IF NOT c_salida%ISOPEN THEN
        OPEN c_salida;
    END IF;
    fetch c_salida into v_STOSALDETART, v_ARTNOM, v_TOTAL_SALIDA;
    mensaje_concatenado := concat(v_ARTNOM, to_Char(v_TOTAL_SALIDA));
    DBMS_OUTPUT.PUT_LINE(mensaje_concatenado);
    while c_salida%FOUND
    LOOP
        fetch c_salida into v_STOSALDETART, v_ARTNOM, v_TOTAL_SALIDA;
        mensaje_concatenado := concat(v_ARTNOM, to_Char(v_TOTAL_SALIDA));
        DBMS_OUTPUT.PUT_LINE(mensaje_concatenado);    
    END LOOP;
    CLOSE c_salida;
END;