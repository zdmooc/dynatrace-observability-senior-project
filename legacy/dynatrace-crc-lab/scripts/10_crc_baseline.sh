#!/usr/bin/env bash
set -euo pipefail
crc status | tee evidence/step00-crc-status.txt
oc whoami | tee evidence/step00-oc-baseline.txt
oc get nodes | tee -a evidence/step00-oc-baseline.txt
oc get co | tee -a evidence/step00-oc-baseline.txt
