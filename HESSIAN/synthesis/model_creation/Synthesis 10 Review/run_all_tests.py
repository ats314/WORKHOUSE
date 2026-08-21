"""
run_all_tests.py - Master Test Runner
======================================
Runs all verification tools and produces summary report.
"""

import subprocess
import sys

def run_test(script_name):
    """Run a test script and capture output."""
    print(f"\n{'='*60}")
    print(f"RUNNING: {script_name}")
    print('='*60)
    
    result = subprocess.run(
        [sys.executable, script_name],
        capture_output=True,
        text=True,
        encoding='utf-8',
        errors='replace'
    )
    
    print(result.stdout)
    if result.stderr:
        print("STDERR:", result.stderr)
    
    return result.returncode == 0

def main():
    print("="*60)
    print("SYNTHESIS 10 MATHEMATICAL VERIFICATION SUITE")
    print("="*60)
    
    tests = [
        ("verify_math.py", "NumPy Numerical Verification"),
        ("symbolic_verify.py", "SymPy Symbolic Verification"),
        ("jax_verify.py", "JAX Autodiff Verification"),
        ("limit_probes.py", "Limit and Scaling Probes"),
    ]
    
    results = {}
    for script, description in tests:
        print(f"\n>>> {description}")
        try:
            success = run_test(script)
            results[script] = "PASS" if success else "FAIL"
        except Exception as e:
            results[script] = f"ERROR: {e}"
    
    # Summary
    print("\n" + "="*60)
    print("VERIFICATION SUMMARY")
    print("="*60)
    
    for script, status in results.items():
        print(f"  {script}: {status}")
    
    print("\n" + "="*60)

if __name__ == "__main__":
    main()
