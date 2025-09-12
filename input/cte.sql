-- arquivo: exemplo_cte_leftjoin.sql

-- CTE para calcular a soma de vendas por cliente
WITH total_vendas AS (
    SELECT
        cliente_id,
        SUM(valor_venda) AS total_venda
    FROM vendas
    GROUP BY cliente_id
),

-- CTE para filtrar clientes ativos
clientes_ativos AS (
    SELECT
        cliente_id,
        nome_cliente
    FROM clientes
    WHERE status = 'ativo'
)

-- Consulta final usando LEFT JOIN
SELECT
    c.cliente_id,
    c.nome_cliente,
    COALESCE(tv.total_venda, 0) AS total_venda
FROM clientes_ativos c
LEFT JOIN total_vendas tv
    ON c.cliente_id = tv.cliente_id
ORDER BY total_venda DESC;
