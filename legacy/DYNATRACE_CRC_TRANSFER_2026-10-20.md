# Dynatrace CRC — consolidation partielle, 20 octobre 2026

**Statut : PARTIAL_TRANSFER / DELETION_BLOCKED.** Propriétaire canonique : [dynatrace-observability-senior-project](https://github.com/zdmooc/dynatrace-observability-senior-project).

## Inventaire

- [Source `dynatrace-crc-lab`](https://github.com/zdmooc/dynatrace-crc-lab) : 27 fichiers, branche principale `main` seulement.
- **25/27 fichiers** copiés *sans modification de contenu* à `legacy/dynatrace-crc-lab/<chemin d'origine>` dans ce dépôt.
- Les scripts Bash, les manifestes Kubernetes et les documents sont conservés dans leur emplacement relatif ; pour exécuter les commandes de l'ancien laboratoire, travailler dans `legacy/dynatrace-crc-lab/`.
- [Inventaire machine complet, chemins et SHA](dynatrace-crc-source-map.json) : `preserved:true/false`.

## Deux fichiers non transférés

1. `docs/10-runbook-replay-from-scratch.md` — SHA original `64dbda86ef02238f690615b9af92adda32ab75d9`.
2. `evidence/step06-incident-rca.md` — SHA original `8b071da839191a1b5cca8bcd50fe8bf374b265a0`.

Le transfert de ces deux fichiers a été refusé par les contrôles de sécurité du connecteur. Il n'a pas été contourné. **Ne supprimer ni ce dépôt source ni ses historiques** avant conservation et vérification intégrale des fichiers manquants.

## Vérité des preuves

La présence de dossiers `evidence/` ne prouve pas des tests CRC réalisés : plusieurs contiennent seulement `(À remplir)`. La consolidation est **documentaire**, et ne change pas l'état réel d'un déploiement Dynatrace (Operator, DynaKube, SLI/SLO). Aucune exécution CRC ou cluster n'a été réalisée par cette opération.

Les historiques Git complets, tickets, paramètres et secrets restent hors de ce transfert. Le dépôt cible est public comme la source ; aucune donnée nouvelle confidentielle n'a été ajoutée.
