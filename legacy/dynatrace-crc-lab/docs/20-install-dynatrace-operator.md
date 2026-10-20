# Installer Dynatrace Operator (OpenShift)

Option recommandée : OperatorHub

Vérif:
```bash
oc get csv -n openshift-operators | grep -i dynatrace || true
oc get pods -n openshift-operators | grep -i dynatrace || true
```
