# Coleção de noticias do site ARQUISP.ORG.BR
> Webscrapping dos dados da seção de notícias do site Arquidiose de SP, com uso de Python.

___Projeto pessoal___ 
**@author**: sliatecinos

## Instalação das dependências usadas no scrapping

Fazer a instalação via pip:
```bash
pip install scrapy
```

## Bloco de captura dos dados
```python
import scrapy 

# Função de recuperação dos dados (Html scrap)
def recupera_noticia(response):
..    
    # html DIV tags infos
    title = response.css('div.title-box')
    h1 =  title.css('div.node_titulo h1::text').get()

    box = response.css('div.box-corpo')
    corpo = box.css('div div div div.region')
    content = corpo.css('div div.content div.node')
    clearfix = content.css('div.-content')

    chamada = clearfix.css('div.field.field-name-field-out-noticia-chamada div div::text').get()

    postdate = clearfix.css('div.noticia_node_data-e-fonte div span::text').get()

    noticia = clearfix.css('div.noticia_corpo p *::text')
    noticiafinal = ' '.join(noticia.getall())
..    
    
```

## Estrutura do projeto

    .
    ├── ...             
    ├── .pytest_cache             # Compiled files (alternatively `dist`)
    ├── .vscode                   # Compiled files (alternatively `dist`)
    ├── README.md                  
    └── noticiasarquisp              # Source files (alternatively `py`)
        ├── __pycache__              # Compiled files (alternatively `dist`)
        └── spiders                  # Runner "spider" location
            └── __pycache__          # Compiled files (alternatively `dist`)

## Links externos

Site de Scrapy: [dj](https://arquisp.org.br/)

Scrapy - official documentation: [DOCS](https://docs.scrapy.org/en/latest/index.html)
