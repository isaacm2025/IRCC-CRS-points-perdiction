class Analyzer:
    def __init__(self, df):
        self.df = df

    def yearly_summary(self):
        # Group by year
        return self.df.groupby(self.df["date"].dt.year).agg({
            "min_crs_score": ["mean", "min", "max"],
            "invitations_issued": "sum"
        })

    def category_summary(self):
        # Group by round_type
        return self.df.groupby("round_type").agg({
            "min_crs_score": ["mean", "min", "max"],
            "invitations_issued": "sum"
        })
