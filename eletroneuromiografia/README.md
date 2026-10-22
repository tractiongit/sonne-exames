# Landing page — Eletroneuromiografia

Nova página estática em `/eletroneuromiografia/`, preparada em 22/10/2026. O `index.html` da raiz continua sendo a página atual de exames.

## Execução local

Na raiz do repositório: `python -m http.server 8765 --bind 127.0.0.1`.
Abrir `http://127.0.0.1:8765/eletroneuromiografia/`.
Não há dependências de build. Publicar a pasta junto com os assets já existentes da raiz. O servidor deve servir diretórios com `index.html` e redirecionar a rota sem barra final para a rota com barra.

## Conteúdo e assets

- Referência visual: páginas Sonne de otoneurologia e neuropediatria (azul, fundos claros, tipografia e marca).
- Informações de exame, modalidades, endereços e WhatsApp: página atual `../index.html`.
- Fotos reais reutilizadas de `../assets/images/exames/eletroneuromiografia.webp` e `../assets/images/clinica/IMG_0483.webp`.
- Logo horizontal oficial enviado pelo usuário em 22/10/2026, preservado como PNG transparente; fonte Inter hospedada localmente com licença OFL em `assets/`.
- Valores, duração, entrega de laudo, preparo e cobertura de planos são encaminhados à equipe; nenhuma condição comercial não confirmada foi anunciada.

## Medição e teste

Mantém o container `GTM-NR84NND4` e o evento `cta_click` da página atual, com os campos `cta_label`, `cta_url` e `page_path`. Acrescenta `landing_page: enmg_v1`, `exam` e `unit`. Os links das unidades iniciam mensagens específicas, e todos funcionam sem JavaScript. Os eventos não levam dados de pacientes. O container carrega somente no domínio de produção para não contaminar a medição com QA local ou preview.

Antes de direcionar tráfego do Google Ads: validar no Tag Assistant se os gatilhos reais do container aceitam a nova rota/labels e se a conversão dispara uma única vez. O teste local verifica o dataLayer; não comprova recebimento pelo Ads. Nenhum container ou campanha foi alterado nesta implementação. Clique no WhatsApp não equivale a agendamento confirmado.

Para o experimento de página, usar esta URL no braço experimental, preservando a definição de conversão do controle. Avaliar também contatos qualificados/agendamentos; não mudar anúncio, orçamento e página juntos.

## Verificação

Chromium nas larguras 320, 390, 768, 1024 e 1440 px: sem overflow horizontal, imagens e fonte carregadas, âncoras válidas, FAQ por clique e teclado, evento único de CTA com unidade correta, sem erros de JS/HTTP. Links e FAQ também verificados sem JavaScript. Conferência visual desktop e celular; preview e script de QA ficam fora do repositório.

Status: publicação das duas páginas solicitada pelo usuário em 22/10/2026. Configuração do experimento e ativação das campanhas são etapas posteriores.

## Revisão visual — 22/10/2026

Ajuste solicitado com referência direta a https://neurotorrino.clinicasonne.com.br/: Inter variável, escala de títulos e textos ampliada, marca e avatar nas proporções da referência, fundo fotográfico/abstrato original, botões em pílula, cards arredondados e tratamento consistente de espaços e cores. Conteúdo e eventos de conversão preservados.

## Versão Unimed

Rota `/eletroneuromiografia/unimed/`, com CSS, JavaScript, fonte, logo e imagens compartilhados. Atendimento de ENMG pela Unimed em Campinas e Hortolândia confirmado pelo usuário em 22/10/2026. A página destaca o convênio e orienta consultar modalidade, condições e eventual autorização com a equipe, sem prometer cobertura de todos os planos ou modalidades.

Todos os CTAs desta versão incluem ENMG e Unimed na mensagem. Links das unidades mantêm a cidade. O evento `cta_click` usa o caminho real, `landing_page: enmg_unimed_v1` e `coverage: unimed`; o controle mantém `enmg_v1`. Validação adicional das duas rotas e de todos os assets por HTTP 200; evento de clique conferido para as duas variantes com identificação e caminho próprios.

Publicação autorizada no mesmo repositório/Cloudflare Pages. Página original `/` preservada. Nenhuma campanha ou orçamento alterado.
