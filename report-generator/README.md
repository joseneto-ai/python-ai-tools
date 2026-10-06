# Report Generator — experimento educacional

Script de estudo que envia um dicionário de métricas à API da OpenAI para gerar um texto de resumo.

Os valores presentes no exemplo são dados de demonstração e não devem ser apresentados como resultados comerciais comprovados.

## Como executar

Com as dependências instaladas, entre nesta pasta:

```bash
cd report-generator
```

Crie um arquivo local chamado `.env`, seguindo `.env.example`:

```env
OPENAI_API_KEY=SUA_CHAVE_AQUI
```

Preencha a chave somente no arquivo local. Execute:

```bash
python generator.py
```

A chamada à API pode gerar cobrança.

## Saída

O script imprime o texto gerado e salva um arquivo no diretório de execução com nome semelhante a:

```text
report_20261006_220000.txt
```

Os números do nome representam data e hora em UTC. O nome padrão não é `report.txt`.

## Limitações atuais

- A IA recebe as métricas e redige o texto, mas o código não verifica seus cálculos ou conclusões.
- Dados agregados não permitem concluir automaticamente quais leads originaram cada agendamento.
- O relatório precisa ser revisado antes de qualquer uso real.
- Em caso de falha da API, o script pode salvar a mensagem de erro como conteúdo do arquivo.
- Ainda não há suíte de testes automatizados.

## Próximo passo

Aprender a calcular e validar métricas com Python, usando a IA apenas para redigir a partir de dados já conferidos.
