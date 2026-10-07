# <svg class="ikona-stazu" viewBox="0 0 24 24"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/><polyline points="10 9 9 9 8 9"/></svg> Oprowadzacz po przyjęciu (Chirurgia)

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
