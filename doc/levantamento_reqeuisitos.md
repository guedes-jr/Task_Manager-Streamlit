## 📌 Levantamento de Requisitos  
### Projeto: Dashboard de Tarefas e Produtividade Pessoal  
### Objetivo:
Criar uma aplicação web simples, de uso pessoal, para gerenciar tarefas diárias, acompanhar a produtividade ao longo do tempo e gerar relatórios simples de desempenho.

---

### 🧩 Requisitos Funcionais (o que o sistema deve fazer)

1. **Cadastro e autenticação de usuários**
   - Registro pela conta google (gmail.com)
   - Login pela conta do google

2. **Cadastro de Tarefas**
   - Inserir título, descrição, categoria, prioridade, data de entrega e status (a fazer, em andamento, feito).
   - Marcar tarefas como concluídas.
   - Editar e excluir tarefas.

3. **Visualização de Tarefas**
   - Listar tarefas por filtros (por status, por data, por prioridade, por projeto).
   - Visualizar tarefas em uma tabela interativa.
   - Exibir estatísticas de produtividade (tarefas concluídas por semana/mês, média de tarefas por dia, etc).

4. **Relatórios de Produtividade**
   - Gráficos simples (barras, pizza, linha do tempo).
   - Exportar relatórios em PDF ou CSV.

5. **Armazenamento Local**
   - Salvar as tarefas em um arquivo local (ex: JSON, CSV ou SQLite).
   - Carregar automaticamente os dados na inicialização do app.

6. **Interface Simples e Intuitiva**
   - Layout dividido por abas: Tarefas | Estatísticas | Relatórios.
   - Inputs amigáveis (caixas de texto, data picker, sliders, etc).
   - Notificações ou mensagens de sucesso ao salvar/excluir.

---

### ⚙️ Requisitos Não Funcionais (como o sistema deve se comportar)

- Deve ser rápido e responsivo.
- Interface simples e acessível (não precisa ser complexa nem bonita demais).
- Portável: rodar localmente sem precisar de servidor web.
- Código limpo, modular, fácil de manter e expandir.

---

### 🧪 Requisitos Técnicos

- **Linguagem:** Python 3.x  
- **Framework:** Streamlit  
- **Armazenamento:** CSV ou SQLite  
- **Bibliotecas auxiliares:**
  - `pandas` (manipulação de dados)
  - `matplotlib` ou `plotly` (gráficos)
  - `datetime` (controle de datas)
  - `reportlab` ou `pdfkit` (gerar PDF, opcional)

---

### 🖥️ Interfaces e Telas

1. **Página de Cadastro de Tarefa**
   - Formulário com campos de texto, data, seleção múltipla.
   - Botão “Salvar Tarefa”.

2. **Página de Listagem de Tarefas**
   - Tabela interativa com filtros por status, prioridade, data.
   - Ações: Editar | Excluir | Marcar como concluída.

3. **Página de Estatísticas**
   - Gráficos de desempenho (tarefas por status, por data).
   - Indicadores: total de tarefas, tarefas por semana/mês, % concluídas.

4. **Página de Relatórios**
   - Geração de relatório PDF com resumo das tarefas do período.
   - Filtros por data e status antes de gerar o relatório.

---

### 🚀 Melhorias Futuras (Extras que você pode adicionar depois)

- Login simples com senha (para uso pessoal mesmo).
- Sincronização com Google Tasks ou Google Sheets.
- Backup automático em nuvem (Google Drive, Dropbox).
- Modo escuro / claro.
- Aplicativo desktop via PyInstaller.