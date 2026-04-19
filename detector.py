import re
import math

def calculate_entropy(text):
    if not text:
        return 0
    
    frequency = {}
    for char in text:
        frequency[char] = frequency.get(char, 0) + 1
    
    entropy = 0
    for count in frequency.values():
        probability = count / len(text)
        entropy -= probability * math.log2(probability)
    
    return entropy
PATTERNS = {
    "AWS Key":         r'AKIA[0-9A-Z]{16}',
    "GitHub Token":    r'ghp_[a-zA-Z0-9]{36}',
    "Password":        r'(?i)password\s*=\s*["\']?.+["\']?',
    "Generic API Key": r'(?i)api_key\s*=\s*["\']?.+["\']?',
}
def detect_secrets(lines):
    findings = []

    for line_number, line in lines:
        
        for secret_type, pattern in PATTERNS.items():
            if re.search(pattern, line):
                findings.append({
                    "line_number": line_number,
                    "line":        line,
                    "type":        secret_type,
                    "method":      "pattern"
                })
        
        for word in line.split():
            score = calculate_entropy(word)
            if score > 4.0 and len(word) > 10:
                findings.append({
                    "line_number": line_number,
                    "line":        line,
                    "type":        "High Entropy String",
                    "method":      "entropy"
                })
                break

    return findings