import os
import re

if os.path.exists("index.html"):
    with open("index.html", "r") as f:
        html = f.read()

    # 1. Usuwamy ładowanie biblioteki html2pdf
    html = re.sub(r'<script src="https://cdnjs\.cloudflare\.com/ajax/libs/html2pdf\.js/.*?></script>', '', html)
    
    # 2. Zastępujemy logikę generowania PDF na generowanie pliku tekstowego .txt
    old_pdf_code = """        const pdfContainer = document.createElement("div");
        pdfContainer.style.backgroundColor = "#ffffff";
        pdfContainer.style.color = "#000000";
        pdfContainer.style.padding = "30px";
        pdfContainer.style.fontFamily = "Arial, sans-serif";
        pdfContainer.style.fontSize = "12px";
        pdfContainer.style.lineHeight = "1.6";
        pdfContainer.style.position = "absolute";
        pdfContainer.style.top = "0";
        pdfContainer.style.left = "0";
        pdfContainer.style.zIndex = "-9999";
        pdfContainer.style.width = "800px";
        pdfContainer.innerHTML = finalStatus.replace(/\\n/g, "<br>");
        document.body.appendChild(pdfContainer);
        
        if(typeof html2pdf !== 'undefined') {
            html2pdf().set({
                margin: 10,
                filename: `Status_${pacjent.replace(/[^a-z0-9]/gi, '_')}_${date}.pdf`,
                image: { type: 'jpeg', quality: 0.98 },
                html2canvas: { scale: 2, windowWidth: 800 },
                jsPDF: { unit: 'mm', format: 'a4', orientation: 'portrait' }
            }).from(pdfContainer).save().then(() => {
                document.body.removeChild(pdfContainer);
                let form = document.getElementById("chirurgia-form");
                if(form) form.reset();
            }).catch(err => {
                document.body.removeChild(pdfContainer);
            });
        } else {
            alert("Błąd: biblioteka html2pdf nie załadowała się prawidłowo.");
        }"""
        
    new_txt_code = """        // --- POBIERANIE JAKO ZWYKŁY PLIK TEKSTOWY (.txt) ---
        const blob = new Blob([finalStatus], { type: 'text/plain;charset=utf-8' });
        const url = URL.createObjectURL(blob);
        const a = document.createElement('a');
        
        let safeName = pacjent.trim().replace(/[^a-zA-Z0-9ąćęłńóśźżĄĆĘŁŃÓŚŹŻ ]/g, "").replace(/\\s+/g, "_");
        if(safeName === "__________________" || !safeName) safeName = "Nieznany";
        
        a.href = url;
        a.download = `Status_${safeName}.txt`;
        document.body.appendChild(a);
        a.click();
        
        // Sprzątanie po pobraniu
        setTimeout(() => {
            document.body.removeChild(a);
            window.URL.revokeObjectURL(url);
            let form = document.getElementById("chirurgia-form");
            if(form) form.reset();
        }, 100);"""

    html = html.replace(old_pdf_code, new_txt_code)
    
    # Podmieniamy alert tekstowy z informacją
    old_alert = """alert("Status wygenerowany! Jeśli PDF się nie pobrał, skopiuj tekst z pola poniżej.");"""
    new_alert = """alert("Status pomyślnie wygenerowany! Właśnie pobrano plik tekstowy (.txt) i skopiowano go do schowka.");"""
    html = html.replace(old_alert, new_alert)

    # Zmiana napisu na przycisku w formularzu (w pliku statusy_chirurgia.md musimy to załatać osobnym skryptem albo SED)

    with open("index.html", "w") as f:
        f.write(html)
    print("Migrated PDF download to TXT download in index.html")

# 3. Zmiana napisu przycisku w statusy_chirurgia.md
if os.path.exists("statusy_chirurgia.md"):
    with open("statusy_chirurgia.md", "r") as f:
        stat = f.read()
    stat = stat.replace("Generuj, Kopiuj i Pobierz PDF", "Generuj, Kopiuj i Pobierz .TXT")
    with open("statusy_chirurgia.md", "w") as f:
        f.write(stat)
    print("Updated button text in statusy_chirurgia.md")
