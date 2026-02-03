"""Simulated ETL pipeline for Maine marketplace data."""

from __future__ import annotations

from pathlib import Path

import pandas as pd


class MaineMarketplaceETL:
	def __init__(self) -> None:
		project_root = Path(__file__).resolve().parents[1]
		self.data_sources = {
			"enrollment": project_root / "data" / "processed" / "enrollment_analysis.csv",
		}
		self.output_path = project_root / "data" / "processed" / "tableau_ready_data.csv"

	def extract(self) -> dict[str, pd.DataFrame]:
		"""Simulate data extraction from multiple sources."""
		print("Extracting data from simulated sources...")
		return {
			name: pd.read_csv(path)
			for name, path in self.data_sources.items()
		}

	def transform(self, data_dict: dict[str, pd.DataFrame]) -> pd.DataFrame:
		"""Apply business logic and transformations."""
		print("Transforming data for analytics...")

		enrollment = data_dict["enrollment"].copy()
		enrollment["assistance_rate"] = enrollment["assistance_avg"] / enrollment["premium_avg"]

		enrollment["disparity_index"] = self.calculate_disparity(enrollment)
		return enrollment

	def load(self, transformed_data: pd.DataFrame) -> Path:
		"""Output data for Tableau consumption."""
		print(f"Loading data to {self.output_path}...")
		self.output_path.parent.mkdir(parents=True, exist_ok=True)
		transformed_data.to_csv(self.output_path, index=False)
		return self.output_path

	@staticmethod
	def calculate_disparity(df: pd.DataFrame) -> pd.Series:
		"""Calculate a simplified health coverage disparity index."""
		overall_rate = df["enrollment_count"].sum() / df["eligible_population"].sum()
		group_rate = df["enrollment_count"] / df["eligible_population"]
		return (group_rate / overall_rate) - 1


def main() -> None:
	etl = MaineMarketplaceETL()
	raw_data = etl.extract()
	transformed = etl.transform(raw_data)
	output_path = etl.load(transformed)
	print(f"Tableau-ready dataset written to {output_path}")


if __name__ == "__main__":
	main()
