#!/bin/bash
# Levanta el dashboard de DoceProjects en ops.doceprojects.com
# Uso: ./serve.sh

PORT=8090
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo "📂 Sirviendo: $DIR"
echo "🌐 Puerto local: $PORT"
echo ""

# Matar cualquier proceso previo en ese puerto
kill $(lsof -t -i:$PORT 2>/dev/null) 2>/dev/null

# Levantar servidor Python en background
cd "$DIR"
python -m http.server $PORT &
SERVER_PID=$!

echo "✅ Servidor local corriendo (PID $SERVER_PID)"
echo "🔗 http://localhost:$PORT/dashboard.html"
echo ""

# Levantar ngrok con dominio fijo
echo "🚀 Iniciando ngrok → ops.doceprojects.com..."
ngrok http $PORT --domain=ops.doceprojects.com

# Al cerrar ngrok, matar el servidor
kill $SERVER_PID 2>/dev/null
echo "Servidor detenido."
