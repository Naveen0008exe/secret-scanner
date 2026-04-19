import subprocess

def run_bandit(folder):
    print("\n Running Bandit (security scanner)...\n")
    
    result = subprocess.run(
        ["python", "-m", "bandit", "-r", folder],
        capture_output=True,
        text=True
    )
    
    print(result.stdout)
    
    if result.returncode != 0:
        print(" Bandit found issues above")
    else:
        print(" Bandit found no issues")