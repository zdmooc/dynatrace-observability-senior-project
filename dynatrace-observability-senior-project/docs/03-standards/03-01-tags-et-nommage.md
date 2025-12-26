# Tags & nommage

## Objectif
Garantir la recherche, le filtrage, le routing d’alertes et les rapports.

## Tags recommandés (exemples)
- `env:dev|qualif|preprod|prod`
- `app:<nom_appli>`
- `service:<nom_service>`
- `team:<squad>`
- `criticality:tier1|tier2|tier3`
- `cost_center:<code>`
- `region:<region>`
- `cluster:<ocp-name>`

## Convention de nommage
- Services : `app-<domaine>-<capability>-<api>`
- Hosts : `vm-<site>-<role>-<nn>`
- Namespaces : `<env>-<domaine>`
