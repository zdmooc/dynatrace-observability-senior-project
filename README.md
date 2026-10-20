# Projet — Expert Senior Dynatrace (Managed + AppMon) — Observabilité OpenSource (Nanterre / Énergie)

Ce dépôt fournit une base **prête à l’emploi** pour cadrer, installer, industrialiser et exploiter Dynatrace
dans un contexte **support N3**, **Kubernetes/OpenShift**, et **SRE (SLI/SLO)**.

## Contenu
- **docs/** : documentation opérationnelle (installation, standards, dashboards, alerting, SLI/SLO, reporting)
- **k8s/** : manifests & templates (Operator/DynaKube, secrets, exemples OpenShift)
- **scripts/** : scripts d’installation / healthchecks (sans secrets)
- **runbooks/** : runbooks N3 (triage, RCA, incidents, crise)
- **backlog/** : backlog (épics/stories) + livrables

## Démarrage rapide
1. Lire **docs/02-installation/README.md**
2. Choisir votre mode de déploiement :
   - **OpenShift** : OperatorHub + `DynaKube` (recommandé)
   - **Linux/VM** : OneAgent + (optionnel) ActiveGate
3. Appliquer les standards :
   - tags / management zones : **docs/03-standards/**
   - dashboards & alerting : **docs/05-dashboards-alerting/**
   - SLI/SLO + reporting : **docs/06-sli-slo/** & **docs/07-reporting/**

## Sécurité / Secrets
Ne jamais committer de tokens Dynatrace. Utiliser des **Secrets Kubernetes**, un **vault**, ou des variables d’environnement locales.
Voir **docs/02-installation/02-07-securite-proxy-certificats-firewall.md**.

## Licence
MIT — voir **LICENSE**.

---
_Généré le 2025-12-24_

## Consolidation du lab Dynatrace CRC — 20 octobre 2026

Le laboratoire historique [`dynatrace-crc-lab`](legacy/dynatrace-crc-lab/) est maintenant **intégralement représenté** : **25 fichiers copiés octet pour octet et 2 documents de référence indépendamment reconstitués**, soit 27/27 chemins présents. Les deux reconstitutions **ne sont pas identiques aux blobs d'origine**. [Rapport et réserves](legacy/DYNATRACE_CRC_TRANSFER_2026-10-20.md) · [Manifeste des SHA](legacy/dynatrace-crc-source-map.json) · [Vérificateur](tools/verify_legacy_transfer.py). Le propriétaire peut supprimer le dépôt source **s'il accepte la perte de ces deux originaux et de l'historique Git**. Les fichiers `evidence/` avec « À remplir » ou « NOT_TESTED » ne prouvent aucun déploiement CRC.
