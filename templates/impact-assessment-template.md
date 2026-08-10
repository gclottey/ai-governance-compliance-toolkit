# Algorithmic Impact Assessment (AIA) Template

**Document ID:** TMP-AIA-01  
**Framework Alignment:** EU AI Act Article 9 (Risk Mgmt), NIST AI RMF Map Function  
**Classification Target:** High-Risk / Limited-Risk AI Deploys  

---

## 1. Project Overview & System Context
*To be filled out by the Project Owner and Technical Lead prior to development.*

* **Project Name:** [Insert Project Name]
* **Target Deployment Date:** [YYYY-MM-DD]
* **Business Objective:** Describe the specific business problem this model solves.
* **Intended End Users:** Who interacts with the output? (e.g., HR team, credit applicants, general public)
* **Core Downstream Impacts:** Describe how a wrong prediction impacts a human user.

---

## 2. Data Lineage & Privacy Controls
*Focuses on the source, hygiene, and legality of the data assets.*

### 2.1 Data Collection & Consent
* **Data Sources:** List all internal databases, public scrape sources, or third-party vendor datasets used.
* **Consent Mechanisms:** What is the legal base for processing this data? (e.g., explicit user opt-in, contractual necessity)

### 2.2 PII & Security Minimization
* **PII Detection:** Does the training pipeline ingest Personally Identifiable Information? (Yes/No)
* **Anonymization Strategy:** Detail the masking, hashing, or synthetic noise injection methods used:
  > *[Write brief summary here]*

---

## 3. Fairness, Bias, & Mitigation Strategy
*Audit benchmarks to prevent discriminatory outputs across protected groups.*

### 3.1 Demographic Disparity Assessment
* **Protected Attributes:** Does the dataset contain variables (or proxies) tracking age, gender, race, or geography?
* **Statistical Metrics Tracking:** (Check all that apply during testing)
  * [ ] Disparate Impact Ratio
  * [ ] Demographic Parity Difference
  * [ ] Equalized Odds

### 3.2 Mitigation Actions
* If data imbalance or bias is discovered, what corrective actions are taken? (e.g., re-weighting, synthetic oversampling, feature dropping)

---

## 4. Explainability & Human-in-the-Loop (HITL)
*Ensuring system outputs remain auditable and clear to operators.*

### 4.1 Interpretability Methods
* Detail the technical approach used to explain predictions (e.g., SHAP values, LIME frameworks, feature importance logs):
  > *[Insert explanation here]*

### 4.2 Override Mechanisms
* **Human Safeguard:** How does an operator flag, block, or reverse an automated AI decision?
* **Escalation Path:** If a model malfunctions in production, who has the structural authority to shut off system access?

---

## 5. Compliance Sign-Off
*Final structural verification before moving to packaging and production branches.*

| Role | Name / Title | Signature | Date |
| :--- | :--- | :--- | :--- |
| **Data Protection Officer (DPO)** | | | |
| **Lead AI Engineer** | | | |
| **Chief Compliance Officer (CCO)**| | | |
