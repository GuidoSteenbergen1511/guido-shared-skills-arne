#!/usr/bin/env python3
"""
Watermark a PDF with a confidential notice and compress for email.

Usage:
  python3 watermark_pdf.py <input.pdf> [output.pdf] [--watermark "CUSTOM TEXT"] [--footer "Custom footer"] [--no-compress]

Dependencies: reportlab, pypdf
Compression: requires ghostscript (gs) on PATH
"""

import argparse
import io
import os
import shutil
import subprocess
import sys
import tempfile

from reportlab.lib.colors import Color
from reportlab.pdfgen import canvas
from pypdf import PdfReader, PdfWriter


DEFAULT_WATERMARK = "CONFIDENTIAL \u2014 DO NOT DISTRIBUTE"
DEFAULT_FOOTER = (
    "CONFIDENTIAL \u2014 For personal use only. "
    "Do not distribute or share without written permission."
)


def create_watermark_page(width, height, watermark_text, footer_text):
    """Create a single-page PDF with diagonal watermark + footer bar."""
    packet = io.BytesIO()
    c = canvas.Canvas(packet, pagesize=(width, height))

    # Diagonal watermark
    c.saveState()
    c.setFillColor(Color(0.5, 0.5, 0.5, alpha=0.15))
    c.setFont("Helvetica-Bold", 48)
    c.translate(width / 2, height / 2)
    c.rotate(35)
    c.drawCentredString(0, 0, watermark_text)
    c.restoreState()

    # Footer bar
    c.setFillColor(Color(0.2, 0.2, 0.2, alpha=0.85))
    c.rect(0, 0, width, 28, fill=True, stroke=False)
    c.setFillColor(Color(1, 1, 1, alpha=1))
    c.setFont("Helvetica", 9)
    c.drawCentredString(width / 2, 9, footer_text)

    c.save()
    packet.seek(0)
    return PdfReader(packet)


def watermark_pdf(input_path, output_path, watermark_text, footer_text):
    """Apply watermark to every page of the input PDF."""
    reader = PdfReader(input_path)
    writer = PdfWriter()

    for page in reader.pages:
        w = float(page.mediabox.width)
        h = float(page.mediabox.height)
        wm = create_watermark_page(w, h, watermark_text, footer_text)
        page.merge_page(wm.pages[0])
        writer.add_page(page)

    with open(output_path, "wb") as f:
        writer.write(f)

    return len(reader.pages)


def compress_pdf(input_path, output_path):
    """Compress PDF using Ghostscript. Returns True if successful."""
    gs_bin = shutil.which("gs")
    if not gs_bin:
        print("Warning: Ghostscript (gs) not found. Skipping compression.", file=sys.stderr)
        shutil.copy2(input_path, output_path)
        return False

    subprocess.run(
        [
            gs_bin,
            "-sDEVICE=pdfwrite",
            "-dCompatibilityLevel=1.4",
            "-dPDFSETTINGS=/ebook",
            "-dNOPAUSE",
            "-dQUIET",
            "-dBATCH",
            f"-sOutputFile={output_path}",
            input_path,
        ],
        check=True,
    )
    return True


def main():
    parser = argparse.ArgumentParser(description="Watermark and compress a PDF")
    parser.add_argument("input", help="Input PDF path")
    parser.add_argument("output", nargs="?", help="Output PDF path (default: <input>-confidential.pdf)")
    parser.add_argument("--watermark", default=DEFAULT_WATERMARK, help="Diagonal watermark text")
    parser.add_argument("--footer", default=DEFAULT_FOOTER, help="Footer bar text")
    parser.add_argument("--no-compress", action="store_true", help="Skip Ghostscript compression")
    args = parser.parse_args()

    if not os.path.exists(args.input):
        print(f"Error: {args.input} not found", file=sys.stderr)
        sys.exit(1)

    # Default output name
    if not args.output:
        base, ext = os.path.splitext(args.input)
        args.output = f"{base} - Confidential{ext}"

    if args.no_compress:
        pages = watermark_pdf(args.input, args.output, args.watermark, args.footer)
    else:
        # Watermark to temp, then compress
        with tempfile.NamedTemporaryFile(suffix=".pdf", delete=False) as tmp:
            tmp_path = tmp.name
        try:
            pages = watermark_pdf(args.input, tmp_path, args.watermark, args.footer)
            compress_pdf(tmp_path, args.output)
        finally:
            os.unlink(tmp_path)

    size_mb = os.path.getsize(args.output) / (1024 * 1024)
    print(f"Done: {args.output} ({pages} pages, {size_mb:.1f} MB)")


if __name__ == "__main__":
    main()
