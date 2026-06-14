#!/usr/bin/env python3
"""Extract text from all 2025 PDFs using PyMuPDF."""
import fitz
import os
import json

pdf_dir = "/Users/sam/Desktop/brain/홍석진-위키/raw/applications/2025"
output_dir = "/Users/sam/Desktop/brain/홍석진-위키/raw/extracted/2025"
os.makedirs(output_dir, exist_ok=True)

results = {}

for fname in sorted(os.listdir(pdf_dir)):
    if not fname.endswith('.pdf'):
        continue
    path = os.path.join(pdf_dir, fname)
    try:
        doc = fitz.open(path)
        num_pages = len(doc)
        text = ''.join(page.get_text() for page in doc)
        doc.close()
        
        # Save extracted text
        base = os.path.splitext(fname)[0]
        txt_path = os.path.join(output_dir, base + '.txt')
        with open(txt_path, 'w', encoding='utf-8') as f:
            f.write(text)
        
        results[fname] = {
            'pages': num_pages,
            'chars': len(text),
            'first_500': text[:500]
        }
        print(f"OK: {fname} ({num_pages} pages, {len(text)} chars)")
    except Exception as e:
        print(f"FAIL: {fname} - {e}")
        results[fname] = {'error': str(e)}

# Save summary
with open(os.path.join(output_dir, '_summary.json'), 'w', encoding='utf-8') as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print(f"\nDone. Extracted {len([r for r in results.values() if 'chars' in r])}/{len(results)} PDFs")
