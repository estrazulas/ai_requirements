#!/bin/bash

# setup.sh - Script de setup para o Módulo 9: Automação de Ecossistema
# Cria ambiente virtual, instala dependências e configura .env

echo "============================================================"
echo "SETUP - Módulo 9: Automação de Ecossistema GitLab ↔ GLPI"
echo "============================================================"
echo ""

# Verifica se o Python 3 está instalado
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 não encontrado. Instale o Python 3.8+ primeiro."
    exit 1
fi

echo "✅ Python 3 encontrado: $(python3 --version)"
echo ""

# Cria o ambiente virtual se não existir
if [ ! -d "venv" ]; then
    echo "🔧 Criando ambiente virtual..."
    python3 -m venv venv
    echo "✅ Ambiente virtual criado"
else
    echo "✅ Ambiente virtual já existe"
fi
echo ""

# Ativa o ambiente virtual
echo "🔧 Ativando ambiente virtual..."
source venv/bin/activate
echo "✅ Ambiente virtual ativado"
echo ""

# Instala as dependências
echo "📦 Instalando dependências..."
pip install --upgrade pip
pip install -r requirements.txt
echo "✅ Dependências instaladas"
echo ""

# Verifica se o .env existe, se não, copia do .env.example
if [ ! -f ".env" ]; then
    echo "📝 Criando arquivo .env a partir de .env.example..."
    cp .env.example .env
    echo "✅ Arquivo .env criado"
    echo ""
    echo "⚠️  IMPORTANTE: Edite o arquivo .env e configure:"
    echo "   - GITLAB_TOKEN (para sincronização MR ↔ ticket)"
    echo "   - GLPI_USER_TOKEN e GLPI_APP_TOKEN (para sincronização MR ↔ ticket)"
    echo "   - OPENAI_API_KEY ou ANTHROPIC_API_KEY (para NL Parser)"
    echo ""
else
    echo "✅ Arquivo .env já existe"
fi
echo ""

# Verifica se os mocks existem
if [ ! -f "mr-mock.json" ] || [ ! -f "ticket-mock.json" ]; then
    echo "⚠️  Arquivos de mock não encontrados"
    echo "   Crie mr-mock.json e ticket-mock.json para testar o modo --local"
else
    echo "✅ Arquivos de mock encontrados"
fi
echo ""

echo "============================================================"
echo "SETUP CONCLUÍDO!"
echo "============================================================"
echo ""
echo "Próximos passos:"
echo ""
echo "1. Edite o arquivo .env com suas chaves de API:"
echo "   nano .env"
echo ""
echo "2. Teste o modo local (sincronização MR ↔ ticket):"
echo "   python ecosystem-bot-gitlab-glpi.py --local"
echo ""
echo "3. Teste o NL Parser (linguagem natural):"
echo "   python ecosystem-bot-gitlab-glpi.py --parse \"Preciso investigar bug no login OAuth\""
echo ""
echo "4. Inicie o servidor webhook (produção):"
echo "   python ecosystem-bot-gitlab-glpi.py"
echo ""
echo "Para mais detalhes, consulte:"
echo "   - README.md (documentação completa)"
echo "   - guia-simulacao.md (exemplos de testes)"
echo ""
echo "Para ativar o ambiente virtual manualmente:"
echo "   source venv/bin/activate"
echo ""
echo "============================================================"
