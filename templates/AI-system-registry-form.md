# AI System Registry Intake Form

**Document ID:** REG-FORM-01  
**Instructions:** This form must be completed by the Project Lead for any new software feature, automated pipeline, or agentic system utilizing machine learning or generative models before production onboarding.

---

## 1. Administrative Information
* **Project Name:** [Insert Project Name]
* **Project Owner / Sponsor:** [Name / Email / Department]
* **Technical Lead Engineer:** [Name / Email]
* **Target Launch Date:** [YYYY-MM-DD]

## 2. Technical Profile
### 2.1 Core Infrastructure
* **Model Type:** (e.g., LLM / Computer Vision / Tabular Regression / Recommendation Engine)
* **Model Hosting:** [ ] Internal Hosting / On-Premise [ ] External Third-Party API (e.g., OpenAI, Anthropic) [ ] Vendor Cloud Package
* **Underlying Architecture:** (e.g., GPT-4o, Llama-3, custom-trained Random Forest)

### 2.2 Data Pipeline
* **Training & Fine-Tuning Data Sources:** List the specific datasets used to build, test, or fine-tune this model.
* **Live Input Data:** What data fields does this model process in real time? (Include any customer attributes, text prompts, or file uploads).

---

## 3. Preliminary Risk & Compliance Self-Assessment
* **Does this system process PII, health details, or payment card data?** [ ] Yes [ ] No
* **Is this system fully autonomous, or is there a human validation step before action?** [ ] Fully Autonomous [ ] Human-in-the-Loop (HITL)
* **Does the model make automated decisions affecting hiring, credit access, or resource distribution?** [ ] Yes [ ] No

---

## 4. Operational Sign-Off Logs
*Do not fill—for Compliance Team use only.*

* **Compliance Intake Reviewer:** [Name / Date]
* **Assigned EU AI Act Category:** [Unacceptable / High / Limited / Minimal]
* **Required Documentation Track:** [ ] Full AIA Required [ ] Standard Logging Only [ ] Disclosures Mandatory
