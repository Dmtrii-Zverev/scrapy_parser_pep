import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        # получаем все строки вложенные в тег <tbody>.
        rows = response.css(
            'section#pep-content section#index-by-category tbody tr'
        )
        for row in rows:
            status, number, title, authors, other = row.css('td')
            next_page = number.css('a')[0]
            if next_page:
                yield response.follow(next_page, callback=self.parse_pep)

    def parse_pep(self, response):
        content = response.css('section#pep-page-section section#pep-content')
        number, name = content.css('h1::text').get().strip().split(' – ')
        status = content.css('dl dt:contains("Status") + dd abbr::text').get()
        data = {
            'number': number,
            'name': name,
            'status': status
        }
        yield PepParseItem(data)
