import scrapy
import lxml
from parse.items import Import

class QuotesSpider(scrapy.Spider):
    name = "sport"

    def start_requests(self):
        url = 'https://sports.giocodigitale.it/it/sports';
        yield scrapy.Request(url=url, callback=self.parse)
    # import pdb; pdb.set_trace()
    def parse(self, response):
        html = lxml.html.fromstring(response.text);
        result = Import();
        for block in html.xpath('//div[@class="highlights-widget ui-widget-content js-mg-form mg-widget"]'):
            title = block.cssselect('h3')[0].text;
            division = '';
            for row in block.cssselect('.mg-table .mg-event-row'):
                if row.cssselect('.mg-group-header .mg-group-header-link'):
                    division = row.cssselect('.mg-group-header-link')[0].text;
                else:
                    result['title'] = title;
                    result['name'] = row.cssselect('.js-mg-tooltip')[0].text_content();
                    result['division'] = division;
                    result['date'] = row.cssselect('.mg-datetime-column')[0].text_content();
                    result['finale_one'] = row.cssselect('.mg-option-button__option-odds')[0].text_content();
                    result['finale_x'] = row.cssselect('.mg-option-button__option-odds')[1].text_content();
                    result['finale_two'] = row.cssselect('.mg-option-button__option-odds')[2].text_content();
                    result['tempo_one'] = row.cssselect('.mg-option-button__option-odds')[3].text_content();
                    result['tempo_x'] = row.cssselect('.mg-option-button__option-odds')[4].text_content();
                    result['tempo_two'] = row.cssselect('.mg-option-button__option-odds')[5].text_content();

                yield result;
