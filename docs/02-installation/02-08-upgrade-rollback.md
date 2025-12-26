# Upgrade & rollback (OneAgent / Operator / Managed)

## OneAgent (Linux)
- Préférer upgrades via mécanisme Dynatrace (remote updates) selon politique
- En cas de rollback :
  - conserver l’installer N-1 en dépôt interne (si autorisé)
  - procédure de désinstallation/reinstall contrôlée
- Vérifier compatibilité JVM / middleware

## Operator / DynaKube
- Upgrader l’Operator selon processus OpenShift (Subscription channel)
- Contrôler les changements CRD/CR
- Revenir à une version précédente : restaurer Subscription / operator version si supporté

## Managed
- Upgrades planifiés (maintenance window)
- Sauvegarde/snapshot avant upgrade si exigence
- Validation post-upgrade : UI, ingest, alerting, dashboards

## Checklist post-changement
- Agents up et remontee données OK
- Pas de bruit alerting
- Dashboards OK
- SLI/SLO OK
