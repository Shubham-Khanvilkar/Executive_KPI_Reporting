from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "monthly_kpis.csv"
OUTPUT = ROOT / "output"


def load() -> pd.DataFrame:
    df = pd.read_csv(DATA, parse_dates=["month"])
    df["nna"] = df["inflows"] - df["outflows"]
    df["nna_variance"] = df["nna"] - df["target_nna"]
    df["nna_attainment"] = df["nna"] / df["target_nna"]
    df["retention_rate"] = df["retained_clients"] / df["clients"]
    return df


def create_insights(df: pd.DataFrame) -> pd.DataFrame:
    monthly = df.groupby("month", as_index=False).agg(
        aum=("aum", "sum"),
        inflows=("inflows", "sum"),
        outflows=("outflows", "sum"),
        nna=("nna", "sum"),
        target_nna=("target_nna", "sum"),
        clients=("clients", "sum"),
        retained_clients=("retained_clients", "sum"),
    )
    monthly["nna_variance"] = monthly["nna"] - monthly["target_nna"]
    monthly["nna_attainment"] = monthly["nna"] / monthly["target_nna"]
    monthly["retention_rate"] = monthly["retained_clients"] / monthly["clients"]
    monthly["nna_mom_pct"] = monthly["nna"].pct_change()
    monthly["primary_driver"] = monthly.apply(
        lambda r: "Inflows" if r["inflows"] >= r["outflows"] else "Outflows", axis=1
    )
    monthly["management_action"] = monthly["nna_attainment"].apply(
        lambda x: "Investigate flow drivers" if x < 0.90
        else "Monitor target variance" if x < 1.00
        else "Maintain performance"
    )
    return monthly


if __name__ == "__main__":
    result = create_insights(load())
    OUTPUT.mkdir(exist_ok=True)
    result.to_csv(OUTPUT / "management_insights.csv", index=False)
    print(result.to_string(index=False))