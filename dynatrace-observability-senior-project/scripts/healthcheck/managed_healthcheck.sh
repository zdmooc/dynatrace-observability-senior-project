#!/usr/bin/env bash
set -euo pipefail

# Healthcheck basique (à adapter) pour Dynatrace Managed via HTTP(S).
# Variables:
#   DT_MANAGED_URL : ex https://dynatrace-managed.example.com

if [[ -z "${DT_MANAGED_URL:-}" ]]; then
  echo "ERROR: DT_MANAGED_URL is not set (ex: https://dynatrace-managed.example.com)"
  exit 1
fi

echo "[*] Checking URL: $DT_MANAGED_URL"
curl -k -I -sS "$DT_MANAGED_URL" | head -n 20
echo "[*] Done."
