# Installation — OpenShift : Dynatrace Operator via OperatorHub

> Objectif : installer Dynatrace Operator dans OpenShift, puis déployer un `DynaKube`.

## Pré-requis
- Accès console OpenShift (admin ou rights operator install)
- Namespace cible (souvent `dynatrace` ou dédié)
- Tokens Dynatrace nécessaires (Operator token, API token, data ingest token selon configuration)

## Méthode via Console OpenShift (OperatorHub)
1. OpenShift Console → **Operators** → **OperatorHub**
2. Chercher **Dynatrace Operator** → **Install**
3. Mode d’installation : **All namespaces** (recommandé en plateforme)
4. Subscriptions : garder defaults sauf contraintes internes
5. Attendre `Install Succeeded` : Operators → Installed Operators

## Vérifications
```bash
oc get pods -n openshift-operators | grep -i dynatrace || true
oc get csv -n openshift-operators | grep -i dynatrace || true
```

## Étape suivante
- Déployer `DynaKube` + secrets : voir `02-06-dynakube-templates.md`

## Références
- Dynatrace Docs “Set up OpenShift monitoring via OperatorHub”
