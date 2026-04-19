from walker   import walk_files
from reader   import read_file
from detector import detect_secrets
from reporter import reporter
from scanning_tools import run_bandit

folder = input("Enter folder to scan: ")
files  = walk_files(folder)

print(f"\nScanning {len(files)} files...\n")

for f in files:
    lines    = read_file(f)
    findings = detect_secrets(lines)
    reporter(f, findings)
run_bandit(folder)
