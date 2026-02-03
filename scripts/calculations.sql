-- Example SQL that would power Tableau dashboards
-- Shows understanding of relational data for marketplace analytics

WITH monthly_enrollment AS (
	SELECT 
		DATE_TRUNC('month', application_date) AS month,
		county,
		plan_tier,
		COUNT(*) AS enrollments,
		AVG(monthly_premium) AS avg_premium,
		AVG(financial_assistance) AS avg_assistance
	FROM marketplace.enrollments
	WHERE application_date >= '2024-01-01'
	GROUP BY 1, 2, 3
),
county_demographics AS (
	SELECT 
		county,
		total_population,
		uninsured_rate,
		median_income
	FROM public.county_stats
	WHERE state = 'ME'
)
SELECT 
	me.*,
	cd.total_population,
	cd.uninsured_rate,
	cd.median_income,
	me.enrollments::float / cd.total_population AS coverage_rate,
	me.avg_assistance / NULLIF(me.avg_premium, 0) AS assistance_rate
FROM monthly_enrollment me
JOIN county_demographics cd ON me.county = cd.county
ORDER BY me.month, me.county;
