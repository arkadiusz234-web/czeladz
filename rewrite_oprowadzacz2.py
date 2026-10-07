import os

if os.path.exists("index.html"):
    with open("index.html", "r") as f:
        html = f.read()

    # Szukamy bloku updateGuide()
    parts = html.split("function updateGuide() {")
    if len(parts) == 2:
        top_half = parts[0]
        # Pozbywamy się starego bloku od updateGuide() do końca
        bottom_part_split = parts[1].split("</script>\n</body>")
        
        new_script = """function updateGuide() {
    let cukrzyca = document.getElementById("q_cukrzyca") ? document.getElementById("q_cukrzyca").checked : false;
    let tarczyca = document.getElementById("q_tarczyca") ? document.getElementById("q_tarczyca").checked : false;
    let cisnienie = document.getElementById("q_cisnienie") ? document.getElementById("q_cisnienie").checked : false;
    let grupa = document.getElementById("q_grupa") ? document.getElementById("q_grupa").checked : false;
    let poranny = document.getElementById("q_poranny") ? document.getElementById("q_poranny").checked : false;
    let wiek = document.getElementById("q_wiek") ? document.getElementById("q_wiek").checked : false;
    let caprini = document.getElementById("q_caprini") ? document.getElementById("q_caprini").checked : false;
    let zabieg = document.getElementById("q_zabieg") ? document.getElementById("q_zabieg").value : "inny";

    let out = "";

    out += "<div class='guide-step'>";
    out += "<h3>1️⃣ Rejestracja i wywiad o lekach (na Izbie)</h3>";
    out += "<ul>";
    out += "<li>Podejdź do rejestratorek po <strong>koperty</strong> zarejestrowanych pacjentów.</li>";
    out += "<li>Poproś pacjentów o <strong>listę leków</strong> (co i kiedy odstawione).</li>";
    out += "<li><strong class='highlight-red'>Bezwzględnie sprawdź odstawienie leków:</strong><br>";
    out += " - <em>p/płytkowe (5-7 dni):</em> Acard, Polocard, Plavix, Areplex, itp.<br>";
    out += " - <em>p/krzepliwe (5-7 dni):</em> Warfin, Acenokumarol<br>";
    out += " - <em>p/krzepliwe (2-3 dni):</em> Pradaxa, Eliquis, Xarelto (Mibrex)<br>";
    out += " - <em>p/cukrzycowe (7 dni):</em> Ozempic, Mounjaro<br>";
    out += " - <em>p/cukrzycowe (2-3 dni):</em> Jardiance, Forxiga</li>";
    out += "<li>Zastrzyki Clexane/Neoparin są DOZWOLONE.</li>";
    out += "</ul>";
    out += "</div>";

    out += "<div class='guide-step'>";
    out += "<h3>2️⃣ Wpisz w system (Rozpoznanie i Uzasadnienie)</h3>";
    out += "<ul>";
    out += "<li><strong>Obserwacja (gotowiec):</strong> ";
    if (zabieg === "endoskopia") out += "Wpisz <em>'kolo/kolo K'</em> lub <em>'gastro'</em>.";
    else out += "Wpisz <em>'przyjęcie/przyjęcie K'</em>.";
    out += "</li>";
    out += "<li><strong>Rozpoznanie przy przyjęciu:</strong> Odczytaj chorobę z koperty (zakładka ICD-10) i wklej/wpisz.</li>";
    out += "<li><strong>Uzasadnienie (Powód przyjęcia):</strong> ";
    if (zabieg === "endoskopia") out += "Wpisz: <em>'do kolono-/gastroskopii/ecpw...'</em> (w przypadku endoskopii należy napisać powód przyjęcia!)";
    else if (zabieg === "ostry") out += "Wpisz: <em>'konieczne leczenie szpitalne'</em>";
    else out += "Wpisz: <em>'do zabiegu operacyjnego'</em>";
    out += "</li>";
    if (zabieg === "przepuklina") {
        out += "<li><strong>Skróty do przepuklin:</strong> HID (pachw. pr.), HIS (pachw. lewa), HIB (obustr.), HU (pępkowa), HV (brzuszna).</li>";
    } else if (zabieg === "rak" || zabieg === "jelito") {
        out += "<li><strong>Skróty onkologiczne:</strong> CA (rak), Recti (prostnica), Sigmoidei (esica), Ceci (kątnica).</li>";
    }
    out += "</ul>";
    out += "</div>";

    out += "<div class='guide-step'>";
    out += "<h3>3️⃣ Zleć Badania i Konsultacje w systemie</h3>";
    out += "<ul>";
    out += "<li>Zleć gotowiec: <strong>chirurgia planówka do zabiegu</strong></li>";
    if (tarczyca) out += "<li><strong class='highlight-red'>Choroby tarczycy:</strong> Dopisz TSH, ft3, ft4 do badań!</li>";
    if (cukrzyca) out += "<li><strong class='highlight-red'>Cukrzyca:</strong> Wpisz <strong>DPC</strong> w polu badań/konsultacji!</li>";
    if (zabieg === "cholecystektomia") out += "<li><strong class='highlight-red'>Cholecystektomia:</strong> Zleć konsultację <strong>Dietetyka</strong>.</li>";
    
    if (zabieg === "endoskopia") {
        out += "<li><strong>Grupa krwi:</strong> <span class='highlight-red'>NIE ZLECAJ grupy krwi na kolonoskopię/gastroskopię.</span></li>";
    } else {
        if (grupa) {
            out += "<li><strong>Grupa krwi:</strong> Zaznacz pole 'wszystkie' w badaniach i wpisz w uwagach: <strong>odpis z dn. XX.YY.ZZZZ</strong></li>";
        } else {
            out += "<li><strong>Grupa krwi:</strong> Brak potwierdzonego wyniku -> Zleć pobranie!</li>";
        }
        out += "<li>Wydrukuj formularz 'Grupa krwi' z zakładki 'epikryza'.</li>";
    }
    out += "</ul>";
    out += "</div>";

    out += "<div class='guide-step'>";
    out += "<h3>4️⃣ Zlecenia Jednorazowe (w systemie i na karcie papierowej)</h3>";
    out += "<ul>";
    if (cisnienie) {
        out += "<li><strong class='highlight-red'>SBP >180:</strong> Zleć <strong>Captopril 12,5/25mg s.l.</strong><br>";
        out += "-> Wpisz na karcie godzinę pomiaru i wynik (np. 180/110).<br>";
        out += "-> Podbij się za osobą podającą lek i wpisz godz. podania!</li>";
    }
    if (zabieg === "endoskopia") {
        out += "<li><strong>Kolonoskopia:</strong> Zleć <strong>Eziclen p.o. 15:00 i 20:00</strong> (na 2 osobnych kratkach).</li>";
    } else if (zabieg === "jelito") {
        out += "<li><strong>Chirurgia grubego (Hemikolektomia, Resekcja):</strong><br>";
        out += " - Eziclen p.o. 15:00 i 20:00<br>";
        out += " - Biofazolin 2,0g i.v. oraz Metronidazol 500mg i.v. na blok operacyjny.</li>";
    } else if (zabieg === "prokto") {
        out += "<li><strong>Zabieg proktologiczny:</strong> Zleć <strong>lewatywę</strong> jednorazowo.</li>";
    } else {
        out += "<li>Zleć profilaktykę antybiotykową/płyny wedle uznania/wymagań operacji.</li>";
    }
    out += "</ul>";
    out += "</div>";

    out += "<div class='guide-step'>";
    out += "<h3>5️⃣ Karta Leków Stałych (Tabela A3)</h3>";
    out += "<ul>";
    out += "<li><strong class='highlight-red'>Czego NIE wpisujemy:</strong> leków p/krzepliwych pacjenta, p/płytkowych, insuliny, p/cukrzycowych, wziewów, witamin i suplementów (w tym żelaza).</li>";
    if (poranny) {
        out += "<li><strong class='highlight-red'>Pacjent zażył poranny lek!</strong> Zaznacz <strong>'Ø'</strong> przy dawce na 8:00, aby pielęgniarka nie podała drugi raz!</li>";
    }
    if (caprini) {
        out += "<li><strong class='highlight-red'>Caprini >= 3 pkt:</strong> Zleć <strong>Neoparin 0,4ml s.c. 0-0-1 20:00</strong>.</li>";
    }
    out += "<li><em>Ściąga rozpisywania godzin:</em><br> p.o. 1-1-1 (8-14-18) <br> i.v. 1-1-1 (6-14-22) lub 1-1-1-1 (6-12-18-24).</li>";
    out += "</ul>";
    out += "</div>";

    out += "<div class='guide-step'>";
    out += "<h3>6️⃣ Dokumenty z Koperty (Wyciągnij)</h3>";
    out += "<ul>";
    out += "<li>Karta zleceń jednorazowych</li>";
    out += "<li>Karta badań i konsultacji</li>";
    out += "<li>Karta zleceń stałych (tabela A3)</li>";
    out += "<li>Kwalifikacja stanu odżywienia NRS</li>";
    out += "<li>Kwalifikacja ryzyka zakażenia</li>";
    out += "</ul>";
    out += "</div>";

    out += "<div class='guide-step'>";
    out += "<h3>7️⃣ Wydruki z systemu (Epikryza -> Wydruki -> Kod 360)</h3>";
    out += "<ul>";
    
    if (zabieg === "endoskopia" || zabieg === "bezzabiegowe") {
        out += "<li>Skala Caprini</li>";
    } else {
        out += "<li>Kwalifikacja do zabiegu (zabiegi operacyjne, port, ECPW, balon)</li>";
    }
    if (wiek) {
        out += "<li>Skala oceny geriatrycznej (dla pacjentów > 60 r.ż.)</li>";
    }
    out += "<li><strong>Karta badania przedmiotowego</strong> -> Wydrukuj i podbij.</li>";
    
    if (zabieg === "endoskopia") {
        out += "<li><strong class='highlight-red'>2x Odpowiednia zgoda</strong> (kolo/gastro, ECPW).<br>";
        out += "-> <strong>OBOWIĄZKOWO</strong> na wydruku zgody musi być wpisany powód badania!<br>";
        out += "-> Wypełnić ankietę z pacjentem w każdej ze zgód.</li>";
    } else {
        out += "<li>Odpowiednie zgody operacyjne i ankieta znieczuleniowa.</li>";
    }
    
    out += "</ul>";
    out += "</div>";
    
    out += "<div style='font-weight: bold; font-size: 1.1em; color: #e74c3c; padding: 10px; text-align: center; border: 2px dashed #e74c3c;'>W razie wątpliwości - dzwonić po pomoc 'dużego' lekarza (283)</div>";

    let guideBox = document.getElementById("dynamic-guide");
    if(guideBox) guideBox.innerHTML = out;
}
"""
        new_html = top_half + new_script + "\n</script>\n</body>"
        with open("index.html", "w") as f:
            f.write(new_html)
        print("Updated index.html logic successfully")


