# <svg class="ikona-stazu" viewBox="0 0 24 24"><path d="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/></svg> Kalkulator BMI

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

