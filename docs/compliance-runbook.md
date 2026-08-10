# AI Compliance Audit Runbook

**Document ID:** RBK-COMP-01  
**Version:** 1.0  
**Target Audience:** Internal Auditors, Compliance Officers, and AI Project Managers  

---

## 1. Objective
This runbook provides an operational, step-by-step guide for conducting a compliance review on internal AI systems. Following these steps ensures your project adheres to the **EU AI Act**, **NIST AI RMF**, and internal company policies before deployment.

---

## 2. Phase 1: Intake and Discovery (Day 1-2)
The audit begins the moment a product team logs a project in the central repository.

### Step 1.1: Verify the Intake Form
* Open `templates/AI-system-registry-form.md`.
* Ensure the project team completed all fields, focusing specifically on **Data Sources** and **Intended End Users**.
* If critical fields are missing, reject the intake form and route it back to the Project Owner.

### Step 1.2: Run the Automated Risk Classifier
* Open your terminal and navigate to the project directory.
* Run the interactive classification script:
  ```bash
  python frameworks/EU-AI-Act-classifier.py
  ```
* Log the resulting classification (*Unacceptable, High, Limited, Minimal*) directly into the project's audit file.

---

## 3. Phase 2: Core Document Audit (Day 3-5)
Review the system safeguards based on the risk level determined in Phase 1.

### Step 2.1: Assess Data Controls (For High-Risk Systems)
* Open the completed **Algorithmic Impact Assessment (AIA)** template.
* Confirm that no raw Personally Identifiable Information (PII) is entering the model training pipeline without clear user consent.
* Ensure the engineering team has logged active data anonymization steps (e.g., data hashing or masking).

### Step 2.2: Review Third-Party Extensions
* Check if the system connects to external LLM providers (like OpenAI or Anthropic APIs).
* If external tools are used, verify that a signed copy of the `policies/vendor-ai-risk-policy.md` exists with the vendor, confirming they do not retrain their models on our data.

---

## 4. Phase 3: Technical Verification (Day 6-7)
Validate that engineering safety claims match actual system code performance.

### Step 3.1: Check LLM Guardrails
* Verify that an active guardrail configuration layer (such as NeMo Guardrails or Llama Guard) is active.
* Test the deployment with sample adversarial inputs to ensure the system successfully blocks toxic queries or requests for sensitive corporate data.

### Step 3.2: Verify Bias Evaluation Logs
* Request the model evaluation reports from the engineering team.
* Confirm that bias testing tools (like `Fairlearn` or `AIF360`) were run against the model package and that the **Disparate Impact Ratio** falls within safe limits (typically between 0.80 and 1.25).

---

## 5. Phase 4: Sign-Off and Continuous Monitoring
* Complete the sign-off matrix at the bottom of the AIA template with digital approvals from the Lead AI Engineer, DPO, and CCO.
* Schedule the next automated audit review inside your project calendar (High-risk tools must repeat this audit cycle every 6 months).
