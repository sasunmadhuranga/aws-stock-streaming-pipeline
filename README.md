Designed and implemented a real-time stock market data analytics pipeline using AWS serverless architecture to ingest, process, store, and analyze streaming stock data. The system collects live stock prices from external APIs (Finnhub and AlphaVantage) through a Python-based producer service and stores raw JSON data in Amazon S3. An event-driven AWS Lambda function is automatically triggered on S3 object creation to validate data, perform anomaly detection, and transform data for storage. Processed data is stored in Amazon DynamoDB for fast access, while raw data is archived in a separate S3 bucket for historical analysis. Amazon SNS is used to send real-time alerts when anomalies are detected. For analytics, Amazon Athena is used to run SQL queries directly on S3 data, and results are visualized using Python (PyAthena, Pandas, Matplotlib). The project also incorporates CI/CD using GitHub Actions to automate Lambda deployment, demonstrating a scalable, event-driven, and cloud-native data engineering pipeline.

✔ Built a Python-based producer service to fetch real-time stock data from Finnhub and AlphaVantage APIs.

✔ Implemented an event-driven architecture using Amazon S3 to trigger AWS Lambda on new data ingestion.

✔ Developed a Lambda function to validate JSON data, detect anomalies, and process stock records.

✔ Handled DynamoDB constraints by converting float values to Decimal for accurate data storage.

✔ Stored processed stock data in Amazon DynamoDB for real-time access and querying.

✔ Archived raw stock data in Amazon S3 to enable historical analysis and data lake architecture.

✔ Integrated Amazon SNS to send real-time alerts when abnormal stock price patterns are detected.

✔ Configured Amazon Athena to run SQL queries on S3 data for analytics and reporting.

✔ Visualized stock insights using Python with PyAthena, Pandas, and Matplotlib.

✔ Implemented CI/CD using GitHub Actions to automate packaging and deployment of Lambda functions.

✔ Enabled monitoring and debugging using Amazon CloudWatch logs.

✔ Designed a fully serverless and scalable pipeline without relying on always-running infrastructure.

Technologies:

Python

boto3

AWS Lambda

Amazon S3

Amazon DynamoDB

Amazon SNS

Amazon Athena

Amazon CloudWatch

GitHub Actions (CI/CD)

PyAthena

Pandas

Matplotlib

Finnhub API

AlphaVantage API