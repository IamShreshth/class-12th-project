"""
Tabular and Statistical Formatting for Experiment Records
CBSE Class XII Computer Science (Subject Code 083) Project
"""

from typing import List, Optional


def format_table(headers: List[str], rows: List[List[str]], title: Optional[str] = None) -> str:
    """Format headers and rows into a clean, bordered ASCII table."""
    if not headers:
        return "No headers provided."
    if not rows:
        return "No records found in this experiment database."

    col_widths = [len(h) for h in headers]
    for row in rows:
        for idx, cell in enumerate(row):
            if idx < len(col_widths):
                col_widths[idx] = max(col_widths[idx], len(str(cell)))

    # Formatting components
    border_line = "+" + "+".join("-" * (w + 2) for w in col_widths) + "+"
    header_line = "|" + "|".join(f" {h:<{col_widths[i]}} " for i, h in enumerate(headers)) + "|"

    output_lines = []
    if title:
        total_width = len(border_line)
        output_lines.append("=" * total_width)
        output_lines.append(f" {title.center(total_width - 2)} ")
        output_lines.append("=" * total_width)

    output_lines.append(border_line)
    output_lines.append(header_line)
    output_lines.append(border_line.replace("-", "="))

    for row_idx, row in enumerate(rows, start=1):
        cells = []
        for i, w in enumerate(col_widths):
            val = str(row[i]) if i < len(row) else ""
            cells.append(f" {val:<{w}} ")
        output_lines.append("|" + "|".join(cells) + "|")

    output_lines.append(border_line)
    output_lines.append(f" Total Records: {len(rows)}\n")

    return "\n".join(output_lines)


def format_statistics(headers: List[str], rows: List[List[str]]) -> str:
    """Calculate and return formatted summary statistics (Mean, Min, Max) for numerical columns."""
    if not rows or not headers:
        return ""

    stats_lines = ["\n[ Statistical Summary of Experimental Readings ]"]
    stats_lines.append("-" * 65)

    num_cols = len(headers)
    for c_idx in range(num_cols):
        values = []
        for row in rows:
            if c_idx < len(row):
                try:
                    val = float(row[c_idx])
                    values.append(val)
                except ValueError:
                    pass

        if values and len(values) == len(rows):
            # Purely numeric column
            avg = sum(values) / len(values)
            min_val = min(values)
            max_val = max(values)
            stats_lines.append(
                f" • {headers[c_idx]}:\n"
                f"     Count: {len(values)} | Mean: {avg:.4f} | Min: {min_val:.4f} | Max: {max_val:.4f}"
            )

    stats_lines.append("-" * 65)
    return "\n".join(stats_lines) if len(stats_lines) > 2 else ""
