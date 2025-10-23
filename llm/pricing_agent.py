import openai

def suggest_price(product_name, competitors, sales_data, context):
    prompt = f"""
    Product: {product_name}
    Competitor Prices: {competitors}
    Sales History: {sales_data}
    Context: {context}
    Goal: Recommend optimal price to maximize revenue and stay competitive.
    """
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content
