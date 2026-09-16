# Casos de Uso 

## 1. Atores

| Ator | Descrição |
|------|-----------|
| **Visitante** | Usuário não autenticado, com acesso limitado (somente consulta). |
| **Usuário** | Usuário autenticado, principal ator do sistema. Consulta agenda, mapeia pistas, avalia e interage. |
| **Administrador** | Usuário com permissão total, incluindo moderação de conteúdo (pistas, avaliações, eventos). |
| **Provedor de Autenticação Externo** | Ator externo (Google, Apple, etc.) responsável por autenticar o usuário. |
| **Sistema de Notificação** | Ator de suporte (interno) responsável pelo envio de e-mails/push. |

---

## 2. Lista de Casos de Uso

| ID | Nome | Ator principal | RF relacionado |
|----|------|-----------------|-----------------|
| UC01 | Autenticar-se no sistema | Usuário / Provedor Externo | RF03 |
| UC02 | Gerenciar perfil | Usuário | RF24 |
| UC03 | Consultar agenda de eventos | Visitante / Usuário | RF12 |
| UC04 | Filtrar eventos | Usuário | RF13 |
| UC05 | Cadastrar evento | Administrador | RF11 |
| UC06 | Editar/Remover evento | Administrador | RF16 |
| UC07 | Marcar interesse em evento | Usuário | RF14 |
| UC08 | Receber notificação de evento | Sistema de Notificação | RF06, RF15 |
| UC09 | Visualizar mapa de pistas | Visitante / Usuário | RF17 |
| UC10 | Buscar pistas próximas | Usuário | RF18 |
| UC11 | Cadastrar pista | Usuário | RF19 |
| UC12 | Avaliar pista | Usuário | RF20, RF22 |
| UC13 | Enviar foto da pista | Usuário | RF21 |
| UC14 | Visualizar detalhes da pista | Visitante / Usuário | RF23 |
| UC15 | Visualizar histórico pessoal | Usuário | RF25 |
| UC16 | Moderar conteúdo | Administrador | RF07 |

---

## 3. Descrição Detalhada dos Casos de Uso

### UC01 — Autenticar-se no sistema

- **Ator principal:** Usuário
- **Atores secundários:** Provedor de Autenticação Externo
- **Pré-condição:** Usuário possui conta em um provedor externo suportado (Google, Apple, etc.).
- **Fluxo principal:**
  1. Usuário seleciona a opção de login.
  2. Sistema apresenta os provedores de autenticação disponíveis.
  3. Usuário escolhe um provedor e é redirecionado.
  4. Provedor externo autentica o usuário e retorna um token.
  5. Sistema valida o token e cria/atualiza a sessão do usuário.
  6. Sistema redireciona o usuário para a página inicial autenticada.
- **Fluxo alternativo:** Se for o primeiro acesso, o sistema cria automaticamente um novo perfil de usuário com os dados básicos recebidos do provedor.
- **Fluxo de exceção:** Se a autenticação falhar, o sistema exibe mensagem de erro e mantém o usuário na tela de login.
- **Pós-condição:** Usuário autenticado, com sessão ativa.

---

### UC02 — Gerenciar perfil

- **Ator principal:** Usuário
- **Pré-condição:** Usuário autenticado (UC01).
- **Fluxo principal:**
  1. Usuário acessa a tela "Meu Perfil".
  2. Sistema exibe dados atuais (nome, foto, cidade).
  3. Usuário edita os campos desejados.
  4. Usuário confirma a alteração.
  5. Sistema valida e persiste os dados.
- **Pós-condição:** Perfil atualizado no banco de dados.

---

### UC03 — Consultar agenda de eventos

- **Ator principal:** Visitante ou Usuário
- **Fluxo principal:**
  1. Ator acessa a seção "Agenda".
  2. Sistema consulta e exibe os eventos cadastrados em formato de calendário/lista.
  3. Ator seleciona um evento para ver detalhes.
- **Pós-condição:** Eventos exibidos ao usuário.

---

### UC04 — Filtrar eventos

- **Ator principal:** Usuário
- **Pré-condição:** UC03 em execução.
- **Fluxo principal:**
  1. Usuário define filtros (data, cidade/estado, tipo de evento).
  2. Sistema aplica os filtros e retorna a lista atualizada.
- **Pós-condição:** Lista de eventos filtrada exibida.

---

### UC05 — Cadastrar evento

- **Ator principal:** Administrador
- **Pré-condição:** Administrador autenticado e com permissão.
- **Fluxo principal:**
  1. Administrador acessa "Novo Evento".
  2. Preenche nome, data, local, descrição, tipo/modalidade.
  3. Submete o formulário.
  4. Sistema valida os dados e persiste o novo evento.
  5. Sistema registra a operação no log (RF07).
- **Fluxo de exceção:** Dados inválidos → sistema exibe mensagens de erro e não persiste.
- **Pós-condição:** Evento disponível na agenda pública.

---

### UC06 — Editar/Remover evento

- **Ator principal:** Administrador
- **Pré-condição:** Evento previamente cadastrado (UC05).
- **Fluxo principal:**
  1. Ator seleciona o evento a ser editado/removido.
  2. Sistema verifica permissão do ator sobre o evento.
  3. Ator realiza a alteração ou confirma a remoção.
  4. Sistema atualiza/remove o registro e grava log da operação (RF07).
