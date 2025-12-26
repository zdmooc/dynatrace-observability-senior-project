# Kubernetes / OpenShift

## Contenu
- `manifests/` : templates `DynaKube`, secrets (sans valeurs), namespace
- `openshift/` : notes SCC/PSA, exemples de commandes
- `helm/` : placeholders si vous encapsulez en chart interne

## Déploiement rapide
```bash
oc new-project dynatrace || true
oc apply -n dynatrace -f manifests/
```
