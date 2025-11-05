# import streamlit as st

# st.header("About")

# st.html("""<section id="about-dataset" style="padding: 20px; font-family: Arial, sans-serif; line-height: 1.6;">
#   <h2>About This Dataset</h2>
#   <p>
#     The <strong> 
#     Cybersecurity Incidents &amp; Data Breaches 2024</strong> dataset provides a detailed collection of 
#     cybersecurity events including breach types, attack vectors, impacted industries, financial losses, and recovery measures. 
#     It serves as a valuable resource for analyzing the landscape of modern cyber threats and their organizational impact.
#   </p>
  
#   <h3>Contents &amp; Structure</h3>
#   <ul>
#     <li><strong>Incident details</strong>: attack type, vector, severity, and reporting date</li>
#     <li><strong>Impact metrics</strong>: records compromised, financial loss, fines, stock impact</li>
#     <li><strong>Organizational data</strong>: industry sector, employee count, security budget, patch status</li>
#     <li><strong>Response &amp; recovery</strong>: recovery time, CISO presence, MFA usage, training hours</li>
#     <li><strong>Reputation impact</strong>: customer churn %, reputation score change</li>
#   </ul>
  
#   <h3>Exploratory Analysis &amp; Visual Insights</h3>
#   <p>
#     To uncover meaningful patterns, multiple charts and visualizations were created from the dataset:
#   </p>
#   <ol>
#     <li><strong>Attack Landscape:</strong> Distribution of attack types and entry vectors, highlighting the most common threats (e.g., phishing, ransomware, unpatched systems).</li>
#     <li><strong>Industry Impact:</strong> Stacked bar charts showing which industries are most affected by specific attacks, and which sectors leak the most customer data.</li>
#     <li><strong>Timeline Trends:</strong> Incident frequency over time, identifying monthly spikes and seasonal attack patterns.</li>
#     <li><strong>Severity &amp; Consequences:</strong> Correlation between severity and records compromised, patch status vs severity, and MFA adoption vs impact.</li>
#     <li><strong>Financial &amp; Recovery Metrics:</strong> Box plots of financial costs by attack type, recovery time comparisons across industries, ransom vs downtime, and security budget effectiveness.</li>
#     <li><strong>Organizational Factors:</strong> Analysis of CISO presence, training hours, and security budgets in reducing recovery times, churn, and costs.</li>
#     <li><strong>Reputation &amp; Stock Performance:</strong> Customer churn, brand reputation changes, regulatory fines, and stock price movements linked to incidents.</li>
#     <li><strong>Advanced Insights:</strong> Bubble charts (impact vs fines vs employee count) and heatmaps showing correlations across key variables like records compromised, churn, reputation, and recovery time.</li>
#   </ol>

#   <h3>Key Applications</h3>
#   <ul>
#     <li>Identifying industry-specific vulnerabilities and common attack vectors.</li>
#     <li>Comparing financial, reputational, and operational impact across breach types.</li>
#     <li>Modeling relationships between prevention measures (e.g., MFA, patching, training) and outcomes.</li>
#     <li>Building dashboards and predictive models to assess cyber risk readiness.</li>
#   </ul>
  
#   <h3>Limitations</h3>
#   <ul>
#     <li>The dataset is not exhaustive and may underrepresent smaller or unreported incidents.</li>
#     <li>Data quality may vary with missing or approximate values.</li>
#     <li>Reported dates may not always match the actual occurrence of the incident.</li>
#   </ul>
  
#   <h3>Access &amp; Citation</h3>
#   <p>
#     Dataset Source: 
#     <a href="https://www.kaggle.com/datasets/imaadmahmood/cybersecurity-incidents-and-data-breaches-2024?resource=download" 
#        target="_blank" rel="noopener">
#        Kaggle – Cybersecurity Incidents &amp; Data Breaches 2024
#     </a> 
#     by <em>Imaad Mahmood</em>. Please cite appropriately when using in research or public projects.
#   </p>
# </section>
# """)





# ABOUT PAGE

import streamlit as st

st.header("About Dataset")

