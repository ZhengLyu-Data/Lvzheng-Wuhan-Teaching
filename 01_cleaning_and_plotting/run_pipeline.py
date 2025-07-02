# run_pipeline.py
import os

# Step 1: Run data cleaning
os.system("python clean_data.py")

# Step 2: Run analysis and export charts
os.system("python pipeline.py")

print("✅ All steps completed. Output saved to /output folder.")