TABLES = ("SELECT `table_name` FROM INFORMATION_SCHEMA.tables "
          "WHERE `TABLE_SCHEMA` NOT IN ('information_schema','performance_schema');")
COLUMNS = ("SELECT `column_name`, `data_type` FROM `INFORMATION_SCHEMA`.`COLUMNS` "
           "WHERE `TABLE_SCHEMA` NOT IN ('information_schema','performance_schema') AND "
           "`TABLE_NAME`= '%s' ;")
