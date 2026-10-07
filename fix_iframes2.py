import os
import re

for file in os.listdir("."):
    if file.endswith(".md") and file not in ["README.md", "_sidebar.md", "spis_stazy.md"]:
        with open(file, "r") as f:
            content = f.read()
        
        # Zamieniamy domene docs.google.com na drive.google.com/file/d/ z koncowka preview
        content = re.sub(
            r'<iframe src="https://docs\.google\.com/document/d/([^/]+)/preview"',
            r'<iframe src="https://drive.google.com/file/d/\1/preview"',
            content
        )
        
        with open(file, "w") as f:
            f.write(content)

print("Podmieniono iframe'y na Drive Preview.")
