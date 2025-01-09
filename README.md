# Programmieren_lernen_fuer_Schueler
Eine Anleitung für Schueler der Unterstufe um einen Einstieg ins Programmieren zu finden

## Die erste Aufgabe

## Betriebssystem
Linux
### Programmiersprache
Python
### IDE
VS Code
CoPilot
### Versionsverwaltung
#### Github
Wir verwalten unsere Applikation mit git bzw. dem Service `github.com`, auf dem wir unseren Code auch aufbewahren können.
#### git
Führe auf der Kommandozeile folgendes aus:<br />
<code>sudo apt install git</code>
Gehe nun in das Verzeichnis mit unserer Datei.
Dort müssen wir git erst klar machen, dass wir hier ein `git` Repository (=Aufbewahrungsort) anlegen wollen.
<code>git init</code>
In `git` gibt es sog. Zweige, bzw. Branches. Mit dieser können wir verschiedene Features verwalten. Das interessiert uns erstmal nicht. Dennoch gibt es eine Philosophie, der wir folgen wollen. Der Hauptzweig heißt _main_. Um den Hauptbranch diesen Namen zu geben, schreiben wir:
<code>git config --global init.defaultBranch main</code>
Nun müssen wir noch auf diesen Zweig wechseln
<code>git branch -m main</code>
Mit
<code>git status</code>
kannst Du nun überprüfen ob alles stimmt. Du solltest einen Hinweis _On branch main_ bekommen, welcher bedeutet dass Du auf dem _main_ Zweig bist. und einen Hinweis _Untracked Files_, also nicht verfolgte oder versionierte Dateien. Hier sollte in roter Schrift Deine Programmdatei auftauchen. Nicht verfolgt bedeutet, dass wir unsere Datei noch nicht der Versionsverwaltung zugeführt haben. Das machen wir jetzt mit:
<code>git add .</code>
Diese Befehl fügt alle Dateien, die noch nicht versionisiert sind, der Versionsverwaltung hinzu. In diesem Fall also nur unser Programm <code>Multiplizieren.py</code>.
Schau doch selber mal mit <code>git status</code> was jetzt anders ist. Die ist vielleicht auch die Zeile `No commits yet` aufgefallen. Darum kümmenr wir uns jetzt.
Damit vom aktuellen Stand unseres Programms eine Version erstellt wird, führen wir einen sog. `commit` aus. Das Wort ist schwer zu übersetzen in unseren Kontext. Es könnte am ehesten mit Versionieren oder Abspeichern übersetzt werden. Führe dazu folgende Zeile aus:
<code>git commit -m "Mein erster Stand"</code>


Dokumentation
Readme.md
siehe https://docs.github.com/de/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax
