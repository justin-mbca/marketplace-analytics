# Maine Health Insurance Marketplace Analytics Portfolio
**Interview Summary Document**

---

## 🎯 Project Overview
Comprehensive healthcare analytics portfolio demonstrating end-to-end data pipeline, semantic modeling, and multi-platform BI implementation for Maine CoverME.gov marketplace enrollment analysis.

**Candidate**: Xiangli Zhang  
**Target Role**: Marketplace Data & Reporting Manager, Maine DHHS  
**Portfolio Links**:
- **Tableau**: https://public.tableau.com/app/profile/xiangli.zhang/viz/ExecutiveSummary_17700932109510/Story1?publish=yes
- **Power BI**: https://app.powerbi.com/groups/b2e957bd-e2b4-43d1-9b5c-8cb379b9831b/reports/9302dd03-cfbe-4a02-b1aa-232f671a7331/08b9033697f6e0551a41
- **GitHub**: https://github.com/justin-mbca/marketplace-analytics

---

## 📊 Completed Deliverables

### 1. Tableau Executive Summary Dashboard ✅
**Platform**: Tableau Public  
**Type**: Interactive story with 4 narrative insights

**Components**:
- **Story Points**: 4 key findings about Maine enrollment trends
- **KPI Cards**: Total Enrollments (29,330), Coverage Rate (0.25), Assistance Rate (0.5874), Disparity Index (-1.0)
- **Geographic Visualization**: County map (color: uninsured rate, size: population)
- **Trend Analysis**: Enrollment stacked bar chart by plan tier (Bronze/Silver/Gold)
- **Demographic Breakdowns**: 
  - Age groups (18-34, 35-49, 50-64)
  - Income brackets (<200% FPL, 200-400% FPL, >400% FPL)
  - Race/ethnicity (pie chart)

**Calculated Fields**:
```tableau
Coverage Rate = SUM([Enrollment Count]) / SUM([Eligible Population])
Assistance Rate = AVG([Assistance Avg]) / NULLIF(AVG([Premium Avg]), 0)
Disparity Index = (Group Rate / Overall Rate) - 1
```

---

### 2. Power BI Executive Summary Report ✅
**Platform**: Power BI Service (Microsoft Fabric)  
**Type**: 5-page report structure (1 page complete, 4 in progress)

**Page 1: Executive Summary (COMPLETE)**
- **12-Month Trend Line**: Jan-Dec 2024 enrollment growth (8.6% increase)
- **4 KPI Cards**: 
  - Total Enrollments: 16,440
  - Coverage Rate: 25.0%
  - Average Premium: $316.92
  - Assistance Rate: calculated %
- **3 Demographic Bar Charts**: Age groups, income brackets, race/ethnicity

**DAX Measures**:
```dax
Total Enrollments = SUM(enrollment_data[enrollment_count])
Coverage Rate = DIVIDE(SUM(enrollment_data[enrollment_count]), SUM(enrollment_data[eligible_population]), 0) * 100
Avg Premium = AVERAGE(enrollment_data[premium_avg])
Assistance Rate = DIVIDE(CALCULATE(SUM(enrollment_data[enrollment_count]), enrollment_data[assistance_avg] > 0), SUM(enrollment_data[enrollment_count]), 0) * 100
```

**Data Pipeline**: GitHub CSV → Power BI Dataflow Gen2 → Semantic Model → Report

---

## 📁 Data Sources (Synthetic)

All datasets are **synthetic** (simulated for portfolio purposes) and designed to approximate realistic Maine CoverME.gov enrollment patterns.

### Primary Dataset: enrollment_data.csv
- **Rows**: 158 (expanded from 40 to cover full year)
- **Time Period**: Jan-Dec 2024 (monthly granularity)
- **Geography**: 6 Maine counties (Cumberland, Penobscot, York, Androscoggin, Kennebec, Aroostook)

