# Tiperly

Ein freundlicher Trainer fürs 10-Finger-Tippen. Die Web-App läuft in modernen Browsern, merkt sich deinen Lernstand und Darstellung (Hell-/Dunkelmodus) lokal auf dem Gerät und kann als Windows-Anwendung gestartet werden.

## Web-App

Öffne `index.html` direkt im Browser oder veröffentliche den Ordner auf einem statischen Webserver. Als installierbare/offlinefähige Web-App wird Tiperly über HTTPS (oder localhost) bereitgestellt; der Service Worker speichert die App-Dateien für die Offline-Nutzung.

## Windows-Programm

Voraussetzungen zum Bauen: Node.js 20 oder neuer und eine Internetverbindung für den erstmaligen Paketdownload.

```powershell
npm install
npm run start
npm run build:exe
```

Die portable Windows-Datei liegt danach in `release/Tiperly-1.0.0-Windows-portabel.exe`. Zum Erzeugen eines klassischen Installers kann `npm run build:installer` verwendet werden.

## Daten und Privatsphäre

Übungsfortschritt und Einstellungen werden lokal im Browser/App-Profil gespeichert. Es gibt keine Konten, Analytics oder Cloud-Synchronisierung. Der Name „Tiperly“ ist der Produktname dieses Prototyps; Marken- und Domainverfügbarkeit wurden nicht geprüft.
