# Rejeu Dynatrace sur CRC — guide reconstruit (2026-10-20)

> Document de référence **nouvellement rédigé**, pas une copie de l'ancien runbook.
> Les commandes ci-dessous servent à préparer et documenter un laboratoire OpenShift Local.
> Aucun déploiement ou test runtime n'est prouvé par la présence de ce fichier.

## Préparer le laboratoire

Vérifier l'accès au cluster CRC avec `oc whoami`, `oc get nodes` et `oc get pods -A`. Ne pas modifier d'environnement partagé sans autorisation. Enregistrer l'horodatage, la version d'OpenShift, les prérequis et les limites de ressources.

## Étapes de validation

| Étape | Objectif | Preuve attendue |
|---|---|---|
| 00 | Établir l'état initial de CRC | `evidence/step00-oc-baseline.txt` |
| 01 | Installer et vérifier Dynatrace Operator | `evidence/step01-operator-installed.txt` |
| 02 | Configurer les secrets nécessaires et vérifier DynaKube | `evidence/step02-dynakube-ready.txt` |
| 03 | Lancer des charges de test nginx, httpbin et PostgreSQL | `evidence/step03-demo-apps.txt` |
| 04 | Configurer tableaux de bord et alertes | `evidence/step04-dashboards-alerts.md` |
| 05 | Évaluer SLI, SLO et reporting | `evidence/step05-slo-reporting.md` |
| 06 | Simuler un incident, établir le diagnostic et documenter la RCA | `evidence/step06-incident-rca.md` |
| 07 | Documenter les limites et la couverture des exigences | `docs/99-matrice-couverture-mission.md` |

## Critères de clôture

- Chaque étape doit produire une observation réelle, datée, attribuée à un environnement identifiable.
- Distinguer *manifeste préparé*, *déploiement observé*, *résultat de test* et *hypothèse*.
- Redacter les jetons, URL internes, identifiants et données client avant de publier une preuve.
- En cas de blocage de licence Dynatrace, signaler `NOT_TESTED_LICENSE` plutôt que `PASS`.
- N'attribuer aucun statut `CRC_RUNTIME_PROVEN` sans les sorties effectives et vérifiées.

## Références au contenu conservé

Les manifests sont sous `k8s/dynatrace/` et `k8s/demo-apps/`. Le fichier `COMMAND_LOG.md` est le journal de commandes, et `runbooks/` contient les aides au diagnostic.
