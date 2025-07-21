#!/usr/bin/env python3
"""
Site Romântico - Para Minha Namorada 💖 (Versão 4.0 - COM TEMPORIZADORES DE DATAS ESPECIAIS!)

🎉 VERSÃO 4.0 - NOVAS FUNCIONALIDADES:
✅ TEMPORIZADORES DE DATAS ESPECIAIS com contagem regressiva em tempo real
✅ Textos atualizados conforme solicitado
✅ Todas as correções anteriores mantidas
✅ Performance otimizada e estável

Como executar:
1. Instale as dependências: pip install -r requirements.txt
2. Execute: python main.py
3. Abra o navegador em: http://localhost:5000

NOVAS FUNCIONALIDADES v4.0:
- ⏰ TEMPORIZADORES DE DATAS ESPECIAIS:
  * Um dia Bom (04/08/2025) ☀️
  * Um dia Perfeito (22/08/2025) ✨
  * O Dia (18/11/2025) 💎
- 📅 Contagem regressiva em tempo real (Meses, Dias, Horas, Minutos, Segundos)
- 🎨 Cards glassmorphism para os temporizadores
- 🔄 Atualização automática a cada segundo

TEXTOS ATUALIZADOS:
- Menu: "Para o Meu [Vermelho: Amor]"
- Subtítulo: "Um canto especial só para você lembrar de mim 😍"
- Música: "Nossas Músicas"
- Descrição música: "Cada música desta playlist tem um significado especial e me faz pensar em você, mo. Espero que goste! 🎧💖"

FUNCIONALIDADES MANTIDAS:
- Playlist do Spotify integrada
- Caixas de surpresas virtuais
- Quiz personalizado atualizado
- Animações românticas ESTÁVEIS
- Design glassmorphism moderno
- Plano de fundo interativo otimizado
- Design responsivo mobile
- ZERO RECARREGAMENTOS AUTOMÁTICOS!
"""

import os
from flask import Flask, send_from_directory

# Configuração da aplicação Flask
app = Flask(__name__, static_folder='static')
app.config['SECRET_KEY'] = 'site-romantico-v4-temporizadores-2025'

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    """
    Serve os arquivos estáticos da aplicação React.
    Para qualquer rota não encontrada, retorna o index.html (SPA behavior).
    """
    static_folder_path = app.static_folder
    if static_folder_path is None:
        return "Pasta static não configurada", 404

    # Se o arquivo existe, serve diretamente
    if path != "" and os.path.exists(os.path.join(static_folder_path, path)):
        return send_from_directory(static_folder_path, path)
    else:
        # Caso contrário, serve o index.html (comportamento SPA)
        index_path = os.path.join(static_folder_path, 'index.html')
        if os.path.exists(index_path):
            return send_from_directory(static_folder_path, 'index.html')
        else:
            return "index.html não encontrado", 404

@app.route('/health')
def health():
    """Endpoint de saúde da aplicação"""
    return {
        "status": "ok", 
        "message": "Site romântico v4.0 - COM TEMPORIZADORES! 💖",
        "version": "4.0",
        "new_features": [
            "Temporizadores de datas especiais",
            "Contagem regressiva em tempo real",
            "Textos atualizados",
            "Cards glassmorphism para temporizadores"
        ],
        "special_dates": [
            {"name": "Um dia Bom", "date": "04/08/2025"},
            {"name": "Um dia Perfeito", "date": "22/08/2025"},
            {"name": "O Dia", "date": "18/11/2025"}
        ]
    }

if __name__ == '__main__':
    print("🚀 Iniciando Site Romântico v4.0 - COM TEMPORIZADORES!")
    print("💖 Para Minha Namorada - AGORA COM DATAS ESPECIAIS!")
    print("📱 Acesse: http://localhost:5000")
    print("⏰ NOVO: Temporizadores de contagem regressiva!")
    print("📅 Datas especiais: 04/08/2025, 22/08/2025, 18/11/2025")
    print("✨ Textos atualizados conforme solicitado!")
    print("=" * 70)
    
    # Executa o servidor Flask
    app.run(
        host='0.0.0.0',  # Permite acesso externo
        port=5000,       # Porta padrão
        debug=True       # Modo debug para desenvolvimento
    )

