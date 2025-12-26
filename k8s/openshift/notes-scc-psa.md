# OpenShift — notes SCC/PSA (à adapter)

- Vérifier les contraintes de sécurité (SCC) selon version OpenShift.
- Le daemonset OneAgent peut nécessiter des privilèges (hostPID/hostNetwork/volumes hostPath).
- Appliquer le standard sécurité interne (exceptions justifiées, audit).

## Commandes utiles
```bash
oc get scc
oc describe scc <name>
oc adm policy who-can use scc/<name>
```
