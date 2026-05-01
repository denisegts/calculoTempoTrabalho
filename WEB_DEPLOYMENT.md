# 🌐 Deployment da Interface Web - Cálculo de Tempo de Trabalho

Este guia mostra como usar e fazer deploy das interfaces web do seu projeto.

---

## 📦 Opções Disponíveis

### 1️⃣ **HTML/JavaScript** (Mais Rápido)
- **Arquivo:** `web/index.html`
- **Tecnologia:** HTML + CSS + JavaScript puro
- **Vantagens:** Sem dependências, funciona direto no navegador
- **Melhor para:** Usuários que querem algo leve e rápido

### 2️⃣ **Streamlit** (Mais Fácil)
- **Arquivo:** `app.py`
- **Tecnologia:** Streamlit (Framework Python)
- **Vantagens:** Interface profissional, fácil de usar
- **Melhor para:** Desenvolvedores que querem algo robusto

---

## 🚀 Como Usar Localmente

### Opção 1: HTML/JavaScript

1. **Clone o repositório:**
```bash
git clone https://github.com/denisegts/calculoTempoTrabalho.git
cd calculoTempoTrabalho
```

2. **Abra o arquivo no navegador:**
```bash
# No Windows
start web/index.html

# No macOS
open web/index.html

# No Linux
xdg-open web/index.html
```

**Pronto!** A aplicação está rodando no seu navegador. 🎉

---

### Opção 2: Streamlit

1. **Clone o repositório:**
```bash
git clone https://github.com/denisegts/calculoTempoTrabalho.git
cd calculoTempoTrabalho
git checkout web-interface
```

2. **Instale as dependências:**
```bash
pip install -r requirements.txt
```

3. **Execute a aplicação:**
```bash
streamlit run app.py
```

4. **Acesse no navegador:**
```
http://localhost:8501
```

---

## 🌐 Deployment Online

### Opção 1: GitHub Pages (HTML/JS)

#### Passo 1: Garantir que os arquivos estão no repositório
```bash
git add web/index.html
git commit -m "feat: Add web interface"
git push origin web-interface
```

#### Passo 2: Configurar GitHub Pages
1. Vá em **Settings** do seu repositório
2. Navegue até **Pages**
3. Em "Build and deployment", selecione:
   - **Source:** Deploy from a branch
   - **Branch:** `web-interface`
   - **Folder:** `/web`
4. Clique em "Save"

#### Passo 3: Acessar a página
Após alguns minutos, sua página estará disponível em:
```
https://seu-usuario.github.io/seu-repo
```

**Exemplo:**
```
https://denisegts.github.io/calculoTempoTrabalho
```

---

### Opção 2: Streamlit Cloud (Streamlit App)

#### Passo 1: Garantir que os arquivos estão no repositório
```bash
git add app.py requirements.txt
git commit -m "feat: Add Streamlit web app"
git push origin web-interface
```

#### Passo 2: Deploy no Streamlit Cloud
1. Acesse https://share.streamlit.io/
2. Clique em "Deploy an app"
3. Preencha com:
   - **GitHub repository:** `denisegts/calculoTempoTrabalho`
   - **Branch:** `web-interface`
   - **Main file path:** `app.py`
4. Clique em "Deploy"

#### Passo 3: Acessar a aplicação
Streamlit fornecerá um URL como:
```
https://seu-app-123456.streamlit.app
```

---

### Opção 3: Vercel (HTML/JS - Premium)

1. Acesse https://vercel.com/
2. Importe seu repositório GitHub
3. Configure:
   - **Framework:** Other
   - **Root Directory:** `.`
4. Deploy

---

### Opção 4: Render (Streamlit - Free Tier)

1. Acesse https://render.com/
2. Clique em "New +"
3. Selecione "Web Service"
4. Conecte seu repositório GitHub
5. Configure:
   - **Name:** calculoTempoTrabalho
   - **Runtime:** Python 3
   - **Build command:** `pip install -r requirements.txt`
   - **Start command:** `streamlit run app.py`
6. Deploy

---

## 📊 Comparação: HTML vs Streamlit

| Aspecto | HTML/JS | Streamlit |
|---------|---------|-----------|
| **Velocidade** | ⚡ Super rápido | 🚀 Rápido |
| **Tamanho** | 📦 ~10KB | 📦 ~100MB (instalação) |
| **Deploy** | 🟢 Muito fácil | 🟢 Fácil |
| **Custo** | 💰 Grátis | 💰 Grátis |
| **Customização** | 🎨 Total | 🎨 Limitada |
| **Responsivo** | 📱 Sim | 📱 Sim |
| **Interatividade** | ✅ Boa | ✅ Excelente |
| **Backend** | ❌ Não | ✅ Sim (Python) |

---

## 🔧 Troubleshooting

### GitHub Pages não funciona
- Verifique se o arquivo está em `web/index.html`
- Aguarde 1-2 minutos após o push
- Limpe o cache do navegador (Ctrl + Shift + Delete)

### Streamlit não carrega
- Verifique se `requirements.txt` tem `streamlit>=1.28.0`
- Certifique-se que o arquivo é `app.py` (não `main.py`)
- Reinicie o app

### App muito lenta
- HTML/JS é mais rápido que Streamlit
- Considere usar GitHub Pages para o HTML

---

## 📝 Exemplo de Fluxo Completo

```bash
# 1. Clonar o repositório
git clone https://github.com/denisegts/calculoTempoTrabalho.git
cd calculoTempoTrabalho

# 2. Mudar para branch web-interface
git checkout web-interface

# 3. Testar localmente (HTML)
open web/index.html

# 4. Ou testar localmente (Streamlit)
pip install -r requirements.txt
streamlit run app.py

# 5. Fazer changes
# ... edite os arquivos ...

# 6. Fazer commit
git add .
git commit -m "Update web interface"

# 7. Push para GitHub
git push origin web-interface

# 8. GitHub Pages / Streamlit Cloud atualiza automaticamente!
```

---

## 🎯 Próximos Passos

- [ ] Escolher entre HTML/JS ou Streamlit
- [ ] Deploy online (GitHub Pages ou Streamlit Cloud)
- [ ] Compartilhar o link com amigos
- [ ] Coletar feedback e melhorar
- [ ] Adicionar novos recursos

---

## 📞 Suporte

Se tiver problemas:
1. Verifique a seção **Troubleshooting**
2. Abra uma [issue no GitHub](https://github.com/denisegts/calculoTempoTrabalho/issues)
3. Consulte a documentação oficial:
   - [GitHub Pages](https://docs.github.com/pages)
   - [Streamlit Cloud](https://docs.streamlit.io/deploy/streamlit-cloud)

---

**Desenvolvido com ❤️ por @denisegts**
