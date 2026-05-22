import pandas as pd
import glob
import os

print("Phase 2: Data Transformation Start Aagiduchu...\n")

# 1. raw_data folder-la irukka latest CSV file-a thedurom
path = os.path.join('raw_data', 'live_supplier_data_*.csv')
files = glob.glob(path)

if not files:
    print("Raw data file kidaikkala Boss!")
else:
    # Latest file-a eduthu read pandrom
    latest_file = max(files, key=os.path.getctime)
    df = pd.read_csv(latest_file)
    print(f"File open panniyachu: {latest_file}\n")

    print("--- Pazhaiya Data (Clean pandrathukku munnadi) ---")
    print(df[['supplier_price', 'stock_status']].head(3))

    # 2. THE ENGINEERING MAGIC (Data Cleaning)
    
    print("\nData clean aaguthu (Fixing Price & Stock logic)...")
    
    # Pandas warning-a fix pandrathukku
    pd.set_option('future.no_silent_downcasting', True)
    
    # Price column-la irukka thevaiyillatha symbols-a thookitu, numeric-a maathurom
    df['supplier_price'] = df['supplier_price'].astype(str).str.replace('£', '').str.replace('Â', '')
    df['supplier_price'] = pd.to_numeric(df['supplier_price'], errors='coerce')

    # Stock logic fix: Text-la "In stock" nu irundha 1 (True/Available) nu vaikkum, illana 0 nu vaikkum.
    df['stock_status'] = df['stock_status'].astype(str).str.contains('In stock', case=False, na=False).astype(int)

    print("\n--- Pudhu Data (Clean pannunathukku aparam) ---")
    print(df[['supplier_price', 'stock_status']].head(3))