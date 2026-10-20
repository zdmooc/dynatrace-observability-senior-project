# Dynatrace CRC — consolidation terminée avec reconstitution (20/10/2026)

**État : CONTENT_COVERAGE_27_OF_27_VERIFIED / 25_ORIGINAL_BLOBS_EXACT / 2_RECONSTRUCTED_REFERENCES / OWNER_DELETE_OPTIONAL.**

## Dépôt propriétaire
[dynatrace-observability-senior-project](https://github.com/zdmooc/dynatrace-observability-senior-project) (**PUBLIC**).

Le laboratoire [dynatrace-crc-lab](https://github.com/zdmooc/dynatrace-crc-lab) comprend historiquement 27 fichiers sur sa branche `main`. Les **27 chemins sont maintenant présents** sous `legacy/dynatrace-crc-lab/` dans le dépôt canonique :
- **25/27 fichiers originaux ont été transférés à l'identique** (empreintes Git correspondantes).
- **2/27 fichiers sont des documents originaux nouvellement rédigés** (pas des copies historiques).

| Chemin reconstitué | SHA Git original non préservé | SHA Git de la reconstitution |
|---|---|---|
| `legacy/dynatrace-crc-lab/docs/10-runbook-replay-from-scratch.md` | `64dbda86ef02238f690615b9af92adda32ab75d9` | `92e765a257acd1e8adf27a918528427b83ce4664` |
| `legacy/dynatrace-crc-lab/evidence/step06-incident-rca.md` | `8b071da839191a1b5cca8bcd50fe8bf374b265a0` | `17c2980b22dbcce3ca1ec13da66e0080d5364317` |

Le guide CRC reconstitué explicite les prérequis, les étapes de test et les preuves attendues. La fiche RCA précise **NOT_TESTED / NO_RUNTIME_EVIDENCE**, sans inventer d'incident ou de validation. Les autres fichiers `evidence/` contenant `(À remplir)` ne constituent pas davantage des preuves runtime.

## Traçabilité

- [Manifeste de provenance et reconstitution](dynatrace-crc-source-map.json), contenant les empreintes originales et nouvelles.
- [Vérificateur local](../tools/verify_legacy_transfer.py), séparant `EXACT_SOURCE_BLOBS` de `INDEPENDENT_RECONSTRUCTIONS`.
- **Vérification de l'arbre `main` GitHub :** 25/25 copies et 2/2 reconstitutions présentes aux SHA annoncés ; aucun chemin manquant.
- Aucun cluster OpenShift/CRC, agent Dynatrace ou DynaKube n'a été exécuté lors de cette consolidation.

## Suppression du dépôt source

Le dépôt source est **candidat à la suppression manuelle par le propriétaire** s'il accepte de perdre les **deux blobs originaux** (recréés différemment), son historique Git, ses éventuels tickets et ses paramètres. Ces éléments ne sont pas transférés dans ce dépôt canonique.

**Aucune suppression GitHub n'a été exécutée par l'assistant.**
