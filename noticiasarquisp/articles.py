# -*- coding: latin1 -*-
# import lxml.html as lh
# from io import StringIO


def recupera_noticia(response):
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

    #create a dictionary to store the scraped info
    scraped_news = {
        'data' : postdate,
        'titulo' : h1,
        'chamada' : chamada,
        'noticia' : noticiafinal,
    }

    #yield or give the scraped news to scrapy
    yield scraped_news

