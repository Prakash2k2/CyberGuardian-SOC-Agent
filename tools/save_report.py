"""
Save report to disk and optionally render to PDF if wkhtmltopdf is installed.
"""
from pathlib import Path
import pdfkit
import os

OUT_DIR = Path('reports')
OUT_DIR.mkdir(parents=True, exist_ok=True)

def save_report_markdown(md_text: str) -> str:
    # Save markdown
    md_files = list(OUT_DIR.glob('report_*.md'))
    idx = len(md_files) + 1
    md_path = OUT_DIR / f'report_{idx}.md'
    md_path.write_text(md_text, encoding='utf-8')

    # Try convert to PDF (optional); pdfkit requires wkhtmltopdf installed
    pdf_path = OUT_DIR / f'report_{idx}.pdf'
    try:
        # if wkhtmltopdf not installed this will raise OSError; we fail silently
        pdfkit.from_file(str(md_path), str(pdf_path))
    except Exception:
        # conversion not critical for demo
        pass

    return md_path.read_text(encoding='utf-8')