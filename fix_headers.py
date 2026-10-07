import os
import re

svg_base = '<svg class="ikona-stazu" viewBox="0 0 24 24">'
svg_folder_new = f'{svg_base}<path d="M4 20h16a2 2 0 0 0 2-2V8a2 2 0 0 0-2-2h-7.93a2 2 0 0 1-1.66-.9l-.82-1.2A2 2 0 0 0 7.93 3H4a2 2 0 0 0-2 2v13c0 1.1.9 2 2 2Z"/></svg>'
svg_file_new = f'{svg_base}<path d="M14.5 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V7.5L14.5 2z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/><line x1="10" y1="9" x2="8" y2="9"/></svg>'

for file in os.listdir("."):
    if file.endswith(".md") and file not in ["README.md", "_sidebar.md", "spis_stazy.md"]:
        with open(file, "r") as f:
            content = f.read()
        
        # We need to make sure the headers are properly formatted as markdown block elements.
        # This means they need an empty line before and after.
        # Replace the problematic blocks.
        
        # Wymień "### 📁 Pliki w folderze" na wersję z SVG i pustymi liniami
        content = re.sub(
            r'### 📁 Pliki w folderze',
            f'\n<br>\n\n### {svg_folder_new} Pliki w folderze\n\n',
            content
        )
        
        # Wymień "### 📝 Główne notatki" na wersję z SVG i pustymi liniami
        content = re.sub(
            r'### 📝 Główne notatki',
            f'\n<br>\n\n### {svg_file_new} Główne notatki\n\n',
            content
        )
        
        # Zabezpieczenie przed brakującymi znacznikami (np. w plikach gdzie zostało to "doklejone" do <hr>)
        content = content.replace('<hr style="margin: 30px 0;">', '\n\n<hr style="margin: 30px 0;">\n\n')
        
        # Posprzątajmy ewentualne wielokrotne puste linie, żeby to wyglądało ładnie
        content = re.sub(r'\n{3,}', '\n\n', content)
        
        with open(file, "w") as f:
            f.write(content)

print("Naprawiono nagłówki i podmieniono emotikony na ikony Lucide w poszczególnych stronach.")
