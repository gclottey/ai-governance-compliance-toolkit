# Third-Party Vendor AI Risk Procurement Policy

**Policy ID:** POL-VND-02  
**Version:** 1.0  
**Effective Date:** August 10, 2026  
**Applicability:** Procurement, Security, Legal, and Engineering teams vetting external AI solutions.

---

## 1. Purpose
Organizations increasingly rely on external vendors for APIs, foundational models, and embedded AI tools. This policy establishes a mandatory vetting procedure to ensure third-party AI software aligns with internal security, privacy, and regulatory obligations before contract signing.

## 2. Mandatory Vendor Pre-Screening Questionnaire
Every incoming AI vendor must complete our standardized vetting questionnaire. Procurement teams cannot sign contracts without written verification of the following items:

### 2.1 Data Privacy & Retraining Guardrails
* **Retraining Exemption:** Does the vendor use our inputted corporate prompts or fine-tuning datasets to train their public models? *(A written contractual guarantee of "No Retraining" is required).*
* **Data Residency:** Where are customer inputs processed and stored? (e.g., EU, US). Data locations must comply with local privacy jurisdictions.
* **Retention Policy:** How long are prompt logs cached for abuse monitoring? Any log retention exceeding 30 days requires Chief Compliance Officer approval.

### 2.2 Security & Model Reliability
* **Independent Audits:** Does the vendor possess a valid SOC 2 Type II certification covering the AI platform?
* **Vulnerability Disclosure:** How does the vendor patch and protect against prompt injection, model inversion, or training data poisoning?
* **SLA & Fallbacks:** What is the operational uptime guarantee for their hosting infrastructure, and what fallback logic is provided if their API endpoints experience an outage?

---

## 3. Risk Tiering & Assessment Matrix
Vendors are categorized based on their systemic data access and automated impact:

| Risk Tier | System Criteria | Vetting Requirement | Approval Authority |
| :--- | :--- | :--- | :--- |
| **Tier 1: High** | Direct ingestion of customer PII, financial data, or operational source code. | Full Algorithmic Impact Assessment + Legal Deep-Dive | Chief Compliance Officer |
| **Tier 2: Medium**| Ingestion of internal non-public text, general code snippets, or product analytics. | Security Checklist & Retraining Waiver Sign-off | VP of Engineering |
| **Tier 3: Low** | Public text processing, open web searches, or unclassified marketing assets. | Standard Vendor Terms Review | Procurement Lead |

---

## 4. Continuous Vetting & Right to Audit
* **Performance Drift Reviews:** High-risk vendors must be reviewed bi-annually to check for performance drift, updates to their baseline data terms, or new downstream compliance gaps under the EU AI Act.
* **Termination Safeguards:** Contracts must contain "Data Portability" exit clauses. If a vendor changes their data collection privacy policy, our organization retains the explicit right to extract our organizational data and terminate services without penalty.
