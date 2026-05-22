import pandas as pd
from sqlalchemy import create_engine, text
import os
import urllib.parse  # <-- INDHA LINE ROMBA MUKKIYAM (Idhu thaan magic pandrathu)

print("Phase 3: Data Load (Database-kku push pandrom) 🚀\n")

# 1. Clean panna data-va thedi edukkurom
clean_file = 'clean_data/cleaned_supplier_data.csv'

if not os.path.exists(clean_file):
    print("Cleaned data file illai! First Phase 2 (Transformer) run pannunga.")
else:
    df = pd.read_csv(clean_file)
    print(f"Data theliva irukku. Total rows to upload: {len(df)}")

    # 2. MySQL Database Setup
    db_user = 'root'
    raw_password = 'Your Password'  
    
    # Password-la irukka '@' symbol-a safe-a maathiduvom (Praga%4081900 nu maaridum)
    db_password = urllib.parse.quote_plus(raw_password)
    
    db_host = 'localhost:3306'
    db_name = 'supply_chain_db'

    try:
        # First, Database illana pudhusa create panna code
        server_engine = create_engine(f"mysql+mysqlconnector://{db_user}:{db_password}@{db_host}/")
        with server_engine.connect() as conn:
            conn.execute(text(f"CREATE DATABASE IF NOT EXISTS {db_name}"))
        print(f"Database '{db_name}' theliva ready aagiduchu!")

        # 3. Ippo antha specific database-kku connect pandrom
        db_engine = create_engine(f"mysql+mysqlconnector://{db_user}:{db_password}@{db_host}/{db_name}")

        # 4. DataFrame-a apdiye SQL Table-kku thallurom (The Magic Line)
        table_name = 'supplier_inventory'
        
        # if_exists='replace' na, daily puthu data varum pothu table update aagidum
        df.to_sql(name=table_name, con=db_engine, if_exists='replace', index=False)
        
        print(f"Success Boss! Data motham MySQL-la '{table_name}' ngra table-la mass-a ukkanthuruchu! 🎉")
        print("--- ETL Pipeline 100% Completed! ---")

    except Exception as e:
        print("\n🚨 Database Error vandhuruchu:")
        print("MySQL unga system-la ON-la irukkaa nu check pannunga.")
        print(f"Technical Error details: {e}")