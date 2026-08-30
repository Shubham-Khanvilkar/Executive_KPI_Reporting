from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "monthly_kpis.csv"
OUTPUT = ROOT / "output"


def load_data() -> pd.DataFrame:
    df = pd.read_csv(DATA, parse_dates=["month"])
    df["nna"] = df["inflows"] - df["outflows"]
    df["net_flow_rate"] = df["nna"] / df["aum"]
    df["operating_margin"] = (df["revenue"] - df["opex"]) / df["revenue"]
    df["retention_rate"] = df["retained_clients"] / df["clients"]
    df["nna_vs_target"] = df["nna"] - df["target_nna"]
    df["nna_attainment"] = df["nna"] / df["target_nna"]
    return df


def build_management_view(df: pd.DataFrame) -> pd.DataFrame:
    monthly = df.groupby("month").agg(
        aum=("aum", "sum"),
        inflows=("inflows", "sum"),
        outflows=("outflows", "sum"),
        nna=("nna", "sum"),
        revenue=("revenue", "sum"),
        opex=("opex", "sum"),
        clients=("clients", "sum"),
        retained_clients=("retained_clients", "sum"),
        target_nna=("target_nna", "sum"),
    )
    monthly["net_flow_rate"] = monthly["nna"] / monthly["aum"]
    monthly["operating_margin"] = (monthly["revenue"] - monthly["opex"]) / monthly["revenue"]
    monthly["retention_rate"] = monthly["retained_clients"] / monthly["clients"]
    monthly["nna_vs_target"] = monthly["nna"] - monthly["target_nna"]
    monthly["nna_attainment"] = monthly["nna"] / monthly["target_nna"]
    monthly["nna_mom_pct"] = monthly["nna"].pct_change()
    return monthly.reset_index()


def commentary(row: pd.Series) -> str:
    attainment = row["nna_attainment"]
    if attainment < 0.9:
        return "NNA materially below target; investigate flow drivers."
    if attainment < 1.0:
        return "NNA below target; monitor inflows and outflows."
    if row["operating_margin"] < 0.35:
        return "NNA on target, but operating margin warrants review."
    return "NNA on/above target with healthy operating margin."


def main() -> None:
    df = load_data()
    management = build_management_view(df)
    management["management_commentary"] = management.apply(commentary, axis=1)

    OUTPUT.mkdir(exist_ok=True)
    df.to_csv(OUTPUT / "kpi_detail.csv", index=False)
    management.to_csv(OUTPUT / "management_kpi_summary.csv", index=False)

    latest = management.iloc[-1]
    print("EXECUTIVE KPI REPORT")
    print("=" * 21)
    print(f"Latest month: {latest['month'].date()}")
    print(f"AUM: {latest['aum']:,.0f}")
    print(f"NNA: {latest['nna']:,.0f}")
    print(f"NNA attainment: {latest['nna_attainment']:.1%}")
    print(f"Operating margin: {latest['operating_margin']:.1%}")
    print(f"Client retention: {latest['retention_rate']:.1%}")
    print(f"MoM NNA change: {latest['nna_mom_pct']:.1%}")
    print(f"Commentary: {latest['management_commentary']}")

    print("\nBUSINESS UNIT NNA RANKING")
    ranking = df.groupby("business_unit").agg(nna=("nna", "sum"), revenue=("revenue", "sum"))
    print(ranking.sort_values("nna", ascending=False).to_string())


if __name__ == "__main__":
    main()
