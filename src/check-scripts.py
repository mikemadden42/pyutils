#!/usr/bin/env python3
import glob

# Grab all .sh and .bash files
scripts = glob.glob("*.sh") + glob.glob("*.bash")

print("Checking for shebang/extension mismatches...\n")

for filepath in sorted(scripts):
    with open(filepath, "r") as f:
        # Read the first line and strip whitespace/newlines
        first_line = f.readline().strip()

    ext = filepath.split(".")[-1]

    # Check 1: .bash files should invoke bash
    if ext == "bash" and "bash" not in first_line:
        print(f"❌ MISMATCH: {filepath}")
        print(f"   Extension is '.bash', but shebang is: {first_line}\n")

    # Check 2: .sh files should ideally invoke standard sh, not bash
    elif ext == "sh" and "bash" in first_line:
        print(f"⚠️  WARNING: {filepath}")
        print(
            f"   Extension is '.sh' (implies POSIX), but shebang invokes bash: {first_line}\n"
        )

    # Check 3: Missing shebang entirely
    elif not first_line.startswith("#!"):
        print(f"❓ MISSING: {filepath}")
        print(f"   No valid shebang found on line 1.\n")

print("Audit complete.")
