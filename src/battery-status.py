#!/usr/bin/env python3
import sys
from pathlib import Path


def read_file(path):
    """Reads a file and returns the stripped content, or None if missing."""
    try:
        return path.read_text().strip()
    except (FileNotFoundError, OSError):
        return None


def main():
    power_supply_dir = Path("/sys/class/power_supply")

    if not power_supply_dir.exists():
        print(f"Error: {power_supply_dir} not found.")
        sys.exit(1)

    print("Scanning for batteries...")
    print("-" * 50)

    batteries = list(power_supply_dir.glob("BAT*"))

    if not batteries:
        print("No batteries found.")
        return

    for bat_path in batteries:
        # --- Read Basic Stats ---
        name = bat_path.name
        status = read_file(bat_path / "status") or "Unknown"
        capacity = read_file(bat_path / "capacity") or "N/A"
        cycle_count = read_file(bat_path / "cycle_count") or "N/A"

        # --- Health Calculation ---
        # Try 'energy' (newer kernels) then 'charge' (older kernels)
        current_max = read_file(bat_path / "energy_full") or read_file(
            bat_path / "charge_full"
        )
        design_max = read_file(bat_path / "energy_full_design") or read_file(
            bat_path / "charge_full_design"
        )

        health_str = "N/A"
        if current_max and design_max:
            try:
                c_max = float(current_max)
                d_max = float(design_max)
                if d_max > 0:
                    health_percent = (c_max / d_max) * 100
                    health_str = f"{health_percent:.2f}%"
            except ValueError:
                pass  # Keep as N/A if conversion fails

        # --- Output ---
        print(f"Battery:       {name}")
        print(f"Status:        {status}")
        print(f"Current Level: {capacity}%")
        print(f"Cycle Count:   {cycle_count}")
        print(f"Health:        {health_str} of original capacity")
        print("-" * 50)


if __name__ == "__main__":
    main()
