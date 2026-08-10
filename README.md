# Enterprise AI Governance & Compliance Toolkit

[![License: MIT](https://shields.io)](https://opensource.org)
[![Compliance: EU AI Act](https://shields.io)](https://artificialintelligenceact.eu)
[![Framework: NIST AI RMF](https://shields.io)](https://nist.gov)

An open-source, operational framework designed to help organizations safely govern, evaluate, and deploy Artificial Intelligence systems. This repository contains enterprise-grade policy templates, risk assessment structures, and automation scripts mapped directly to global regulatory standards (EU AI Act, NIST AI RMF, and ISO/IEC 42001).

---

## 🚀 Key Components

### 1. Risk Tiering & Automation Tooling (`/frameworks`)
* **`EU-AI-Act-classifier.py`**: A CLI Python utility that prompts product teams about data inputs, system autonomy, and deployment contexts to instantly classify an AI application into the EU AI Act risk tiers (*Unacceptable, High, Limited, or Minimal*).

### 2. Organizational Policies (`/policies`)
* **Generative AI & LLM Acceptable Use Policy**: Clear guidelines for employees on data privacy, intellectual property, and prohibited prompts.
* **Vendor AI Risk Procurement Standard**: Pre-built security and compliance questionnaires for vetting third-party AI vendors.

### 3. Compliance Assessments (`/templates`)
* **Algorithmic Impact Assessment (AIA)**: A comprehensive, multi-disciplinary template to document model data lineage, bias mitigation strategies, and human-in-the-loop overrides.
* **AI System Registry Intake Form**: A standardized form ensuring all internal AI projects are logged in a central inventory before moving to production.

---

## 🛠️ Getting Started

### Prerequisites
* Python 3.10+ (for running automation scripts)

### Installation & Local Usage
1. Clone the repository:
   ```bash
   git clone https://github.com
   cd ai-governance-compliance-toolkit
   ```

2. Run the interactive risk classification script:
   ```bash
   python frameworks/EU-AI-Act-classifier.py
   ```

---

## 📊 Framework Mapping Matrix

Our controls bridge the gap between abstract ethical principles and concrete corporate compliance:

| Policy Control ID | Control Name | NIST AI RMF Function | EU AI Act Alignment | ISO 42001 Clause |
| :--- | :--- | :--- | :--- | :--- |
| **GOV-01** | AI System Registry Intake | GOVERN 1.1 | Art 60 (EU Database) | Clause 8.2 |
| **GOV-02** | Risk Classification | MEASURE 2.1 | Art 6 (Risk Tiers) | Annex A.5 |
| **GOV-03** | Algorithmic Impact Assessment | MAP 1.1, 1.2 | Art 9 (Risk Mgmt) | Clause 6.1.2 |
| **GOV-04** | Continuous Bias Monitoring | MANAGE 1.3 | Art 10 (Data Gov) | Annex A.8 |

---

## 🤝 Contributing
Contributions are highly encouraged! If you are a legal expert, AI researcher, or compliance professional, please open an issue to suggest updates based on evolving international regulations.

## 📄 License
Distributed under the MIT License. See `LICENSE` for more information.
