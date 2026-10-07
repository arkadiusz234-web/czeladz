import os
import re

svg_base = '<svg class="ikona-stazu" viewBox="0 0 24 24">'

svg_home = f'{svg_base}<path d="m3 9 9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/></svg>'
svg_folder = f'{svg_base}<path d="M22 19a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h5l2 3h9a2 2 0 0 1 2 2z"/></svg>'
svg_edit = f'{svg_base}<path d="M17 3a2.828 2.828 0 1 1 4 4L7.5 20.5 2 22l1.5-5.5L17 3z"/></svg>'

icons = {
    'personalizowane': f'{svg_base}<path d="M19 21v-2a4 4 0 0 0-4-4H9a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg>',
    'chirurgia': f'{svg_base}<path d="m18 2 4 4"/><path d="m17 7 3-3"/><path d="M19 9 8.7 19.3c-1 1-2.5 1-3.4 0l-.6-.6c-1-1-1-2.5 0-3.4L15 5"/><path d="m9 11 4 4"/><path d="m5 19-3 3"/><path d="m14 4 6 6"/></svg>',
    'chirurgia_urazowo_ortopedyczna': f'{svg_base}<path d="M17 10c.7-.7 1.69 0 2.5 0a2.5 2.5 0 1 0 0-5 .5.5 0 0 1-.5-.5 2.5 2.5 0 1 0-5 0c0 .81.7 1.8 0 2.5l-4.6 4.6c-.7-.7-1.69 0-2.5 0a2.5 2.5 0 1 0 0 5 .5.5 0 0 1 .5.5 2.5 2.5 0 1 0 5 0c0-.81-.7-1.8 0-2.5l4.6-4.6Z"/></svg>',
    'choroby_wewnetrzne': f'{svg_base}<path d="M19 14c1.49-1.46 3-3.21 3-5.5A5.5 5.5 0 0 0 16.5 3c-1.76 0-3 .5-4.5 2-1.5-1.5-2.74-2-4.5-2A5.5 5.5 0 0 0 2 8.5c0 2.3 1.5 4.05 3 5.5l7 7Z"/></svg>',
    'medycyna_ratunkowa': f'{svg_base}<polyline points="22 12 18 12 15 21 9 3 6 12 2 12"/></svg>',
    'medycyna_rodzinna': f'{svg_base}<path d="M4.8 2.3A.3.3 0 1 0 5 2H4a2 2 0 0 0-2 2v5a6 6 0 0 0 6 6v0a6 6 0 0 0 6-6V4a2 2 0 0 0-2-2h-1a.2.2 0 1 0 .3.3"/><path d="M8 15v1a6 6 0 0 0 6 6v0a6 6 0 0 0 6-6v-4"/><circle cx="20" cy="10" r="2"/></svg>',
    'oit': f'{svg_base}<polyline points="22 12 18 12 15 21 9 3 6 12 2 12"/></svg>',
    'pediatria': f'{svg_base}<circle cx="12" cy="12" r="10"/><path d="M8 14s1.5 2 4 2 4-2 4-2"/><line x1="9" y1="9" x2="9.01" y2="9"/><line x1="15" y1="9" x2="15.01" y2="9"/></svg>'
}

# Usuń stare, dziwne ikony z zawartości plików (jeśli jeszcze jakieś zostały)
for file in os.listdir("."):
    if file.endswith(".md") and file not in ["README.md", "_sidebar.md", "spis_stazy.md"]:
        with open(file, "r") as f:
            content = f.read()
        
        # Wymiana przycisków na nowe ikony (nawet jeśli są to stare SVG)
        # Najpierw usuwamy CAŁE stare bloki <div> z przyciskami i podmieniamy na świeże
        lines = content.split("\n")
        new_lines = []
        skip = False
        in_div = False
        
        # Odtwórz zawartość pliku, ale przebuduj div z przyciskami i nagłówek
        for line in lines:
            if line.startswith("# "):
                # Extract text without any SVGs
                title_text = re.sub(r'<svg.*?</svg>\s*', '', line[2:])
                name = file.replace(".md", "")
                if name in icons:
                    new_lines.append(f"# {icons[name]} {title_text}")
                else:
                    new_lines.append(line)
            elif '<div style="display: flex;' in line:
                in_div = True
                continue
            elif in_div and '</div>' in line:
                in_div = False
                # Insert the new buttons!
                # We need the URLs
                import re
                urls = re.findall(r'href="(.*?)"', content)
                folder_url = urls[0] if len(urls) > 0 else "#"
                doc_url = urls[1] if len(urls) > 1 else None
                
                div_html = f'<div style="display: flex; gap: 15px; margin-bottom: 20px;">\n'
                div_html += f'  <a href="{folder_url}" target="_blank" style="padding: 10px 20px; border: 1px solid currentColor; border-radius: 5px; text-decoration: none;">\n'
                div_html += f'    {svg_folder} Otwórz folder (pliki)\n  </a>\n'
                
                if doc_url:
                    div_html += f'  <a href="{doc_url}" target="_blank" style="padding: 10px 20px; border: 1px solid currentColor; border-radius: 5px; text-decoration: none;">\n'
                    div_html += f'    {svg_edit} Edytuj dokument\n  </a>\n'
                
                div_html += '</div>'
                new_lines.append(div_html)
            elif in_div:
                pass
            else:
                new_lines.append(line)
                
        with open(file, "w") as f:
            f.write("\n".join(new_lines))

# 2. Update README.md
readme = """# Czeladź Staż

Wybierz oddział z poniższej listy, aby przejść do szczegółów:

<br>

"""
for key, icon in icons.items():
    if key == "personalizowane":
        readme += f"### [{icon} [PERSONALIZOWANE]]({key}.md)\n\n"
    elif key == "chirurgia":
        readme += f"### [{icon} Chirurgia]({key}.md)\n\n"
    elif key == "chirurgia_urazowo_ortopedyczna":
        readme += f"### [{icon} Chirurgia Urazowo-Ortopedyczna]({key}.md)\n\n"
    elif key == "choroby_wewnetrzne":
        readme += f"### [{icon} Choroby Wewnętrzne]({key}.md)\n\n"
    elif key == "medycyna_ratunkowa":
        readme += f"### [{icon} Medycyna Ratunkowa]({key}.md)\n\n"
    elif key == "medycyna_rodzinna":
        readme += f"### [{icon} Medycyna Rodzinna]({key}.md)\n\n"
    elif key == "oit":
        readme += f"### [{icon} OIT]({key}.md)\n\n"
    elif key == "pediatria":
        readme += f"### [{icon} Pediatria]({key}.md)\n\n"

with open("README.md", "w") as f:
    f.write(readme)

# 3. Update _sidebar.md
sidebar = f"""* [{svg_home} Strona główna](/)
* [{icons['personalizowane']} [PERSONALIZOWANE]](personalizowane.md)
* [{icons['chirurgia']} Chirurgia](chirurgia.md)
* [{icons['chirurgia_urazowo_ortopedyczna']} Chirurgia Urazowo-Ortopedyczna](chirurgia_urazowo_ortopedyczna.md)
* [{icons['choroby_wewnetrzne']} Choroby Wewnętrzne](choroby_wewnetrzne.md)
* [{icons['medycyna_ratunkowa']} Medycyna Ratunkowa](medycyna_ratunkowa.md)
* [{icons['medycyna_rodzinna']} Medycyna Rodzinna](medycyna_rodzinna.md)
* [{icons['oit']} OIT](oit.md)
* [{icons['pediatria']} Pediatria](pediatria.md)
"""

with open("_sidebar.md", "w") as f:
    f.write(sidebar)
