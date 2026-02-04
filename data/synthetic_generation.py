"""Synthetic data generation for marketplace analytics."""

from __future__ import annotations

from datetime import datetime
from pathlib import Path

import numpy as np
import pandas as pd


def generate_enrollment_data() -> pd.DataFrame:
	"""Create synthetic enrollment data for Maine counties."""
	rng = np.random.default_rng(42)
	counties = ["Cumberland", "Penobscot", "York", "Androscoggin", "Kennebec"]
	races = ["White", "Black", "Hispanic", "Asian", "Other"]
	months = pd.date_range("2024-01-01", "2024-12-01", freq="MS")

	rows = []
	for month in months:
		for county in counties:
			for race in races:
				eligible_population = rng.integers(1500, 12000)
				enrollment_count = rng.integers(300, min(eligible_population, 5000))
				premium_avg = rng.uniform(280, 760)
				assistance_avg = rng.uniform(80, 420)
				rows.append(
					{
						"month": month.strftime("%Y-%m"),
						"county": county,
						"race_ethnicity": race,
						"eligible_population": int(eligible_population),
						"enrollment_count": int(enrollment_count),
						"premium_avg": round(float(premium_avg), 2),
						"assistance_avg": round(float(assistance_avg), 2),
					}
				)

	return pd.DataFrame(rows)


def update_raw_enrollment_data(raw_path: Path) -> None:
	"""Append eligible_population to the raw enrollment CSV."""
	if not raw_path.exists():
		raise FileNotFoundError(f"Raw enrollment file not found: {raw_path}")

	df = pd.read_csv(raw_path)
	if "eligible_population" not in df.columns:
		df.insert(
			loc=df.columns.get_loc("enrollment_count") + 1,
			column="eligible_population",
			value=(df["enrollment_count"] * 4).astype(int),
		)
		df.to_csv(raw_path, index=False)


def main() -> None:
	output_path = Path(__file__).resolve().parents[1] / "data" / "processed" / "enrollment_analysis.csv"
	output_path.parent.mkdir(parents=True, exist_ok=True)

	raw_path = Path(__file__).resolve().parents[1] / "data" / "raw" / "enrollment_data.csv"
	update_raw_enrollment_data(raw_path)

	df = generate_enrollment_data()
	df.to_csv(output_path, index=False)
	print(f"Generated synthetic data at {output_path}")


if __name__ == "__main__":
	main()
