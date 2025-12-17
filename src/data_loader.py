import pandas as pd

def load_data(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)

    # Clean column names: remove spaces and lowercase for consistency
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

    # Now your columns will be like: 'round_number', 'draw_date', 'minimum_crs', etc.
    # Convert date column
    df["draw_date"] = pd.to_datetime(df["draw_date"], errors="coerce")

    # Rename important columns to match code
    df = df.rename(columns={
        "draw_date": "date",
        "minimum_crs": "min_crs_score",
        "invitations": "invitations_issued",
        "round_type": "round_type"  # should exist in CSV
    })

    # Ensure numeric columns
    # Remove commas and convert to numeric, coerce errors to NaN
    df["invitations_issued"] = df["invitations_issued"].astype(str).str.replace(",", "", regex=True)
    df["invitations_issued"] = pd.to_numeric(df["invitations_issued"], errors='coerce')

    # For min_crs_score too, if needed
    df["min_crs_score"] = pd.to_numeric(df["min_crs_score"], errors='coerce')


    return df
