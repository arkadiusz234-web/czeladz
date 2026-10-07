import os

if os.path.exists("index.html"):
    with open("index.html", "r") as f:
        html = f.read()

    # Szukamy miejsca z htmlContent
    old_pdf_code = """        const htmlContent = '<div style="background-color: #ffffff; color: #000000; padding: 30px; font-family: Arial, sans-serif; font-size: 12px; line-height: 1.6;">' + finalStatus.replace(/\\n/g, "<br>") + '</div>';
        
        if(typeof html2pdf !== 'undefined') {
            html2pdf().set({
                margin: 10,
                filename: `Status_${pacjent.replace(/[^a-z0-9]/gi, '_')}_${date}.pdf`,
                image: { type: 'jpeg', quality: 0.98 },
                html2canvas: { scale: 2 },
                jsPDF: { unit: 'mm', format: 'a4', orientation: 'portrait' }
            }).from(htmlContent).save().then(() => {
                let form = document.getElementById("chirurgia-form");
                if(form) form.reset();
            });
        } else {
            alert("Błąd: biblioteka html2pdf nie załadowała się prawidłowo.");
        }"""
        
    new_pdf_code = """        const pdfContainer = document.createElement("div");
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

    html = html.replace(old_pdf_code, new_pdf_code)

    with open("index.html", "w") as f:
        f.write(html)
    print("Fixed PDF generation logic by manually attaching container to DOM")
