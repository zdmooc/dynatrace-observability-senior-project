#!/usr/bin/env bash
set -euo pipefail

# Exemple générique: privilégier la commande générée par l’UI Dynatrace.
# Variables attendues:
#   DT_ACTIVEGATE_INSTALL_URL : URL complète de téléchargement (incluant token) fournie par Dynatrace UI

if [[ -z "${DT_ACTIVEGATE_INSTALL_URL:-}" ]]; then
  echo "ERROR: DT_ACTIVEGATE_INSTALL_URL is not set."
  echo "Hint: Dynatrace Hub -> ActiveGate -> Set up -> Linux (copy the download command)."
  exit 1
fi

tmp="/tmp/dt-activegate-installer.sh"
echo "[*] Downloading ActiveGate installer..."
curl -fsSL "$DT_ACTIVEGATE_INSTALL_URL" -o "$tmp"
chmod +x "$tmp"

echo "[*] Installing ActiveGate (root required)..."
sudo /bin/sh "$tmp"

echo "[*] Verifying service..."
sudo systemctl status dynatracegateway --no-pager || true
echo "[*] Done."
