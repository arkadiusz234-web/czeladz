import os

svg_folder = '<svg class="ikona-stazu" viewBox="0 0 24 24"><path d="M10 4H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V8c0-1.1-.9-2-2-2h-8l-2-2z"/></svg>'
svg_edit = '<svg class="ikona-stazu" viewBox="0 0 24 24"><path d="M3 17.25V21h3.75L17.81 9.94l-3.75-3.75L3 17.25zM20.71 7.04c.39-.39.39-1.02 0-1.41l-2.34-2.34c-.39-.39-1.02-.39-1.41 0l-1.83 1.83 3.75 3.75 1.83-1.83z"/></svg>'

icons = {
    'personalizowane': '<svg class="ikona-stazu" viewBox="0 0 24 24"><path d="M12 12c2.21 0 4-1.79 4-4s-1.79-4-4-4-4 1.79-4 4 1.79 4 4 4zm0 2c-2.67 0-8 1.34-8 4v2h16v-2c0-2.66-5.33-4-8-4z"/></svg>',
    'chirurgia': '<svg class="ikona-stazu" viewBox="0 0 24 24"><path d="M19 3H5c-1.1 0-1.99.9-1.99 2L3 19c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm-2 9h-4v4h-2v-4H7v-2h4V7h2v4h4v2z"/></svg>',
    'chirurgia_urazowo_ortopedyczna': '<svg class="ikona-stazu" viewBox="0 0 24 24"><path d="M8 11h8v10h-2v-6h-4v6H8zM12 2c1.66 0 3 1.34 3 3s-1.34 3-3 3-3-1.34-3-3 1.34-3 3-3z"/></svg>',
    'choroby_wewnetrzne': '<svg class="ikona-stazu" viewBox="0 0 24 24"><path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z"/></svg>',
    'medycyna_ratunkowa': '<svg class="ikona-stazu" viewBox="0 0 24 24"><path d="M19 3H5c-1.1 0-1.99.9-1.99 2L3 19c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm-9 12H7v-2h3v-3h2v3h3v2h-3v3h-2v-3z"/></svg>',
    'medycyna_rodzinna': '<svg class="ikona-stazu" viewBox="0 0 24 24"><path d="M16 11c1.66 0 2.99-1.34 2.99-3S17.66 5 16 5c-1.66 0-3 1.34-3 3s1.34 3 3 3zm-8 0c1.66 0 2.99-1.34 2.99-3S9.66 5 8 5C6.34 5 5 6.34 5 8s1.34 3 3 3zm0 2c-2.33 0-7 1.17-7 3.5V19h14v-2.5c0-2.33-4.67-3.5-7-3.5zm8 0c-.29 0-.62.02-.97.05 1.16.84 1.97 1.97 1.97 3.45V19h6v-2.5c0-2.33-4.67-3.5-7-3.5z"/></svg>',
    'oit': '<svg class="ikona-stazu" viewBox="0 0 24 24"><path d="M19 3H5c-1.1 0-1.99.9-1.99 2L3 19c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm-2 9h-4v4h-2v-4H7v-2h4V7h2v4h4v2z"/></svg>',
    'pediatria': '<svg class="ikona-stazu" viewBox="0 0 24 24"><path d="M8 11h8v10h-2v-6h-4v6H8zM12 2c1.66 0 3 1.34 3 3s-1.34 3-3 3-3-1.34-3-3 1.34-3 3-3z"/></svg>'
}

# 1. Update individual markdown files
for file in os.listdir("."):
    if file.endswith(".md") and file not in ["README.md", "_sidebar.md", "spis_stazy.md"]:
        with open(file, "r") as f:
            content = f.read()
        
        # Replace emojis with SVGs
        content = content.replace("🗂️", svg_folder)
        content = content.replace("📝", svg_edit)
        
        # Add the specific internship icon next to the main header
        name = file.replace(".md", "")
        if name in icons:
            content = content.replace(f"# ", f"# {icons[name]} ")
        
        with open(file, "w") as f:
            f.write(content)

# 2. Update README.md
with open("README.md", "r") as f:
    readme_content = f.read()

# Replace generic SVG with specific SVGs in README
for key, icon in icons.items():
    # E.g. [Chirurgia](chirurgia.md) -> we replace the generic SVG before it
    generic_svg = '<svg class="ikona-stazu" viewBox="0 0 24 24"><path d="M10 4H4C2.9 4 2.01 4.9 2.01 6L2 18C2 19.1 2.9 20 4 20H20C21.1 20 22 19.1 22 18V8C22 6.9 21.1 6 20 6H12L10 4Z"/></svg>'
    # the format in README is ### [generic_svg Name](key.md)
    # this is a bit hard to replace directly, let's just regenerate the list.

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
svg_home = '<svg class="ikona-stazu" viewBox="0 0 24 24"><path d="M10 20v-6h4v6h5v-8h3L12 3 2 12h3v8z"/></svg>'
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
