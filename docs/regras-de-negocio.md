# Regras de negócio 

## 1. Acesso e Permissões
* **Autenticação Externa:** O usuário deve realizar login por meio de um provedor externo.
* **Controle de Acesso Baseado em Perfil (RBAC):** O usuário só poderá executar ações permitidas pelo seu perfil:
  * **Visitante:** Acesso a consultas e interações simples.
  * **Usuário:** Permissões estendidas para criação e edição de avaliações e particiação de eventos.
  * **Administrador:** Acesso total para gestão, moderação e controle do sistema.

---

## 2. Perfil e Histórico
* **Edição de Perfil:** O usuário pode editar suas próprias informações de perfil.
* **Consulta de Histórico:** O usuário pode consultar todo o seu histórico no sistema, incluindo:
  * Eventos salvos / participações;
  * Pistas cadastradas;
  * Avaliações realizadas;
  * Comentários publicados;
  * Fotos enviadas.

---

## 3. Gestão de Eventos
* **Ações do Usuário:**
  * Consultar e filtrar eventos ;
  * Sugerir novos eventos;
  * Demonstrar interesse em eventos existentes.
* **Ações do Administrador:** Gerenciar (criar, editar, remover ou aprovar) todos os eventos da plataforma.

---

## 4. Gestão de Pistas
* **Geolocalização e Mapa:** Usuários podem consultar pistas diretamente em uma interface de mapa e buscar pistas próximas à sua localização atual.
* **Cadastro e Detalhes:** Usuários podem solicitar o cadastro de novas pistas no sistema e visualizar detalhes completos de qualquer pista existente.

---

## 5. Avaliações e Conteúdo
* **Contribuições de Usuário:** Usuários podem avaliar, comentar e enviar fotos das pistas.
* **Limites e Formatos:** As submissões devem respeitar os limites de tamanho e os formatos de arquivo permitidos pela plataforma.
* **Unicidade de Avaliação:** Cada usuário pode possuir apenas uma avaliação ativa por pista. Novas avaliações para a mesma pista devem atualizar a avaliação existente.

---

## 6. Média das Avaliações
* **Cálculo Consistente:** A média de nota de cada pista deve considerar exclusivamente avaliações válidas/ativas.
* **Concorrência:** O cálculo e a atualização da média devem ser tratados corretamente mesmo quando houver submissões e avaliações simultâneas (concorrência).

---

## 7. Notificações
* **Eventos Próximos:** O sistema deve notificar os usuários interessados sobre eventos ocorrendo nas proximidades.
* **Atualizações de Eventos:** Notificar automaticamente os usuários interessados sempre que houver alterações importantes nos eventos aos quais demonstraram interesse.

---

## 8. Moderação de Conteúdo
* **Ações Administrativas:** Administradores têm permissão para editar, ocultar ou remover:
  * Eventos;
  * Pistas;
  * Avaliações;
  * Comentários;
  * Fotos.
* **Critérios de Moderação:** Remoções ou edições devem ocorrer em casos de conteúdo inadequado, ofensivo, spams ou registros duplicados.

---

## 9. Privacidade e Segurança
* **Proteção de Dados:** O sistema deve garantir a proteção e o sigilo de dados pessoais, imagens e dados de localização dos usuários.
* **Consentimento de Localização:** A localização geográfica do usuário só poderá ser acessada e utilizada mediante autorização prévia e expressa.

---

## 10. Auditoria e Operação
* **Registro de Logs:** Ações importantes (críticas ou administrativas) devem ser devidamente registradas em log para fins de auditoria.
* **Segregação de Ambientes:** Os ambientes (ex: Desenvolvimento, Staging, Produção) devem ser estritamente separados.
* **Automação e IaC:** As implantações (deployments) devem ser realizadas utilizando **Infraestrutura como Código (IaC)** e executadas por meio de pipelines automatizados de CI/CD.