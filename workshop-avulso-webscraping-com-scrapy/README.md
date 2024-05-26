# workshop-avulso-webscraping-com-scrapy

Para obter as bibliotecas utilizadas, rode o comando abaixo dentro da pasta do projeto:
```bash
pip freeze > requirements.txt
```

Para rodar o webscraping usando o Scrapy, rode o comando abaixo dentro da pasta spiders:

```bash
scrapy crawl mercadolivre -o ../../data/data.json
```

Para rodar o transform usando o pandas, rode o comando abaixo dentro da pasta src:

```bash
python transform/main.py
```