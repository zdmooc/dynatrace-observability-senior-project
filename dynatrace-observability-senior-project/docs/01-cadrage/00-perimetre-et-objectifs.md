# Périmètre & objectifs

## Objectifs
- Assurer l’observabilité des solutions OpenSource (apps + middlewares + K8s) via Dynatrace.
- Mettre en place des standards : instrumentation, dashboards, alerting, SLI/SLO.
- Assurer le support N3 (diagnostic, résolution, prévention), y compris en cellule de crise.

## Périmètre technique (à adapter)
- Dynatrace Managed (cluster) + (optionnel) ActiveGate
- OneAgent (Linux / Windows / containers)
- Kubernetes / OpenShift (Operator + DynaKube)
- Middlewares typiques : JVM, Nginx/Apache, PostgreSQL, Kafka, Redis, Elastic, etc.
- Intégrations : ITSM, alert routing, webhooks, e-mail, etc.

## Exigences non-fonctionnelles
- Sécurité : RBAC, secrets, proxies, certificats, segmentation réseau
- Performance : overhead agent acceptable, sampling, budgets d’ingestion
- Conformité : rétention logs/metrics, traçabilité changements, audit
