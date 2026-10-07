import os
import re

# 1. Update kalkulator_bmi.md: change waga type to text
if os.path.exists("kalkulator_bmi.md"):
    with open("kalkulator_bmi.md", "r") as f:
        content = f.read()
    content = content.replace('type="number" id="waga"', 'type="text" id="waga"')
    with open("kalkulator_bmi.md", "w") as f:
        f.write(content)
    print("Fixed kalkulator_bmi.md")

# 2. Update index.html
if os.path.exists("index.html"):
    with open("index.html", "r") as f:
        html = f.read()
    
    # Fix mocz
    old_mocz = """if(radio("mocz") === "cewnik Foleya") m += ` (${radio("mocz_cecha")})`;"""
    new_mocz = """m += ` (${radio("mocz_cecha")})`;"""
    html = html.replace(old_mocz, new_mocz)
    
    # Fix html2pdf empty generation
    old_pdf = """        const pdfContainer = document.createElement("div");
        pdfContainer.style.padding = "30px";
        pdfContainer.style.fontFamily = "Arial, sans-serif";
        pdfContainer.style.fontSize = "12px";
        pdfContainer.style.lineHeight = "1.6";
        pdfContainer.innerHTML = finalStatus.replace(/\\n/g, "<br>");
        
        if(typeof html2pdf !== 'undefined') {
            html2pdf().set({
                margin: 10,
                filename: `Status_${pacjent.replace(/[^a-z0-9]/gi, '_')}_${date}.pdf`,
                image: { type: 'jpeg', quality: 0.98 },
                html2canvas: { scale: 2 },
                jsPDF: { unit: 'mm', format: 'a4', orientation: 'portrait' }
            }).from(pdfContainer).save().then(() => {"""
            
    new_pdf = """        const htmlContent = '<div style="padding: 30px; font-family: Arial, sans-serif; font-size: 12px; line-height: 1.6;">' + finalStatus.replace(/\\n/g, "<br>") + '</div>';
        
        if(typeof html2pdf !== 'undefined') {
            html2pdf().set({
                margin: 10,
                filename: `Status_${pacjent.replace(/[^a-z0-9]/gi, '_')}_${date}.pdf`,
                image: { type: 'jpeg', quality: 0.98 },
                html2canvas: { scale: 2 },
                jsPDF: { unit: 'mm', format: 'a4', orientation: 'portrait' }
            }).from(htmlContent).save().then(() => {"""
            
    html = html.replace(old_pdf, new_pdf)

    # Improve copy fallback
    old_copy = """        navigator.clipboard.writeText(finalStatus).then(() => {
            alert("Status wygenerowany i skopiowany do schowka!");
        }).catch(err => {
            if(textarea) {
                textarea.select();
                document.execCommand('copy');
            }
            alert("Status wygenerowany i skopiowany do schowka!");
        });"""
        
    new_copy = """        if (navigator.clipboard && window.isSecureContext) {
            navigator.clipboard.writeText(finalStatus).catch(err => {
                if(textarea) { textarea.select(); document.execCommand('copy'); }
            });
        } else {
            if(textarea) { textarea.select(); document.execCommand('copy'); }
        }
        alert("Status wygenerowany! Jeśli PDF się nie pobrał, skopiuj tekst z pola poniżej.");"""
        
    html = html.replace(old_copy, new_copy)

    with open("index.html", "w") as f:
        f.write(html)
    print("Fixed index.html logic")
