import scrapy
import logging

from ..articles import recupera_noticia


logger = logging.getLogger('meuscraplog')


class NoticiasSpiderSpider(scrapy.Spider):
    name = 'noticias'

    start_urls = [
        'http://arquisp.org.br/noticias/todas'
    ]

    def parse(self, response):
        """
        Metodo de construct do spider crawl
        """
        url_arquisp = 'http://arquisp.org.br'

        li = response.css('li.pager-next')
        newslink = response.css('div[class*=views-field-field-out-noticia-img-destaque] div.field-content a::attr(href)')

        for link in newslink:
            next_page_url = url_arquisp + link.get()
            nova_noticia = scrapy.Request(next_page_url)
            nova_noticia.callback = recupera_noticia
            yield nova_noticia

            # page = response.url.split("/")[-2]
            page = response.url
            filename = '[%s]' % page
            # with open(filename, 'wb') as f:
            #     f.write(response.body)
            # self.log('Passing by address... %s' % filename)
            logger.info('Passando pelo http... %s', filename)

        if li is not None:
            a = li.css('a').attrib['href']
            a_next = url_arquisp + a

            next_page_panel = a_next
            logger.info('Passando pela http page... %s', next_page_panel)
            next_page_panel = response.urljoin(next_page_panel)
            yield scrapy.Request(next_page_panel, callback=self.parse)
        