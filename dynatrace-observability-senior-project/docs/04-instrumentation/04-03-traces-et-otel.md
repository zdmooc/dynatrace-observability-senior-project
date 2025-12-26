# Traces & OpenTelemetry (si applicable)

## Objectif
- Compléter l’auto-instrumentation si nécessaire (serverless, libs spécifiques)
- Standardiser la propagation trace context

## Approche
- Prioriser OneAgent (simplicité)
- Ajouter OTEL là où OneAgent ne couvre pas ou pour enrichir

## Contrôles
- Propagation traceId entre services
- Sampling conforme (coûts)
