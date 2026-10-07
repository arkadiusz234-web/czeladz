import os

html_content = """# <svg class="ikona-stazu" viewBox="0 0 24 24"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/><polyline points="10 9 9 9 8 9"/></svg> Oprowadzacz po przyjęciu (Chirurgia)

<style>
.step-container {
    background: var(--background);
    padding: 20px;
    border-radius: 8px;
    border: 1px solid var(--borderColor);
    margin-bottom: 20px;
}
.step-title {
    font-size: 1.2em;
    font-weight: bold;
    margin-bottom: 15px;
    color: var(--textColor);
    border-bottom: 2px solid var(--borderColor);
    padding-bottom: 5px;
}
.question-row {
    margin-bottom: 10px;
    display: flex;
    align-items: center;
    gap: 10px;
}
.question-row label {
    cursor: pointer;
    font-weight: 500;
}
.btn-action {
    background: var(--textColor);
    color: var(--background);
    border: none;
    padding: 8px 16px;
    font-size: 0.9em;
    font-weight: bold;
    border-radius: 6px;
    cursor: pointer;
    margin-top: 10px;
    margin-right: 10px;
}
.btn-action:hover {
    opacity: 0.8;
}
.output-box {
    margin-top: 15px;
    background: #f8f9fa;
    color: #000;
    border-left: 4px solid #3498db;
    padding: 15px;
    border-radius: 4px;
    font-family: monospace;
    white-space: pre-wrap;
    display: none;
}
body.is-dark-mode .output-box {
    background: #2c3e50;
    color: #fff;
    border-left-color: #2980b9;
}
.hint-text {
    font-size: 0.85em;
    color: #7f8c8d;
    margin-top: 5px;
    display: block;
}
</style>

<p>Kreator, który krok po kroku wygeneruje dokładne instrukcje co i gdzie wpisać w karcie pacjenta. Zaznacz poniższe informacje o pacjencie:</p>

<div class="step-container">
    <div class="step-title">Krok 1: Profil pacjenta i planowany zabieg</div>
    
    <div class="question-row">
        <input type="checkbox" id="q_cukrzyca"> 
        <label for="q_cukrzyca">Pacjent ma cukrzycę</label>
    </div>
    
    <div class="question-row">
        <input type="checkbox" id="q_cisnienie"> 
        <label for="q_cisnienie">Nadciśnienie na Izbie Przyjęć (SBP > 180, ew. > 170)</label>
    </div>
    
    <div class="question-row">
        <input type="checkbox" id="q_grupa"> 
        <label for="q_grupa">Posiada POTWIERDZONĄ grupę krwi w systemie/na papierze</label>
    </div>

    <div class="question-row" style="margin-top: 15px;">
        <label>Planowany zabieg:</label>
        <select id="q_zabieg" style="padding: 5px; border-radius: 4px; background: var(--background); color: var(--textColor); border: 1px solid var(--borderColor);">
            <option value="inny">Inny (standardowy)</option>
            <option value="endoskopia">Kolonoskopia / Gastroskopia</option>
            <option value="cholecystektomia">Cholecystektomia</option>
            <option value="przepuklina">Przepuklina (HID/HIS/HIB/HU/HV)</option>
            <option value="zylaki">Żylaki (VEIS/VEID)</option>
            <option value="rak">Rak (CA Recti/Sigmoidei/Ceci...)</option>
        </select>
    </div>
</div>

<div class="step-container">
    <div class="step-title">1. Karta Zleceń Jednorazowych</div>
    <p style="font-size: 0.9em;">W tej karcie wpisujemy doraźne leki i przygotowanie do zabiegu (np. antybiotyk profilaktyczny na blok, leki zbijające ciśnienie). <i>Zgodnie z prośbą, nie generujemy tu leków stałych pacjenta.</i></p>
    
    <button class="btn-action" onclick="genJednorazowe()">Generuj treść do wpisania</button>
    <div id="out_jednorazowe" class="output-box"></div>
</div>

<div class="step-container">
    <div class="step-title">2. Karta Konsultacji i Badań</div>
    <p style="font-size: 0.9em;">Wpisujemy zlecenia badań z krwi, grupy krwi, konsultacje (np. dietetyk), EKG, RTG.</p>
    
    <button class="btn-action" onclick="genBadania()">Generuj treść do wpisania</button>
    <div id="out_badania" class="output-box"></div>
</div>

<div class="step-container">
    <div class="step-title">3. Wywiad (Badanie podmiotowe i przedmiotowe)</div>
    <p style="font-size: 0.9em;">Jak wypełniać kratki w historii choroby przy przyjęciu.</p>
    
    <button class="btn-action" onclick="genWywiad()">Generuj przypomnienia</button>
    <div id="out_wywiad" class="output-box"></div>
</div>

<script>
function genJednorazowe() {
    let out = [];
    out.push("Co dokładnie wpisać w tabelę ZLECENIA JEDNORAZOWE:\\n");
    
    let cisnienie = document.getElementById("q_cisnienie").checked;
    
    if (cisnienie) {
        out.push("[ ] Captopril 12,5 mg s.l. (lub 25mg)");
        out.push("    -> UWAGA: Wpisz obok godzinę pomiaru i wartość ciśnienia (np. 180/110).");
        out.push("    -> Podbij się za osobą podającą lek i wpisz godzinę podania!");
    }
    
    out.push("[ ] Ewentualna profilaktyka antybiotykowa na blok operacyjny (np. Biofazolin 2,0g i.v. / Metronidazol 500mg i.v. - zgodnie z zaleceniem dla zabiegu).");
    out.push("[ ] Ewentualne zlecenia płynów (np. PWE 500ml i.v. nawodnienie).");
    out.push("[ ] Profilaktyka p/zakrzepowa (np. Clexane 40mg s.c. - podaj godzinę).");
    
    if(out.length === 1) {
        out.push("Brak specjalnych zleceń dla zaznaczonego profilu pacjenta. Wpisz standardowe leki okołooperacyjne.");
    }
    
    let box = document.getElementById("out_jednorazowe");
    box.innerText = out.join("\\n");
    box.style.display = "block";
    kopiuj(out.join("\\n"));
}

function genBadania() {
    let out = [];
    let cukrzyca = document.getElementById("q_cukrzyca").checked;
    let grupa = document.getElementById("q_grupa").checked;
    let zabieg = document.getElementById("q_zabieg").value;
    
    out.push("Co dokładnie wpisać w tabelę KONSULTACJE I BADANIA:\\n");
    
    if (cukrzyca) {
        out.push("[ ] DPC (Dopisać w zleceniach badaniach z powodu cukrzycy)");
    }
    
    if (zabieg === "cholecystektomia") {
        out.push("[ ] Dietetyk (Konieczne zlecenie konsultacji dietetycznej przy cholecystektomii)");
    }
    
    if (zabieg === "endoskopia") {
        out.push("[!] NIE ZLECAJ grupy krwi! (Czysta endoskopia nie wymaga grupy krwi).");
        out.push("[!] Dopisz POWÓD PRZYJĘCIA przy zlecaniu zabiegu endoskopowego.");
    } else {
        if (grupa) {
            out.push("[ ] Grupa krwi: W kratce 'Uwagi' wpisz: odpis z dn. XX.YY.ZZZZ (zaznaczając opcję 'wszystkie' w sekcji badania).");
        } else {
            out.push("[ ] Grupa krwi (zlecenie badania, jeśli brak dokumentu).");
        }
    }
    
    out.push("[ ] EKG (Rutynowo przed zabiegiem)");
    out.push("[ ] Podstawowe badania laboratoryjne przed zabiegiem");
    
    let box = document.getElementById("out_badania");
    box.innerText = out.join("\\n");
    box.style.display = "block";
    kopiuj(out.join("\\n"));
}

function genWywiad() {
    let out = [];
    out.push("Zasady uzupełniania badania podmiotowego i przedmiotowego:\\n");
    
    out.push("1. NIE OMIJAJ ŻADNEJ KRATKI!");
    out.push("   - Jeśli pacjent nie ma innych dolegliwości, w pustych polach wpisz: 'neguje', 'nie zgłasza', 'jak wyżej', 'nie było' lub 'brak'.");
    out.push("   - Nie zostawiaj pustych kratek!");
    out.push("2. KARTA LEKÓW STAŁYCH (czego NIE rozpisujemy):");
    out.push("   - leków p/krzepliwych pacjenta");
    out.push("   - leków p/płytkowych");
    out.push("   - insuliny");
    out.push("   - leków p/cukrzycowych");
    out.push("   - wziewów");
    out.push("   - witamin i suplementów (w tym żelaza)");
    out.push("3. Zaznaczaj WIELE kratek jeśli pasują (np. przy oddechu, tętnie, brzuchu, zorientowaniu auto-allo psychicznym).");
    
    let zabieg = document.getElementById("q_zabieg").value;
    if(zabieg === "przepuklina") {
        out.push("\\nSkróty dla przepuklin (do użycia w karcie):");
        out.push("- HID: hernia inguinalis dextra (pachwinowa prawa)");
        out.push("- HIS: hernia inguinalis sinistra (pachwinowa lewa)");
        out.push("- HIB: hernia inguinalis bilateralis (pachwinowa obustronna)");
        out.push("- HU: hernia umbilicalis (pępkowa)");
        out.push("- HV: hernia ventricularis/lineae albae (brzuszna/kresy białej)");
    } else if (zabieg === "rak") {
        out.push("\\nSkróty onkologiczne (do użycia w karcie):");
        out.push("- CA: Carcinoma (rak)");
        out.push("- Recti: prostnicy");
        out.push("- Sigmoidei: esicy");
        out.push("- Ceci: kątnicy");
    } else if (zabieg === "zylaki") {
        out.push("\\nSkróty żylaków (do użycia w karcie):");
        out.push("- VEIS: żylaki KD lewej");
        out.push("- VEID: żylaki KD prawej");
    }
    
    out.push("\\n[!] W razie wątpliwości na izbie dzwoń po 'dużego' lekarza: 283.");

    let box = document.getElementById("out_wywiad");
    box.innerText = out.join("\\n");
    box.style.display = "block";
    kopiuj(out.join("\\n"));
}

function kopiuj(tekst) {
    if (navigator.clipboard && window.isSecureContext) {
        navigator.clipboard.writeText(tekst).catch(err => console.log(err));
    }
}
</script>
"""

