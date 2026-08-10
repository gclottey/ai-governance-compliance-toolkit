import sys

def run_classifier():
    print("==================================================")
    print("      EU AI ACT RISK CLASSIFICATION TOOL         ")
    print("==================================================\n")

    # Step 1: Check for Unacceptable Risk
    print("[?] Does the system use subliminal techniques, exploit vulnerabilities,")
    print("    or deploy real-time biometric identification in public spaces?")
    q1 = input("    (yes/no): ").strip().lower()
    if q1 == 'yes':
        return "❌ UNACCEPTABLE RISK (Prohibited under EU AI Act Article 5)"

    # Step 2: Check for High Risk
    print("\n[?] Is the AI used in critical infrastructure, medical devices, law enforcement,")
    print("    employment recruitment, or credit scoring?")
    q2 = input("    (yes/no): ").strip().lower()
    if q2 == 'yes':
        return "⚠️ HIGH RISK (Requires strict compliance, data governance, and conformity logging)"

    # Step 3: Check for Limited Risk (Generative AI)
    print("\n[?] Does the system generate or manipulate content (e.g., LLMs, Deepfakes, Chatbots)?")
    q3 = input("    (yes/no): ").strip().lower()
    if q3 == 'yes':
        return "ℹ️ LIMITED RISK (Requires clear transparency disclosures to end-users)"

    # Step 4: Minimal Risk Default
    return "✅ MINIMAL RISK (No obligations under the Act, follow voluntary codes of conduct)"

if __name__ == "__main__":
    result = run_classifier()
    print("\n==================================================")
    print(f"RESULT: {result}")
    print("==================================================")
