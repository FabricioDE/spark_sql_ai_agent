import pickle

sql_differences = {
    "date_time": {
        "description": "Differences in Date and Time Handling",
        "examples": [
            {
                "sql_standard": "SELECT CURRENT_DATE;",
                "spark_sql": "SELECT current_date();"
            },
            {
                "sql_standard": "SELECT EXTRACT(YEAR FROM '2025-09-12');",
                "spark_sql": "SELECT year('2025-09-12');"
            },
            {
                "sql_standard": "SELECT DATE_ADD('2025-09-12', INTERVAL 5 DAY);",
                "spark_sql": "SELECT date_add('2025-09-12', 5);"
            }
        ]
    },
    "array": {
        "description": "Differences in Array Handling",
        "examples": [
            {
                "sql_standard": "SELECT ARRAY[1, 2, 3];",
                "spark_sql": "SELECT array(1, 2, 3);"
            },
            {
                "sql_standard": "SELECT arr[1] FROM (SELECT ARRAY[10, 20, 30] AS arr);",
                "spark_sql": "SELECT element_at(array(10, 20, 30), 1);"
            },
            {
                "sql_standard": "SELECT UNNEST(ARRAY[1,2,3]);",
                "spark_sql": "SELECT explode(array(1,2,3));"
            }
        ]
    },
    "create_table": {
        "description": "Differences in Table Creation",
        "examples": [
            {
                "sql_standard": "CREATE TABLE users (id INT, name VARCHAR(100));",
                "spark_sql": "CREATE TABLE users (id INT, name STRING) USING parquet;"
            },
            {
                "sql_standard": "CREATE TEMP TABLE temp_users AS SELECT * FROM users;",
                "spark_sql": "CREATE TEMP VIEW temp_users AS SELECT * FROM users;"
            },
            {
                "sql_standard": "DROP TABLE users;",
                "spark_sql": "DROP TABLE IF EXISTS users;"
            }
        ]
    }
}


with open("../../../input/pickel/spark_glossary.pkl", "wb") as f:
    pickle.dump(sql_differences, f)
