# API Estoque

## Iniciando docker

Certifique-se de que tenha instalado o docker em sua maquina para rodar os comandos a seguir.

- Primeiro configure as variaveis de ambiente no arquivo .env

- Depois de configuradas, rode o comando:

```bash
    docker-compose up -d
```

- Com o container rodando corretamente, acesse:

```bash
    http://localhost:8081/
```

## Migrations db

- Primeiro rode

```bash
    flask db init
```

- Depois

```bash
    flask db migrate -m "Mensagem da migration"
```

- Depois

```bash
    flask db upgrade
```
