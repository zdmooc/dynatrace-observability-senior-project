#!/usr/bin/env bash
set -euo pipefail

# Applique les manifests (sans secrets réels)
# Usage:
#   ./apply_all.sh
#
# Prérequis: oc/kubectl connecté au cluster

kubectl apply -f k8s/manifests/00-namespace.yaml
kubectl apply -n dynatrace -f k8s/manifests/01-secret-templates.yaml
kubectl apply -n dynatrace -f k8s/manifests/dynakube.yaml

echo "[*] Applied. Now check:"
echo "    kubectl get pods -n dynatrace"
