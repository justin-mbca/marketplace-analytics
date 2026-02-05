# Health Insurance Marketplace Analytics

## Overview
Comprehensive healthcare analytics portfolio demonstrating end-to-end data pipeline, semantic modeling, and multi-platform BI implementation. Features a 5-page Power BI report analyzing Maine CoverME.gov marketplace enrollment, equity, consumer experience, and regulatory compliance.

**Status**: Power BI Executive Summary **COMPLETE** ✅ | 4 additional pages in progress

---

## 📊 Project Deliverables

### Tableau Executive Summary ✅ **COMPLETE**
**Platform**: Tableau Desktop/Story
**Status**: Executive Summary dashboard + story completed (see [tableau/documentation.md](tableau/documentation.md))
**Link**: https://public.tableau.com/app/profile/xiangli.zhang/viz/ExecutiveSummary_17700932109510/Story1?publish=yes

**Included**:
- Story narrative with 4 key findings
- KPI cards: Total Enrollments, Coverage Rate KPI, Assistance Rate, Disparity Index
- County map (color: uninsured rate, size: population)
- Enrollment trend (stacked by plan tier)
- Demographic breakdowns: age group, income bracket, race/ethnicity

### Power BI Report (5 Pages)
**Platform**: Power BI Service (Microsoft Fabric)  
**Data Source**: GitHub CSV → Power BI Dataflow Gen2 → Semantic Model → Report  
**Link**: https://app.powerbi.com/groups/b2e957bd-e2b4-43d1-9b5c-8cb379b9831b/reports/9302dd03-cfbe-4a02-b1aa-232f671a7331/08b9033697f6e0551a41?redirectedFromSignup=1&experience=power-bi

#### Page 1: Executive Summary ✅ **COMPLETE**
**8 Visualizations**:
1. 12-Month Enrollment Trend (Line Chart) - 8.6% growth Jan→Dec
2. Total Enrollments (KPI) - 16,440
3. Coverage Rate (KPI) - 25.0%
4. Average Premium (KPI) - $316.92
5. Enrollment with Assistance (KPI) - % subsidies
6. Enrollment by Age Group (Bar Chart)
7. Enrollment by Income Bracket (Bar Chart)
8. Enrollment by Race/Ethnicity (Bar Chart)

#### Page 2: Consumer Experience (IN PROGRESS)
- [ ] Application completion rate
- [ ] Plan tier distribution
- [ ] Demographic reach analysis
- [ ] Support metrics

#### Page 3: Equity & Disparity (IN PROGRESS)
- [ ] Coverage gaps by demographic
- [ ] Race/ethnicity disparities
- [ ] Income bracket analysis
- [ ] Geographic equity metrics

#### Page 4: Regulatory Reporting (IN PROGRESS)
- [ ] Enrollment certifications
- [ ] Data quality scorecard
- [ ] DHHS submission timeline
- [ ] Compliance dashboard

#### Page 5: Outreach Effectiveness (IN PROGRESS)
- [ ] Campaign performance by county
- [ ] ROI analysis
- [ ] Seasonal trends
- [ ] Conversion metrics

---

## 🔄 Development Process

### Phase 1: Data Expansion ✅
- Original: 40 rows (Jan-Mar 2024)
- Result: 158 rows (12 months, Jan-Dec 2024)
- GitHub commit: b3bd08b

### Phase 2: Data Pipeline Setup ✅
- Power BI Dataflow Gen2 + GitHub integration
- 5 CSV tables loaded
- Month data type resolved

### Phase 3: Semantic Model Development ✅
- 2 relationships created
- 5 tables with 158 enrollment rows
- All 6 Maine counties covered

### Phase 4: DAX Measures ✅
- 4 measures deployed (Enrollments, Coverage Rate, Avg Premium, Assistance Rate)
- All formulas tested

### Phase 5: Visualization ✅
- 8 visualizations completed
- 1 trend + 4 KPIs + 3 demographics
- Executive Summary page done

---

## 🎯 To-Do: Remaining Reports

**Consumer Experience**
- [ ] Application completion rate
- [ ] Plan tier visualization
- [ ] Channel reach analysis
- [ ] Support metrics

**Equity & Disparity**
- [ ] Disparity calculations
- [ ] Heat maps by demographic
- [ ] Income gap analysis
- [ ] Geographic equity

**Regulatory Reporting**
- [ ] Certification tracker
- [ ] Quality scorecard
- [ ] Submission timeline
- [ ] Compliance status

**Outreach Effectiveness**
- [ ] Campaign ROI
- [ ] County heat map
- [ ] Seasonal analysis
- [ ] Conversion metrics

**Publishing**
- [ ] Deploy to Power BI Service
- [ ] Generate portfolio URLs
- [ ] Update job application
- [ ] Publish Tableau workbook/story

---

## 📁 Project Structure
```
marketplace-analytics/
├── data/
│   ├── raw/
│   │   ├── enrollment_data.csv (158 rows, 12 months)
│   │   ├── county_demographics.csv
│   │   ├── consumer_metrics.csv
│   │   ├── outreach_campaigns.csv
│   │   └── regulatory_reporting.csv
├── notebooks/
├── scripts/
├── tableau/
├── DATA_DICTIONARY.md
└── README.md
```

---

## 🧪 Synthetic Data Summary
All datasets in this project are **synthetic** (simulated) and created for portfolio purposes only. They are designed to **approximate realistic enrollment patterns** without using any real patient or marketplace data.

**Scope & Coverage**:
- **Time period**: Jan–Dec 2024 (monthly)
- **Geography**: 6 Maine counties (Cumberland, Penobscot, York, Androscoggin, Kennebec, Aroostook)
- **Core dimensions**: age group, income bracket (FPL), plan tier, race/ethnicity, disability flag
- **Measures**: enrollment counts, eligible population, average premium, average assistance

**How the synthetic data behaves**:
- **Seasonal growth**: Enrollment trends increase month over month to simulate open enrollment patterns.
- **Demographic segmentation**: Counts are split across age, income, race/ethnicity, and plan tiers to enable equity analysis.
- **Eligibility vs enrollment**: Eligible population values are higher than enrollments to allow calculation of coverage rate.
- **Premium & assistance**: Average premiums and subsidies follow realistic directional logic (higher premiums for Gold; lower assistance for higher-income tiers).

**Why synthetic data**:
- Avoids PHI/PII exposure
- Enables reproducible analytics examples
- Allows interviewers to focus on modeling, BI design, and storytelling

---

## 🛠 Technical Stack
**Data**: GitHub CSVs  
**ETL**: Power BI Dataflow Gen2, Power Query  
**Analytics**: Semantic Model, DAX, Power BI Desktop, Tableau Desktop  
**Deployment**: Power BI Service, GitHub, Tableau  

---

## 📊 Key Metrics
| Metric | Value |
|--------|-------|
| Total Enrollments | 16,440 |
| Coverage Rate | 25.0% |
| Avg Premium | $316.92 |
| Data Period | Jan-Dec 2024 |
| Growth Rate | 8.6% |
| Counties | 6 Maine |

---

## 🎓 Skills Demonstrated
✅ Data Engineering (ETL, relationships)
✅ Analytics (DAX, KPIs)
✅ Healthcare Analytics (enrollment, equity)
✅ Project Management (5-page planning)

---

## 📞 Contact
- **Name**: Justin Zhang
- **Email**: justinzhang.xl@gmail.com
- **GitHub**: github.com/justin-mbca
- **Target**: Maine DHHS Data & Reporting Manager
- **GitHub Repo**: https://github.com/justin-mbca/marketplace-analytics
