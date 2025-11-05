# DASHBOARD PAGE
import streamlit as st
import pandas as pd
import plotly.express as px

# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(page_title="Cybersecurity Dashboard 2024", layout="wide")

st.title("🛡️ Cybersecurity Incidents & Data Breaches Dashboard (2024)")
st.markdown("Explore 2024 global cybersecurity insights — attacks, recovery times, and financial impacts.")

# ==========================================
# LOAD DATA
# ==========================================
df = pd.read_csv('dataset/Cybersecurity Incidents and Data Breaches 2024.csv')

# ==========================================
# QUICK STATS
# ==========================================
st.divider()
st.subheader("📊 Quick Stats Overview")

col1, col2, col3, col4 = st.columns(4)
col1.metric("💥 Total Incidents", f"{len(df):,}")
col2.metric("💰 Avg Financial Impact", f"${df['Financial_Impact_Million_USD'].mean():.2f}M")
col3.metric("⏳ Avg Recovery Time", f"{df['Recovery_Time_Days'].mean():.0f} Days")
col4.metric("📉 Avg Customer Churn", f"{df['Customer_Churn_Percent'].mean():.1f}%")

st.divider()

# ==========================================
# 1️⃣ ATTACK PATTERNS
# ==========================================
st.header("🎯 Attack Patterns and Vectors")

# 1st

fig = px.bar(df, x='Attack_Type', y='Previous_Incidents',
             title='Attack Type vs Incident Count',
             color='Previous_Incidents', template='plotly_dark')
st.plotly_chart(fig, use_container_width=True)
st.caption("➡️ Most common attack types include ransomware and phishing.")

st.divider()

# 2nd
fig = px.bar(df, x='Attack_Vector', y='Previous_Incidents',
             title='Attack Vector vs Incident Count',
             color='Previous_Incidents', template='plotly_dark')
st.plotly_chart(fig, use_container_width=True)
st.caption("➡️ Email and unpatched systems are major weak entry points.")

st.divider()

# 3rd
fig = px.bar(df, x='Industry', y='Attack_Type',
             title='Industry vs Attack Type',
             color='Previous_Incidents', template='plotly_dark')
st.plotly_chart(fig, use_container_width=True)
st.caption("➡️ Healthcare and finance are more prone to targeted attacks.")

st.divider()

# 4th
fig = px.bar(df, x='Date_Reported', y='Previous_Incidents',
             title='Incidents over Time (Date Reported)',
             color='Date_Reported', template='plotly_dark')
st.plotly_chart(fig, use_container_width=True)
st.caption("➡️ Shows seasonal spikes or specific months of high attack activity.")

st.divider()

# ==========================================
# 2️⃣ INDUSTRY IMPACT
# ==========================================
st.header("🏢 Industry-Wise Impact Analysis")

# 5th
fig = px.bar(df, x='Industry', y='Records_Compromised',
             title='Records Compromised by Industry',
             color='Industry', template='plotly_dark')
st.plotly_chart(fig, use_container_width=True)
st.caption("➡️ Industries like healthcare face maximum data breaches.")

st.divider()

# 6th
fig = px.box(df, x="Attack_Type", y="Financial_Impact_Million_USD",
             points="all", color='Financial_Impact_Million_USD',
             title="Financial Impact by Attack Type", template='plotly_dark')
st.plotly_chart(fig, use_container_width=True)
st.caption("➡️ Ransomware has the highest median financial impact.")

st.divider()

# 7th
# df[['Industry','Recovery_Time_Days']]
new_data = df.copy()
meanRecoveryDays = new_data.groupby("Industry")["Recovery_Time_Days"].mean().reset_index()
# st.dataframe(meanRecoveryDays)
fig = px.bar(meanRecoveryDays, x='Industry', y='Recovery_Time_Days',
             title='Average Recovery Time by Industry',
             color='Recovery_Time_Days', template='plotly_dark')
st.plotly_chart(fig, use_container_width=True)
st.caption("➡️ Government and manufacturing sectors show longer downtimes.")

st.divider()

# 8th
fig = px.scatter(df, x="Ransom_Amount_USD", y="Recovery_Time_Days",
                 title="Recovery Time vs Ransom Amount",
                 color='Recovery_Time_Days', template='plotly_dark')
st.plotly_chart(fig, use_container_width=True)
st.caption("➡️ Higher ransom demands often mean longer recovery.")

st.divider()

# ==========================================
# 3️⃣ SEVERITY & PATCH STATUS
# ==========================================
st.header("🔥 Incident Severity and System Readiness")

# 9th

fig = px.bar(df, x='Incident_Severity', y='Records_Compromised',
             title='Incident Severity vs Records Compromised',
             color='Records_Compromised', template='plotly_dark')
st.plotly_chart(fig, use_container_width=True)

