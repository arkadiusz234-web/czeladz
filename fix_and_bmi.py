import os
import re

# Fix statusy_chirurgia.md
if os.path.exists("statusy_chirurgia.md"):
    with open("statusy_chirurgia.md", "r") as f:
        content = f.read()
    
    # 1. Remove 4-space indentations
    content = content.replace("    <", "<")
    content = content.replace("        <", "<")
    # 2. Remove blank lines inside the HTML
    content = re.sub(r'</div>\n\n<div class="status-row">', '</div>\n<div class="status-row">', content)
    content = re.sub(r'</div>\n\n<h4', '</div>\n<h4', content)
    content = re.sub(r'</h4>\n\n<div', '</h4>\n<div', content)
    
    with open("statusy_chirurgia.md", "w") as f:
        f.write(content)
    print("Fixed statusy_chirurgia.md")

# Create kalkulator_bmi.md
bmi_content = """# <svg class="ikona-stazu" viewBox="0 0 24 24"><path d="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/></svg> Kalkulator BMI

<style>
.tool-container {
background: var(--background);
padding: 25px;
border-radius: 8px;
border: 1px solid var(--borderColor);
margin-top: 20px;
max-width: 400px;
}
.tool-row {
margin-bottom: 20px;
}
.tool-row label {
display: block;
font-weight: bold;
margin-bottom: 5px;
}
.tool-input {
width: 100%;
padding: 10px;
font-size: 1.1em;
border: 1px solid var(--borderColor);
border-radius: 5px;
background: var(--background);
color: var(--textColor);
}
.bmi-result {
margin-top: 20px;
font-size: 1.5em;
font-weight: bold;
text-align: center;
padding: 15px;
border-radius: 8px;
background: #f0f0f0;
color: #000;
display: none;
}
.bmi-text {
font-size: 0.8em;
display: block;
margin-top: 5px;
}
</style>

<div class="tool-container">
<div class="tool-row">
<label>Wzrost (cm lub m):</label>
<input type="text" id="wzrost" class="tool-input" placeholder="np. 175 lub 1.75" oninput="obliczBMI()">
</div>
<div class="tool-row">
<label>Waga (kg):</label>
<input type="number" id="waga" class="tool-input" placeholder="np. 70" oninput="obliczBMI()">
</div>
<div id="wynik-box" class="bmi-result">
<span id="wynik-liczba">--</span>
<span id="wynik-tekst" class="bmi-text">--</span>
</div>
</div>

<script>
function obliczBMI() {
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

// Jeśli wzrost < 3, traktujemy to jako metry (np. 1.75). Jeśli > 3, to cm.
if(h > 3) {
h = h / 100;
}

let bmi = w / (h * h);
let wynikBox = document.getElementById('wynik-box');
let wynikLiczba = document.getElementById('wynik-liczba');
let wynikTekst = document.getElementById('wynik-tekst');

wynikBox.style.display = 'block';
wynikLiczba.innerText = "BMI: " + bmi.toFixed(2);

let kol = "#000";
let txt = "";
if(bmi < 18.5) {
txt = "Niedowaga";
kol = "#3498db"; // niebieski
} else if(bmi >= 18.5 && bmi < 25) {
txt = "Waga prawidłowa";
kol = "#2ecc71"; // zielony
} else if(bmi >= 25 && bmi < 30) {
txt = "Nadwaga";
kol = "#f1c40f"; // zolty
} else if(bmi >= 30 && bmi < 35) {
txt = "Otyłość I stopnia";
kol = "#e67e22"; // pomarancz
} else if(bmi >= 35 && bmi < 40) {
txt = "Otyłość II stopnia";
kol = "#e74c3c"; // czerwony
} else {
txt = "Otyłość skrajna (III stopnia)";
kol = "#c0392b"; // ciemny czerwony
}

wynikBox.style.backgroundColor = kol;
wynikBox.style.color = "#fff";
wynikTekst.innerText = txt;
}
</script>
"""

with open("kalkulator_bmi.md", "w") as f:
    f.write(bmi_content)
print("Created kalkulator_bmi.md")

# Add BMI tool to _sidebar.md
if os.path.exists("_sidebar.md"):
    with open("_sidebar.md", "r") as f:
        sidebar = f.read()
    
    if "Kalkulator BMI" not in sidebar:
        sidebar = sidebar.replace("* [Statusy (Chirurgia)](statusy_chirurgia.md)\n", "* [Statusy (Chirurgia)](statusy_chirurgia.md)\n  * [Kalkulator BMI](kalkulator_bmi.md)\n")
        with open("_sidebar.md", "w") as f:
            f.write(sidebar)
        print("Updated _sidebar.md")
