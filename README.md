# 🐧 dashboard_linux

Projeto desenvolvido em **Python** com foco em **monitoramento de recursos do sistema Linux**, utilizando interface gráfica via **Streamlit** e visualização de dados com **Altair**.
Este projeto faz parte do meu processo de aprendizado prático em **Python, Linux, visualização de dados e arquitetura de aplicações**, aplicando conceitos utilizados em ambientes reais de desenvolvimento.

---

## 📌 Objetivo do Projeto

Desenvolver uma aplicação capaz de **coletar, processar e exibir informações do sistema operacional Linux em tempo real**, de forma clara e organizada.

Atualmente, o projeto monitora:

* 🧠 Uso de **CPU**
* 💾 Uso de **memória RAM**
* 🗄️ Uso de **disco**

O foco principal é **aprendizado contínuo**, organização de código, boas práticas em Python e construção de um projeto evolutivo.

---

## 🖥️ Funcionalidades

* Interface gráfica web com **Streamlit**
* Atualização automática dos dados
* Indicadores visuais (KPIs) para leitura rápida
* Gráficos em tempo real com **Altair**
* Histórico de dados utilizando `st.session_state`
* Execução focada em ambiente **Linux**
* Estrutura preparada para futuras expansões (ex: integração com **SLM/IA**)

---

## 🛠️ Tecnologias Utilizadas

* **Python 3**
* **Linux**
* **Streamlit**
* **Altair**
* **psutil**
* **Pandas**
* **Git e GitHub**
* **Black Formatter** (padronização de código)

---

## 📁 Estrutura do Projeto

```bash
dashboard_linux/
├── main.py
├── requirements.txt
├── README.md
├── .gitignore
├── .editorconfig
└── venv/
```

---

## 🚧 Próximos Passos

* 📊 Aprimorar visualização com novos gráficos
* 🚨 Implementar alertas (ex: CPU acima de determinado limite)
* 🧠 Integrar **SLM / IA** para análise dos dados do sistema
* 📦 Estudar empacotamento da aplicação para distribuição futura

---

## ▶️ Como Executar o Projeto

```bash
# criar e ativar ambiente virtual
python -m venv venv
source venv/bin/activate

# instalar dependências
pip install -r requirements.txt

# executar aplicação
streamlit run main.py
```

---

## 👤 Autor

**Arthur Fernandes Barros**
Estudante de **Sistemas para a Internet**
Interesses: **Python, Linux, Visualização de Dados e Inteligência Artificial**
