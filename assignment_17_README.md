# Assignment 17 - PySpark DataFrame Sales Processing

## Build and Run
```bash
docker build -t pyspark-df -f assignment_17_Dockerfile .
docker run pyspark-df
```

## Output
- All products sorted by sales (desc) displayed on console
- Top 3 products displayed on console
- Products with sales > 80,000 saved to `high_sales_output/` as CSV
