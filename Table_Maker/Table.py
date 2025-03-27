import pandas as pd

# Membuat data struktur tabel dalam satu sheet
data = {
    "id": [],
    "user_type": [],
    "username": [],
    "email": [],
    "password": [],
    "product_name": [],
    "product_description": [],
    "price": [],
    "transaction_status": [],
    "transaction_date": [],
    "report_details": [],
    "created_at": []
}

# Membuat DataFrame
df = pd.DataFrame(data)

# Menyimpan ke dalam file Excel
file_path = "C:/Users/dillo/OneDrive/Desktop/Table_Maker/Output.xlsx"
df.to_excel(file_path, index=False)

# Memberikan file kepada pengguna
file_path
