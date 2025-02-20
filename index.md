# CMS Prescription Drug Event (PDE) Processing Solution

## Project Overview
This project provides a scalable, secure, and cost-effective solution for ingesting, processing, and analyzing CMS Prescription Drug Event (PDE) files. It leverages AWS services such as S3, Lambda, Glue, and Athena to create an efficient ETL pipeline.

## Key Features
- **Automated Ingestion:** Files are ingested via AWS S3 and processed using AWS Lambda.
- **ETL Pipeline:** AWS Glue transforms and validates PDE files.
- **Data Storage:** Processed data stored in S3 and accessible via Athena.
- **Monitoring:** CloudWatch logs and alerts for pipeline health.
- **Visualization:** QuickSight dashboards for reporting and insights.

## Project Structure
```
📦 cms-pde-processing-solution
├─ 📂 src               # Infrastructure as Code (AWS CDK/Terraform)
├─ 📂 lambdas           # AWS Lambda functions for file ingestion and validation
├─ 📂 glue-scripts      # AWS Glue ETL scripts for data transformation
├─ 📂 data-validation   # JSON schemas for PDE data validation
├─ 📂 dashboards        # QuickSight templates for visualization
├─ 📂 docs              # Architecture diagrams and documentation
├─ 📄 README.md         # Project overview and setup instructions
└─ 📄 architecture.png  # High-level architecture diagram
```

## Technology Stack
- **Cloud:** AWS (S3, Lambda, Glue, Athena, Redshift, QuickSight)
- **Infrastructure:** AWS CDK / Terraform
- **Programming:** Python for Lambda and Glue jobs
- **Monitoring:** CloudWatch, SNS alerts

## Solution Architecture
1. **Data Ingestion:** PDE files uploaded to S3.
2. **Processing:** AWS Lambda triggers AWS Glue jobs for ETL.
3. **Storage:** Transformed data stored as Parquet in S3.
4. **Querying:** AWS Athena enables querying of processed data.
5. **Visualization:** QuickSight dashboards for insights.

## Deployment
1. Clone the repository:
```bash
git clone https://github.com/yourusername/cms-pde-processing-solution.git
cd cms-pde-processing-solution
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Deploy AWS infrastructure using CDK:
```bash
cd src
cdk deploy
```

## Sample Queries (Athena)
```sql
SELECT *
FROM cms_pde_processed
WHERE drug_name = 'Lisinopril';
```

## Security Considerations
- Encryption at rest and in transit using AWS KMS.
- IAM policies for least privilege access.
- Logging and monitoring with CloudWatch and CloudTrail.

## Cost Estimation
- **S3 Storage:** $0.023/GB per month (Standard storage)
- **AWS Lambda:** Pay per execution (~$10–50/month based on volume)
- **AWS Glue:** $0.44 per DPU-hour for ETL jobs
- **Athena:** $5 per TB scanned

## Roadmap
- [x] Initial ETL pipeline
- [ ] Implement data quality checks
- [ ] Build QuickSight dashboards
- [ ] API endpoint for processed data

## License
This project is licensed under the MIT License.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request.

## Contact
For questions or support, contact me at nkiran.kasi@gmail.com