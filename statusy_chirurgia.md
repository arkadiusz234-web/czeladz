# <svg class="ikona-stazu" viewBox="0 0 24 24"><path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"/></svg> Narzędzia - Statusy (Chirurgia)

<style>
.status-form {
font-size: 0.9em;
background: var(--background);
padding: 20px;
border-radius: 8px;
border: 1px solid var(--borderColor);
}
.status-row {
margin-bottom: 15px;
padding-bottom: 10px;
border-bottom: 1px dashed var(--borderColor);
}
.status-row:last-child {
border-bottom: none;
}
.status-row label {
cursor: pointer;
margin-right: 15px;
display: inline-flex;
align-items: center;
}
.status-row input[type="text"], .status-row input[type="number"] {
background: var(--background);
color: var(--textColor);
border: 1px solid var(--borderColor);
border-radius: 4px;
padding: 2px 5px;
width: 60px;
margin: 0 5px;
}
.status-row input.wide-text {
width: 200px;
}
.group-title {
font-weight: bold;
margin-bottom: 8px;
display: inline-block;
}
.btn-generate {
background: var(--textColor);
color: var(--background);
border: none;
padding: 12px 24px;
font-size: 1.1em;
font-weight: bold;
border-radius: 6px;
cursor: pointer;
margin-top: 20px;
width: 100%;
transition: opacity 0.2s;
}
.btn-generate:hover {
opacity: 0.8;
}
textarea#output-status {
width: 100%;
height: 300px;
margin-top: 20px;
background: var(--background);
color: var(--textColor);
border: 1px solid var(--borderColor);
border-radius: 8px;
padding: 15px;
font-family: monospace;
font-size: 0.95em;
resize: vertical;
}
</style>

<form class="status-form" id="chirurgia-form" onsubmit="return false;">
<div class="status-row">
<span class="group-title">Pacjent:</span>
<input type="text" id="patient_name" class="wide-text" placeholder="Imię i nazwisko">
<label><input type="radio" name="gender" value="M" checked> Mężczyzna</label>
<label><input type="radio" name="gender" value="K"> Kobieta</label>
</div>

<div class="status-row">
<label><input type="checkbox" id="inc_doba" checked> <span class="group-title">Doba hospitalizacji:</span></label>
<input type="number" id="doba_hosp" value="1">
| <span class="group-title">Doba po zabiegu:</span>
<input type="number" id="doba_zabieg" value="1">
<input type="text" id="nazwa_zabiegu" class="wide-text" placeholder="nazwa zabiegu">
</div>
<div class="status-row">
<label><input type="checkbox" id="inc_stan_og" checked> <span class="group-title">Stan ogólny:</span></label>
<label><input type="radio" name="stan_ogolny" value="dobry" checked> dobry</label>
<label><input type="radio" name="stan_ogolny" value="średni"> średni</label>
<label><input type="radio" name="stan_ogolny" value="ciężki"> ciężki</label>
</div>
<div class="status-row">
<label><input type="checkbox" id="inc_swiadomosc" checked> <span class="group-title">Świadomość:</span></label>
<label><input type="radio" name="swiadomosc" value="pełna, zorientowany" data-f="pełna, zorientowana" checked> pełna, zorientowany</label>
<label><input type="radio" name="swiadomosc" value="podsypiający" data-f="podsypiająca"> podsypiający</label>
<label><input type="radio" name="swiadomosc" value="nielogiczny" data-f="nielogiczna"> nielogiczny</label>
</div>
<div class="status-row">
<label><input type="checkbox" id="inc_kraz_odd" checked> <span class="group-title">Układ krążenia i oddechowy:</span></label>
<label><input type="radio" name="kraz_odd" value="wydolny" checked> wydolny</label>
<label><input type="radio" name="kraz_odd" value="niewydolny"> niewydolny</label>
(tlenoterapia: <input type="text" id="tlenoterapia" placeholder="brak">)
</div>
<div class="status-row">
<label><input type="checkbox" id="inc_parametry" checked> <span class="group-title">Parametry:</span></label>
RR: <input type="text" id="param_rr" value="120/80"> mmHg |
HR: <input type="text" id="param_hr" value="70"> /min |
SpO2: <input type="text" id="param_spo2" value="98"> % |
Temp: <input type="text" id="param_temp" value="36.6"> °C |
Diureza: <input type="text" id="param_diureza" placeholder="..."> ml
</div>
<div class="status-row">
<label><input type="checkbox" id="inc_dolegliwosci" checked> <span class="group-title">Dolegliwości:</span></label>
<label><input type="radio" name="dolegliwosci" value="neguje" checked> neguje</label>
<label><input type="radio" name="dolegliwosci" value="ból operowanej okolicy"> ból operowanej okolicy (NRS: <input type="number" id="nrs_bol" value="3" style="width:40px;">)</label>
<label><input type="radio" name="dolegliwosci" value="nudności"> nudności</label>
<label><input type="radio" name="dolegliwosci" value="wymioty"> wymioty</label>
<label><input type="radio" name="dolegliwosci" value="duszność"> duszność</label>
</div>
<div class="status-row">
<label><input type="checkbox" id="inc_dieta" checked> <span class="group-title">Dieta:</span></label>
<label><input type="radio" name="dieta" value="doustna, toleruje" checked> doustna, toleruje</label>
<label><input type="radio" name="dieta" value="ścisła"> ścisła</label>
<label><input type="radio" name="dieta" value="płynna"> płynna</label>
<label><input type="radio" name="dieta" value="nudności po posiłku"> nudności po posiłku</label>
</div>
<div class="status-row">
<label><input type="checkbox" id="inc_pp" checked> <span class="group-title">Przewód pokarmowy:</span></label>
<label><input type="radio" name="gazy" value="gazy (+)" checked> gazy (+)</label>
<label><input type="radio" name="gazy" value="gazy (-)"> gazy (-)</label> | 
<label><input type="radio" name="stolec" value="stolec (+)" checked> stolec (+)</label>
<label><input type="radio" name="stolec" value="stolec (-)"> stolec (-)</label>
</div>
<h4 style="margin-top: 15px;">Badanie przedmiotowe</h4>

