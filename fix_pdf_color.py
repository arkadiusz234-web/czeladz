import os

if os.path.exists("index.html"):
    with open("index.html", "r") as f:
        html = f.read()

    old_htmlContent = """const htmlContent = '<div style="padding: 30px; font-family: Arial, sans-serif; font-size: 12px; line-height: 1.6;">' + finalStatus.replace(/\\n/g, "<br>") + '</div>';"""
    
    # Dodajemy background-color i color, ponieważ tryb ciemny Docsify powoduje wygenerowanie białego tekstu na białym tle
    new_htmlContent = """const htmlContent = '<div style="background-color: #ffffff; color: #000000; padding: 30px; font-family: Arial, sans-serif; font-size: 12px; line-height: 1.6;">' + finalStatus.replace(/\\n/g, "<br>") + '</div>';"""

    html = html.replace(old_htmlContent, new_htmlContent)

    with open("index.html", "w") as f:
        f.write(html)
    
    print("Fixed empty PDF due to Dark Mode white text bug!")
