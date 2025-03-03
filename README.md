# Brute Force MD5 Hash Reversing

![Projektstatus](https://img.shields.io/badge/status-finished-green)
![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)

## Projektübersicht

Dieses Projekt zielt darauf ab, ein Python-Tool zu entwickeln, das mittels Brute-Force-Methodik MD5-Hashes zurück in ihre ursprünglichen Schlüsselwörter umwandelt. Dies ist besonders nützlich, wenn die ursprünglichen Schlüsselwörter verloren gegangen sind und nur die MD5-Hashes vorliegen.

## Funktionen

- **Benutzerabfrage**: Erfassung des MD5-Hashes, der Länge des Schlüsselworts und der Information, ob Gross- und Kleinbuchstaben verwendet wurden.
- **Brute-Force-Algorithmus**: Generierung aller möglichen Buchstabenkombinationen basierend auf den Benutzereingaben und Vergleich der MD5-Hashes, um das ursprüngliche Schlüsselwort zu identifizieren.

## Installation

1. **Repository klonen**:

    ```bash
    git clone https://github.com/nick-sohl/teko_brute_force.git
    cd teko_brute_force
    ```

## Nutzung

1. **Programm starten**:

    ```bash
    python reverse_hash.py
    ```

2. **Eingaben tätigen**:

    - MD5-Hash: `eingegebener_md5_hash`
    - Länge des Schlüsselworts: `4`
    - Enthält das Schlüsselwort Grossbuchstaben? (ja/nein): `ja`

3. **Ergebnis**:

    Das Programm wird alle möglichen Kombinationen generieren und den passenden MD5-Hash finden, um das ursprüngliche Schlüsselwort anzuzeigen.

## Dokumentation

Eine ausführliche Dokumentation des Projekts, einschliesslich theoretischer Hintergründe und Implementierungsdetails, findest du in der Datei [Dokumentation Md5](./docs/).

## Beitrag leisten

Beiträge zum Projekt sind willkommen! Bitte folge diesen Schritten:

1. **Forke** das Repository.
2. Erstelle einen neuen **Branch**: `git checkout -b feature/neues-feature`
3. **Committe** deine Änderungen: `git commit -m 'Füge neues Feature hinzu'`
4. **Pushe** den Branch: `git push origin feature/neues-feature`
5. Stelle einen **Pull-Request**.

## Lizenz

Dieses Projekt steht unter der MIT-Lizenz. Siehe die [LICENSE](LICENSE) Datei für Details.
