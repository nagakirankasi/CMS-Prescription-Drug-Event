import pandas as pd
import json

# Load schema from JSON
with open('pde_schema.json') as f:
    schema = json.load(f)

# Read PDE file
pde_file = "2025_PDE_Outbound_File.txt"

# Define column names based on schema
column_names = [field['name'] for field in schema['fields']]

# Read file with defined columns
df = pd.read_csv(pde_file, sep='|', names=column_names, dtype=str)

# Process data (example transformation)
df['Claim_Amount'] = df['Claim_Amount'].astype(float)

# Save processed file
df.to_parquet('processed_pde.parquet', index=False)

print("Processing complete.")
