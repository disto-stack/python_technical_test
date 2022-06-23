'''
  En este ejemplo se utiliza Scrapy, para hacer 'web scraping' y poder obtener
  los datos de las ofertas de mercado libre por el dia del padre.

  Estas ofertas están en el link: https://listado.mercadolibre.com.co/_Deal_dia-del-padre-2022
'''

# Primero se instala scrapy, y posteriormente se importa
import scrapy 

# Se crea un Spider, donde se define el comportamiento al hacer scraping a determinado sitio
class MercadoLibreSpider(scrapy.Spider):
    name = "mercadolibre" # Nombre del spider
    
    # Se define el link o conjunto de links donde se va a extraer la información
    start_urls = [
        'https://listado.mercadolibre.com.co/_Deal_dia-del-padre-2022',
    ]

    # Se coloca esta linea para evitar error 403, de acceso denegado
    user_agent = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"

    # Se coloca esta constante para definir la codficación del texto en el archivo de salida
    FEED_EXPORT_ENCODING="utf-8"

    # En este método se hará el parseo y el como se exportará la información extraida
    def parse(self, response):
        # Buscamos en el sitio, la clase CSS del div que contenga cada una de los items con la información del producto,
        # y se recorre y posteriormente se retorna cada uno de estos
        for item in response.css('div.ui-search-result__content-wrapper'):
            yield {
                # Dentro de cada item se busca el elemento HTML y su clase CSS que contenga el nombre el del producto
                'nombre': item.css('h2.ui-search-item__title::text').get(), 
                # Dentro de cada item se busca el elemento HTML y su clase CSS que contenga el precio del producto
                'precio': item.css('span.price-tag-fraction::text').get(),
                # Dentro de cada item se busca el elemento HTML y su clase CSS que contenga el descuento del producto,
                # en caso de no haber descuento, se coloca 'Sin descuento'. Esto se válida mediante un condicional ternario
                'descuento': item.css('span.ui-search-price__discount::text').get()
                   if item.css('span.ui-search-price__discount::text').get() 
                   else 'Sin descuento',
            }

'''
  Para visualizar los datos se pueden utilizar lo siguientes comandos en la terminal:

  scrapy runspider exercise_7.py -O ofertas.xml (para exportar como archivo xml)
  scrapy runspider exercise_7.py -O ofertas.json (para exportar como archivo json)
  scrapy runspider exercise_7.py -O ofertas.csv (para exportar como archivo csv)
'''