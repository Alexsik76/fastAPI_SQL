tablename = ''
TABLES = "select table_name from INFORMATION_SCHEMA.tables where `TABLE_SCHEMA`='carshop';"
COLUMNS = "SELECT `COLUMN_NAME` FROM `INFORMATION_SCHEMA`.`COLUMNS` WHERE `TABLE_SCHEMA`='carshop' AND `TABLE_NAME`= '%s' ;"