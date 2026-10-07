import os
import re
import shutil

links = {
    "chirurgia.md": "https://docs.google.com/spreadsheets/d/1GmIf2fyX4gcT_tZk0eqcwwMdRJCBYIzXpwbWSj8kyKg/edit?gid=1241902551#gid=1241902551",
    "pediatria.md": "https://docs.google.com/spreadsheets/d/1GmIf2fyX4gcT_tZk0eqcwwMdRJCBYIzXpwbWSj8kyKg/edit?gid=1449721214#gid=1449721214",
    "medycyna_ratunkowa.md": "https://docs.google.com/spreadsheets/d/1GmIf2fyX4gcT_tZk0eqcwwMdRJCBYIzXpwbWSj8kyKg/edit?gid=266424938#gid=266424938",
    "medycyna_rodzinna.md": "https://docs.google.com/spreadsheets/d/1GmIf2fyX4gcT_tZk0eqcwwMdRJCBYIzXpwbWSj8kyKg/edit?gid=1308142330#gid=1308142330",
    "chirurgia_urazowo_ortopedyczna.md": "https://docs.google.com/spreadsheets/d/1GmIf2fyX4gcT_tZk0eqcwwMdRJCBYIzXpwbWSj8kyKg/edit?gid=226719925#gid=226719925",
    "oit.md": "https://docs.google.com/spreadsheets/d/1GmIf2fyX4gcT_tZk0eqcwwMdRJCBYIzXpwbWSj8kyKg/edit?gid=5786351#gid=5786351",
    "personalizowane.md": "https://docs.google.com/spreadsheets/d/1GmIf2fyX4gcT_tZk0eqcwwMdRJCBYIzXpwbWSj8kyKg/edit?gid=1998228717#gid=1998228717"
}

# Update existing files
for filename, edit_url in links.items():
    if os.path.exists(filename):
        with open(filename, "r") as f:
            content = f.read()
        
        # 1. Update the iframe src.
        # Find existing iframe src and replace it.
        # The correct iframe format is .../edit?rm=minimal#gid=...
        iframe_url = edit_url.replace("?gid=", "?rm=minimal#gid=").split("#gid=")[0] + "#gid=" + edit_url.split("#gid=")[-1]
        
        # Regex to find <iframe src="..."
        content = re.sub(r'<iframe src="[^"]+" width="100%" height="900"', f'<iframe src="{iframe_url}" width="100%" height="900"', content)
        
        # 2. Update the "Edytuj dokument" button href.
        # It's inside an anchor tag containing "Edytuj dokument"
        # We need to replace the href of the a tag that wraps Edytuj dokument
        # Regex to match href="..." ...> ... Edytuj dokument
        content = re.sub(r'href="[^"]+"( target="_blank"[^>]+>\s*<svg[^>]+>.*?</svg>\s*Edytuj dokument)', f'href="{edit_url}"\\1', content)
        
        # Change "Edytuj dokument" text to "Edytuj arkusz" to be more accurate
        content = content.replace("Edytuj dokument", "Edytuj arkusz")
        
        with open(filename, "w") as f:
            f.write(content)

# Create neonatologia.md
neonatologia_url = "https://docs.google.com/spreadsheets/d/1GmIf2fyX4gcT_tZk0eqcwwMdRJCBYIzXpwbWSj8kyKg/edit?gid=226719925#gid=226719925"
neonatologia_iframe = neonatologia_url.replace("?gid=", "?rm=minimal#gid=").split("#gid=")[0] + "#gid=" + neonatologia_url.split("#gid=")[-1]

# Copy base structure from pediatria.md
if os.path.exists("pediatria.md"):
    with open("pediatria.md", "r") as f:
        content = f.read()
    
    # Change Title (including the icon, keeping the baby icon)
    content = re.sub(r'# <svg[^>]+>.*?</svg>\s*Pediatria', r'# <svg class="ikona-stazu" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><path d="M8 14s1.5 2 4 2 4-2 4-2"/><line x1="9" y1="9" x2="9.01" y2="9"/><line x1="15" y1="9" x2="15.01" y2="9"/></svg> Neonatologia', content)
    
    # Add text "?coś takiego jest (dodam pozniej)" after the title
    content = content.replace("Neonatologia", "Neonatologia\n\n?coś takiego jest (dodam pozniej)")
    
    # Update Iframe URL
    content = re.sub(r'<iframe src="[^"]+" width="100%" height="900"', f'<iframe src="{neonatologia_iframe}" width="100%" height="900"', content)
    
    # Update button URL
    content = re.sub(r'href="[^"]+"( target="_blank"[^>]+>\s*<svg[^>]+>.*?</svg>\s*Edytuj arkusz)', f'href="{neonatologia_url}"\\1', content)
    
    with open("neonatologia.md", "w") as f:
        f.write(content)

# Add Neonatologia to README.md
if os.path.exists("README.md"):
    with open("README.md", "r") as f:
        readme = f.read()
    if "Neonatologia" not in readme:
        baby_icon = '<svg class="ikona-stazu" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><path d="M8 14s1.5 2 4 2 4-2 4-2"/><line x1="9" y1="9" x2="9.01" y2="9"/><line x1="15" y1="9" x2="15.01" y2="9"/></svg>'
        # Insert after pediatria
        readme = readme.replace(f"### [{baby_icon} Pediatria](pediatria.md)\n\n", f"### [{baby_icon} Pediatria](pediatria.md)\n\n### [{baby_icon} Neonatologia](neonatologia.md)\n\n")
        with open("README.md", "w") as f:
            f.write(readme)

# Add Neonatologia to _sidebar.md
if os.path.exists("_sidebar.md"):
    with open("_sidebar.md", "r") as f:
        sidebar = f.read()
    if "Neonatologia" not in sidebar:
        baby_icon = '<svg class="ikona-stazu" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><path d="M8 14s1.5 2 4 2 4-2 4-2"/><line x1="9" y1="9" x2="9.01" y2="9"/><line x1="15" y1="9" x2="15.01" y2="9"/></svg>'
        sidebar = sidebar.replace(f"* [{baby_icon} Pediatria](pediatria.md)\n", f"* [{baby_icon} Pediatria](pediatria.md)\n* [{baby_icon} Neonatologia](neonatologia.md)\n")
        with open("_sidebar.md", "w") as f:
            f.write(sidebar)

print("Skrypt zakończony.")
