#!/bin/bash

# Script de setup para o ambiente virtual

echo "🔧 Configurando ambiente virtual..."

# Cria o venv se não existir
if [ ! -d "venv" ]; then
    python3 -m venv venv
    echo "✅ Ambiente virtual criado"
else
    echo "✅ Ambiente virtual já existe"
fi

# Ativa o venv
source venv/bin/activate

# Instala as dependências
echo "📦 Instalando dependências..."
pip install -r requirements.txt

echo "✅ Setup completo!"
echo ""
echo "Para ativar o ambiente virtual:"
echo "  source venv/bin/activate"
echo ""
echo "Para testar os scripts:"
echo "  python danger-gitlab-ifsc.py --local --mock mr-mock-sucesso.json"
echo "  python compliance-checker.py --local --mock mr-mock-sucesso.json"
