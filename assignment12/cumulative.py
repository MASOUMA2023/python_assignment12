import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
import os

conn= sqlite3.connect('../db/lesson.db')

query = """
SELECT o.order_id, SUM(p.price * l.quantity) AS total_price
FROM orders o
JOIN line_items l ON o.order_id = l.order_id
JOIN products p ON l.product_id = p.product_id
GROUP BY o.order_id
ORDER BY o.order_id;
"""

df = pd.read_sql_query(query, conn)
conn.close()
def cumulative(row):
    totals_above = df['total_price'][0:row.name + 1]
    return totals_above.sum()

df['cumulative_apply'] = df.apply(cumulative, axis=1)
df['cumulative'] = df['total_price'].cumsum()

plt.figure(figsize=(10, 6))
plt.plot(df['order_id'], df['cumulative'], marker='o', color='skyblue')
plt.title('Cumulative revenue by order')
plt.xlabel('Order ID')
plt.ylabel('Cumulative revenue')
plt.grid(True)
plt.tight_layout()
plt.show()