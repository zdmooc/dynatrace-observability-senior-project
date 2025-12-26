# Déploiement — `DynaKube` (Kubernetes / OpenShift)

> Objectif : créer les secrets et la ressource `DynaKube` qui pilote l’installation (OneAgent + composants) sur le cluster.

## 1) Récupérer le manifest `dynakube.yaml` depuis Dynatrace (recommandé)
Dynatrace propose une “Quickstart” K8s :
- Installer l’Operator
- Saisir les tokens (Operator token, data ingest)
- Télécharger un `dynakube.yaml` prêt

Ensuite, vous l’adaptez aux standards internes (namespace, proxy, tolerations, zones, etc.).

## 2) Namespace
```bash
oc new-project dynatrace || true
```

## 3) Secrets (exemples — à adapter)
> Ne jamais committer de valeurs de tokens dans Git.

```bash
# Exemple: secret contenant API token (lecture config + ingest selon besoin)
oc -n dynatrace create secret generic dynatrace-api-token   --from-literal=apiToken='<REDACTED>'

# Exemple: token data ingest (si requis)
oc -n dynatrace create secret generic dynatrace-data-ingest-token   --from-literal=dataIngestToken='<REDACTED>'
```

## 4) Appliquer DynaKube
- Exemple de manifest : `k8s/manifests/dynakube.yaml` (templates)
```bash
oc apply -n dynatrace -f k8s/manifests/dynakube.yaml
```

## 5) Vérifications
```bash
oc get dynakube -n dynatrace
oc get pods -n dynatrace
oc get events -n dynatrace --sort-by='.lastTimestamp' | tail -n 30
```

## Notes OpenShift
- SCC / PSA : vérifier autorisations nécessaires au daemonset OneAgent
- Proxies : configurer variables d’environnement et/ou options Operator
- Registry : allowlist images Dynatrace si politique “restricted”

## Références
- Dynatrace Docs “Get started with Kubernetes platform monitoring + Application observability”
- Dynatrace Docs “Quickstart” (download dynakube.yaml)
