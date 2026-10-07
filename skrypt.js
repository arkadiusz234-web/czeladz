function wygenerujSpisStazy() {
  var glownyFolderNazwa = "Czeladź staż";
  var foldery = DriveApp.getFoldersByName(glownyFolderNazwa);
  
  if (!foldery.hasNext()) {
    Logger.log("Nie znaleziono głównego folderu!");
    return;
  }
  var glownyFolder = foldery.next();
  
  var markdown = "# Spis wszystkich stazy\n\n";
  markdown += "[Otworz glowny folder Czeladz staz na Dysku Google](" + glownyFolder.getUrl() + ")\n\n---\n\n";
  
  var podfoldery = glownyFolder.getFolders();
  var listaStazy = [];
  
  while (podfoldery.hasNext()) {
    var sub = podfoldery.next();
    listaStazy.push({
      nazwa: sub.getName(),
      url: sub.getUrl(),
      folder: sub
    });
  }
  
  // Sortowanie alfabetyczne
  listaStazy.sort(function(a, b) {
    return a.nazwa.localeCompare(b.nazwa);
  });
  
  for (var i = 0; i < listaStazy.length; i++) {
    var element = listaStazy[i];
    markdown += "### [" + element.nazwa + "](" + element.url + ")\n";
    
    // Pobiera dokumenty Google Docs (notatki) z folderu
    var pliki = element.folder.getFilesByType(MimeType.GOOGLE_DOCS);
    while (pliki.hasNext()) {
      var plik = pliki.next();
      markdown += "* [" + plik.getName() + "](" + plik.getUrl() + ")\n";
    }
    markdown += "\n";
  }
  
  var nazwaPliku = "spis_stazy.md";
  var starePliki = glownyFolder.getFilesByName(nazwaPliku);
  while (starePliki.hasNext()) {
    starePliki.next().setTrashed(true);
  }
  
  glownyFolder.createFile(nazwaPliku, markdown, MimeType.PLAIN_TEXT);
  Logger.log("Gotowe! Wygenerowano nowy plik spis_stazy.md");
}