<div class="status-row">
<label><input type="checkbox" id="inc_klatka" checked> <span class="group-title">Klatka piersiowa:</span></label>
<label><input type="radio" name="klatka" value="szmer pęcherzykowy prawidłowy, symetryczny" checked> szmer pęcherzykowy prawidłowy, symetryczny</label><br>
<label style="margin-left:25px;"><input type="radio" name="klatka" value="osłabiony"> osłabiony</label>
<label><input type="radio" name="klatka" value="świsty"> świsty</label>
<label><input type="radio" name="klatka" value="rzężenia"> rzężenia</label>
</div>
<div class="status-row">
<label><input type="checkbox" id="inc_powloki" checked> <span class="group-title">Powłoki brzuszne:</span></label>
<label><input type="radio" name="powloki" value="w poziomie" checked> w poziomie</label>
<label><input type="radio" name="powloki" value="wysklepione"> wysklepione</label>
<label><input type="radio" name="powloki" value="wzdęte"> wzdęte</label>
</div>
<div class="status-row">
<label><input type="checkbox" id="inc_palpacja" checked> <span class="group-title">Palpacja brzucha:</span></label>
<label><input type="radio" name="palpacja1" value="miękki" checked> miękki</label>
<label><input type="radio" name="palpacja1" value="wzmożone napięcie powłok"> wzmożone napięcie powłok</label>
<label><input type="radio" name="palpacja1" value="twardy"> twardy</label> | 
<label><input type="radio" name="palpacja2" value="niebolesny" checked> niebolesny</label>
<label><input type="radio" name="palpacja2" value="bolesny w rzucie rany"> bolesny w rzucie rany</label>
<label><input type="radio" name="palpacja2" value="bolesny rozlany"> bolesny rozlany</label>
</div>
<div class="status-row">
<label><input type="checkbox" id="inc_otrzewna" checked> <span class="group-title">Objawy otrzewnowe:</span></label>
<label><input type="radio" name="otrzewna" value="ujemne" checked> ujemne</label>
<label><input type="radio" name="otrzewna" value="Blumberg (+)"> Blumberg (+)</label>
<label><input type="radio" name="otrzewna" value="obrona mięśniowa (+)"> obrona mięśniowa (+)</label>
</div>
<div class="status-row">
<label><input type="checkbox" id="inc_perystaltyka" checked> <span class="group-title">Perystaltyka:</span></label>
<label><input type="radio" name="perystaltyka" value="obecna, prawidłowa" checked> obecna, prawidłowa</label>
<label><input type="radio" name="perystaltyka" value="osłabiona, leniwa"> osłabiona, leniwa</label>
<label><input type="radio" name="perystaltyka" value="brak (cisza w jamie brzusznej)"> brak</label>
</div>
<h4 style="margin-top: 15px;">Stan miejscowy</h4>
<div class="status-row">
<label><input type="checkbox" id="inc_rana" checked> <span class="group-title">Rana operacyjna:</span></label>
<label><input type="radio" name="rana" value="opatrunek czysty, suchy" checked> opatrunek czysty, suchy</label><br>
<label style="margin-left:25px;"><input type="radio" name="rana" value="wyciek treści"> wyciek treści:</label>
<label><input type="checkbox" id="rana_tre_surowicza"> surowiczej</label>
<label><input type="checkbox" id="rana_tre_krwista"> krwistej</label>
<label><input type="checkbox" id="rana_tre_ropna"> ropnej</label><br>
<label style="margin-left:25px;"><input type="checkbox" id="rana_rozejscie"> rozejście brzegów</label>
<label><input type="checkbox" id="rana_krwiak"> krwiak</label>
<label><input type="checkbox" id="rana_obrzek"> obrzęk i zaczerwienienie</label>
</div>
<div class="status-row">
<label><input type="checkbox" id="inc_dren" checked> <span class="group-title">Dren:</span></label>
<label><input type="radio" name="dren" value="brak" checked> brak</label>
<label><input type="radio" name="dren" value="obecny"> obecny, treść:</label>
<label><input type="checkbox" id="dren_tre_sur"> surowicza</label>
<label><input type="checkbox" id="dren_tre_krw"> krwista</label>
<label><input type="checkbox" id="dren_tre_zol"> żółciowa</label>
<label><input type="checkbox" id="dren_tre_jel"> jelitowa</label>
<label><input type="checkbox" id="dren_tre_rop"> ropna</label>
| objętość: <input type="text" id="dren_obj" placeholder="..."> ml
</div>
<div class="status-row">
<label><input type="checkbox" id="inc_naczynie" checked> <span class="group-title">Dostęp naczyniowy:</span></label>
<label><input type="radio" name="naczynie" value="wkłucie obwodowe" checked> wkłucie obwodowe</label>
<label><input type="radio" name="naczynie" value="C primitive"> C primitive</label> | 
<label><input type="radio" name="zapalenie" value="bez cech zapalenia" checked> bez cech zapalenia</label>
<label><input type="radio" name="zapalenie" value="odczyn zapalny"> odczyn zapalny</label>
</div>
<div class="status-row">
<label><input type="checkbox" id="inc_mocz" checked> <span class="group-title">Pęcherz moczowy:</span></label>
<label><input type="radio" name="mocz" value="mikcja samoistna" checked> mikcja samoistna</label>
<label><input type="radio" name="mocz" value="cewnik Foleya"> cewnik Foleya</label> 
(<label><input type="radio" name="mocz_cecha" value="mocz klarowny" checked> mocz klarowny</label> / 
<label><input type="radio" name="mocz_cecha" value="krwiomocz"> krwiomocz</label>)
</div>
<h4 style="margin-top: 15px;">Plan i zalecenia</h4>
<div class="status-row">
<label><input type="checkbox" id="inc_leczenie" checked> <span class="group-title">Leczenie:</span></label>
<label><input type="radio" name="leczenie" value="kontynuacja wg IKZL" checked> kontynuacja wg IKZL</label>
<label><input type="radio" name="leczenie" value="modyfikacja zleceń"> modyfikacja zleceń: <input type="text" id="mod_zlec" class="wide-text"></label>
</div>
<div class="status-row">
<label><input type="checkbox" id="inc_zywienie" checked> <span class="group-title">Żywienie:</span></label>
<label><input type="radio" name="zywienie" value="dieta lekkostrawna" checked> dieta lekkostrawna</label>
<label><input type="radio" name="zywienie" value="na czczo"> na czczo</label>
<label><input type="radio" name="zywienie" value="nawodnienie i.v."> nawodnienie i.v.</label>
<label><input type="radio" name="zywienie" value="włączenie płynów p.o."> włączenie płynów p.o.</label>
</div>
<div class="status-row">
<label><input type="checkbox" id="inc_uruchamianie" checked> <span class="group-title">Uruchamianie:</span></label>
<label><input type="radio" name="uruchamianie" value="pełne" checked> pełne</label>
<label><input type="radio" name="uruchamianie" value="reżim łóżkowy"> reżim łóżkowy</label>
<label><input type="radio" name="uruchamianie" value="siadanie"> siadanie</label>
<label><input type="radio" name="uruchamianie" value="pionizacja z asystą"> pionizacja z asystą</label>
</div>
<div class="status-row">
<label><input type="checkbox" id="inc_procedury" checked> <span class="group-title">Procedury:</span></label>
<label><input type="checkbox" id="proc_toaleta"> toaleta rany i zmiana opatrunku</label>
<label><input type="checkbox" id="proc_dren"> usunięcie drenu</label>
<label><input type="checkbox" id="proc_foley"> usunięcie cewnika Foleya</label>
<label><input type="checkbox" id="proc_szwy"> usunięcie szwów</label>
</div>
<div class="status-row">
<label><input type="checkbox" id="inc_diagnostyka" checked> <span class="group-title">Diagnostyka:</span></label>
<label><input type="checkbox" id="diag_lab"> kontrola badań laboratoryjnych</label>
<label><input type="checkbox" id="diag_obraz"> badania obrazowe:</label> <input type="text" id="diag_obraz_txt" class="wide-text">
</div>
<div class="status-row">
<label><input type="checkbox" id="inc_decyzja" checked> <span class="group-title">Decyzja:</span></label>
<label><input type="radio" name="decyzja" value="dalsza hospitalizacja" checked> dalsza hospitalizacja</label>
<label><input type="radio" name="decyzja" value="kwalifikacja do wypisu"> kwalifikacja do wypisu: <input type="text" id="wypis_txt" class="wide-text"></label>
</div>

<div class="status-row">
<span class="group-title">Dodatkowe informacje (uwagi):</span><br>
<input type="text" id="dodatkowe_info" style="width: 100%; padding: 5px;" placeholder="...">
</div>

<button type="button" class="btn-generate" onclick="generujStatus()">Generuj, Kopiuj i Pobierz PDF</button>
</form>

<textarea id="output-status" readonly placeholder="Tutaj pojawi się wygenerowany status..."></textarea>

