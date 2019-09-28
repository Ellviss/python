
dates =[{'date':15,'mounth':'may'},
        {'date':16,'mounth':'may'},
        {'date':19,'mounth':'may'},
        {'date':17,'mounth':'june'},
        {'date':18,'mounth':'june'},
        {'date':14,'mounth':'july'},
        {'date':16,'mounth':'july'},
        {'date':14,'mounth':'august'},
        {'date':15,'mounth':'august'},
        {'date':17,'mounth':'august'},
        ]

duples = list({v['date']:v for v in dates}.values())
#duples = [x for n, x in enumerate(dates.) if x in dates[:n]]
print (duples)