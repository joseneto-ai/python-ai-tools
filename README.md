# Python AI Tools — estudos em Python

Sou José Neto, estudante de Engenharia de Computação no CEFET-MG. Estou aplicando meus estudos de Python em pequenos programas e aprofundando práticas de organização, validação de dados e tratamento de erros.

Este repositório reúne scripts de estudo sobre processamento de dados e integração com IA. São experimentos educacionais em revisão, sem garantia de uso em produção.

## Objetivos de aprendizagem

- Organizar programas em funções e módulos com responsabilidades claras.
- Tratar entradas incompletas e situações de erro.
- Compreender dados recebidos por webhooks e APIs.
- Aprender a validar as respostas de serviços externos.
- Criar testes e melhorar a documentação dos exemplos.

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

O exemplo no formato de webhook da Meta é um estudo separado da minha experiência em um negócio local, onde usei uma integração não oficial com WhatsApp.

## Próximos passos

1. Revisar o parser e documentar com clareza os formatos aceitos.
2. Acrescentar testes para entradas válidas, vazias e incompletas.
3. Melhorar a validação das respostas nos experimentos com IA.
4. Aplicar esses aprendizados em um projeto independente de comparação de tabelas de preços.

## Autoria e revisão

José Neto — estudante de Engenharia de Computação no CEFET-MG.

Esta revisão de documentação e os pequenos ajustes propostos tiveram apoio de IA. Meu objetivo é compreender, executar e melhorar o código durante os estudos.
