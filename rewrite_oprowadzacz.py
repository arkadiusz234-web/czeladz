import os
import re

# 1. Update oprowadzacz_przyjecie.md
markdown_content = """# <svg class="ikona-stazu" viewBox="0 0 24 24"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/><polyline points="10 9 9 9 8 9"/></svg> Oprowadzacz po przyjęciu (Chirurgia)

<style>
.oprowadzacz-container {
    padding: 0;
}
.form-section {
    background: #f8f9fa;
    padding: 20px;
    border-radius: 8px;
    border: 1px solid #e1e4e8;
    margin-bottom: 25px;
    box-shadow: 0 2px 4px rgba(0,0,0,0.05);
}
body.is-dark-mode .form-section {
    background: #1e1e1e;
    border-color: #333;
}
.form-section label {
    display: flex;
    align-items: center;
    gap: 10px;
    margin-bottom: 12px;
    cursor: pointer;
    font-size: 1.05em;
}
.form-section select {
    width: 100%;
    padding: 10px;
    font-size: 1em;
    border-radius: 6px;
    border: 1px solid #ccc;
    background: #fff;
    margin-top: 5px;
}
body.is-dark-mode .form-section select {
    background: #2d2d2d;
    color: #fff;
    border-color: #555;
}

#dynamic-guide {
    display: flex;
    flex-direction: column;
    gap: 20px;
}
.guide-step {
    background: #ffffff;
    border-left: 5px solid #3498db;
    padding: 20px;
    border-radius: 6px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.08);
}
body.is-dark-mode .guide-step {
    background: #252525;
    border-left-color: #2980b9;
}
.guide-step h3 {
    margin-top: 0;
    margin-bottom: 15px;
    font-size: 1.3em;
    color: #2c3e50;
    display: flex;
    align-items: center;
    gap: 10px;
}
body.is-dark-mode .guide-step h3 {
    color: #ecf0f1;
}
.guide-step ul {
    margin: 0;
    padding-left: 20px;
}
.guide-step li {
    margin-bottom: 10px;
    font-size: 1.05em;
}
.highlight-red {
    color: #e74c3c;
    font-weight: bold;
}
</style>

<div class="oprowadzacz-container">
    <div class="form-section">
        <div style="font-weight: bold; font-size: 1.2em; margin-bottom: 15px; border-bottom: 1px solid #ccc; padding-bottom: 10px;">📋 Opcje przyjęcia (zmieniaj w locie, instrukcja poniżej dopasuje się sama)</div>
        
        <label><input type="checkbox" id="q_cukrzyca" onchange="updateGuide()"> Pacjent ma cukrzycę</label>
        <label><input type="checkbox" id="q_cisnienie" onchange="updateGuide()"> Nadciśnienie na Izbie Przyjęć (SBP > 180, ew. > 170)</label>
        <label><input type="checkbox" id="q_grupa" onchange="updateGuide()"> Posiada POTWIERDZONĄ grupę krwi w systemie/na papierze</label>
        
        <div style="margin-top: 15px;">
            <div style="font-weight: 500; margin-bottom: 5px;">Planowany zabieg:</div>
            <select id="q_zabieg" onchange="updateGuide()">
                <option value="inny">Inny (standardowy)</option>
                <option value="endoskopia">Kolonoskopia / Gastroskopia</option>
                <option value="cholecystektomia">Cholecystektomia</option>
                <option value="przepuklina">Przepuklina (np. pachwinowa)</option>
                <option value="zylaki">Żylaki kończyn</option>
                <option value="rak">Rak (CA)</option>
            </select>
        </div>
    </div>

    <!-- Tu dynamicznie wpada instrukcja -->
    <div id="dynamic-guide"></div>
</div>

<!-- Automatyczne odpalenie po załadowaniu html przez docsify -->
<img src onerror="if(typeof updateGuide === 'function') updateGuide()">
"""

if os.path.exists("oprowadzacz_przyjecie.md"):
    with open("oprowadzacz_przyjecie.md", "w") as f:
        f.write(markdown_content)
    print("Updated oprowadzacz_przyjecie.md")

