# Architecture cible (référence)

## Modèle “Managed + K8s/OpenShift”
- Dynatrace Managed : cluster (1..n nodes) pour héberger l’UI, traitement, stockage.
- ActiveGate (optionnel) :
  - routage/collecte dans réseau segmenté
  - extensions exécutées côté ActiveGate
  - réduction d’exposition réseau
- OneAgent :
  - instrumentation JVM/OS/containers
  - collecte métriques & traces, (et logs si configuré)
- Kubernetes/OpenShift :
  - Dynatrace Operator + ressource `DynaKube`
  - injection/daemonset OneAgent & composants requis selon mode

## Découpage opérationnel
- Environnements : dev / qualif / préprod / prod (zones & tags)
- Ownership : service owner / platform / SRE / N3
- Gouvernance : standards + revue mensuelle + backlog d’amélioration
