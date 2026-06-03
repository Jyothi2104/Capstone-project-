-- 1. Top 5 Funds by AUM

SELECT scheme_name, aum_crore
FROM fact_performance
ORDER BY aum_crore DESC
LIMIT 5;

-- 2. Average NAV per Fund

SELECT amfi_code, AVG(nav) AS avg_nav
FROM fact_nav
GROUP BY amfi_code;

-- 3. Total SIP Amount by Fund

SELECT amfi_code, SUM(amount_inr) AS total_sip
FROM fact_transactions
WHERE transaction_type = 'Sip'
GROUP BY amfi_code
ORDER BY total_sip DESC;

-- 4. Transactions by State

SELECT state, COUNT(*) AS total_transactions
FROM fact_transactions
GROUP BY state
ORDER BY total_transactions DESC;

-- 5. Funds with Expense Ratio < 1%

SELECT scheme_name, expense_ratio_pct
FROM fact_performance
WHERE expense_ratio_pct < 1;

-- 6. Top 10 Funds by Sharpe Ratio

SELECT scheme_name, sharpe_ratio
FROM fact_performance
ORDER BY sharpe_ratio DESC
LIMIT 10;

-- 7. Highest Return Funds (5 Year)

SELECT scheme_name, return_5yr_pct
FROM fact_performance
ORDER BY return_5yr_pct DESC
LIMIT 10;

-- 8. Transactions by KYC Status

SELECT kyc_status, COUNT(*) AS total
FROM fact_transactions
GROUP BY kyc_status;

-- 9. Average Transaction Amount by Type

SELECT transaction_type,
       AVG(amount_inr) AS avg_amount
FROM fact_transactions
GROUP BY transaction_type;

-- 10. Fund House Wise Scheme Count

SELECT fund_house,
       COUNT(*) AS scheme_count
FROM dim_fund
GROUP BY fund_house
ORDER BY scheme_count DESC;