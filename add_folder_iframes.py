import os
import re

for file in os.listdir("."):
    if file.endswith(".md") and file not in ["README.md", "_sidebar.md", "spis_stazy.md"]:
        with open(file, "r") as f:
            content = f.read()
        
        folder_match = re.search(r'drive\.google\.com/drive/folders/([a-zA-Z0-9_-]+)', content)
        
        if folder_match:
            folder_id = folder_match.group(1)
            
            if "embeddedfolderview" not in content:
                folder_iframe = f'\n\n### 📁 Pliki w folderze\n<iframe src="https://drive.google.com/embeddedfolderview?id={folder_id}#list" width="100%" height="350" frameborder="0" style="border: 1px solid currentColor; border-radius: 8px; margin-bottom: 20px;"></iframe>\n'
                
                if '<hr style="margin: 30px 0;">' in content:
                    content = content.replace('<hr style="margin: 30px 0;">', folder_iframe + '\n<hr style="margin: 30px 0;">\n### 📝 Główne notatki')
                else:
                    content += folder_iframe
                
                with open(file, "w") as f:
                    f.write(content)

print("Dodano interaktywne podglądy folderów do wszystkich stron.")
