import pandas as pd
from scraper.competitor_prices import scrape_prices
from rag.retriever import retrieve_context
from llm.pricing_agent import suggest_price

product_name = "Tire Inflator X200"
competitors = scrape_prices(product_name)
sales_data = pd.read_csv("data/sample_sales.csv").to_dict(orient="records")
context = retrieve_context(product_name)

suggestion = suggest_price(product_name, competitors, sales_data, context)
print("💡 LLM Pricing Suggestion:")
print(suggestion)