- **Fluxo de exceção:** Ator sem permissão → sistema nega a operação.
- **Pós-condição:** Evento atualizado ou removido.

---

### UC07 — Marcar interesse em evento

- **Ator principal:** Usuário
- **Pré-condição:** Usuário autenticado; evento existente.
- **Fluxo principal:**
  1. Usuário acessa detalhes de um evento.
  2. Usuário seleciona "Tenho interesse".
  3. Sistema associa o usuário ao evento.
  4. Sistema agenda notificações futuras para esse evento (inclui UC08).
- **Pós-condição:** Interesse registrado; usuário passa a receber lembretes.

---

### UC08 — Receber notificação de evento

- **Ator principal:** Sistema de Notificação
- **Ator secundário:** Usuário
- **Relação:** incluso de UC07
- **Fluxo principal:**
  1. Sistema verifica periodicamente eventos próximos com usuários interessados.
  2. Para cada usuário interessado, sistema dispara e-mail e/ou notificação push.
  3. Sistema registra o envio no log.
- **Pós-condição:** Usuário notificado sobre o evento.

---

### UC09 — Visualizar mapa de pistas

- **Ator principal:** Visitante ou Usuário
- **Fluxo principal:**
  1. Ator acessa a seção "Mapa de Pistas".
  2. Sistema carrega e exibe as pistas cadastradas geolocalizadas no mapa.
  3. Ator pode clicar em um marcador para ver resumo da pista.
- **Pós-condição:** Mapa exibido com as pistas.

---

### UC10 — Buscar pistas próximas

- **Ator principal:** Usuário
- **Pré-condição:** Permissão de geolocalização concedida pelo navegador.
- **Fluxo principal:**
  1. Usuário solicita "Pistas perto de mim".
  2. Sistema obtém a localização atual do dispositivo.
  3. Sistema calcula e retorna as pistas ordenadas por proximidade.
  4. Sistema exibe o resultado no mapa e/ou em lista.
- **Fluxo de exceção:** Localização negada → sistema solicita que o usuário informe manualmente uma cidade/endereço.
- **Pós-condição:** Lista de pistas próximas exibida.

---

### UC11 — Cadastrar pista

- **Ator principal:** Usuário
- **Pré-condição:** Usuário autenticado.
- **Fluxo principal:**
  1. Usuário seleciona "Cadastrar nova pista".
  2. Informa nome, endereço, tipo de pista, estrutura disponível.
  3. Opcionalmente anexa fotos (inclui UC13).
  4. Sistema valida e persiste a nova pista.
  5. Sistema registra a operação no log (RF07).
- **Pós-condição:** Pista disponível no mapa para todos os usuários.

---

### UC12 — Avaliar pista

- **Ator principal:** Usuário
- **Pré-condição:** Usuário autenticado; pista existente.
- **Fluxo principal:**
  1. Usuário acessa os detalhes de uma pista (UC14).
  2. Usuário atribui uma nota e, opcionalmente, um comentário.
  3. Sistema persiste a avaliação.
  4. Sistema recalcula a média de avaliação da pista (RF22), garantindo consistência sob concorrência (RNF09).
- **Pós-condição:** Avaliação registrada; nota média atualizada.

---

### UC13 — Enviar foto da pista

- **Ator principal:** Usuário
- **Pré-condição:** Usuário autenticado; pista existente.
- **Fluxo principal:**
  1. Usuário acessa os detalhes da pista.
  2. Seleciona "Adicionar foto" e escolhe o arquivo de imagem.
  3. Sistema valida formato/tamanho (RNF04) e envia a imagem ao armazenamento de objetos.
  4. Sistema associa a URL da imagem à pista.
- **Fluxo de exceção:** Arquivo inválido (formato/tamanho) → sistema rejeita e informa o motivo.
- **Pós-condição:** Foto disponível na galeria da pista.

---

### UC14 — Visualizar detalhes da pista

- **Ator principal:** Visitante ou Usuário
- **Fluxo principal:**
  1. Ator seleciona uma pista no mapa ou em uma lista.
  2. Sistema exibe nome, localização, estrutura, fotos, avaliação média e comentários.
- **Pós-condição:** Detalhes da pista exibidos.

---

### UC15 — Visualizar histórico pessoal

- **Ator principal:** Usuário
- **Pré-condição:** Usuário autenticado.
- **Fluxo principal:**
  1. Usuário acessa "Meu Histórico".
  2. Sistema lista eventos marcados como interesse, pistas cadastradas e avaliações feitas pelo usuário.
- **Pós-condição:** Histórico exibido.

---

### UC16 — Moderar conteúdo

- **Ator principal:** Administrador
- **Pré-condição:** Administrador autenticado.
- **Fluxo principal:**
  1. Administrador acessa painel de moderação.
  2. Visualiza pistas, avaliações, fotos ou eventos sinalizados/reportados.
  3. Administrador aprova, edita ou remove o conteúdo.
  4. Sistema registra a ação no log (RF07).
- **Pós-condição:** Conteúdo moderado; integridade da plataforma mantida.

---
