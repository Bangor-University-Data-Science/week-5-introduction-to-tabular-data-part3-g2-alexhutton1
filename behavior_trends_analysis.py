import pandas as pd

def import_data(filename: str) -> pd.DataFrame:

    #df = pd.read_csv(filename)
    df = pd.read_excel(filename)
    return df

def filter_data(df):
    #remove rows where customerid is missing
    filtered_data = df.dropna(subset=['Customer ID'])
    #remove rows where Quantity or Unit Price are negative
    filtered_data = filtered_data[(filtered_data['Quantity']) <= 0 & filtered_data(filtered_data['Unit Price']) <= 0] #not sure if only negative or 0 included
    return filtered_data

def loyalty_customers(df, min_purchases):
    # group customers by quanitity of product purchased
    purchases_count = df.groupby('CustomerID')['Quantity'].sum()
    # check if number of purchases exceeds min_purchases
    purchases_count = purchases_count[purchases_count > min_purchases]
    return purchases_count

def quarterly_revenue(df):
    #calculate the revenue
    df['Revenue'] = df['Quantity'] * df['Unit Price']
    #change invoice date to date/time 
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'], dayfirst=True)
    #convert invoice date to quarterly period
    df['Quarter'] = df['InvoiceDate'].dt.to_period('Q')
    #total revenue grouped by quarters, resetting index so that quarter is a column rather than an index
    quarterly_revenue_df = df.groupby('Quarter')['Revenue'].sum().reset_index()
    return quarterly_revenue_df


def high_demand_products(df, top_n):
    #calculate each total quantity sold per product name
    products_by_quantity_sold = df.groupby('Description')['Quantity'].sum()
    #sort index so that highest quantity products appear at the top in descending order
    sorted_products = products_by_quantity_sold.sort_values(ascending=False)
    #return only top_n products
    return sorted_products.head(top_n)

def purchase_patterns(df):
    #summmary with product as index and average quantity and unit prices
    purchase_patterns_summary = df.groupby('Description').agg(
        avg_quantity=('Quantity', 'mean'),
        avg_unit_price=('UnitPrice', 'mean')
    ).reset_index()
    #rename 'description' to product
    purchase_patterns_summary.rename(columns={'Description': 'product'})
    return purchase_patterns_summary

def answer_conceptual_questions():
    answers = {
        'Q1': {'A', 'C', 'D'},
        'Q2': {'B', 'D'},
        'Q3': {'A', 'B', 'C'},
        'Q4': {'A', 'B', 'C'},
        'Q5': {'A', 'D'},
    }
    return answers


