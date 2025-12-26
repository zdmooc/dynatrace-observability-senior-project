# Installation Dynatrace — Guide détaillé

## Choisir votre scénario
- **A — Kubernetes / OpenShift (recommandé)** : Operator + `DynaKube`
  - voir `02-05-openshift-operatorhub.md` puis `02-06-dynakube-templates.md`
- **B — Linux/VM** : OneAgent + (optionnel) ActiveGate
  - voir `02-03-oneagent-linux.md` et `02-02-activegate-linux.md`
- **C — Dynatrace Managed (cluster)** : déploiement / prérequis
  - voir `02-01-dynatrace-managed-cluster.md`

## Checklist avant installation
- Accès Dynatrace (UI + droits) : création tokens (PaaS / API / Operator selon besoin)
- DNS / proxy / certificats : flux sortants/entrants validés
- Sécu : règles firewall, RBAC OpenShift, policy images/registries
- Nommage : tags / management zones (voir docs/03-standards)
