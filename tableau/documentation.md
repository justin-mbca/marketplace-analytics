# Maine Marketplace Analytics Documentation

## Data Sources
- Synthetic enrollment data (simulating CoverME.gov)
- Maine county demographics (public data)
- Consumer experience metrics (placeholder for expansion)

## Methodology
1. Disparity Index Calculation: $\text{Disparity Index} = \frac{\text{Group Coverage Rate}}{\text{Overall Coverage Rate}} - 1$
2. Outreach ROI: $\text{ROI} = \frac{\text{Engagement Gain}}{\text{Outreach Cost}}$
3. Data Validation: null checks, positive premium checks, logical date ranges

## Dashboard Architecture
- **Executive Summary**: KPI-focused
- **Equity Analysis**: Disparity indices by county and demographic group
- **Regulatory Reporting**: Compliance and trend tracking
- **Consumer Experience**: Application journey and support metrics
- **Outreach Effectiveness**: Campaign performance and ROI

## Refresh Cadence
- Monthly updates aligned with enrollment cycles
- Ad-hoc refresh for policy changes or emergency enrollment periods

## Tableau Build Checklist
### Data Connections
1. Connect to [data/raw/enrollment_data.csv](data/raw/enrollment_data.csv)
2. Connect to [data/raw/consumer_metrics.csv](data/raw/consumer_metrics.csv)
3. Connect to [data/raw/county_demographics.csv](data/raw/county_demographics.csv)
4. Connect to [data/raw/outreach_campaigns.csv](data/raw/outreach_campaigns.csv)
5. Connect to [data/raw/regulatory_reporting.csv](data/raw/regulatory_reporting.csv)

### Dashboard 1: Executive Summary
- KPI cards: Total Enrollments (YTD), Consumer Satisfaction, Outreach ROI, Disparity Index
- Enrollment trend: Month vs Enrollment Count, color by Plan Tier, county filter
- County map: Color by uninsured rate, size by population
- Demographic breakdown: age group, income bracket, race/ethnicity

### Dashboard 2: Consumer Experience
- Journey funnel (aware → interested → applied → completed → enrolled)
- Support metrics: calls per enrollment, call resolution rate
- Digital engagement: website visits, form abandonment

### Dashboard 3: Equity & Disparity Analysis
- Disparity heat map (rows: demographic, columns: county)
- Coverage gap analysis: eligible vs enrolled
- Priority outreach matrix: uninsured rate vs poverty rate

### Dashboard 4: Regulatory Reporting
- Compliance calendar (Gantt)
- Data quality scorecards
- Submission tracking timeline

### Dashboard 5: Outreach Effectiveness
- Campaign ROI dashboard
- Target population analysis
- Seasonal patterns by campaign

## Advanced Tableau Features to Include
### Parameter Controls
- Date Range Selector: Last 30 Days, Quarter to Date, Year to Date, Full History

### Calculated Fields
1. Outreach Effectiveness Score
```
([enrollments_generated] / [contacts_made]) * 100 
/ AVG([enrollments_generated] / [contacts_made])
```
2. Equity Score
```
1 - ABS(( [subgroup_rate] - [overall_rate] ) / [overall_rate])
```
3. Consumer Journey Drop-off
```
PREVIOUS_VALUE([stage_count]) - [stage_count]
```

### LOD Expressions
- County-level averages
```
{ FIXED [county] : AVG([premium_avg]) }
```
- Running totals
```
RUNNING_SUM(SUM([enrollment_count]))
```

## Branding & Accessibility
- Colors: Maine blue #003087, pine green #00843D
- Font: Arial or Verdana
- High contrast and readable labels
