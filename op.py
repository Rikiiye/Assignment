import pandas as pd
URL = "https://github.com/Rikiiye/Assignment/blob/main/user.csv"

# Load data
df = pd.read_csv(URL)

# --- Retrieve ---
print("Retrieve user with ID=2:")
print(df[df['id'] == 2])

# --- Update ---
df.loc[df['id'] == 2, 'phone'] = '98765'

# --- Add new user ---
new_user = {"id": 3, "name": "Charlie", "email": "charlie@example.com", "phone": "55555"}
df = pd.concat([df, pd.DataFrame([new_user])], ignore_index=True)

# --- Save locally ---
df.to_csv("users.csv", index=False)
print("File updated! Commit and push users.csv back to GitHub.")
