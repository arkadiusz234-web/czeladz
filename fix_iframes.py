import os

for file in os.listdir("."):
    if file.endswith(".md") and file not in ["README.md", "_sidebar.md", "spis_stazy.md"]:
        with open(file, "r") as f:
            content = f.read()
        
        # Zmiana z /pub?embedded=true na /preview
        content = content.replace("/pub?embedded=true", "/preview")
        
        with open(file, "w") as f:
            f.write(content)

print("Podmieniono iframe'y.")
