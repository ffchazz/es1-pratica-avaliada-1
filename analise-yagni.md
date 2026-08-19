# Análise de Design Simples e Princípio YAGNI

## 1. Contexto e Requisitos Atuais do Sistema

O princípio **YAGNI** (*You Aren't Gonna Need It* — "Você não vai precisar disso") é um dos pilares do Design Simples no Extreme Programming (XP). Ele estabelece que os desenvolvedores não devem implementar funcionalidades, abstrações ou estruturas de dados baseadas em suposições sobre o futuro, focando apenas no que é estritamente necessário no presente.

Atualmente, o módulo de usuários da AgileTech possui apenas três requisitos funcionais:
1. **Cadastrar usuários** informando nome, e-mail e senha (com hash seguro e validação de e-mail duplicado).
2. **Fazer login** validando e-mail e senha.
3. **Listar todos os usuários** cadastrados.

Qualquer código além desses três requisitos viola o princípio YAGNI, gerando custo desnecessário de manutenção, maior superfície para bugs e complexidade acidental.

---

## 2. Violações de YAGNI na Classe `Usuario`

### 2.1 Atributos Desnecessários Identificados

* **`id` (gerado via UUID):** Não há requisito atual de identificador UUID exposto; a busca e autenticação são feitas diretamente pelo e-mail.
* **`data_cadastro`, `ultimo_login` e `historico_logins`:** Metadados de auditoria e telemetria de acessos que não foram solicitados pelo cliente.
* **`perfil` e `permissoes`:** Estrutura antecipada de controle de acesso baseado em papéis (RBAC - *Role-Based Access Control*), funcionalidade que não faz parte do escopo atual.
* **`configuracoes`:** Dicionário genérico para preferências de usuário inexistentes no momento.
* **`foto_perfil_url`, `telefone` e `endereco`:** Campos de cadastro estendido que não constam nos requisitos de registro básico.
* **`empresa`, `cargo` e `departamento`:** Dados corporativos especulativos adicionados sem demanda do Product Owner.

### 2.2 Métodos Desnecessários Identificados

* **`_gerar_id()`:** Método auxiliar para gerar UUID, dependente do atributo `id` não utilizado.
* **`adicionar_permissao()`, `remover_permissao()` e `tem_permissao()`:** Métodos de manipulação de regras de acesso (RBAC) prematuros.
* **`atualizar_configuracao()`:** Manipulação de configurações personalizadas inexistentes.
* **`registrar_login()`:** Registro de log de auditoria com data e IP não demandado.
* **`exportar_json()` e `exportar_xml()`:** Rotinas de serialização de dados adicionadas preventivamente sem necessidade de negócio.
* **`atualizar_foto_perfil()` e `atualizar_dados_profissionais()`:** Métodos de atualização de campos que foram removidos da entidade.

---

## 3. Violações de YAGNI na Classe `GerenciadorUsuarios`

### 3.1 Atributos Desnecessários Identificados

* **`cache`:** Mecanismo de cache manual em memória para buscas por ID. Para a escala inicial e os requisitos atuais, uma coleção simples em lista atende plenamente sem necessidade de camadas de cache prematuras.

### 3.2 Métodos Desnecessários Identificados

* **`_atualizar_cache()` e `buscar_por_id()`:** Métodos voltados à gestão do cache por ID, inexistente nos requisitos.
* **`buscar_por_perfil()` e `buscar_por_permissao()`:** Consultas filtradas baseadas no sistema de permissões especulativo.
* **`exportar_todos_json()` e `importar_usuarios_json()`:** Operações em lote de exportação/importação em JSON sem demanda funcional.
* **`gerar_relatorio_atividade()`:** Rotina analítica de métricas de uso prematura.

---

## 4. Impacto da Refatoração

A remoção de todos os elementos listados resultou em:
* **Redução drástica de linhas de código e dependências externas** (remoção dos módulos `json`, `xml.etree.ElementTree` e `datetime`).
* **Código coeso e legível**, onde cada classe e método possui uma única responsabilidade bem definida.
* **Facilidade de teste e manutenção**, mantendo o comportamento funcional exigido pelo sistema de forma direta e segura.
