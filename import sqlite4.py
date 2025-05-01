import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

def main():
    db_file = 'sales_data.db'

    try:
        conn = sqlite3.connect(db_file)

        # Query 1: Total quantity and revenue by product
        query1 = """
            SELECT product, SUM(quantity) AS total_qty, SUM(quantity * price) AS revenue
            FROM sales
            GROUP BY product
        """
        df1 = pd.read_sql_query(query1, conn)
        print("Sales Summary by Product:")
        print(df1)

        # Plot bar chart for revenue by product
        ax = df1.plot(kind='bar', x='product', y='revenue', color='skyblue', legend=False)
        ax.set_title("Total Revenue by Product")
        ax.set_xlabel("Product")
        ax.set_ylabel("Revenue ($)")
        plt.tight_layout()
        plt.savefig("sales_chart.png")
        print("Bar chart saved as 'sales_chart.png'. Please open this file to view the chart.")
        plt.show()

        # Query 2: Total quantity sold by date
        query2 = """
            SELECT date, SUM(quantity) AS total_quantity
            FROM sales
            GROUP BY date
            ORDER BY date
        """
        df2 = pd.read_sql_query(query2, conn)
        print("\nTotal Quantity Sold by Date:")
        print(df2)

    except Exception as e:
        print(f"Error: {e}")
    finally:
        if 'conn' in locals():
            conn.close()

if __name__ == "__main__":
    main()
