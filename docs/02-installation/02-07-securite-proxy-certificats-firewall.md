# Sécurité / Proxy / Certificats / Firewall

## Tokens (rotation / stockage)
- Utiliser **Secrets K8s** ou un **vault**
- Mettre en place rotation (mensuelle/trim) selon politique
- Limiter les scopes (least privilege)

## Proxy
- Valider `http_proxy/https_proxy/no_proxy` sur nœuds K8s si corporate proxy
- OneAgent / ActiveGate : options d’installation et configuration proxy (selon doc éditeur)
- Tester connectivité (curl/wget) avant déploiement

## Certificats (TLS)
- Si inspection TLS (proxy) : intégrer CA interne dans hôtes/containers selon standard
- Reverse-proxy devant Managed : TLS “corporate” + durcissement (HSTS, cipher policy)

## Firewall
- Ouvrir strictement les flux requis :
  - Agents → Dynatrace (ou ActiveGate)
  - ActiveGate → Dynatrace
  - Inter-nœuds Managed (ports internes)
- Fermer les ports internes Managed depuis l’extérieur si possible.

## Contrôles
- Tests connectivité : `curl -vk https://<endpoint>/`
- Vérifier erreurs dans logs agent/activegate/operator
