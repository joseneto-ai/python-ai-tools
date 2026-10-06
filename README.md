# Python AI Tools — estudos em Python

Sou José Neto, estudante do segundo período de Engenharia de Computação no CEFET-MG. Conheço o básico de Python e estou aprofundando meus fundamentos.

Este repositório reúne scripts de estudo sobre processamento de dados e integração com IA. São experimentos educacionais em revisão, sem garantia de uso em produção.

## Objetivos de aprendizagem

- Praticar funções, dicionários, listas e tratamento de erros.
- Entender formatos de dados recebidos por webhooks.
- Estudar chamadas a APIs e processamento das respostas.
- Melhorar documentação e acrescentar testes conforme aprender.

## Scripts

| Pasta | Conteúdo | Dependências |
|---|---|---|
| [webhook-parser](./webhook-parser/README.md) | Normalização de exemplos de dados de formulário, JSON simples e mensagens de texto no formato de webhook da Meta. | Biblioteca padrão do Python. |
| [message-classifier](./message-classifier/README.md) | Experimento de classificação de mensagens usando a API da OpenAI. | `openai`, `python-dotenv` e chave de API. |
| [report-generator](./report-generator/README.md) | Experimento de geração de texto a partir de métricas fornecidas em um dicionário. | `openai`, `python-dotenv` e chave de API. |

## Como começar

Use Python 3.10 ou superior. A partir da raiz deste repositório, execute o parser:

```bash
python webhook-parser/parser.py
```

Esse exemplo não precisa de chave de API.

Para os experimentos com IA, instale as dependências em um ambiente virtual:

```bash
python -m pip install -r requirements.txt
```

As instruções de configuração estão nos READMEs de cada pasta. Chamadas à API podem gerar cobrança.

## Limitações atuais

- Os scripts ainda não incluem uma suíte de testes automatizados.
- O parser aceita estruturas específicas; não é um parser universal.
- O classificador não valida completamente os campos e valores retornados pelo modelo.
- O gerador não verifica os cálculos produzidos pela IA.
- Os exemplos não demonstram integração real com WhatsApp, n8n ou CRM.
- Não há resultados comerciais comprovados por este repositório.

O exemplo no formato de webhook da Meta é um estudo separado da minha experiência na hamburgueria, onde usei uma integração não oficial com WhatsApp.

## Próximos passos

1. Executar e compreender o parser.
2. Criar testes para entradas válidas, vazias e incompletas.
3. Melhorar a validação de dados.
4. Estudar os experimentos com IA depois de consolidar essa base.

## Autoria e revisão

José Neto — estudante de Engenharia de Computação no CEFET-MG.

Esta revisão de documentação e os pequenos ajustes propostos tiveram apoio de IA. Meu objetivo é compreender, executar e melhorar o código durante os estudos.
