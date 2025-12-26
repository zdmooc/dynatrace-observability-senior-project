# Runbook — Incident triage (N3)

## Objectif
Qualifier rapidement un incident (impact, périmètre, cause probable) et engager les actions de mitigation.

## Étapes
1. Confirmer l’alerte : service, env, criticité, MZ.
2. Identifier l’impact : SLO, utilisateurs, régions.
3. Correlater : traces, logs, infra (CPU/mem), dépendances (DB/Kafka/Ingress).
4. Mitigation :
   - rollback / scale / circuit breaker / feature flag (selon contexte)
5. Communication :
   - status update toutes les X minutes
6. RCA :
   - collecter preuves (screenshots, exports, timelines)

## Preuves à collecter
- timeline Dynatrace
- service flow
- top exceptions / endpoints
- événements K8s (pods, restarts)
