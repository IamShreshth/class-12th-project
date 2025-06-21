"""
Unit Tests for CSV Persistence, Formatting, and Statistics
CBSE Class XII Computer Science (Subject Code 083) Project
"""

import unittest
import tempfile
import os
from pathlib import Path
from src.storage.csv_handler import CSVRepository
from src.storage.formatter import format_table, format_statistics


class TestStorageAndFormatting(unittest.TestCase):
    """Verifies CSV persistence, formatted ASCII table generation, and statistical summaries."""

    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.repo = CSVRepository(data_dir=Path(self.temp_dir.name))

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_save_and_retrieve_records(self):
        headers = ["Col A", "Col B", "Col C"]
        row1 = [10.5, 20.2, 30.1]
        row2 = [11.0, 22.0, 33.0]

        file_name = "test_experiment.csv"

        # Save first row (creates file and writes headers)
        saved = self.repo.save_record(file_name, headers, row1)
        self.assertTrue(saved)

        # Save second row
        saved2 = self.repo.save_record(file_name, headers, row2)
        self.assertTrue(saved2)

        # Retrieve records
        success, ret_headers, rows, msg = self.repo.retrieve_records(file_name)
        self.assertTrue(success)
        self.assertEqual(ret_headers, headers)
        self.assertEqual(len(rows), 2)
        self.assertEqual(rows[0], [str(x) for x in row1])
        self.assertEqual(rows[1], [str(x) for x in row2])

    def test_retrieve_non_existent_file(self):
        success, headers, rows, msg = self.repo.retrieve_records("non_existent_file.csv")
        self.assertFalse(success)
        self.assertEqual(len(rows), 0)

    def test_ascii_table_formatting(self):
        headers = ["Measurement", "Value", "Unit"]
        rows = [
            ["Acceleration g", "9.8066", "m/s^2"],
            ["Focal Length", "24.0", "cm"]
        ]
        table_output = format_table(headers, rows, title="Sample Laboratory Test")
        self.assertIn("Sample Laboratory Test", table_output)
        self.assertIn("Acceleration g", table_output)
        self.assertIn("Total Records: 2", table_output)

    def test_statistical_summary(self):
        headers = ["ID", "Measurement"]
        rows = [
            ["1", "10.0"],
            ["2", "20.0"],
            ["3", "30.0"]
        ]
        stats = format_statistics(headers, rows)
        self.assertIn("Measurement:", stats)
        self.assertIn("Mean: 20.0000", stats)
        self.assertIn("Min: 10.0000", stats)
        self.assertIn("Max: 30.0000", stats)


if __name__ == "__main__":
    unittest.main()
