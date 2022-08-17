import scrapy 

class bbcSpider(scrapy.Spider):
    name = 'bbcnews'
    start_urls  = ['https://www.bbc.com/russian/topics/cez0n29ggrdt']

    def parse(self, response):
        for link in response.css('h2.bbc-1fyz53t.e47bds20 a::attr(href)'):
            yield response.follow(link, callback=self.parse_news)

            # for i in range (1, 41):
            #     next_page = f'https://www.bbc.com/russian/topics/cez0n29ggrdt?page={i}'
            #     yield response.follow(next_page, callback = self.parse)


    def parse_news(self, response):
        yield{
            'title':response.xpath('//h1[@id="content"]/text()').get(),
            'text':response.xpath('//p[@class="bbc-hhl7in e17g058b0"]/text()').getall(),
            'date':response.css('time.bbc-1dafq0j.e1mklfmt0::text').get(),
            'link':response.css('h2.bbc-1fyz53t.e47bds20 a::attr(href)').getall()                  

        }


        next_page = response.css('a.bbc-1bq9izx.e19602dz0 a::attr(href)').get() 
        if next_page is not None:
            yield response.follow(next_page,callback=self.parse )

        
        


    

    
    