# Installation — OneAgent (Windows)

> Objectif : installer Dynatrace OneAgent sur une VM Windows.

## Pré-requis
- Accès UI Dynatrace + droits pour générer token
- Réseau sortant vers Dynatrace (ou via ActiveGate)
- Droits admin local

## Méthode recommandée (via UI Dynatrace)
1. Dynatrace Hub → OneAgent → Set up → Windows
2. Générer/coller le token demandé
3. Télécharger l’installer MSI/EXE proposé
4. Installer en mode interactif ou silencieux (selon standard poste)

## Exemple (installation silencieuse — à adapter à votre pack)
```powershell
# Exemple générique (le vrai nom/paramètres sont fournis par Dynatrace UI)
Start-Process msiexec.exe -Wait -ArgumentList '/i Dynatrace-OneAgent-Windows.msi /qn'
```

## Vérifications
- Services Windows : Dynatrace OneAgent
- “Deployment status” dans l’UI Dynatrace
