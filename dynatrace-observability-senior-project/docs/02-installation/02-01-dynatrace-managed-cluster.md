# Installation — Dynatrace Managed (cluster)

> Objectif : déployer ou intégrer un cluster Dynatrace Managed (sur VMs/bare-metal) pour héberger la plateforme.

## 1) Pré-requis (à valider avec l’équipe infra/sécurité)
- OS/VM : Linux supporté par Dynatrace Managed (valider la matrice support éditeur).
- DNS : noms et résolution inter-nœuds.
- Stockage : volumes dédiés (selon sizing).
- Réseau :
  - flux sortants vers la “Mission Control” Dynatrace (selon politique) et/ou dépôts.
  - flux internes entre nœuds du cluster (ports requis).
  - exposition UI via reverse-proxy/LB si nécessaire.

> Remarque : Dynatrace Managed utilise des ports internes entre nœuds (ex. 8020/8021/8022 selon configurations),
> qui doivent rester ouverts **entre nœuds** (et idéalement fermés depuis l’extérieur, via firewall).
> Valider la liste exacte dans la documentation “Managed / networking”.

## 2) Déploiement (high level)
1. Télécharger l’installeur Dynatrace Managed depuis le portail Dynatrace (accès sous licence).
2. Sur le 1er nœud (root) :
   - lancer l’installeur (mode interactive ou unattended)
   - définir le répertoire d’installation, stockage, paramètres cluster
3. Ajouter les nœuds supplémentaires (si cluster multi-nœuds) :
   - joindre au cluster via les procédures Dynatrace Managed
4. Accéder à l’UI Managed :
   - initialiser l’admin
   - créer/enregistrer les environnements (tenant/environments) si applicable
5. Sécuriser l’exposition :
   - TLS / certificats
   - reverse-proxy / WAF
   - durcir firewall (accès externe uniquement via ports exposés)

## 3) Opérations initiales
- Configurer sauvegarde / snapshot (si requis par politique interne)
- Mettre en place monitoring du cluster lui-même (CPU/RAM/disk)
- Mettre en place RBAC (admin, ops, read-only)
- Standardiser tokens et rotation

## 4) Références
- Voir la documentation officielle “Dynatrace Managed” (section Deploy Dynatrace / Cluster).
