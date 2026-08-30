"""Prepare a clean reporting dataset for Power BI.

The script creates a presentation-ready fact table while keeping the raw CSV unchanged.
"""
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "data" / "monthly_kpis.csv"
OUTPUT = ROOT / "output" / "powerbi_fact_kpis.csv"


def prepare() -> pd.DataFrame:
    df = pd.read_csv(INPUT, parse_dates=["month"])
    numeric = [
        "aum", "inflows", "outflows", "revenue", "opex", "clients",
        "retained_clients", "advisors", "target_nna"
    ]
    df[numeric] = df[numeric].apply(pd.to_numeric, errors="coerce")
    if df[numeric].isna().any().any():
        raise ValueError("Numeric KPI fields contain invalid or missing values")

    df["nna"] = df["inflows"] - df["outflows"]
    df["nna_variance_to_target"] = df["nna"] - df["target_nna"]
    df["nna_attainment_pct"] = df["nna"] / df["target_nna"]
    df["retention_rate_pct"] = df["retained_clients"] / df["clients"]
    df["operating_profit"] = df["revenue"] - df["opex"]
    df["operating_margin_pct"] = df["operating_profit"] / df["revenue"]
    df["net_flow_rate_pct"] = df["nna"] / df["aum"]
    df["advisor_nna"] = df["nna"] / df["advisors"]
    return df


def main() -> None:
    df = prepare()
    OUTPUT.parent.mkdir(exist_ok=True)
    df.to_csv(OUTPUT, index=False)
    print(f"Prepared {len(df):,} rows for Power BI")
    print(f"Output: {OUTPUT}")


if __name__ == "__main__":
    main()
