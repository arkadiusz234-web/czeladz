# <svg class="ikona-stazu" viewBox="0 0 24 24"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/><polyline points="10 9 9 9 8 9"/></svg> Oprowadzacz po przyjęciu (Chirurgia)

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

