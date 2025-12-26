# Alerting & baselines

## Principes
- Distinguer symptôme vs cause
- Un seul “pager” par incident (déduplication)
- Alertes basées sur SLO (burn rate) pour le critique

## Exemples d’alertes
- Burn rate (1h / 6h) sur availability SLO
- Latence p95 au-dessus baseline
- Erreurs 5xx au-dessus baseline
- Saturation CPU > 90% (sur durée) + corrélation HPA/requests
