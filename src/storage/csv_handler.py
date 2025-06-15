"""
CSV Persistence and Data Access Repository
Handles atomic writing, schema initialization, and retrieval of experiment records.
CBSE Class XII Computer Science (Subject Code 083) Project
"""

import csv
import os
from pathlib import Path
from typing import Any, List, Optional, Tuple
from src.config import DATA_DIR, PROJECT_ROOT, EXPERIMENTS


class CSVRepository:
    """Manages CSV file operations for physics experiment records."""

    def __init__(self, data_dir: Optional[Path] = None):
        self.data_dir = data_dir or DATA_DIR
        os.makedirs(self.data_dir, exist_ok=True)

    def resolve_read_path(self, file_name: str) -> Path:
        """Resolve file path across data directory, current directory, and legacy aliases."""
        target = Path(file_name)
        if target.is_absolute() and target.exists():
            return target

        # Check in standard data directory
        p = self.data_dir / target.name
        if p.exists():
            return p

        # Check in project root
        p_root = PROJECT_ROOT / target.name
        if p_root.exists():
            return p_root

        # Check for legacy names from config
        for exp in EXPERIMENTS.values():
            if exp.get("file_name") == target.name or exp.get("legacy_file_name") == target.name:
                p_legacy = self.data_dir / exp.get("legacy_file_name", "")
                if p_legacy.exists():
                    return p_legacy
                p_std = self.data_dir / exp["file_name"]
                if p_std.exists():
                    return p_std

        # Default fallback
        return self.data_dir / target.name

    def resolve_write_path(self, file_name: str) -> Path:
        """Ensure writing always targets the designated data directory."""
        return self.data_dir / Path(file_name).name

    def save_record(self, file_name: str, headers: List[str], row_data: List[Any]) -> bool:
        """Append a single record to the CSV file. Writes headers if file is new or empty."""
        try:
            write_path = self.resolve_write_path(file_name)
            is_new = not write_path.exists() or write_path.stat().st_size == 0

            with open(write_path, mode="a", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                if is_new:
                    writer.writerow(headers)
                writer.writerow(row_data)
            return True
        except Exception as e:
            print(f"Error saving data to {file_name}: {e}")
            return False

    def retrieve_records(self, file_name: str) -> Tuple[bool, List[str], List[List[str]], str]:
        """
        Read all records from CSV.
        Returns: (success, headers, rows, message)
        """
        read_path = self.resolve_read_path(file_name)

        if not read_path.exists() or read_path.stat().st_size == 0:
            return False, [], [], f"File '{file_name}' not found or contains no records."

        try:
            with open(read_path, mode="r", newline="", encoding="utf-8") as f:
                reader = csv.reader(f)
                all_rows = [row for row in reader if any(cell.strip() for cell in row)]

            if not all_rows:
                return False, [], [], f"File '{file_name}' is empty."

            headers = all_rows[0]
            data_rows = all_rows[1:]
            return True, headers, data_rows, f"Successfully retrieved {len(data_rows)} records."
        except Exception as e:
            return False, [], [], f"An error occurred while reading '{file_name}': {e}"
