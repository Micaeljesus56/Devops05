import  sqlite3
conn  =  sqlite3 . conectar ( 'exemplo.db' )
c  =  con . cursor ()
c . execute ( '' 'CREATE TABLE ações (texto da data, texto trans, texto do símbolo, quantidade real, preço real)' '' )
c . execute ( "INSERT INTO stocks VALUES ('2006-01-05', 'BUY', 'RHAT', 100,35.14)" )
con . commit ()
con . fechar ()
