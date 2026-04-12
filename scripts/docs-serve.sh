#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
VENV_DIR="$ROOT_DIR/.venv"
PYTHON_BIN="${PYTHON_BIN:-python3}"
DEV_ADDR="${MKDOCS_DEV_ADDR:-127.0.0.1:8000}"

if [ ! -x "$VENV_DIR/bin/python" ]; then
  echo "Creating docs virtual environment at $VENV_DIR"
  "$PYTHON_BIN" -m venv "$VENV_DIR"
  "$VENV_DIR/bin/python" -m pip install --upgrade pip
fi

echo "Installing docs dependencies"
"$VENV_DIR/bin/python" -m pip install -r "$ROOT_DIR/requirements-docs.txt"

echo "Generating MkDocs navigation"
"$VENV_DIR/bin/python" "$ROOT_DIR/scripts/generate_mkdocs_nav.py"

echo "Starting MkDocs dev server at http://$DEV_ADDR/Agentic-Design-Patterns-CN/"
exec "$VENV_DIR/bin/mkdocs" serve -f "$ROOT_DIR/mkdocs-strict.yml" --dev-addr "$DEV_ADDR"
