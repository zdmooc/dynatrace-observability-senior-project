#!/usr/bin/env bash
set -euo pipefail

# Exemple générique: privilégier la commande générée par l’UI Dynatrace.
# Variables attendues:
#   DT_ONEAGENT_INSTALL_URL : URL complète de téléchargement (incluant token) fournie par Dynatrace UI
# Exemple:
#   export DT_ONEAGENT_INSTALL_URL="https://<env>/api/v1/deployment/installer/agent/unix/default/latest?Api-Token=<TOKEN>&arch=x86&flavor=default"

if [[ -z "${DT_ONEAGENT_INSTALL_URL:-}" ]]; then
  echo "ERROR: DT_ONEAGENT_INSTALL_URL is not set."
  echo "Hint: copy the download command from Dynatrace Hub -> OneAgent -> Set up -> Linux."
  exit 1
fi

tmp="/tmp/dt-oneagent-installer.sh"
echo "[*] Downloading OneAgent installer..."
curl -fsSL "$DT_ONEAGENT_INSTALL_URL" -o "$tmp"
chmod +x "$tmp"

echo "[*] Installing OneAgent (root required)..."
sudo /bin/sh "$tmp"

echo "[*] Verifying service..."
sudo systemctl status dynatraceoneagent --no-pager || true
echo "[*] Done."
