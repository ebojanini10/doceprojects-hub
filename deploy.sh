#!/bin/bash
# deploy.sh — Encrypt and deploy deliverables to doceprojects.com
# Usage: ./deploy.sh <client-slug> <type> <source-html> [password]
#
# Types: prop | f1 | f2 | f3 | ... | final
#
# Examples:
#   ./deploy.sh construhigienicas prop proposal-construhigienicas.html
#   ./deploy.sh casa-ardente f1 entregable-f1.html
#   ./deploy.sh casa-ardente final entregable-final.html
#
# Password defaults to: doce-<client>-<type>
# All deliverables use shared salt from .staticrypt.json

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$SCRIPT_DIR"

# --- Args ---
CLIENT="${1:-}"
TYPE="${2:-}"
SOURCE="${3:-}"
PASSWORD="${4:-}"

if [[ -z "$CLIENT" || -z "$TYPE" || -z "$SOURCE" ]]; then
  echo "Usage: ./deploy.sh <client-slug> <type> <source-html> [password]"
  echo ""
  echo "  client-slug   e.g. construhigienicas, casa-ardente, eqr"
  echo "  type          prop | f1 | f2 | f3 | ... | final"
  echo "  source-html   Path to the unencrypted HTML file"
  echo "  password      Optional. Defaults to doce-<client>-<type>"
  echo ""
  echo "Deployed deliverables:"
  for client_dir in */; do
    [[ ! -d "$client_dir" ]] && continue
    for type_dir in "${client_dir}"*/; do
      [[ -f "${type_dir}index.html" ]] && echo "  doceprojects.com/${client_dir%/}/${type_dir##${client_dir}}"
    done
  done
  exit 1
fi

if [[ ! -f "$SOURCE" ]]; then
  echo "Error: Source file not found: $SOURCE"
  exit 1
fi

# Validate type
if [[ ! "$TYPE" =~ ^(prop|f[0-9]+|final)$ ]]; then
  echo "Error: type must be 'prop', 'f1', 'f2', ..., or 'final'"
  exit 1
fi

# Default password
if [[ -z "$PASSWORD" ]]; then
  PASSWORD="doce-${CLIENT}-${TYPE}"
fi

# --- Check staticrypt ---
if ! command -v staticrypt &>/dev/null; then
  echo "Error: staticrypt not found. Install with: npm install -g staticrypt"
  exit 1
fi

# --- Template ---
TEMPLATE="${SCRIPT_DIR}/staticrypt-template.html"
if [[ ! -f "$TEMPLATE" ]]; then
  echo "Error: Branded template not found: $TEMPLATE"
  exit 1
fi

# --- Label for login screen ---
case "$TYPE" in
  prop)  LABEL="Propuesta Comercial" ;;
  final) LABEL="Entregable Final" ;;
  *)     LABEL="Entregable ${TYPE^^}" ;;
esac

# --- Encrypt ---
DEST="${CLIENT}/${TYPE}"
echo "Encrypting ${CLIENT}/${TYPE}..."
mkdir -p "$DEST"

staticrypt "$SOURCE" \
  -p "$PASSWORD" \
  --remember 0 \
  -d "$DEST" \
  --config .staticrypt.json \
  --short \
  -t "$TEMPLATE" \
  --template-button "ACCEDER" \
  --template-title "$LABEL" \
  --template-placeholder "Contraseña" \
  --template-error "Contraseña incorrecta" \
  --template-instructions "Ingresa la contraseña proporcionada para acceder."

# Rename to index.html
ENCRYPTED_FILE="$DEST/$(basename "$SOURCE")"
if [[ -f "$ENCRYPTED_FILE" && "$ENCRYPTED_FILE" != "$DEST/index.html" ]]; then
  mv "$ENCRYPTED_FILE" "$DEST/index.html"
fi

echo "Encrypted: $DEST/index.html"

# --- Git commit & push ---
git add "${DEST}/index.html"
git add -f .staticrypt.json 2>/dev/null || true
git commit -m "deploy: ${CLIENT}/${TYPE}"
git push origin main

echo ""
echo "  URL:      https://doceprojects.com/${CLIENT}/${TYPE}/"
echo "  Password: ${PASSWORD}"
