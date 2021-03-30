# Bot McDelivery

## Sumário

1. Introdução
2. Detalhamento
3. Conclusão

## Introdução

Alguns scripts desenvolvemos com alegria, mas esse eu desenvolvi com muito amor <3

### Objetivo

Automatizar o pedido do McDelivery.


## Detalhamento

### Configuração:

#### Criar arquivo config.py
```python
BASE_URL = 'https://mcdelivery.mcdonalds.com.br'
ZIPCODE = ''
NUMBER = ''
COMPLEMENT = ''
STANDARD_SNACK = '/4-por-19/p'
EMAIL = ''

```

### Fluxo

1. Preencher endereço com configurados
2. Realizar seleção dos lanches do pedido padrão
3. Confirmar pedido
4. Finalizar pedido

### Complicações

1. Dependendo do CEP o delivery não funciona
2. Existe um horário de funcionamento


## Conclusão

Referências:
- [Link do vídeo](https://drive.google.com/file/d/1jrTffwnK3zqLmESwHgCyMbV4aLwBOpnB/view?usp=sharing) 👨🏼‍🏫 - Demonstração