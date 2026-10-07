# Załączniki i Folder Google Drive

Poniżej znajduje się przykład, jak możesz wyświetlić całą zawartość folderu z Google Drive, tak aby użytkownicy mogli z niego pobierać pliki. Możesz również dodać ręczne, eleganckie przyciski do najważniejszych plików.

---

### 🗂️ Podgląd całego folderu
Aby to zadziałało, upewnij się, że Twój folder na Google Drive ma włączoną opcję udostępniania **"Każda osoba mająca link może przeglądać"**.

*(Zastąp `1A2B3C4D5E6F_przykladoweID` identyfikatorem swojego folderu. Znajdziesz go w pasku adresu, wchodząc do folderu na Dysku Google).*

<iframe src="https://drive.google.com/embeddedfolderview?id=1A2B3C4D5E6F_przykladoweID#list" width="100%" height="500" frameborder="0" style="border: 1px solid #333; border-radius: 8px;"></iframe>

<div style="margin-top: 20px; margin-bottom: 40px;">
  <a href="https://drive.google.com/drive/folders/1A2B3C4D5E6F_przykladoweID?usp=sharing" target="_blank" style="background-color: #4DBA87; color: #121212; padding: 10px 20px; text-decoration: none; border-radius: 4px; font-weight: bold; font-family: 'Merriweather', serif;">
    🔗 Otwórz ten folder bezpośrednio w Google Drive
  </a>
</div>

---

### 📎 Pojedyncze załączniki do pobrania
Jeśli wolisz ręcznie wstawiać linki do najważniejszych plików (np. PDFów lub dokumentów Word), użyj tego formatowania:

<div style="display: flex; flex-direction: column; gap: 15px;">
  <!-- Przykład przycisku dla pliku 1 -->
  <a href="https://drive.google.com/uc?export=download&id=ID_TWOJEGO_PLIKU_1" style="display: block; background-color: #1e1e1e; color: #fff; padding: 15px; text-decoration: none; border: 1px solid #4DBA87; border-left: 5px solid #4DBA87; border-radius: 4px;">
    <strong>📄 Formularz_zgloszeniowy.pdf</strong><br>
    <span style="font-size: 0.85em; color: #aaa;">Kliknij, aby pobrać na dysk (PDF, 2MB)</span>
  </a>

  <!-- Przykład przycisku dla pliku 2 -->
  <a href="https://drive.google.com/uc?export=download&id=ID_TWOJEGO_PLIKU_2" style="display: block; background-color: #1e1e1e; color: #fff; padding: 15px; text-decoration: none; border: 1px solid #4DBA87; border-left: 5px solid #4DBA87; border-radius: 4px;">
    <strong>📝 Wzor_umowy.docx</strong><br>
    <span style="font-size: 0.85em; color: #aaa;">Kliknij, aby pobrać na dysk (Word, 500KB)</span>
  </a>
</div>
