import streamlit as st
import pandas as pd

# Set up the page title and header
st.title("Pay Stub Generator")
st.write("Generate a customized pay stub with detailed earnings, deductions, and year-to-date summaries.")

# Step 1: Employee Information
st.header("1. Employee Information")
employee_name = st.text_input("Employee Name", "TANYA CHAVIS")
ssn = st.text_input("Social Security Number (SSN)", "XXX-XX-6286")
employee_id = st.text_input("Employee ID", "2454")
check_number = st.text_input("Check Number", "4895")
pay_period_start = st.date_input("Pay Period Start", value=pd.to_datetime("2024-08-19"))
pay_period_end = st.date_input("Pay Period End", value=pd.to_datetime("2024-09-01"))
pay_date = st.date_input("Pay Date", value=pd.to_datetime("2024-09-07"))

# Step 2: Earnings Information
st.header("2. Earnings")
regular_hours = st.number_input("Regular Hours Worked", value=80.0)
overtime_hours = st.number_input("Overtime Hours Worked", value=10.0)
regular_rate = st.number_input("Hourly Rate", value=50.0)
overtime_rate = st.number_input("Overtime Rate (1.5x regular rate)", value=regular_rate * 1.5)
bonus = st.number_input("Bonus Pay", value=0.00)

# Calculate earnings
regular_income = regular_hours * regular_rate
overtime_income = overtime_hours * overtime_rate
total_income = regular_income + overtime_income + bonus

# Display Earnings Summary
st.subheader("Earnings Summary")
st.write(f"Regular Income: ${regular_income:,.2f}")
st.write(f"Overtime Income: ${overtime_income:,.2f}")
st.write(f"Bonus: ${bonus:,.2f}")
st.write(f"Total Earnings: ${total_income:,.2f}")

# Step 3: Deductions
st.header("3. Deductions")
federal_tax = st.number_input("Federal Income Tax", value=2702.49)
social_security_tax = st.number_input("Social Security Tax (6.2%)", value=total_income * 0.062)
medicare_tax = st.number_input("Medicare Tax (1.45%)", value=total_income * 0.0145)
additional_medicare_tax = st.number_input("Additional Medicare Tax (if applicable)", value=69.24)
state_tax = st.number_input("State Tax", value=597.05)
health_insurance = st.number_input("Health Insurance Deduction", value=150.00)
retirement_contribution = st.number_input("401k/Retirement Contribution", value=200.00)
other_deductions = st.number_input("Other Deductions", value=0.00)

# Calculate total deductions
total_deductions = (federal_tax + social_security_tax + medicare_tax + additional_medicare_tax +
                    state_tax + health_insurance + retirement_contribution + other_deductions)

# Step 4: Year-to-Date (YTD) Summary
st.header("4. Year-to-Date (YTD) Summary")
ytd_gross = st.number_input("Year-to-Date Gross Earnings", value=207692.92)
ytd_deductions = st.number_input("Year-to-Date Total Deductions", value=72925.90)
ytd_net_pay = st.number_input("Year-to-Date Net Pay", value=134767.02)

# Update YTD calculations with current period
ytd_gross += total_income
ytd_deductions += total_deductions
ytd_net_pay = ytd_gross - ytd_deductions

# Step 5: Net Pay Calculation
st.header("5. Net Pay")
net_pay = total_income - total_deductions
st.write(f"Net Pay for the Current Period: ${net_pay:,.2f}")

# Display Deductions Summary
st.subheader("Deductions Summary")
st.write(f"Federal Income Tax: ${federal_tax:,.2f}")
st.write(f"Social Security Tax: ${social_security_tax:,.2f}")
st.write(f"Medicare Tax: ${medicare_tax:,.2f}")
st.write(f"Additional Medicare Tax: ${additional_medicare_tax:,.2f}")
st.write(f"State Tax: ${state_tax:,.2f}")
st.write(f"Health Insurance: ${health_insurance:,.2f}")
st.write(f"401k/Retirement Contribution: ${retirement_contribution:,.2f}")
st.write(f"Other Deductions: ${other_deductions:,.2f}")
st.write(f"Total Deductions: ${total_deductions:,.2f}")

# Display Year-to-Date Summary
st.subheader("Year-to-Date Summary")
st.write(f"YTD Gross Earnings: ${ytd_gross:,.2f}")
st.write(f"YTD Deductions: ${ytd_deductions:,.2f}")
st.write(f"YTD Net Pay: ${ytd_net_pay:,.2f}")

# Optional: Download as PDF (using a simple placeholder since Streamlit doesn't natively support PDF downloads)
st.header("6. Download Pay Stub")
st.write("To download this pay stub, take a screenshot or save this page.")
