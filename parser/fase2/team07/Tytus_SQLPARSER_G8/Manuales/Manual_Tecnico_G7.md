
#### Universidad de San Carlos de Guatemala
#### Facultad de Ingeniería
#### Escuela de Ciencias y Sistemas
#### Área de Ciencias de la Computación
#### Organización de Lenguajes y Compiladores 2 - Sección A
#### Ing. Luis Fernando Espino Barrios
#### Aux. Juan Carlos Maeda    
<br>
<div style="text-align: justify">
<table class="default">
  <tr>
    <th>Nombre</th>
    <th>Carnet</th>
  </tr>
  <tr>
    <td>ROMARIO DAVID CASTILLO ECHEVERRIA</td>
    <td>201314064</td>
  </tr>
  <tr>
    <td>ROBERTO EDUARDO CASEROS REYNOSO</td>
    <td>201314177</td>
  </tr>
  <tr>
    <td>CARLOS ENRIQUE CANTÉ LÓPEZ</td>
    <td>201314448</td>
  </tr>
  <tr>
    <td>CARLOS GABRIEL PERALTA CAMBRAN</td>
    <td>201314556</td>
  </tr>
</table>
</div>
<br>

## Índice
- [SQL PARSER Grupo 7 - TytusDB](#SQL_PARSER_Grupo_7-TytusDB) 
- [Objetivos](#Objetivos)
- [Requisitos del Sistema](#Requisitos_del_Sistema)
- [¿Cómo Funciona?](#¿Cómo_Funciona?)
- [Análisis Léxico](#Análisis_Léxico)
- [Análisis Sintáctico](#Análisis_Sintáctico)
- [Archivo Entrada](#Archivo_Entrada)

<br>

# SQL_PARSER_Grupo_7-TytusDB

<div style="text-align: justify">TytusDB es un proyecto Open Source para desarrollar un administrador de bases de datos. Está compuesto por tres componentes interrelacionados: el administrador de almacenamiento de la base de datos, que estará a cargo del curso de Estructuras de Datos; el administrador de la base de datos, que estará a cargo del curso de Sistemas de Bases de Datos 1, este administrador se compone a su vez de un servidor y de un cliente; y el SQL Parser, que estará a cargo del curso de Organización de Lenguajes y Compiladores 2.</div>

<p align="center">
  <img src="img/topologia.png" width="800" alt="TytusDB Architecture">
</p>

<br>

## Objetivos  
### General  
* <div style="text-align: justify">Traducir, optimizar y ejecutar el codigo del SQL Parser cumpliendo con las caracteristicas del código tres direcciones y ejecutando el coódigo generado desde python para mostrar los resultados al administrador de bases de datos.</div>

### Específicos  
* <div style="text-align: justify">Agregar al parser la administración de índices.</div>
* <div style="text-align: justify"> Agregar al parser el lenguaje procedural PL/pgSQL</div>
* <div style="text-align: justify">Traducir a código tres direcciones las instrucciones sql y PL/SQL</div>
* <div style="text-align: justify">Optimizar y ejecutar el código tres direcciones.</div>
<br>

## Requisitos_del_Sistema
<div style="text-align: justify">El programa se podrá ejecutarse media vez se cumplan con las siguientes
características mínimas:  

* Procesador Intel(R) Core(TM) i5-7200U CPU @ 2.50GHz, 2712 Mhz, 2 procesadores principales, 4 procesadores lógicos
* Python Versión 3.9  
* Sistema Operativo: Windows 7 o superior.
</div>
<br>

## ¿Cómo_Funciona?
<div style="text-align: justify">

<h3>SQL Parser</h3>

Este componente proporciona al servidor una función encargada de interpretar sentencias del subconjunto del lenguaje SQL especificado en la siguiente documentación.

<h3>Componentes</h3>

Está compuesto por tres sub componentes:
SQL Parser: es el intérprete de sentencias de SQL y PL/pgSQL, que proporcionará una función para invocar al parser, al recibir una instrucción el parser luego del proceso interno y de la planificación de esta debe invocar las diferentes funciones proporcionadas por el componente de administrador de almacenamiento. <br>
Type Checker: es un sub componente que ayudará al parser a la comprobación de tipos. Al crear un objeto cualquiera se debe crear una estructura que almacenará los tipos de datos y cualquier información necesaria para este fin.<br>
Query Tool: es un sub componente que consiste en una ventana gráfica similar al Query Tool de pgadmin de PostgreSQL, para ingresar consultas y mostrar los resultados, incluyendo el resalto de la sintaxis. La ejecución se realizará de todo el contenido del área de texto.<br>
PL/pgSQL: es un lenguaje de procedural para el sistema de base de datos, las funciones creadas con PL/pgSQL se pueden usar en cualquier lugar donde se puedan usar funciones integradas.
</div>


<p align="center">
  <img src="img/topologiaParser.png" width="800" alt="TytusDB Architecture">
</p>

## Análisis_Léxico
<div style="text-align: justify">

<h3>Alfabeto:</h3>
<code>

    Simbolos= , ; . : ( ) = ! + - * < > _
    Letras = A-Z, a-z
    Digitos = 0 - 9, 0.0 - 9.0

</code>

<h3>Tokén:</h3>
<code>

    reservadas = (

        'TABLE', 'INT', 'VARCHAR', 'DATE', 'CHAR', 'DOUBLE', 'DECIMAL', 'NULL', 'PRIMARY', 'KEY', 'REFERENCES', 'FOREIGN',
        'FLOAT',
        'BETWEEN',
        'LIKE',
        'IN',
        'TYPE', 'INHERITS',
        'ENUM', 'IS', 'SHOW', 'DATABASES', 'USE', 'RENAME', 'TO', 'OWNER', 'CURRENT_USER', 'SESSION_USER',
        'IF', 'EXISTS', 'MODE', 'REPLACE', 'DEFAULT', 'UNIQUE', 'CONSTRAINT', 'CHECK', 'DISTINCT',
        # NUMERIC TYPES
        'SMALLINT', 'INTEGER', 'BIGINT', 'NUMERIC', 'REAL', 'PRECISION', 'MONEY', 
        # CHARACTER TYPES
        'CHARACTER', 'VARYING', 'TEXT',
        # DATE/TIME TYPES
        'TIMESTAMP', 'TIME', 'INTERVAL',
        #PARA FECHAS
        'EXTRACT', 'YEAR', 'MONTH', 'DAY', 'HOUR', 'MINUTE', 'SECOND',
        'NOW', 'DATE_PART','CURRENT_DATE', 'CURRENT_TIME',
        # BOOLEAN TYPE
        'BOOLEAN', 'TRUE', 'FALSE',
        # OPERADORES LOGICOS
        'AND', 'OR', 'NOT',
        # SENTENCIAS DML
        'SELECT', 'FROM', 'WHERE', 'AS',
        'INSERT', 'INTO', 'VALUES',
        'UPDATE', 'SET',
        'DELETE',
        # SENTENCIAS DDL
        'CREATE', 'DROP', 'ALTER', 'COLUMN', 'ADD', 'TRUNCATE', 'DATABASE',
        # SENTENCIAS DE AGREGACIÓN
        'SUM', 'MAX', 'MIN', 'AVG', 'COUNT', 'TOP',
        # JOIN
        'INNER', 'JOIN', 'LEFT', 'RIGHT', 'FULL', 'OUTER', 'ON',
        # FUNCTIONS
        'GROUP' , 'HAVING', 
        # MATHEMATICAL FUNCTIONS
        'ABS', 'CBRT', 'CEIL', 'CEILING', 'DEGREES', 'DIV', 
        'EXP', 'FACTORIAL', 'FLOOR', 'GCD',
        'LCM', 'LN', 'LOG', 'LOG10', 'MIN_SCALE', 
        'MOD', 'PI', 'POWER', 'RADIANS', 'ROUND', 'SCALE', 'SIGN', 
        'SQRT', 'TRIM_SCALE', 'TRUNC', 'WIDTH_BUCKET', 'RANDOM', 'SETSEED',
        # BINARY STRING FUNCTIONS
        'LENGTH', 'SUBSTRING', 'TRIM', 'GET_BYTE', 'MD5', 'SET_BYTE', 
        'SHA256', 'SUBSTR', 'CONVERT', 'ENCODE', 'DECODE',
        # TRIGONOMETRIC FUNCTIONS
        'ACOS', 'ACOSD', 'ASIN', 'ASIND', 'ATAN', 'ATAND', 'ATAN2', 'ATAN2D', 
        'COS', 'COSD', 'COT', 'COTD', 'SIN', 'SIND', 'TAN', 'TAND', 'SINH',
        'COSH', 'TANH', 'ASINH', 'ACOSH', 'ATANH',
        # SORTING ROWS
        'ORDER', 'BY', 'FIRST', 'LAST', 'ASC', 'DESC', 'NULLS', 
        #EXPRESSIONS
        'CASE','WHEN','THEN','ELSE', 'LEAST', 'GREATEST',
        #LIMIT AND OFFSET
        'LIMIT', 'OFFSET',
        #COMBINING QUERIES
        'UNION', 'INTERSECT', 'EXCEPT', 'ALL',
        # Begin
        'FUNCTION', 'BEGIN', 'END',
        'DECLARE',
        'PROCEDURE',
        'CONSTANT',
        'LANGUAGE',
        'PLPGSQL',
        'FOR',
        'RETURNS',
        'ROWTYPE',
        'COLLATE',
        'ALIAS',
        'SQLSTATE',
        'EXCEPTION',
        'ELSIF',
        'ELSEIF',
        'RAISE',
        'NOTICE',
        'RETURN',
        'INDEX', 'USING', 'HASH'
    )

    tokens = reservadas + (
        # OPERADORES COMPARADORES
        'IGUAL', 'BLANCO',
        'MAYORQ',
        'MENORQ',
        'MAYOR_IGUALQ',
        'MENOR_IGUALQ',
        'DISTINTO',
        'PARIZQ',
        'PARDER',
        'CORIZQ',
        'CORDER',
        'MAS',
        'LLAVEA',
        'LLAVEC',
        'MENOS',
        'POR',
        'DIVIDIDO',
        'EXPONENCIACION',
        'MODULO',
        'ENTERO',
        'PUNTO_COMA',
        'PUNTO',
        'FDECIMAL',
        'COMA',
        'ID',
        'CADENA',
        'CARACTER',
        'COMENTARIO_MULTILINEA',
        'COMENTARIO_SIMPLE',
        'ARROBA',
        'DOLLAR',
        'DOSP_IGUAL'
    )
</code>
</div>

## Análisis_Sintáctico
<div style="text-align: justify">

<h3>Gramática:</h3>
<code>

    instrucciones : instrucciones instruccion
                | instruccion

    instruccion : CREATE DATABASE if_not_exists ID PUNTO_COMA
            | CREATE DATABASE if_not_exists ID OWNER IGUAL ID PUNTO_COMA
            | CREATE DATABASE if_not_exists ID OWNER IGUAL ID MODE IGUAL ENTERO PUNTO_COMA
            | CREATE DATABASE if_not_exists ID MODE IGUAL ENTERO PUNTO_COMA
            | CREATE OR REPLACE DATABASE if_not_exists ID PUNTO_COMA
            | CREATE OR REPLACE DATABASE if_not_exists ID OWNER IGUAL ID PUNTO_COMA
            | CREATE OR REPLACE DATABASE if_not_exists ID OWNER IGUAL ID MODE IGUAL ENTERO PUNTO_COMA
            | CREATE OR REPLACE DATABASE if_not_exists ID MODE IGUAL ENTERO PUNTO_COMA
            | CREATE TABLE ID PARIZQ campos PARDER PUNTO_COMA
            | CREATE TABLE ID PARIZQ campos PARDER INHERITS PARIZQ ID PARDER PUNTO_COMA
            | USE ID PUNTO_COMA
            | SHOW DATABASES PUNTO_COMA
            | SHOW DATABASES LIKE CARACTER PUNTO_COMA
            | CREATE TYPE ID AS ENUM PARIZQ l_expresiones PARDER PUNTO_COMA
            | TRUNCATE TABLE ID PUNTO_COMA
            | DROP DATABASE ID PUNTO_COMA
            | DROP DATABASE IF EXISTS ID PUNTO_COMA
            | DROP TABLE ID PUNTO_COMA
            | DROP ID
            | UPDATE ID SET l_columnas instructionWhere PUNTO_COMA
            | DELETE FROM ID instructionWhere PUNTO_COMA
            | CREATE FUNCTION ID BEGIN instrucciones END PUNTO_COMA
            | CREATE FUNCTION ID PARIZQ lcol PARDER BEGIN instrucciones END PUNTO_COMA
            | CREATE FUNCTION ID PARIZQ lcol PARDER AS expresion BEGIN instrucciones END PUNTO_COMA
            | DECLARE expresion AS expresion PUNTO_COMA
            | DECLARE expresion tipo PUNTO_COMA
            | SET expresion IGUAL expre PUNTO_COMA
            | ALTER TABLE ID ADD ID tipo PUNTO_COMA
            | ALTER DATABASE ID RENAME TO ID PUNTO_COMA
            | ALTER DATABASE ID OWNER TO list_owner PUNTO_COMA
            | ALTER TABLE ID ADD COLUMN ID tipo PUNTO_COMA
            | ALTER TABLE ID DROP COLUMN ID PUNTO_COMA
            | ALTER TABLE ID ADD CONSTRAINT ID UNIQUE PARIZQ lista_id PARDER PUNTO_COMA
            | ALTER TABLE ID ADD FOREIGN KEY PARIZQ lista_id PARDER REFERENCES ID PARIZQ lista_id PARDER PUNTO_COMA
            | ALTER TABLE ID ALTER COLUMN ID SET NOT NULL PUNTO_COMA
            | ALTER TABLE ID DROP CONSTRAINT ID PUNTO_COMA
            | ALTER TABLE ID ADD CHECK expre PUNTO_COMA
            | ALTER TABLE ID ADD CONSTRAINT ID CHECK expre PUNTO_COMA
            | ALTER TABLE ID RENAME COLUMN ID TO ID PUNTO_COMA
            | INSERT INTO ID PARIZQ lcol PARDER VALUES PARIZQ l_expresiones PARDER PUNTO_COMA
            | INSERT INTO ID VALUES PARIZQ l_expresiones PARDER PUNTO_COMA
            | lquery PUNTO_COMA
            | CREATE PROCEDURE ID PARIZQ parametros_funcion PARDER LANGUAGE PLPGSQL AS DOLLAR DOLLAR declaraciones_funcion BEGIN contenido_funcion END PUNTO_COMA DOLLAR DOLLAR
            | CREATE FUNCTION ID PARIZQ parametros_funcion PARDER returns_n retorno_funcion declaraciones_funcion BEGIN contenido_funcion END PUNTO_COMA DOLLAR DOLLAR LANGUAGE PLPGSQL PUNTO_COMA

    if_not_exists : IF NOT EXISTS
                | 

    instructionWhere :  WHERE expre

    l_columnas : l_columnas COMA expre
            | expre

    list_owner : ID
            | CURRENT_USER
            | SESSION_USER

    lquery : lquery relaciones query
            | query

    relaciones : UNION  
            | UNION ALL 
            | INTERSECT
            | INTERSECT ALL 
            | EXCEPT ALL 
            | EXCEPT

    query : SELECT dist lcol FROM lcol 
        | SELECT dist lcol FROM lcol instructionWhere lrows
        | SELECT dist lcol FROM lcol instructionWhere 
        | SELECT dist lcol FROM lcol linners 
        | SELECT dist lcol FROM lcol linners instructionWhere lrows
        | SELECT dist lcol FROM lcol linners instructionWhere 
        | SELECT dist lcol 
        | SELECT dist lcol FROM lcol lrows

    lcase : lcase case
        | case

    case : WHEN expre THEN expre
        | ELSE expre

    lrows : lrows rows
        | rows

    rows : ORDER BY lista_order
        | GROUP BY l_expresiones
        | HAVING lcol
        | LIMIT l_expresiones OFFSET expre
        | LIMIT l_expresiones

    dist : DISTINCT
            | 

    lista_order : lista_order COMA order_op
            | order_op

    order_op : expre
            | expre DESC
            | expre ASC
            | expre NULLS FIRST
            | expre NULLS LAST

    linners : linners inners
            | inners

    inners : INNER JOIN expre ON expre
            | LEFT JOIN expre ON expre
            | FULL OUTER JOIN expre ON expre
            | JOIN expre ON expre
            | RIGHT JOIN expre ON expre

    expre : expre OR expre
            | expre AND expre
            | NOT expre
            | expre IGUAL expre
            | expre MAYORQ expre
            | expre MENORQ expre
            | expre MAYOR_IGUALQ expre
            | expre MENOR_IGUALQ expre
            | expre DISTINTO expre
            | expre MAS expre
            | expre MENOS expre
            | expre POR expre
            | expre EXPONENCIACION expre
            | expre MODULO expre
            | expre LIKE expre
            | expre NOT LIKE expre
            | expre BETWEEN expresion AND expresion
            | expre NOT BETWEEN expresion AND expresion
            | expre IN PARIZQ lcol PARDER
            | expre IS NULL
            | expre IS NOT NULL
            | expre IS DISTINCT FROM expre
            | expre IS NOT DISTINCT FROM expre
            | MIN PARIZQ expre PARDER
            | MAX PARIZQ expre PARDER
            | SUM PARIZQ expre PARDER
            | AVG PARIZQ expre PARDER
            | COUNT PARIZQ expre PARDER
            | TOP PARIZQ expre PARDER
            | ABS PARIZQ expre PARDER 
            | CBRT PARIZQ expre PARDER 
            | CEIL PARIZQ expre PARDER 
            | CEILING PARIZQ expre PARDER 
            | DEGREES PARIZQ expre PARDER 
            | DIV PARIZQ expre PARDER
            | EXP PARIZQ expre PARDER 
            | FACTORIAL PARIZQ expre PARDER 
            | FLOOR PARIZQ expre PARDER 
            | GCD PARIZQ expre PARDER
            | LCM PARIZQ expre PARDER 
            | LN PARIZQ expre PARDER 
            | LOG PARIZQ expre PARDER 
            | LOG10 PARIZQ expre PARDER 
            | MIN_SCALE PARIZQ expre PARDER
            | MOD PARIZQ expre PARDER 
            | PI PARIZQ expre PARDER 
            | POWER PARIZQ expre PARDER 
            | RADIANS PARIZQ expre PARDER 
            | ROUND PARIZQ expre PARDER 
            | SCALE PARIZQ expre PARDER 
            | SIGN PARIZQ expre PARDER
            | SQRT PARIZQ expre PARDER 
            | TRIM_SCALE PARIZQ expre PARDER 
            | TRUNC PARIZQ expre PARDER 
            | WIDTH_BUCKET PARIZQ expre PARDER 
            | RANDOM PARIZQ expre PARDER 
            | SETSEED PARIZQ expre PARDER
            | LENGTH PARIZQ expre PARDER
            | SUBSTRING PARIZQ lcol PARDER
            | TRIM PARIZQ expre PARDER
            | GET_BYTE PARIZQ lcol PARDER
            | MD5 PARIZQ lcol PARDER
            | SET_BYTE PARIZQ lcol PARDER
            | SHA256 PARIZQ lcol PARDER
            | SUBSTR PARIZQ lcol PARDER
            | CONVERT PARIZQ lcol PARDER
            | ENCODE PARIZQ expre PARDER
            | DECODE PARIZQ expre PARDER
            | ACOS PARIZQ expre PARDER
            | ACOSD PARIZQ expre PARDER
            | ASIND PARIZQ expre PARDER
            | ATAN PARIZQ expre PARDER
            | ATAND PARIZQ expre PARDER
            | ATAN2 PARIZQ expre PARDER
            | ATAN2D PARIZQ expre PARDER
            | COS PARIZQ expre PARDER
            | COSD PARIZQ expre PARDER
            | COT PARIZQ expre PARDER
            | COTD PARIZQ expre PARDER
            | SIN PARIZQ expre PARDER
            | SIND PARIZQ expre PARDER
            | TAN PARIZQ expre PARDER
            | TAND PARIZQ expre PARDER
            | SINH PARIZQ expre PARDER
            | COSH PARIZQ expre PARDER
            | TANH PARIZQ expre PARDER
            | ASINH PARIZQ expre PARDER
            | ACOSH PARIZQ expre PARDER
            | ATANH PARIZQ expre PARDER
            | LEAST PARIZQ lcol PARDER
            | GREATEST PARIZQ lcol PARDER
            | EXTRACT PARIZQ tiempo FROM TIMESTAMP CARACTER PARDER
            | NOW PARIZQ PARDER
            | DATE_PART PARIZQ CARACTER COMA INTERVAL CARACTER PARDER
            | CURRENT_DATE
            | CURRENT_TIME
            | TIMESTAMP CARACTER
            | POR
            | CASE lcase END 
            | PARIZQ expre PARDER
            | PARIZQ query PARDER

    tiempo :  YEAR
            | MONTH
            | DAY
            | HOUR
            | MINUTE
            | SECOND

    expre :  expresion

    expresion : CADENA
            | CARACTER
            | ENTERO
            | FDECIMAL
            | DOUBLE
            | ID
            | ID PUNTO ID
            | ARROBA ID
            | ID PARIZQ lcol PARDER

    campos : campos COMA ID tipo lista_op
            | campos COMA ID tipo
            | campos COMA CHECK expre
            | campos COMA CONSTRAINT ID CHECK expre
            | campos COMA UNIQUE PARIZQ lista_id PARDER
            | campos COMA FOREIGN KEY PARIZQ lista_id PARDER REFERENCES ID PARIZQ lista_id PARDER
            | campos COMA PRIMARY KEY PARIZQ lista_id PARDER
            | ID tipo lista_op
            | ID tipo

    lista_id : lista_id COMA ID
            | ID

    lista_op : lista_op opcion
            | opcion

    opcion : PRIMARY KEY
            | REFERENCES ID
            | DEFAULT expresion
            | NOT NULL
            | NULL
            | UNIQUE
            | CONSTRAINT ID UNIQUE
            | CONSTRAINT ID CHECK expre
            | CHECK expre

    l_expresiones : l_expresiones COMA expresion
                | expresion


    lcol : lcol COMA expre
        | lcol COMA expre ID
        | lcol COMA expre AS ID
        | expre
        | expre ID
        | expre AS ID

    tipo : INT
        | DATE
        | ID PARIZQ ID PARDER
        | VARCHAR PARIZQ ENTERO PARDER
        | CHAR PARIZQ ENTERO PARDER
        | CHARACTER VARYING PARIZQ ENTERO PARDER
        | CHARACTER PARIZQ ENTERO PARDER
        | TEXT
        | DECIMAL PARIZQ ENTERO COMA ENTERO PARDER
        | DOUBLE
        | DECIMAL
        | ENTERO
        | FLOAT PARIZQ ENTERO COMA ENTERO PARDER
        | SMALLINT
        | INTEGER
        | BIGINT
        | NUMERIC
        | REAL
        | DOUBLE PRECISION
        | MONEY
        | BOOLEAN
        | TIMESTAMP
        | TIME
        | INTERVAL

    parametros_funcion : lista_parametros_funcion 
                       |
                           
    lista_parametros_funcion : lista_parametros_funcion COMA parametro_fucion
                             | parametro_fucion
                             
    parametro_fucion : ID tipo
					 | tipo
					    
	returns_n : RETURNS
	          | 
	
	retorno_funcion : tipo AS DOLLAR DOLLAR
				    | TABLE PARIZQ lista_campos_tabla PARDER AS DOLLAR DOLLAR
				    | AS DOLLAR DOLLAR
				    
	lista_campos_tabla : lista_campos_tabla COMA ID tipo
	                   | ID tipo
	                   
	declaraciones_funcion : DECLARE list_dec_var_funcion
	                      |
	                      
	list_dec_var_funcion : list_dec_var_funcion dec_var_funcion PUNTO_COMA
	                     | dec_var_funcion PUNTO_COMA
	                     
	dec_var_funcion : ID constant_n tipo nnull aisgnacion_valor 
	                | ID ALIAS FOR DOLLAR ENTERO
				    | ID ALIAS FOR ID
				    | ID tabla_typerow MODULO type_row
				    
    tabla_typerow : ID PUNTO ID
                  | ID
                  
    type_row : TYPE
			 | ROWTYPE
			 
	constant_n : CONSTANT
	           |
	           
	nnull : NOT NULL
	      | 
	      
	aisgnacion_valor : DEFAULT expre 
					 | DOSP_IGUAL expre 
					 | IGUAL expre 
					 |
					 
	contenido_funcion : contenido_funcion cont_funcion
	                  | cont_funcion
	                  
    cont_funcion : sentencia_if
                 | instruccion
                 | sentencia_retorno
                 | asignacion_var
                 
    sentencia_retorno : RETURN PUNTO_COMA
                      | RETURN expre PUNTO_COMA
                      
    asignacion_var : ID IGUAL expre PUNTO_COMA
                   | ID DOSP_IGUAL expre PUNTO_COMA
                   
    sentencia_if : IF expre THEN instrucciones_if condicionesif ELSE  instrucciones_if END IF PUNTO_COMA
				  | IF expre THEN instrucciones_if condicionesif END IF PUNTO_COMA
				  | IF expre THEN instrucciones_if ELSE  instrucciones_if END IF PUNTO_COMA
				  | IF expre THEN instrucciones_if END IF PUNTO_COMA
				  | CASE ID condiciones_cuando ELSE instrucciones_if END CASE PUNTO_COMA
				  | CASE ID condiciones_cuando END CASE PUNTO_COMA
				  | CASE condiciones_cuandoB ELSE instrucciones_if END CASE PUNTO_COMA
				  | CASE condiciones_cuandoB END CASE PUNTO_COMA
				  | BEGIN instrucciones_if EXCEPTION WHEN l_identificadores THEN instrucciones_if END PUNTO_COMA
				  | BEGIN instrucciones_if EXCEPTION WHEN sql_states THEN instrucciones_if END PUNTO_COMA
				  
	instrucciones_if : instrucciones_if instruccion_if 
                     | instruccion_if
                     
    instruccion_if : cont_funcion
                   | expre PUNTO_COMA
                   | RAISE NOTICE CADENA PUNTO_COMA
                   | RAISE NOTICE CADENA COMA ID PUNTO_COMA
                   | RAISE NOTICE CARACTER PUNTO_COMA
                   | RAISE NOTICE CARACTER COMA ID PUNTO_COMA
                   
    condicionesif : condicionesif condicionif
			      | condicionif
			      
	condicionif : ELSIF expre THEN instrucciones_if 
			    | ELSEIF expre THEN instrucciones_if  
			    
	condiciones_cuando : condiciones_cuando condicion_cuando
				       | condicion_cuando
				       
	condicion_cuando : WHEN l_expresiones THEN instrucciones_if
	
	condiciones_cuandoB : condiciones_cuandoB condicion_cuandoB
					    | condicion_cuandoB
					    
	condicion_cuandoB : WHEN expre THEN instrucciones_if
	
	sql_states : sql_states OR sql_state
			   | sql_state
			   
	sql_state : SQLSTATE CADENA
	
	l_identificadores : l_identificadores OR ID
                      | ID
                      
    if_op : IF EXISTS
          |
          
    nombre_op : ID
              | 
              
    unique_op : UNIQUE
              |
              
    hash_op : USING HASH
            |
    
    l_indexes : l_indexes COMA ID order_op null_op first_last_op
              | ID order_op null_op first_last_op
              | ID PARIZQ ID PARDER
              
    order_op : ASC
             | DESC
             |
             
    null_op : NULLS
            |
            
    first_last_op : FIRST
                  | LAST
                  |
                  
    where_op : instructionWhere
             |
</code>
</div>

## Archivo_Entrada
<div style="text-align: justify">

<h3>Ejemplo de Archivo Entrada:</h3>

<code>

    CREATE DATABASE DBFase2;

    USE DBFase2;

    CREATE FUNCTION myFuncion(texto text) RETURNS text AS $$
    BEGIN
	        RETURN texto;
    END;
    $$ LANGUAGE plpgsql;

    select myFuncion('INICIO CALIFICACION FASE 2');

    CREATE TABLE tbProducto (idproducto integer not null primary key,
    						 producto varchar(150) not null,
  						 fechacreacion date not null,
						 estado integer);

    CREATE UNIQUE INDEX idx_producto ON tbProducto (idproducto);
    INSERT INTO tbProducto values(1,'Laptop Lenovo',now(),1);
    INSERT INTO tbProducto values(2,'Bateria para Laptop Lenovo T420',now(),1);
    INSERT INTO tbProducto values(3,'Teclado Inalambrico',now(),1);
    INSERT INTO tbProducto values(4,'Mouse Inalambrico',now(),1);
    
</code>
</div>

