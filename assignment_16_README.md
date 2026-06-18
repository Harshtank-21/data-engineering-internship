# Assignment 16 - PySpark RDD Employee Processing

## Build and Run
```bash
docker build -t pyspark-rdd -f assignment_16_Dockerfile .
docker run pyspark-rdd
```

## Output
- Employees sorted by salary descending printed to console
- Department-wise salary totals printed to console
- Top 3 employees saved to `top3_output/` directory