# Usuwamy skrypt z pliku markdown i przenosimy do index.html
html_markdown = html_content.split("<script>")[0]

with open("oprowadzacz_przyjecie.md", "w") as f:
    f.write(html_markdown)
print("Created oprowadzacz_przyjecie.md")

js_logic = html_content.split("<script>")[1].split("</script>")[0]

if os.path.exists("index.html"):
    with open("index.html", "r") as f:
        idx_html = f.read()
    
    # Add JS before </body>
    idx_html = idx_html.replace("</body>", js_logic + "\\n</body>")
    with open("index.html", "w") as f:
        f.write(idx_html)
    print("Injected JS to index.html")

# Add to _sidebar.md
if os.path.exists("_sidebar.md"):
    with open("_sidebar.md", "r") as f:
        sidebar = f.read()
    
    if "Oprowadzacz po przyjęciu" not in sidebar:
        sidebar = sidebar.replace("* [Kalkulator BMI](kalkulator_bmi.md)\n", "* [Kalkulator BMI](kalkulator_bmi.md)\n  * [Oprowadzacz po przyjęciu](oprowadzacz_przyjecie.md)\n")
        with open("_sidebar.md", "w") as f:
            f.write(sidebar)
        print("Updated _sidebar.md")

# Remove leading spaces inside the markdown just in case Docsify codeblocks it again
with open("oprowadzacz_przyjecie.md", "r") as f:
    lines = f.readlines()
with open("oprowadzacz_przyjecie.md", "w") as f:
    for line in lines:
        if line.startswith("    "):
            f.write(line.lstrip())
        else:
            f.write(line)
