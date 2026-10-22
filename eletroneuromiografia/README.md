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
- Marca copiada da página local de otoneurologia; fonte Montserrat hospedada localmente com licença OFL em `assets/`.
- Valores, duração, entrega de laudo, preparo e cobertura de planos são encaminhados à equipe; nenhuma condição comercial não confirmada foi anunciada.

## Medição e teste

Mantém o container `GTM-NR84NND4` e o evento `cta_click` da página atual, com os campos `cta_label`, `cta_url` e `page_path`. Acrescenta `landing_page: enmg_v1`, `exam` e `unit`. Os links das unidades iniciam mensagens específicas, e todos funcionam sem JavaScript. Os eventos não levam dados de pacientes. O container carrega somente no domínio de produção para não contaminar a medição com QA local ou preview.

Antes de direcionar tráfego do Google Ads: validar no Tag Assistant se os gatilhos reais do container aceitam a nova rota/labels e se a conversão dispara uma única vez. O teste local verifica o dataLayer; não comprova recebimento pelo Ads. Nenhum container ou campanha foi alterado nesta implementação. Clique no WhatsApp não equivale a agendamento confirmado.

Para o experimento de página, usar esta URL no braço experimental, preservando a definição de conversão do controle. Avaliar também contatos qualificados/agendamentos; não mudar anúncio, orçamento e página juntos.

## Verificação

Chromium nas larguras 320, 390, 768, 1024 e 1440 px: sem overflow horizontal, imagens e fonte carregadas, âncoras válidas, FAQ por clique e teclado, evento único de CTA com unidade correta, sem erros de JS/HTTP. Links e FAQ também verificados sem JavaScript. Conferência visual desktop e celular; preview e script de QA ficam fora do repositório.

Status: implementação para revisão. Publicação e configuração do experimento são etapas posteriores.