st.divider()

# 10th
fig = px.bar(df, x='Patch_Status', y='Incident_Severity',
             title='Patch Status vs Severity',
             color='Incident_Severity', template='plotly_dark')
st.plotly_chart(fig, use_container_width=True)

st.divider()

# 11th
fig = px.bar(df, x='MFA_Enabled', y='Incident_Severity',
             title='MFA Enabled vs Incident Severity',
             color='MFA_Enabled', template='plotly_dark')
st.plotly_chart(fig, use_container_width=True)
st.caption("➡️ Companies with MFA enabled see lower severity incidents.")

st.divider()

# ==========================================
# 4️⃣ FINANCIAL & SECURITY CORRELATION
# ==========================================
st.header("💰 Financial Correlations and Security Readiness")

# 12th
fig = px.scatter(df, x="Security_Budget_Million_USD", y="Financial_Impact_Million_USD",
                 title="Security Budget vs Financial Impact",
                 color='Security_Budget_Million_USD', template='plotly_dark')
st.plotly_chart(fig, use_container_width=True)
st.caption("➡️ Higher security budgets correlate with reduced impact.")

st.divider()

# 13th
fig = px.bar(df, x='CISO_Present', y='Recovery_Time_Days',
             title='CISO Presence vs Recovery Time',
             color='Recovery_Time_Days', template='plotly_dark')
st.plotly_chart(fig, use_container_width=True)
st.caption("➡️ Organizations with CISOs tend to recover faster.")

st.divider()

# 14th
fig = px.scatter(df, x="Security_Training_Hours", y="Customer_Churn_Percent",
                 title="Training Hours vs Customer Churn",
                 color='Security_Training_Hours', template='plotly_dark')
st.plotly_chart(fig, use_container_width=True)
st.caption("➡️ More training leads to reduced churn and better resilience.")

st.divider()

# 15th
fig = px.bar(df, x='Industry', y='Regulatory_Fine_Million_USD',
             title='Regulatory Fines by Industry',
             color='Industry', template='plotly_dark')
st.plotly_chart(fig, use_container_width=True)
st.caption("➡️ Finance and energy industries face heavy penalties.")

st.divider()

# 16th
fig = px.scatter(df, x="Financial_Impact_Million_USD", y="Stock_Impact_Percent",
                 title="Stock Impact % vs Financial Impact",
                 color='Financial_Impact_Million_USD', template='plotly_dark')
st.plotly_chart(fig, use_container_width=True)
st.caption("➡️ Stock prices often drop proportionally to financial losses.")

st.divider()

# 17th
fig = px.bar(df, x='Attack_Type', y='Customer_Churn_Percent',
             title='Customer Churn (%) by Attack Type',
             color='Customer_Churn_Percent', template='plotly_dark')
st.plotly_chart(fig, use_container_width=True)
st.caption("➡️ Phishing and insider threats increase customer churn the most.")

st.divider()

# 18th
fig = px.bar(df, x='Industry', y='Reputation_Score_Change',
             title='Reputation Score Change by Industry',
             color='Industry', template='plotly_dark')
st.plotly_chart(fig, use_container_width=True)
st.caption("➡️ Healthcare and tech sectors see significant reputation damage.")

st.divider()

# 19th
fig = px.scatter(df, x="Financial_Impact_Million_USD", y="Regulatory_Fine_Million_USD",
                 title="Financial Impact vs Regulatory Fine",
                 color='Financial_Impact_Million_USD', template='plotly_dark')
st.plotly_chart(fig, use_container_width=True)
st.caption("➡️ Financial losses and fines go hand-in-hand for large firms.")

st.divider()

# 20th
cols = ['Records_Compromised', 'Financial_Impact_Million_USD', 'Recovery_Time_Days',
        'Customer_Churn_Percent', 'Reputation_Score_Change']
corr_matrix = df[cols].corr()

fig = px.imshow(corr_matrix, text_auto=True, aspect="auto",
                color_continuous_scale='RdBu_r', template='plotly_dark',
                title="Correlation Heatmap – Key Variables")
st.plotly_chart(fig, use_container_width=True)
st.caption("➡️ Strong correlation between financial losses, records compromised, and reputation drop.")

st.divider()

# ==========================================
# FINAL SUMMARY
# ==========================================
st.header("🧠 Summary Insights")
st.markdown("""
- **Ransomware** and **phishing** are the most frequent and damaging attacks.  
- **Email** is still the most exploited attack vector.
- **Healthcare** & **Finance** industries face the largest data and financial losses.  
- **MFA, CISO presence, and security training** greatly reduce incident severity.
- **High security budgets** and **patch compliance** help prevent costly damage.
""")

st.success("✅ Strategic investment in prevention and response yields measurable reductions in impact and recovery time.")