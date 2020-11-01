import sqlite3 as sql

conn = sql.connect('mtg_db.db')

conn.execute('CREATE TABLE Card (Number INT,\
Name CHAR(30),\
Set_Id CHAR(5),\
Rarity Char(10),\
Color CHAR(15),\
Tcg_Id INT,\
Layout CHAR(15),\
Booster BIT,\
Scryfall_Id CHAR(70),\
Has_Foil BIT,\
Has_NonFoil BIT,\
Is_Promo BIT,\
Is_Land BIT,\
Image_Url CHAR(70),\
PRIMARY KEY(Number, Name, Set_Id))')

conn.execute('CREATE TABLE Card_Images (Scryfall_Id CHAR(70),\
Num_sides INT,\
Price DECIMAL(8,2),\
Price_Foil DECIMAL(8,2),\
Front_Image CHAR(80),\
Back_Image CHAR(80),\
PRIMARY KEY(Scryfall_ID),\
FOREIGN KEY(Scryfall_ID) REFERENCES Card(Scryfall_ID))') 

conn.close()


