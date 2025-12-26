# Management Zones

## Objectif
Isoler la visibilité, déléguer l’exploitation, et sécuriser l’accès par périmètre.

## Stratégie
- 1 MZ par environnement + domaine (ex: `prod-paiement`, `preprod-data`)
- Une règle de scope sur tags (env/team/app)

## Contrôles
- Vérifier qu’un utilisateur “team” ne voit pas prod global
- Vérifier routing d’alertes par MZ
