import os

# 1. Update statusy_chirurgia.md
if os.path.exists("statusy_chirurgia.md"):
    with open("statusy_chirurgia.md", "r") as f:
        content = f.read()
    # Remove the script block
    script_start = content.find("<!-- Użycie zewnętrznej")
    if script_start != -1:
        content = content[:script_start]
        with open("statusy_chirurgia.md", "w") as f:
            f.write(content)
        print("Removed script from statusy_chirurgia.md")

# 2. Update kalkulator_bmi.md
if os.path.exists("kalkulator_bmi.md"):
    with open("kalkulator_bmi.md", "r") as f:
        content = f.read()
    script_start = content.find("<script>")
    if script_start != -1:
        content = content[:script_start]
        with open("kalkulator_bmi.md", "w") as f:
            f.write(content)
        print("Removed script from kalkulator_bmi.md")

# 3. Update index.html
js_logic = """
  <!-- Zewnętrzne biblioteki do narzędzi -->
  <script src="https://cdnjs.cloudflare.com/ajax/libs/html2pdf.js/0.10.1/html2pdf.bundle.min.js"></script>

  <!-- Globalna logika dla narzędzi ze stron markdown -->
  <script>
    // --- Kalkulator BMI ---
    window.obliczBMI = function() {
      let w = document.getElementById('waga').value.replace(',', '.');
      let h = document.getElementById('wzrost').value.replace(',', '.');
      if(!w || !h) {
        document.getElementById('wynik-box').style.display = 'none';
        return;
      }
      w = parseFloat(w);
      h = parseFloat(h);
      if(isNaN(w) || isNaN(h) || w <= 0 || h <= 0) {
        document.getElementById('wynik-box').style.display = 'none';
        return;
      }

      if(h > 3) h = h / 100;

      let bmi = w / (h * h);
      let wynikBox = document.getElementById('wynik-box');
      let wynikLiczba = document.getElementById('wynik-liczba');
      let wynikTekst = document.getElementById('wynik-tekst');

      wynikBox.style.display = 'block';
      wynikLiczba.innerText = "BMI: " + bmi.toFixed(2);

      let kol = "#000";
      let txt = "";
      if(bmi < 18.5) {
        txt = "Niedowaga"; kol = "#3498db"; 
      } else if(bmi >= 18.5 && bmi < 25) {
        txt = "Waga prawidłowa"; kol = "#2ecc71";
      } else if(bmi >= 25 && bmi < 30) {
        txt = "Nadwaga"; kol = "#f1c40f";
      } else if(bmi >= 30 && bmi < 35) {
        txt = "Otyłość I stopnia"; kol = "#e67e22";
      } else if(bmi >= 35 && bmi < 40) {
        txt = "Otyłość II stopnia"; kol = "#e74c3c";
      } else {
        txt = "Otyłość skrajna (III stopnia)"; kol = "#c0392b";
      }

      wynikBox.style.backgroundColor = kol;
      wynikBox.style.color = "#fff";
      wynikTekst.innerText = txt;
    };

    // --- Statusy Chirurgia ---
    function val(id) {
        let el = document.getElementById(id);
        return el ? el.value : "";
    }
    function isChecked(id) {
        let el = document.getElementById(id);
        return el ? el.checked : false;
    }
    function radio(name) {
        const el = document.querySelector(`input[name="${name}"]:checked`);
        if(!el) return "";
        const genderEl = document.querySelector(`input[name="gender"]:checked`);
        const gender = genderEl ? genderEl.value : "M";
        if(gender === "K" && el.getAttribute("data-f")) {
            return el.getAttribute("data-f");
        }
        return el.value;
    }

    window.generujStatus = function() {
        let out = [];
        const date = new Date().toLocaleDateString('pl-PL');
        const time = new Date().toLocaleTimeString('pl-PL', {hour: '2-digit', minute:'2-digit'});
        
        let pacjent = val("patient_name") || "__________________";
        out.push(`STATUS LEKARSKI - CHIRURGIA`);
        out.push(`Data: ${date} ${time}`);
        out.push(`Pacjent: ${pacjent}`);
        out.push(``);
        
        if(isChecked("inc_doba")) {
            let doba = `Doba hospitalizacji: ${val("doba_hosp")} | Doba po zabiegu: ${val("doba_zabieg")}`;
            if(val("nazwa_zabiegu")) doba += ` (zabieg: ${val("nazwa_zabiegu")})`;
            out.push(doba);
        }
        
        if(isChecked("inc_stan_og")) out.push(`Stan ogólny: ${radio("stan_ogolny")}`);
        if(isChecked("inc_swiadomosc")) out.push(`Świadomość: ${radio("swiadomosc")}`);
        
        if(isChecked("inc_kraz_odd")) {
            let ko = `Układ krążenia i oddechowy: ${radio("kraz_odd")}`;
            if(val("tlenoterapia")) ko += ` (tlenoterapia: ${val("tlenoterapia")})`;
            out.push(ko);
        }
        
        if(isChecked("inc_parametry")) {
            let param = `Parametry: RR: ${val("param_rr")} mmHg | HR: ${val("param_hr")} /min | SpO2: ${val("param_spo2")}% | Temp: ${val("param_temp")} °C`;
            if(val("param_diureza")) param += ` | Diureza: ${val("param_diureza")} ml`;
            out.push(param);
        }
        
        if(isChecked("inc_dolegliwosci")) {
            let d = `Dolegliwości: ${radio("dolegliwosci")}`;
            if(radio("dolegliwosci") === "ból operowanej okolicy") d += ` (NRS: ${val("nrs_bol")})`;
            out.push(d);
        }
        
        if(isChecked("inc_dieta")) out.push(`Dieta: ${radio("dieta")}`);
        
        if(isChecked("inc_pp")) {
            out.push(`Przewód pokarmowy: ${radio("gazy")} | ${radio("stolec")}`);
        }
        
        out.push(``);
        out.push(`BADANIE PRZEDMIOTOWE:`);
        if(isChecked("inc_klatka")) out.push(`- Klatka piersiowa: ${radio("klatka")}`);
        if(isChecked("inc_powloki")) out.push(`- Powłoki brzuszne: ${radio("powloki")}`);
        if(isChecked("inc_palpacja")) out.push(`- Palpacja brzucha: ${radio("palpacja1")} | ${radio("palpacja2")}`);
        if(isChecked("inc_otrzewna")) out.push(`- Objawy otrzewnowe: ${radio("otrzewna")}`);
        if(isChecked("inc_perystaltyka")) out.push(`- Perystaltyka: ${radio("perystaltyka")}`);
        
        out.push(``);
        out.push(`STAN MIEJSCOWY:`);
        if(isChecked("inc_rana")) {
            let r = `- Rana operacyjna: ${radio("rana")}`;
            if(radio("rana") === "wyciek treści") {
                let tr = [];
                if(isChecked("rana_tre_surowicza")) tr.push("surowiczej");
                if(isChecked("rana_tre_krwista")) tr.push("krwistej");
                if(isChecked("rana_tre_ropna")) tr.push("ropnej");
                if(tr.length) r += ` ${tr.join(", ")}`;
            }
            let dodatki = [];
            if(isChecked("rana_rozejscie")) dodatki.push("rozejście brzegów");
            if(isChecked("rana_krwiak")) dodatki.push("krwiak");
            if(isChecked("rana_obrzek")) dodatki.push("obrzęk i zaczerwienienie");
            if(dodatki.length) r += ` | ` + dodatki.join(", ");
            out.push(r);
        }
        if(isChecked("inc_dren")) {
            let dr = `- Dren: ${radio("dren")}`;
            if(radio("dren") === "obecny") {
                let tr2 = [];
                if(isChecked("dren_tre_sur")) tr2.push("surowicza");
                if(isChecked("dren_tre_krw")) tr2.push("krwista");
                if(isChecked("dren_tre_zol")) tr2.push("żółciowa");
                if(isChecked("dren_tre_jel")) tr2.push("jelitowa");
                if(isChecked("dren_tre_rop")) tr2.push("ropna");
                if(tr2.length) dr += ` ` + tr2.join(", ");
                if(val("dren_obj")) dr += ` | objętość: ${val("dren_obj")} ml`;
            }
            out.push(dr);
        }
        if(isChecked("inc_naczynie")) out.push(`- Dostęp naczyniowy: ${radio("naczynie")} | ${radio("zapalenie")}`);
        if(isChecked("inc_mocz")) {
            let m = `- Pęcherz moczowy: ${radio("mocz")}`;
            if(radio("mocz") === "cewnik Foleya") m += ` (${radio("mocz_cecha")})`;
            out.push(m);
        }
        
        out.push(``);
        out.push(`PLAN I ZALECENIA:`);
        if(isChecked("inc_leczenie")) {
            let l = `- Leczenie: ${radio("leczenie")}`;
            if(radio("leczenie") === "modyfikacja zleceń" && val("mod_zlec")) l += ` ${val("mod_zlec")}`;
            out.push(l);
        }
        if(isChecked("inc_zywienie")) out.push(`- Żywienie: ${radio("zywienie")}`);
        if(isChecked("inc_uruchamianie")) out.push(`- Uruchamianie: ${radio("uruchamianie")}`);
        if(isChecked("inc_procedury")) {
            let pr = [];
            if(isChecked("proc_toaleta")) pr.push("toaleta rany i zmiana opatrunku");
            if(isChecked("proc_dren")) pr.push("usunięcie drenu");
            if(isChecked("proc_foley")) pr.push("usunięcie cewnika Foleya");
            if(isChecked("proc_szwy")) pr.push("usunięcie szwów");
            if(pr.length) out.push(`- Procedury: ${pr.join(", ")}`);
        }
        if(isChecked("inc_diagnostyka")) {
            let di = [];
            if(isChecked("diag_lab")) di.push("kontrola badań laboratoryjnych");
            if(isChecked("diag_obraz")) {
                let txt = "badania obrazowe";
                if(val("diag_obraz_txt")) txt += ` (${val("diag_obraz_txt")})`;
                di.push(txt);
            }
            if(di.length) out.push(`- Diagnostyka: ${di.join(", ")}`);
        }
        if(isChecked("inc_decyzja")) {
            let dec = `- Decyzja: ${radio("decyzja")}`;
            if(radio("decyzja") === "kwalifikacja do wypisu" && val("wypis_txt")) dec += ` (${val("wypis_txt")})`;
            out.push(dec);
        }
        
        if(val("dodatkowe_info")) {
            out.push(``);
            out.push(`Uwagi dodatkowe: ${val("dodatkowe_info")}`);
        }
        
        const finalStatus = out.join("\\n");
        
        const textarea = document.getElementById("output-status");
        if(textarea) textarea.value = finalStatus;
        
        navigator.clipboard.writeText(finalStatus).then(() => {
            alert("Status wygenerowany i skopiowany do schowka!");
        }).catch(err => {
            if(textarea) {
                textarea.select();
                document.execCommand('copy');
            }
            alert("Status wygenerowany i skopiowany do schowka!");
        });
        
        const pdfContainer = document.createElement("div");
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
            }).from(pdfContainer).save().then(() => {
                let form = document.getElementById("chirurgia-form");
                if(form) form.reset();
            });
        } else {
            alert("Błąd: biblioteka html2pdf nie załadowała się prawidłowo.");
        }
    };
  </script>
</body>
"""

if os.path.exists("index.html"):
    with open("index.html", "r") as f:
        html = f.read()
    if "window.generujStatus =" not in html:
        html = html.replace("</body>", js_logic)
        with open("index.html", "w") as f:
            f.write(html)
        print("Injected JS into index.html")