# Zaktualizowanie samego markdowna (dodanie nowych checklist)
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

<label><input type="checkbox" id="q_cukrzyca" onchange="updateGuide()"> Pacjent ma cukrzycę (DPC)</label>
<label><input type="checkbox" id="q_tarczyca" onchange="updateGuide()"> Pacjent choruje na tarczycę (TSH, ft3, ft4)</label>
<label><input type="checkbox" id="q_cisnienie" onchange="updateGuide()"> Nadciśnienie na Izbie Przyjęć (SBP > 180, ew. > 170)</label>
<label><input type="checkbox" id="q_grupa" onchange="updateGuide()"> Posiada POTWIERDZONĄ grupę krwi w systemie/na papierze</label>
<label><input type="checkbox" id="q_poranny" onchange="updateGuide()"> Zażył rano lek stały z listy (Ø o 8:00)</label>
<label><input type="checkbox" id="q_wiek" onchange="updateGuide()"> Wiek pacjenta > 60 r.ż. (Ocena geriatryczna)</label>
<label><input type="checkbox" id="q_caprini" onchange="updateGuide()"> Skala Caprini &#8805; 3 punkty (Neoparin)</label>

<div style="margin-top: 15px;">
<div style="font-weight: 500; margin-bottom: 5px;">Planowany zabieg:</div>
<select id="q_zabieg" onchange="updateGuide()">
<option value="inny">Inny (standardowy)</option>
<option value="endoskopia">Kolonoskopia / Gastroskopia</option>
<option value="cholecystektomia">Cholecystektomia</option>
<option value="jelito">Zabieg na jelicie grubym (np. Hemikolektomia, Resekcja)</option>
<option value="przepuklina">Przepuklina (np. pachwinowa)</option>
<option value="zylaki">Żylaki kończyn</option>
<option value="rak">Rak (CA)</option>
<option value="prokto">Zabieg proktologiczny drobny (lewatywa)</option>
<option value="ostry">Ostre przyjęcie (bez planu / na ostro)</option>
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
