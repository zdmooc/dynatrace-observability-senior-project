# Installation — OneAgent (Linux)

> Objectif : installer Dynatrace OneAgent sur une VM/serveur Linux pour instrumentation full-stack.

## Pré-requis
- Accès à l’UI Dynatrace (Managed / SaaS selon environnement)
- **PaaS token** (ou “Installer download token” selon UI) pour télécharger l’installer
- Accès réseau sortant vers Dynatrace (ou via ActiveGate)
- Droits root/sudo

## Méthode recommandée (via UI Dynatrace)
1. Dynatrace Hub → **OneAgent**
2. **Set up** → **Linux**
3. Générer/coller un **PaaS token** dans “Installer download token”
4. Choisir l’architecture (x86_64, etc.)
5. Copier/coller les commandes fournies (download + install)

> Dynatrace génère les commandes exactes pour votre environnement (URL + token).

## Exemple générique (shell)
```bash
# 1) Télécharger (commande fournie par l’UI, ex: wget ...)
# wget -O Dynatrace-OneAgent-Linux.sh "<TENANT_URL>/api/v1/deployment/installer/agent/unix/default/latest?Api-Token=<TOKEN>&arch=x86&flavor=default"

# 2) Exécuter en root
sudo /bin/sh Dynatrace-OneAgent-Linux.sh

# 3) Vérifier
sudo systemctl status dynatraceoneagent
```

## Personnalisation (cas proxy / réseau / tenant)
Selon la doc Dynatrace, l’installer Linux supporte des paramètres (optionnels), par ex. :
- `--set-tenant=<envId>`
- `--set-tenant-token=<token>`
- `--set-server=<endpoint>`

> Utiliser surtout si vous ne pouvez pas utiliser la commande générée par l’UI.

## Bonnes pratiques post-install
- Redémarrer les services applicatifs si nécessaire pour instrumentation complète (JVM)
- Poser des tags (host/service) et Management Zones
- Activer/valider log monitoring si requis (budget ingestion)

## Références
- Dynatrace Docs “Install OneAgent on Linux” (maj 2025-11-07)
- Dynatrace Docs “Customize OneAgent installation on Linux”