**Dimensions**:
- Age groups: 18-34, 35-49, 50-64
- Income brackets: <200% FPL, 200-400% FPL, >400% FPL
- Plan tiers: Bronze, Silver, Gold
- Race/ethnicity: White, Black, Hispanic
- Disability flag: Yes/No

**Measures**:
- `enrollment_count`: Number of enrolled individuals
- `eligible_population`: Total eligible population
- `premium_avg`: Average monthly premium ($)
- `assistance_avg`: Average financial assistance ($)

### Supporting Datasets
1. **county_demographics.csv** - Population, uninsured rates, poverty rates
2. **consumer_metrics.csv** - Application journey, support metrics
3. **outreach_campaigns.csv** - Campaign performance, ROI
4. **regulatory_reporting.csv** - Compliance tracking, submission timeline

---

## 🎯 To-Do: Remaining Dashboards

### Page 2: Consumer Experience (Next Priority)
- [ ] Application completion funnel
- [ ] Plan tier distribution by demographics
- [ ] Digital engagement metrics (web visits, form abandonment)
- [ ] Support call metrics (volume, resolution rate)

### Page 3: Equity & Disparity Analysis
- [ ] Coverage gap analysis (eligible vs enrolled)
- [ ] Disparity heat map by demographic x county
- [ ] Income bracket equity metrics
- [ ] Priority outreach matrix (uninsured rate vs poverty rate)

### Page 4: Regulatory Reporting
- [ ] Enrollment certification tracker
- [ ] Data quality scorecard
- [ ] DHHS submission timeline (Gantt chart)
- [ ] Compliance calendar dashboard

### Page 5: Outreach Effectiveness
- [ ] Campaign ROI analysis by county
- [ ] Target population reach metrics
- [ ] Seasonal enrollment patterns by campaign
- [ ] Cost per enrollment tracking

---

## 🛠️ Technical Skills Demonstrated

### Data Engineering
- ETL pipeline design (GitHub → Dataflow Gen2 → Semantic Model)
- Data expansion (40 rows → 158 rows, 3 months → 12 months)
- Data validation and quality checks
- Relationship modeling (2 M:1 relationships defined)

### Analytics & BI
- **Tableau**: Story creation, calculated fields, geographic visualizations
- **Power BI**: DAX measures, KPI cards, trend analysis, semantic modeling
- **Data Visualization**: KPIs, trend lines, demographic breakdowns, maps
- **Healthcare Metrics**: Coverage rate, assistance rate, disparity indices

### Documentation & Governance
- Data dictionary creation
- Process documentation (5-phase development timeline)
- Synthetic data design principles
- GitHub version control and portfolio publishing

---

## 💡 Key Insights from Analysis

1. **Growth Trend**: Maine enrollment grew 8.6% from Jan to Dec 2024
2. **Coverage Rate**: 25% of eligible population enrolled
3. **Geographic Leader**: Cumberland County leads in enrollment volume
4. **Income-Based Gaps**: Measurable disparities across income brackets
5. **Assistance Effectiveness**: 58.7% assistance rate shows subsidy utilization

---

## 🎓 Alignment with OHIM Role Requirements

| JD Requirement | Portfolio Evidence |
|----------------|-------------------|
| Data analysis & cleaning | Expanded dataset, validated 158 rows, normalized demographics |
| Operational reporting | KPI definitions, calculated measures, metrics framework |
| Tableau/Power BI experience | Both platforms deployed with published dashboards |
| Documentation | README, data dictionary, calculated fields documentation |
| Programmatic reporting | Reproducible pipeline, automated data flow |
| Healthcare analytics | Enrollment metrics, coverage rates, equity analysis |
| Stakeholder translation | Story points, KPI cards, visual dashboards |

---

## 📞 Contact & Portfolio Access
- **Email**: justinzhang.xl@gmail.com
- **GitHub**: https://github.com/justin-mbca/marketplace-analytics
- **LinkedIn**: [Profile Link]
- **Portfolio Status**: Live dashboards published, PDF extract available
