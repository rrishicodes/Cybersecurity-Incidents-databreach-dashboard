# HOME PAGE
import streamlit as st

st.html("""
<section id="home" style="
  font-family: 'Segoe UI', Roboto, sans-serif; 
  text-align: center; 
  color: #1e293b;
  padding: 20px 40px 60px 40px;
  line-height: 1.7;
">

  <!-- Banner Image -->
  <div style="margin: 0 auto 30px auto; max-width: 1000px; border-radius: 12px; overflow: hidden; box-shadow: 0 4px 20px rgba(0,0,0,0.1);">
    <img src="https://www.reliancetechnologies.co.uk/wp-content/uploads/2016/06/cyber-security-banner.jpg" 
         alt="Cybersecurity Banner" 
         style="width: 100%; height: auto; display: block;">
  </div>

  <h1 style="font-size: 2.5em; margin-bottom: 15px; color: #0f172a;">
    🔒 Cybersecurity Incidents &amp; Data Breaches Dashboard 2024
  </h1>

  <p style="font-size: 1.15em; max-width: 850px; margin: 0 auto 40px; color: #334155;">
    Welcome to the <strong>Cybersecurity Insights Dashboard</strong> — your hub for exploring 
    <strong>real-world cyber incidents and data breaches from 2024</strong>.  
    Analyze attack patterns, industry impacts, financial losses, and recovery trends to stay ahead of modern threats.
  </p>

  <!-- Feature Cards -->
  <div style="
    display: flex; 
    flex-wrap: wrap; 
    justify-content: center; 
    gap: 25px; 
    margin-top: 20px;
  ">
    <div style="
      flex: 1 1 250px; 
      background: #ffffff; 
      padding: 25px; 
      border-radius: 14px; 
      box-shadow: 0 2px 6px rgba(0,0,0,0.1);
      transition: transform 0.3s ease, box-shadow 0.3s ease;
    " 
    onmouseover="this.style.transform='translateY(-6px)'; this.style.boxShadow='0 6px 15px rgba(0,0,0,0.15)';"
    onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='0 2px 6px rgba(0,0,0,0.1)';">
      <h3 style="color: #1e40af; margin-bottom: 10px;">📊 Explore Attacks</h3>
      <p style="color: #475569;">Visualize the most common attack types and entry vectors — from phishing to ransomware.</p>
    </div>

    <div style="
      flex: 1 1 250px; 
      background: #ffffff; 
      padding: 25px; 
      border-radius: 14px; 
      box-shadow: 0 2px 6px rgba(0,0,0,0.1);
      transition: transform 0.3s ease, box-shadow 0.3s ease;
    " 
    onmouseover="this.style.transform='translateY(-6px)'; this.style.boxShadow='0 6px 15px rgba(0,0,0,0.15)';"
    onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='0 2px 6px rgba(0,0,0,0.1)';">
      <h3 style="color: #1e40af; margin-bottom: 10px;">🏭 Industry Impact</h3>
      <p style="color: #475569;">Compare how industries like finance, healthcare, and retail are affected by cyber breaches.</p>
    </div>

    <div style="
      flex: 1 1 250px; 
      background: #ffffff; 
      padding: 25px; 
      border-radius: 14px; 
      box-shadow: 0 2px 6px rgba(0,0,0,0.1);
      transition: transform 0.3s ease, box-shadow 0.3s ease;
    " 
    onmouseover="this.style.transform='translateY(-6px)'; this.style.boxShadow='0 6px 15px rgba(0,0,0,0.15)';"
    onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='0 2px 6px rgba(0,0,0,0.1)';">
      <h3 style="color: #1e40af; margin-bottom: 10px;">💰 Financial &amp; Recovery</h3>
      <p style="color: #475569;">Dive into financial losses, ransom demands, downtime, and recovery effectiveness.</p>
    </div>

    <div style="
      flex: 1 1 250px; 
      background: #ffffff; 
      padding: 25px; 
      border-radius: 14px; 
      box-shadow: 0 2px 6px rgba(0,0,0,0.1);
      transition: transform 0.3s ease, box-shadow 0.3s ease;
    " 
    onmouseover="this.style.transform='translateY(-6px)'; this.style.boxShadow='0 6px 15px rgba(0,0,0,0.15)';"
    onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='0 2px 6px rgba(0,0,0,0.1)';">
      <h3 style="color: #1e40af; margin-bottom: 10px;">📈 Correlations</h3>
      <p style="color: #475569;">Identify key relationships between records leaked, churn, reputation loss, and stock value.</p>
    </div>
  </div>

  <p style="margin-top: 50px; font-size: 1em; color: #64748b;">
    Data Source: 
    <a href="https://www.kaggle.com/datasets/imaadmahmood/cybersecurity-incidents-and-data-breaches-2024?resource=download" 
       target="_blank" rel="noopener" 
       style="color: #1e40af; font-weight: 600; text-decoration: none;">
       Kaggle – Cybersecurity Incidents &amp; Data Breaches 2024
    </a>
  </p>

</section>
""")