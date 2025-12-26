# Installation — ActiveGate (Linux)

> Objectif : installer un **Environment ActiveGate** (recommandé en réseau segmenté, proxy, extensions).

## Quand utiliser un ActiveGate ?
- Réseaux segmentés : pas de flux direct des agents vers Dynatrace
- Exécution d’extensions “ActiveGate-based”
- Centraliser certaines collectes (cloud, remote tech) selon modèle

## Pré-requis
- Compte avec droits Dynatrace pour générer un **PaaS token**
- Accès sortant vers Dynatrace (HTTPS/443) et ports ActiveGate selon besoin
- OS Linux supporté + droits sudo/root

## Étapes (UI Dynatrace)
1. Dynatrace Hub → **ActiveGate** → **Set up**
2. Choisir **Linux**
3. Choisir le “purpose” (routing/monitoring/extensions)
4. Générer / fournir un **PaaS token**
5. Copier la commande `wget` fournie par l’UI

## Commandes (exemple générique)
> Les commandes exactes sont générées par Dynatrace UI et incluent votre token.

```bash
# 1) Télécharger l'installer via la commande fournie par l'UI (ex: wget ...)
# 2) Exécuter en root
sudo /bin/sh Dynatrace-ActiveGate-Linux-x86-<...>.sh
```

## Vérifications
```bash
# service
sudo systemctl status dynatracegateway

# logs (chemins variables selon version)
sudo journalctl -u dynatracegateway -n 200 --no-pager
```

## Notes réseau
- ActiveGate écoute par défaut sur un port entrant dédié (souvent 9999 selon doc ActiveGate)
- Il initie des connexions sortantes vers Dynatrace via 443
- Valider vos règles firewall et proxy.

## Références
- Guide ActiveGate Linux (UI + prérequis) : Dynatrace Docs “Install an Environment ActiveGate on Linux”