# 2. Update index.html logic
if os.path.exists("index.html"):
    with open("index.html", "r") as f:
        html = f.read()
    
    # We need to remove the old functions (genJednorazowe, genBadania, genWywiad) and insert the new updateGuide.
    # The old functions are between <script> and </script>\n</body>. We can use a regex to replace everything after the 
    # `// --- POBIERANIE JAKO ZWYKŁY PLIK TEKSTOWY (.txt) ---` block's closing bracket or just replace the specific function blocks.
    
    # A safe way: regex to replace everything from `function genJednorazowe()` to `function kopiuj`
    
    pattern = r"function genJednorazowe\(\) \{.*?(?=</script>\s*</body>)"
    
    new_script = """function updateGuide() {
    let cukrzyca = document.getElementById("q_cukrzyca") ? document.getElementById("q_cukrzyca").checked : false;
    let cisnienie = document.getElementById("q_cisnienie") ? document.getElementById("q_cisnienie").checked : false;
    let grupa = document.getElementById("q_grupa") ? document.getElementById("q_grupa").checked : false;
    let zabieg = document.getElementById("q_zabieg") ? document.getElementById("q_zabieg").value : "inny";

    let html = "";

    // 1. WPISZ W SYSTEM
    html += "<div class='guide-step'>";
    html += "<h3>🖥️ Krok 1: Wpisz w system</h3>";
    html += "<ul>";
    html += "<li><strong>Rozpoznanie:</strong> (wpisz odpowiednie dla zabiegu)</li>";
    if (zabieg === "endoskopia") {
        html += "<li><strong>Powód przyjęcia:</strong> <span class='highlight-red'>OBOWIĄZKOWO wpisz powód, dla którego robiona jest endoskopia!</span></li>";
    } else {
        html += "<li><strong>Powód przyjęcia:</strong> (uzupełnij)</li>";
    }
    html += "</ul>";
    html += "</div>";

    // 2. ZLEĆ W SYSTEMIE
    html += "<div class='guide-step'>";
    html += "<h3>💊 Krok 2: Zleć w systemie</h3>";
    html += "<ul>";
    html += "<li><strong>Zlecenia stałe:</strong> Użyj gotowca (np. <em>'planówka do zabiegu'</em>)</li>";
    
    if (zabieg === "endoskopia") {
        html += "<li><strong class='highlight-red'>Uwaga (Grupa krwi):</strong> NIE ZLECAJ grupy krwi na czystą endoskopię!</li>";
    } else {
        if (grupa) {
            html += "<li><strong>Grupa krwi:</strong> Zaznacz opcję 'wszystkie' -> w polu <em>Uwagi</em> wpisz: <strong>odpis z dn. XX.YY.ZZZZ</strong></li>";
        } else {
            html += "<li><strong>Grupa krwi:</strong> Zleć badanie grupy krwi (brak potwierdzonego wyniku w systemie/na papierze).</li>";
        }
    }
    
    if (cukrzyca) {
        html += "<li><strong>Badania/Konsultacje:</strong> Dopisz <strong>DPC</strong>.</li>";
    }
    if (zabieg === "cholecystektomia") {
        html += "<li><strong>Konsultacje:</strong> Zleć konsultację <strong>Dietetyka</strong>.</li>";
    }
    if (cisnienie) {
        html += "<li><strong>Zlecenia jednorazowe:</strong> Zleć <strong>Captopril 12,5 mg s.l.</strong> (lub 25mg).<br><span style='color: #7f8c8d; font-size: 0.9em;'>-> Wpisz godzinę pomiaru i wartość ciśnienia (np. 180/110).<br>-> Podbij się za osobą podającą lek i wpisz godzinę podania!</span></li>";
    }
    
    html += "<li><strong>Inne badania:</strong> Zleć EKG oraz podstawowe badania laboratoryjne (jeśli nie było zlecone/zrobione).</li>";
    html += "</ul>";
    html += "</div>";

    // 3. WYDRUKUJ
    html += "<div class='guide-step'>";
    html += "<h3>🖨️ Krok 3: Wydrukuj z systemu</h3>";
    html += "<ul>";
    html += "<li>Historia choroby / Karta informacyjna</li>";
    html += "<li>Karta zleceń lekarskich (stałych, jednorazowych, badań/konsultacji)</li>";
    html += "<li>Karta badania przedmiotowego (do wydruku i podpisu)</li>";
    if (zabieg === "endoskopia") {
        html += "<li><strong>Zgoda na endoskopię:</strong> <span class='highlight-red'>OBOWIĄZKOWO musi zawierać wydrukowany powód badania!</span></li>";
    } else {
        html += "<li>Zgoda na zabieg operacyjny (odpowiednia do rodzaju zabiegu)</li>";
        html += "<li>Zgoda na znieczulenie (jeśli dotyczy)</li>";
    }
    html += "</ul>";
    html += "</div>";

    // 4. UZUPEŁNIJ (PAPIERY)
    html += "<div class='guide-step'>";
    html += "<h3>📝 Krok 4: Uzupełnij fizycznie (papiery)</h3>";
    html += "<ul>";
    html += "<li>Wypełnij stosowne druki i zgody</li>";
    html += "<li><strong>Karta żywieniowa</strong> - wypełnij.</li>";
    html += "<li><strong>Karta dupowa</strong> (ocena ryzyka odleżyn itp.) - wypełnij.</li>";
    html += "<li><strong>Karta badania przedmiotowego:</strong> Upewnij się, że jest podpisana i ma pieczątkę.</li>";
    html += "</ul>";
    html += "</div>";

    // 5. SZCZEGÓŁY WYWIADU
    html += "<div class='guide-step'>";
    html += "<h3>🔍 Krok 5: Szczegóły Wywiadu (Badanie podmiotowe/przedmiotowe)</h3>";
    html += "<ul>";
    html += "<li><strong>Nie omijaj żadnej kratki!</strong> Jeśli pacjent nie ma innych dolegliwości, wpisuj: <em>'neguje'</em>, <em>'brak'</em>, <em>'nie zgłasza'</em>, <em>'nie było'</em>. Zaznaczaj WIELE kratek jeśli pasują.</li>";
    html += "<li><strong>Czego NIE wpisujemy w listę leków stałych:</strong> leków p/krzepliwych pacjenta, p/płytkowych, insuliny, leków p/cukrzycowych, wziewów, witamin (w tym żelaza).</li>";
    
    if (zabieg === "przepuklina") {
        html += "<li><strong>Skróty do użycia:</strong><br>HID (pachwinowa pr.), HIS (pachwinowa lewa), HIB (obustronna), HU (pępkowa), HV (brzuszna).</li>";
    } else if (zabieg === "rak") {
        html += "<li><strong>Skróty do użycia:</strong><br>CA (rak), Recti (prostnicy), Sigmoidei (esicy), Ceci (kątnicy).</li>";
    } else if (zabieg === "zylaki") {
        html += "<li><strong>Skróty do użycia:</strong><br>VEIS (żylaki KD lewej), VEID (żylaki KD prawej).</li>";
    }
    
    html += "<li><strong class='highlight-red'>W razie wątpliwości na izbie:</strong> Dzwoń po 'dużego' lekarza (283).</li>";
    html += "</ul>";
    html += "</div>";

    let guideBox = document.getElementById("dynamic-guide");
    if(guideBox) guideBox.innerHTML = html;
}
"""
    
    # We can replace everything starting from function genJednorazowe() up to function kopiuj()
    # It's safer to just split by "function genJednorazowe()" and replace.
    parts = html.split("function genJednorazowe()")
    if len(parts) == 2:
        top_half = parts[0]
        # remove everything up to </script>\n</body>
        bottom_part_split = parts[1].split("</script>\n</body>")
        if len(bottom_part_split) > 0:
            new_html = top_half + new_script + "\n</script>\n</body>"
            with open("index.html", "w") as f:
                f.write(new_html)
            print("Updated index.html logic successfully")
        else:
            print("Could not parse bottom part of index.html")
    else:
        print("Could not find genJednorazowe in index.html")
