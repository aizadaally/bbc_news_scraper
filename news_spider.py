import scrapy 


class NewsSpider(scrapy.Spider):
    name = 'newsbbc'
    start_urls = ['https://www.bbc.com/russian/topics/cez0n29ggrdt']

    def parse(self, response):
        for link in response.css('div.bbc-1mtos2m.e3hd7yi0 a::attr(href)'):
            yield response.follow(link, callback=self.parse_news)


        for i in range (1, 41):
            next_page = f'https://www.bbc.com/russian/topics/cez0n29ggrdt?page={i}'
            yield response.follow(next_page, callback = self.parse)



    
    def parse_news(self, response):
        yield {
            'title':response.css('h1.bbc-7ota8y.e1yj3cbb0::text').get(),
            'text': response.xpath('.//p/text()').getall(),
            'date':response.css('time.bbc-14xtggo.exyigsi0::text').get()

        }
        
             
        

