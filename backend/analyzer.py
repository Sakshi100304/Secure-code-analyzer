import re
import os
import difflib
from collections import defaultdict


# 🔹 MAIN ANALYZER
def analyze_code(file_path):
    issues = []
    seen_lines = set()

    with open(file_path, 'r', encoding="utf-8", errors="ignore") as file:
        lines = file.readlines()

    for i, line in enumerate(lines, start=1):
        stripped = line.strip()

        # HIGH
        if re.search(r'password\s*=\s*["\'].*["\']', line):
            issues.append((i, "HIGH", "Hardcoded Password", stripped, 
                           "Use environment variables or config files instead of hardcoding passwords."))

        if re.search(r'(api[_-]?key|token)\s*=\s*["\'].*["\']', line, re.IGNORECASE):
            issues.append((i, "HIGH", "Hardcoded API Key", stripped,
                           "Store API keys securely using environment variables."))

        if "eval(" in line:
            issues.append((i, "HIGH", "Use of eval()", stripped,
                           "Avoid eval(); use safer alternatives like ast.literal_eval()."))

        if ("execute" in line and "+" in line) or ("format(" in line):
            issues.append((i, "HIGH", "SQL Injection Risk", stripped,
                           "Use parameterized queries instead of string formatting."))

        if "os.system(" in line:
            issues.append((i, "HIGH", "Command Injection Risk", stripped,
                           "Use subprocess module with proper argument handling."))

        # MEDIUM
        if "md5(" in line.lower() or "sha1(" in line.lower():
            issues.append((i, "MEDIUM", "Weak Hashing", stripped,
                           "Use stronger hashing algorithms like bcrypt or SHA-256."))

        if "pickle.load(" in line:
            issues.append((i, "MEDIUM", "Insecure Deserialization", stripped,
                           "Avoid loading untrusted pickle data."))

        # LOW
        if stripped in seen_lines and stripped != "":
            issues.append((i, "LOW", "Duplicate Code", stripped,
                           "Refactor duplicate code into functions or reuse logic."))
        else:
            seen_lines.add(stripped)

        if len(line) > 120:
            issues.append((i, "LOW", "Long Line (>120 chars)", stripped,
                           "Break the line into smaller readable parts."))

    return issues


# 🔹 SUMMARY
def calculate_summary(issues):
    summary = defaultdict(int)

    for issue in issues:
        summary[issue[1]] += 1

    high = summary["HIGH"]
    medium = summary["MEDIUM"]
    low = summary["LOW"]

    risk_score = (high * 3) + (medium * 2) + (low * 1)

    return {
        "total": len(issues),
        "high": high,
        "medium": medium,
        "low": low,
        "risk_score": risk_score
    }


# 🔹 NEW: PLAGIARISM DETECTION
def check_similarity(file_path, folder="uploads"):
    similarities = []

    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        content1 = f.read()

    for fname in os.listdir(folder):
        other_path = os.path.join(folder, fname)

        if other_path == file_path:
            continue

        try:
            with open(other_path, "r", encoding="utf-8", errors="ignore") as f:
                content2 = f.read()

            ratio = difflib.SequenceMatcher(None, content1, content2).ratio()

            if ratio > 0.6:  # threshold
                similarities.append({
                    "file": fname,
                    "similarity": round(ratio * 100, 2),
                    "suggestion": suggest_fix(ratio * 100)
                })
        except:
            continue

    return similarities


# 🔹 NEW: SUGGESTION FOR COPYING
def suggest_fix(similarity_score):
    if similarity_score > 90:
        return "Rewrite the code completely using your own logic."
    elif similarity_score > 70:
        return "Change logic structure, variable names, and improve implementation."
    elif similarity_score > 50:
        return "Refactor and optimize the code."
    else:
        return "Code is mostly original."      