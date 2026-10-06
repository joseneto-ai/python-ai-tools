# Message Classifier — experimento educacional

Script de estudo que envia uma mensagem de texto à API da OpenAI e tenta interpretar a resposta como JSON.

O prompt solicita as categorias `HIGH_INTENT`, `WARM`, `LOW_INTENT`, `URGENT` e `UNRELATED`. Em alguns erros, o código retorna `ERROR`.

## Como executar

Com as dependências instaladas, entre nesta pasta:

```bash
cd message-classifier
```

Crie um arquivo local chamado `.env`, seguindo o modelo de `.env.example`. Preencha sua chave somente no arquivo local:

```env
OPENAI_API_KEY=SUA_CHAVE_AQUI
```

Execute:

```bash
python classifier.py
```

O script envia as mensagens de exemplo à API. Essas chamadas podem gerar cobrança.

## Exemplo ilustrativo de resposta

```json
{
  "intent": "HIGH_INTENT",
  "confidence": "high",
  "reasoning": "A mensagem pergunta sobre preço e disponibilidade.",
  "recommended_action": "route_to_sales"
}
```

Esse exemplo descreve o formato solicitado; não registra uma execução verificada. A resposta real pode variar.

## Limitações

- O código interpreta JSON, mas ainda não valida completamente sua estrutura e seus valores.
- `confidence` é uma avaliação declarada pelo modelo, não uma medida de precisão validada.
- `URGENT` é uma categoria experimental; este script não foi validado para triagem clínica ou emergências.
- Não há integração implementada com WhatsApp, n8n, CRM ou equipe de atendimento neste script.
- Ainda não há avaliação de acerto com um conjunto de mensagens rotuladas.

## Objetivos de estudo

Compreender chamadas de API, prompts, respostas JSON e tratamento de erros.
