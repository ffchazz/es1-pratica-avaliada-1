# Estruturação de Processo: XP e Scrum

**Link do Quadro no GitHub Projects:**  
https://github.com/users/ffchazz/projects/1/views/1

---

## 1. Práticas de Extreme Programming (XP) Adotadas

A equipe da AgileTech utiliza o Scrum para gerenciar o fluxo de entregas e adota cinco práticas de engenharia do XP para assegurar a qualidade do código:

### 1.1 Desenvolvimento Guiado por Testes (Test-Driven Development - TDD)
* **Como funciona:** O desenvolvedor escreve o teste automatizado antes de implementar o código de produção, seguindo o ciclo de criar o teste com falha, escrever o código mínimo para passar e refatorar em seguida.
* **Integração com o Scrum:** É aplicado diariamente durante o desenvolvimento de cada história na Sprint. Nenhuma tarefa é movida para revisão sem os testes unitários correspondentes estarem passando.

### 1.2 Integração Contínua (Continuous Integration - CI)
* **Como funciona:** As alterações são integradas à branch principal diariamente através de Pull Requests, com execução automática da suíte de testes a cada envio.
* **Integração com o Scrum:** Evita problemas de integração no final do ciclo, garantindo que o incremento a ser demonstrado na Sprint Review esteja sempre estável.

### 1.3 Design Simples (Princípio YAGNI)
* **Como funciona:** O sistema é implementado para resolver estritamente os requisitos atuais conhecidos, evitando criar métodos, classes ou estruturas antecipadas (*You Aren't Gonna Need It*).
* **Integração com o Scrum:** Mantém o escopo da Sprint focado no que agrega valor imediato, acelerando a entrega e mantendo a base de código fácil de manter.

### 1.4 Refatoração Contínua (Refactoring)
* **Como funciona:** Melhoria constante da estrutura interna do código (remoção de duplicações, nomenclatura clara e simplificação de funções) sem alterar seu comportamento externo.
* **Integração com o Scrum:** Faz parte da rotina diária em cada tarefa e nas revisões de código, evitando o acúmulo de débito técnico entre as Sprints.

### 1.5 Padrões de Código (Coding Standards)
* **Como funciona:** Adoção de regras compartilhadas de estilo e formatação em toda a base de código (no ecossistema Python, uso das convenções da PEP 8 e tipagem com Type Hints).
* **Integração com o Scrum:** Garante consistência nos arquivos, facilitando a leitura durante os code reviews e permitindo que qualquer desenvolvedor trabalhe em qualquer parte do sistema.

---

## 2. Fluxo de Trabalho Semanal e Cronograma da Sprint

A equipe opera em **Sprints de 2 semanas (10 dias úteis)**, combinando as cerimônias do Scrum com o desenvolvimento guiado por XP.

### Cronograma da Sprint

| Dia / Momento | Cerimônia / Atividade | Duração | Participantes | Objetivo Principal |
| :--- | :--- | :--- | :--- | :--- |
| **Semana 1 - Seg (09:00)** | Sprint Planning | 2h | PO e Devs | Definir a meta da Sprint, selecionar as histórias do Product Backlog e planejar as tarefas técnicas. |
| **Diariamente (09:00)** | Daily Scrum | 15 min | Devs (PO opcional) | Alinhamento rápido: o que foi concluído ontem, o que será feito hoje e identificação de impedimentos. |
| **Semanas 1 e 2 (Diário)** | Desenvolvimento com XP | Contínuo | Devs | Execução das tarefas aplicando TDD, Design Simples, commits frequentes e abertura de Pull Requests. |
| **Semana 2 - Qui (14:00)** | Refinamento de Backlog | 1h | PO e Devs | Esclarecer dúvidas de negócio e detalhar critérios de aceite para a próxima Sprint. |
| **Semana 2 - Sex (15:00)** | Sprint Review | 1h | PO, Devs e Cliente | Demonstração prática do incremento funcional ao cliente para validação e coleta de feedback. |
| **Semana 2 - Sex (16:30)** | Sprint Retrospective | 45 min | PO e Devs | Avaliação do processo interno da equipe e definição de melhorias para o próximo ciclo. |

### Aplicação das Práticas XP ao Longo da Sprint
* **Início de cada tarefa:** Aplicação de TDD com a criação dos testes unitários para a história.
* **Durante a codificação:** Aplicação de Design Simples e padrões de código (PEP 8).
* **Ao concluir a tarefa:** Abertura de Pull Request para disparo da Integração Contínua e revisão por pares (*Code Review*).
* **Antes do merge:** Refatoração do código para manter a base limpa.

### Entregas Esperadas ao Final da Sprint
* Incremento de software funcional testado e validado nos critérios de aceite do PO.
* Suíte de testes automatizados executando com 100% de sucesso na esteira de CI.
* Código revisado e integrado na branch principal sem débitos técnicos pendentes.

---

## 3. Comparativo: Scrum vs. Kanban

| Critério | Scrum | Kanban | Abordagem Combinada (Scrumban) |
| :--- | :--- | :--- | :--- |
| **Cadência** | Iterações de tempo fixo (*time-boxes* de 1 a 4 semanas). | Fluxo contínuo de trabalho, sem iterações obrigatórias. | Mantém o ritmo de Sprints do Scrum com a visualização de fluxo contínuo do Kanban. |
| **Limites de Trabalho (WIP)** | Indireto: delimitado pela quantidade de itens planejados para a Sprint. | Direto: limites explícitos de itens permitidos simultaneamente por coluna. | Aplica limites numéricos de WIP nas colunas dentro do período da Sprint. |
| **Papéis** | Papéis formais definidos (Product Owner, Scrum Master e Desenvolvedores). | Não prescreve papéis fixos; adapta-se à estrutura existente. | Mantém os papéis do Scrum (PO priorizando e time técnico executando). |
| **Mudanças de Escopo** | Mudanças durante a Sprint são evitadas para proteger a meta do ciclo. | Mudanças de prioridade podem ocorrer a qualquer momento no topo do backlog. | Backlog da Sprint protegido, com flexibilidade gerenciada pelos limites de WIP. |
| **Métricas** | Velocidade da equipe (*Velocity*) e gráficos de Burndown. | Tempo de ciclo (*Cycle Time*), Tempo de entrega (*Lead Time*) e Vazão (*Throughput*). | Utiliza métricas de fluxo do Kanban para refinar a capacidade de estimativa das Sprints. |
| **Indicação de Uso** | Projetos de novos produtos com metas periódicas e validações frequentes com clientes. | Ambientes de suporte contínuo, manutenção e sustentação com demandas imprevisíveis. | Times de desenvolvimento de produto que buscam previsibilidade de entrega sem engessar o fluxo técnico diário. |
