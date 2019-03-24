from simple.Scrapy import Scrapy
from simple.config import config
con=config()
scrapy=Scrapy()
scrapy.login(con.session(),con.Headers(),con.credintials())
scrapy.boards(con.session())
scrapy.scrapyparser(con.session())
#print()