# Webhook Payload Parser — estudo de processamento de dados

Script educacional que transforma alguns formatos de dicionário Python em uma estrutura comum.

Um webhook é uma forma de um sistema enviar dados a outro quando um evento acontece. Este script estuda o processamento desses dados; ele não cria um servidor para receber webhooks.

## Formatos previstos

- `generic`: dicionário com campos como `sender_id`, `message` e `timestamp`.
- `webform`: dicionário com campos como `email`, `phone`, `message`, `body` ou `text`.
- `whatsapp`: exemplo de estrutura de mensagem de texto no formato de webhook da Meta.

A referência à Meta descreve o formato estudado. Não comprova uso da API oficial em uma implantação real e é separada da minha experiência na hamburgueria com integração não oficial.

## Como executar

Na raiz do repositório:

```bash
python webhook-parser/parser.py
```

Requer Python 3.10 ou superior e utiliza somente a biblioteca padrão.

O script imprime exemplos de remetente, mensagem e horário para os três formatos.

## Estrutura retornada

As funções retornam campos como `source`, `sender_id`, `message`, `timestamp` e `raw`.

O campo `raw` preserva os dados de entrada; eles não são anonimizados automaticamente.

No exemplo de WhatsApp, o timestamp `1700000000` corresponde a `2023-11-14T22:13:20+00:00`, em UTC.

## Limitações atuais

- A entrada esperada é um dicionário Python.
- O exemplo de WhatsApp lê somente a primeira entrada, a primeira alteração e a primeira mensagem.
- Eventos de status, múltiplas mensagens e diferentes tipos de mídia ainda não são tratados adequadamente.
- A validação de tipos e formatos é limitada.
- Uma origem desconhecida utiliza o parser genérico.

## Próximos passos

Criar testes para formulário, JSON simples, mensagem de texto válida, campos ausentes e timestamp inválido.
