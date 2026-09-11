
## Requisitos Funcionais (RF)

| ID | Descrição |
|----|-----------|
| RF01 | O sistema deve ser uma aplicação cliente-servidor sobre plataforma Web, com frontend executado no navegador (código baixado sob demanda) e backend na nuvem atendendo às requisições. |
| RF02 | O sistema deve expor uma API RESTful documentada para comunicação entre frontend e backend. |
| RF03 | O sistema deve controlar acesso por autenticação/autorização via provedor externo (Google, Apple, etc.). |
| RF04 | O sistema deve persistir dados de usuários em banco de dados. |
| RF05 | O sistema deve possuir documentação de modelagem de dados e de arquitetura. |
| RF06 | O sistema deve enviar e-mails e notificações aos usuários. |
| RF07 | O sistema deve registrar (log) todas as operações críticas dos usuários para análise posterior. |
| RF08 | O sistema deve possuir ambientes de desenvolvimento e de produção. |
| RF09 | O sistema deve ser implantado em nuvem via Infraestrutura como Código (IaC). |
| RF10 | O sistema deve ter implantação automática em produção via pipeline CI/CD. |

### Agenda de eventos

| ID | Descrição |
|----|-----------|
| RF11 | O sistema deve permitir a sugestão de cadastro de eventos de skate (nome, data, local, descrição, tipo/modalidade, organizador). |
| RF12 | O sistema deve permitir a visualização dos eventos.
| RF13 | O sistema deve permitir filtrar eventos por data, estado/cidade e tipo de evento. |
| RF14 | O sistema deve permitir que o usuário marque interesse/participação em um evento. |
| RF15 | O sistema deve notificar o usuário sobre eventos próximos aos quais demonstrou interesse. |
| RF16 | O sistema deve permitir que usuários autorizados (organizadores/admins) editem ou removam eventos cadastrados. |

### Mapeamento de pistas de skate

| ID | Descrição |
|----|-----------|
| RF17 | O sistema deve exibir um mapa com as pistas de skate cadastradas, geolocalizadas. |
| RF18 | O sistema deve permitir localizar pistas próximas à posição atual do usuário (geolocalização). |
| RF19 | O sistema deve permitir o cadastro de novas pistas por usuários (nome, endereço/coordenadas, tipo de pista, estrutura disponível). |
| RF20 | O sistema deve permitir que usuários avaliem pistas e deixem comentários. |
| RF21 | O sistema deve permitir o upload de fotos das pistas pelos usuários. |
| RF22 | O sistema deve calcular e exibir a avaliação média de cada pista com base nas avaliações dos usuários. |
| RF23 | O sistema deve permitir que o usuário visualize detalhes de uma pista (fotos, avaliações, comentários, localização). |

### Gestão de usuário

| ID | Descrição |
|----|-----------|
| RF24 | O sistema deve permitir que o usuário visualize e edite seu perfil (nome, foto, cidade). |
| RF25 | O sistema deve permitir que o usuário visualize seu histórico de eventos e pistas avaliadas/cadastradas. |

<br>

## Requisitos Não Funcionais (RNF)

| ID | Descrição |
|----|-----------|
| RNF01 | O sistema deve ter boa responsividade (adaptação a diferentes tamanhos de tela — desktop e mobile). |
| RNF02 | O sistema deve operar com baixa latência nas requisições. |
| RNF03 | O sistema deve operar com custo mínimo na nuvem. |
| RNF04 | O sistema deve suportar upload de imagens (fotos de pistas) com limite de tamanho e formato definidos (ex.: JPEG/PNG, até X MB), armazenadas em serviço de armazenamento de objetos (ex.: S3/Blob Storage) e não diretamente no banco. |
| RNF05 | O sistema deve escalar horizontalmente o backend conforme aumento de carga (ex.: picos de acesso perto de grandes eventos). |
| RNF06 | O sistema deve proteger dados sensíveis dos usuários (LGPD), especialmente dados de localização e imagens enviadas. |
| RNF07 | O sistema deve ter usabilidade adequada para uso em campo (via celular, muitas vezes fora de casa, ao visitar uma pista). |
| RNF08 | O sistema deve manter consistência dos dados de avaliação (nota média) mesmo sob concorrência de múltiplas avaliações simultâneas. |

---

