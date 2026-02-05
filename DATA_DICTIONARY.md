# Data Dictionary

## Synthetic Data Notes
All tables in this repository are **synthetic** datasets created for portfolio and demonstration purposes. Values are simulated to reflect realistic enrollment behavior (seasonal growth, demographic segmentation, eligibility vs enrollment) without using any real marketplace or personal data.

## enrollment_data.csv

### Columns

| Column | Type | Description |
|--------|------|-------------|
| month | Date | Enrollment month (YYYY-MM format) |
| county | String | Maine county name |
| age_group | String | Age bracket (18-34, 35-49, 50-64) |
| income_bracket | String | Federal Poverty Level ranges for subsidy eligibility:<br>- <200% FPL: Low income, high subsidies<br>- 200-400% FPL: Moderate income, partial subsidies<br>- >400% FPL: Higher income, no subsidies |
| plan_tier | String | Insurance plan metal level (Bronze/Silver/Gold = coverage level) |
| enrollment_count | Integer | Number of people enrolled |
| eligible_population | Integer | Total people eligible to enroll |
| premium_avg | Float | Average monthly insurance premium cost ($) |
| assistance_avg | Float | Average financial assistance provided ($) |
| disability_flag | String | Has disability (Yes/No) |
| race_ethnicity | String | Demographic group (White, Black, Hispanic, Asian, Other) |

## Dashboard KPIs

### 1. Total Enrollments
Sum of all enrolled individuals. Shows program reach and growth.

**Formula:** `SUM([enrollment_count])`

### 2. Coverage Rate
Percentage of eligible people who enrolled. Measures enrollment effectiveness.

**Formula:** `SUM([enrollment_count]) / SUM([eligible_population])`

**Example:** 0.25 = 25% of eligible people are enrolled

### 3. Assistance Rate
Financial help as percentage of premium cost. Shows subsidy utilization.

**Formula:** `SUM([assistance_avg]) / SUM([premium_avg])`

**Example:** 0.65 = 65% of premium costs are covered by subsidies

### 4. Disparity Index
Equity metric showing if certain groups are under/over-enrolled compared to overall average.

**Formula:** `(Group Coverage Rate / Overall Coverage Rate) - 1`

**Interpretation:**
- Positive value: Group is over-enrolled (better than average)
- Negative value: Group is under-enrolled (equity gap)
- Zero: Group enrollment matches overall rate (parity)

## Additional Datasets

### consumer_metrics.csv
Tracks application journey and consumer experience metrics including completion rates, support calls, and digital engagement.

### county_demographics.csv
Maine county population data including uninsured rates, median income, poverty rates, and eligible unenrolled populations.

### outreach_campaigns.csv
Campaign effectiveness data tracking contacts, enrollments generated, and cost per enrollment.

### regulatory_reporting.csv
Compliance tracking for required reports including CMS submissions and state reporting.
