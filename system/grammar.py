

grammar = {

   "<start>": ["<sql_stmt_list>"],


   "<sql_stmt_list>": ["<sql_stmt>", "<sql_stmt>; <sql_stmt_list>"],
   "<sql_stmt>": ["<explain_clause> <stmt_list>"],


   "<explain_clause>": ["", "EXPLAIN", "EXPLAIN QUERY PLAN"],


   "<stmt_list>": [
       "<create_temporary_table>", # extra
       "<create_view>",
       "<alter_table>",
       "<delete_stmt>",
       "<delete_stmt_limited>",
       "<begin_stmt>",
       "<commit_stmt>",
       "<analyze_stmt>",
       "<attach_stmt>",
       "<detach_stmt>",
       "<create_index>",
       "<create_trigger>",


       "<create_table_stmt>",
       "<select_stmt>",
       "<insert_stmt>",
       "<update_stmt>",
       "<savepoint_stmt>",
       "<release_stmt>",
       "<vacuum_stmt>",
       "<pragma_stmt>",
       "<reindex_stmt>",
       "<drop_view_stmt>",
       "<drop_trigger_stmt>",
       "<drop_table_stmt>",
       "<drop_index_stmt>",
       "<detach_stmt>",
       "<rollback_stmt>"
   ],

   # SCHEMA
   "<schema_name>": ["main", "temp"],
   "<schema_name_with_dot>": ["", "<schema_name>."],

# CREATE TEMPORARY TABLE syntax
  "<create_temporary_table>": [
      "CREATE TEMPORARY TABLE <temp_table_name> (<column_definitions>)",
      "CREATE TEMPORARY TABLE <temp_table_name> AS SELECT * FROM <table_name>"
  ],
  "<temp_table_name>":  ["<string>"],




  "<create_view>":                     ["CREATE VIEW <view_name> AS <select_stmt>"],
  "<view_name>":                     ["<string>"],
   # ALTER TABLE syntax
  "<alter_table>":      [
      "ALTER TABLE <table_name> ADD <column_name> <column_type>",
      "ALTER TABLE <table_name> RENAME TO <new_table_name>",
      "ALTER TABLE <table_name> RENAME COLUMN <old_column_name> TO <new_column_name>",
      "ALTER TABLE <table_name> DROP COLUMN <column_name>"
  ],
  "<new_table_name>":   ["<string>"],
  "<old_column_name>":  ["<string>"],
  "<new_column_name>":  ["<string>"],
   # DELETE syntax
  "<delete_stmt>":      ["DELETE FROM <table_name> WHERE <expr>"],




  # DELETE with LIMIT
  "<delete_stmt_limited>": [
      "DELETE FROM <table_name> WHERE <expr> LIMIT <limit_value>",
      "DELETE FROM <table_name> WHERE <expr> ORDER BY <column_name> LIMIT <limit_value>"
  ],
   "<limit_value>":      ["1", "5", "10", "100"],




  # BEGIN TRANSACTION syntax
  "<begin_stmt>":       ["BEGIN <transaction_mode> TRANSACTION"],
  "<transaction_mode>": ["", "DEFERRED", "IMMEDIATE", "EXCLUSIVE"],


  # COMMIT TRANSACTION syntax
  "<commit_stmt>":      ["COMMIT", "COMMIT TRANSACTION"],




  # ANALYZE syntax
  "<analyze_stmt>":     ["ANALYZE", "ANALYZE <table_name>", "ANALYZE <index_name>", "ANALYZE <schema_name>"],




  # ATTACH and DETACH syntax
  "<attach_stmt>":      ["ATTACH DATABASE <file_name> AS <schema_name>"],
  "<detach_stmt>":      ["DETACH DATABASE <schema_name>"],




  # CREATE INDEX syntax
  "<create_index>":     [
      "CREATE INDEX <index_name> ON <table_name> (<column_list>)",
      "CREATE UNIQUE INDEX <index_name> ON <table_name> (<column_list>)"
  ],


  # CREATE TRIGGER syntax
  "<create_trigger>":   [
      "CREATE TRIGGER <trigger_name> <trigger_timing> <trigger_event> ON <table_name> BEGIN <trigger_action>; END",
      "CREATE TRIGGER <trigger_name> <trigger_timing> <trigger_event> ON <table_name> WHEN <trigger_condition> BEGIN <trigger_action>; END"
  ],
  "<trigger_name>":     ["<string>"],
  "<trigger_timing>":   ["BEFORE", "AFTER", "INSTEAD OF"],
  "<trigger_event>":    ["INSERT", "UPDATE", "DELETE"],
  "<trigger_action>":   ["INSERT INTO <table_name> (<column_name>) VALUES (<value>);",
                         "UPDATE <table_name> SET <column_name> = <value> WHERE <expr>;",
                         "DELETE FROM <table_name> WHERE <expr>;"],
  "<trigger_condition>":["<column_name> = <value>", "<column_name> > <value>", "<column_name> IS NOT NULL"],


  # File names and schema names for ATTACH
  "<file_name>":        ["'<file_path>'"],
  "<file_path>":        ["example.db", "main.db", "temp.db", "data.db"],  # Example file paths
  "<schema_name>":      ["main", "temp", "attached_schema"],


  # Index and schema names
  "<index_name>":       ["<string>"],  # Define index names similarly to table or column names


   # DROP VIEW Statement
   "<drop_view_stmt>": ["DROP VIEW <if_exists> <schema_name_with_dot><view_name>"],
   "<if_exists>": ["", "IF EXISTS"],
   "<view_name>": ["<string>"],



   # DROP TRIGGER Statement
   "<drop_trigger_stmt>": ["DROP TRIGGER <if_exists> <schema_name_with_dot><trigger_name>"],
   "<trigger_name>": ["<string>"],


   # DROP TABLE Statement
   "<drop_table_stmt>": ["DROP TABLE <if_exists> <schema_name_with_dot><table_name>"],


   # DROP INDEX Statement
   "<drop_index_stmt>": ["DROP INDEX <if_exists> <schema_name_with_dot><index_name>"],
   "<index_name>": ["<string>"],


   # DETACH Statement
   "<detach_stmt>": ["DETACH <string>", "DETACH DATABASE <schema_name>"],


   # CREATE TABLE Statement
   "<create_table_stmt>": ["CREATE TABLE <table_name> (<column_definitions>)"],
   "<column_definitions>": ["<column_definition>", "<column_definition>, <column_definitions>"],
   "<column_definition>": ["<column_name> <column_type> <column_constraints>"],
   "<column_constraints>": ["", "NOT NULL", "PRIMARY KEY", "UNIQUE", "DEFAULT <value>"],


   # Table Names, Columns, and Indexes
   "<table_name>": ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
                       "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
                       "w", "x", "y", "z"],
   "<column_list>": [
       "<column_name>", "<column_name>, <column_list>"
   ],
   "<column_name>": ["id", "name", "age", "price", "created_at", "category_id"],


   # Column Types
   "<column_type>": ["INTEGER", "TEXT", "REAL", "BLOB", "NUMERIC"],


   # Select Statement
   "<select_stmt>": ["<select_core>"], # removed with_clause and moved order and limit to select_core to simplify

  
   # SELECT CORE
   "<select_core>": [
       "SELECT <result_column_agg> <result_column> FROM <table_or_subquery> <join_clause> <where_clause> <group_by_clause> <window_clause> <order_by_clause> <limit_clause>", # moved order and limit clause here because it doesn't seem to work with VALUES
       "VALUES (<value_list>)" 
   ],
   "<result_column_agg>": ["", "ALL", "DISTINCT"],
   "<result_column>": [
       "*",
       "<table_name>.*",
       "<column_list>" 
   ],


   # Table or subquery
   "<table_or_subquery>": [
       "<schema_name_with_dot><table_name> <as_alias>",
       "<table_function_name>(<column_list>) <as_alias>", 
       "(<select_stmt>) <as_alias>"
   ],
   "<as_alias>": [
       "",
       "AS <alias_name>"
   ],
   "<alias_name>": ["<string>"],
   "<table_function_name>": [
       "avg",
       "count",
       "group_concat",
       "min",
       "max",
       "sum",
       "total",
       "string_agg",
   ],


   # JOIN Clause
   "<join_clause>": [
       "<join_operator> <table_name> <join_constraint>",
       "<join_operator> <table_name> <join_constraint> <join_clause>"
   ],
   "<join_operator>": [
       ",",
       "<join_operator_type> JOIN"
   ],
   "<join_operator_type>": [
       "LEFT <join_outer>",
       "RIGHT <join_outer>",
       "FULL <join_outer>",
       "INNER",
       "CROSS"
   ],
   "<join_outer>": ["", "OUTER"],
   "<join_constraint>": [
       "ON <expr>",
       "USING (<column_list>)"
   ],


   # WHERE Clause
   "<where_clause>": ["WHERE <expr>"],
   "<expr>": [
       "<column_name> <comparison_op> <value>",
       "<expr> AND <expr>",
       "<expr> OR <expr>",
       "NOT <expr>",
       "<column_name> BETWEEN <number> AND <number>",
       "<column_name> IN (<value_list>)",
       "<column_name> LIKE '<string_pattern>'"
   ],
   # "<expr_list>": [
   #     "<expr>",
   #     "<expr>, <expr_list>"
   # ],


   # GROUP BY Clause
   "<group_by_clause>": ["", "GROUP BY <column_list> <having_clause>"],


   # HAVING Clause
   "<having_clause>": ["", "HAVING <expr>"],


   # Window Clause
   "<window_clause>": [
       "",
       "WINDOW <window_name> AS (<window_definition>)"
   ],
   "<window_name>": ["<string>"],
   "<window_definition>": ["ORDER BY <column_name>"],


   # ORDER BY Clause
   "<order_by_clause>": ["", "ORDER BY <column_list> <order>"],
   "<order>": ["ASC", "DESC"],
  
   # LIMIT Clause
   "<limit_clause>": ["", "LIMIT <number> OFFSET <number>"],


   # INSERT Statement
   "<insert_stmt>": [
       "INSERT <insert_update_or> INTO <schema_name_with_dot><table_name> (<column_list>) VALUES (<value_list>)", # can be improved to match number of columns
       "INSERT INTO <table_name> DEFAULT VALUES"
   ],
   "<insert_update_or>": [
       "OR ABORT",
       "OR FAIL",
       "OR IGNORE",
       "OR REPLACE",
       "OR ROLLBACK",
   ],


   # UPDATE Statement
   "<update_stmt>": ["UPDATE <insert_update_or> <table_name> SET <update_assignments> <where_clause>"],
   "<update_assignments>": ["<column_name> = <value>", "<column_name> = <value>, <update_assignments>"],


   # SAVEPOINT Statement
   "<savepoint_stmt>": ["SAVEPOINT <savepoint_name>"],
   "<savepoint_name>": ["<string>"],


   # RELEASE Statement
   "<release_stmt>": ["RELEASE SAVEPOINT <savepoint_name>"],


   # ROLLBACK Statement
   "<rollback_stmt>": [
       "ROLLBACK TRANSACTION",
       "ROLLBACK TRANSACTION TO SAVEPOINT <savepoint_name>"
   ],


   # VACUUM Statement
   "<vacuum_stmt>": [
       "VACUUM"
   ],


   # PRAGMA Statement
   "<pragma_stmt>": ["PRAGMA <pragma_type>"],


   "<pragma_type>": [
       "<pragma_name>",  # Without value
       "<pragma_name> = <pragma_value>",  # With equals assignment
       "<pragma_name> (<pragma_value>)",  # With parentheses
       "<schema_name_with_dot><pragma_name>",  # With schema name
       "<schema_name_with_dot><pragma_name> = <pragma_value>",
       "<schema_name_with_dot><pragma_name> (<pragma_value>)"
   ],
   "<pragma_name>": [
       "analysis_limit"
       "application_id",
       "auto_vacuum",
       "automatic_index",
       "busy_timeout",
       "cache_size",
       "cache_spill",
       "case_sensitive_like",
       "cell_size_check"
       "checkpoint_fullfsync",
       "collation_list",
       "compile_options",
       "data_store_directory",
       "count_changes",
       "data_version",
       "database_list",
       "default_cache_size"
       "defer_foreign_keys",
       "empty_result_callbacks",
       "encoding",
       "foreign_key_check",
       "foreign_key_list",
       "foreign_keys",
       "freelist_count",
       "full_column_names",
       "fullfsync",
       "function_list",
       "hard_heap_limit",
       "ignore_check_constraints",
       "incremental_vacuum",
       "index_info",
       "index_list",
       "index_xinfo",
       "integrity_check",
       "journal_mode",
       "journal_size_limit",
       "legacy_alter_table",
       "legacy_file_format",
       "locking_mode",
       "max_page_count",
       "mmap_size",
       "module_list",
       "optimize",
       "page_count",
       "page_size",
       "parser_trace",
       "pragma_list",
       "query_only",
       "quick_check",
       "read_uncommitted",
       "recursive_triggers",
       "reverse_unordered_selects",
       "schema_version",
       "secure_delete",
       "short_column_names",
       "shrink_memory",
       "soft_heap_limit",
       "stats",
       "synchronous",
       "table_info",
       "table_list",
       "table_xinfo",
       "temp_store",
       "temp_store_directory",
       "threads",
       "user_version",
       "wal_autocheckpoint",
       "wal_checkpoint",
       "writable_schema"
   ],
   "<pragma_value>": [
       "0",
       "1",
       "'off'",
       "'on'",
       "'yes'",
       "'no'",
       "'true'",
       "'false'",
   ],


   # REINDEX Statement
   "<reindex_stmt>": [
       "REINDEX",
       "REINDEX <schema_name_with_dot><table_name>"
   ],


   # Values and Patterns
   "<value>": ["'<string>'", "<number>", "NULL"],
   "<value_list>": ["<value>", "<value>, <value_list>"],
   "<number>": ["0", "1", "-1", "42", "3.14"],
   "<string_pattern>": ["%Alice%", "_B%", "A%_C"],
   "<string>":           ["<letter>", "<letter><string>"],
   "<letter>":           ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
                       "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
                       "w", "x", "y", "z"],


   # Comparison Operators
   "<comparison_op>": ["=", "!=", "<", "<=", ">", ">=", "IS", "IS NOT"],



}
