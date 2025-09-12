To convert the provided SQL query into Spark SQL syntax, you can use the same structure, but ensure that you are using the appropriate Spark SQL functions and syntax. Here’s how you can rewrite the query:

```sql
WITH total_vendas AS (
    SELECT
        cliente_id,
        SUM(valor_venda) AS total_venda
    FROM vendas
    GROUP BY cliente_id
),

clientes_ativos AS (
    SELECT
        cliente_id,
        nome_cliente
    FROM clientes
    WHERE status = 'ativo'
)

SELECT
    c.cliente_id,
    c.nome_cliente,
    COALESCE(tv.total_venda, 0) AS total_venda
FROM clientes_ativos c
LEFT JOIN total_vendas tv
    ON c.cliente_id = tv.cliente_id
ORDER BY total_venda DESC
```

### Notes:
1. The syntax for `WITH` clauses (Common Table Expressions) is the same in Spark SQL as in standard SQL.
2. The `COALESCE` function is also available in Spark SQL, so it can be used as is.
3. The `LEFT JOIN` and `ORDER BY` clauses are also supported in Spark SQL without any changes.

Make sure that your Spark environment is set up to execute SQL queries, and you can run this query directly in a Spark SQL context.