st.html("""
<section id="about-dataset" style="
  font-family: 'Segoe UI', Roboto, sans-serif; 
  line-height: 1.8;
  color: #1e293b; 
  padding: 10px 20px;
">

  <h2 style="color: #0d47a1; font-size: 1.8rem; margin-top: 10px;">
    🔐 About This Dataset
  </h2>
  <p style="font-size: 1.05rem;">
    The <strong>Cybersecurity Incidents &amp; Data Breaches 2024</strong> dataset offers comprehensive insights into 
    real-world cybersecurity events — detailing attack types, breach vectors, affected industries, and financial consequences. 
    It’s an essential resource for analyzing <strong>cyber threat patterns</strong> and their impact on organizations.
  </p>

  <h3 style="color: #1565c0; margin-top: 30px;">📘 Contents &amp; Structure</h3>
  <ul style="margin-left: 25px;">
    <li><strong>Incident details:</strong> Type, vector, severity, and report date</li>
    <li><strong>Impact metrics:</strong> Compromised records, losses, fines, stock impact</li>
    <li><strong>Organization data:</strong> Sector, employees, budget, patch status</li>
    <li><strong>Response &amp; recovery:</strong> Recovery time, CISO, MFA, training hours</li>
    <li><strong>Reputation impact:</strong> Churn %, reputation score change</li>
  </ul>

  <h3 style="color: #1565c0; margin-top: 30px;">📊 Exploratory Analysis &amp; Visual Insights</h3>
  <p>
    The dataset was deeply analyzed through multiple interactive charts and plots:
  </p>
  <ol style="margin-left: 25px;">
    <li><strong>Attack Landscape:</strong> Distribution of attack types and vectors (phishing, ransomware, etc.).</li>
    <li><strong>Industry Impact:</strong> Which sectors face the most incidents and data exposure.</li>
    <li><strong>Timeline Trends:</strong> Monthly spikes and seasonal attack patterns.</li>
    <li><strong>Severity &amp; Consequences:</strong> Correlation between severity, compromised data, and patch status.</li>
    <li><strong>Financial &amp; Recovery Metrics:</strong> Box plots of cost, downtime, and ransom impact.</li>
    <li><strong>Organizational Factors:</strong> Impact of MFA, CISO, and training on resilience.</li>
    <li><strong>Reputation &amp; Stock:</strong> Effects on brand trust, churn rate, and stock value.</li>
    <li><strong>Advanced Insights:</strong> Bubble and heatmap correlations across major risk dimensions.</li>
  </ol>

  <h3 style="color: #1565c0; margin-top: 30px;">🚀 Key Applications</h3>
  <ul style="margin-left: 25px;">
    <li>Identify high-risk industries and vulnerable systems</li>
    <li>Compare attack outcomes across financial, operational, and reputational factors</li>
    <li>Evaluate how security practices (e.g., MFA, patching) influence outcomes</li>
    <li>Develop dashboards and predictive cyber risk models</li>
  </ul>

  <h3 style="color: #1565c0; margin-top: 30px;">⚠️ Limitations</h3>
  <ul style="margin-left: 25px;">
    <li>Not all smaller or unreported breaches are included</li>
    <li>Some records contain estimates or missing values</li>
    <li>Reported dates may not reflect the true incident date</li>
  </ul>

  <h3 style="color: #1565c0; margin-top: 30px;">🔗 Access &amp; Citation</h3>
  <p style="font-size: 1.05rem;">
    Dataset Source: 
    <a href="https://www.kaggle.com/datasets/imaadmahmood/cybersecurity-incidents-and-data-breaches-2024?resource=download" 
       target="_blank" rel="noopener"
       style="color: #0d47a1; text-decoration: none; font-weight: 600;">
       Kaggle – Cybersecurity Incidents &amp; Data Breaches 2024
    </a> 
    by <em>Imaad Mahmood</em>. <br>
    Please cite this dataset when using in analytics or research projects.
  </p>

  <hr style="border: none; height: 1px; background: #cbd5e1; margin-top: 40px;">
  <p style="color: #64748b; font-size: 0.95rem; margin-top: 10px;">
    © 2024 Cyber Threat Analysis Project | Designed for analytical visualization and insight generation.
  </p>
</section>
""")