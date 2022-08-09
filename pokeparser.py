import requests as re
import csv

class PokeScrapper():
    
    
    def __init__(self,name):
        self.name = name
        self.datalist = {}
        self.get_poke_data()
        
    
    def get_poke_data(self):
        url = 'https://pokeapi.co/api/v2/pokemon/' + str(self.name)
        result = re.get(url)

        parse_json = result.json()


        abilities = parse_json.get('abilities')
        name = parse_json['name']
        types = parse_json['types']
        stats = parse_json['stats']

        

        self.datalist.update({'name': name})


        typelist=[]
        for i in range(len(types)):
            staginglist = types[i]['type']
            typelist.append(staginglist['name'])
        self.datalist.update({'types' : typelist})
            
        abillist = []

        for i in range(len(abilities)):
            staginglist = abilities[i]['ability']
            abillist.append(staginglist['name'])
        self.datalist.update({'abilities' :abillist})

        statdict = {}

        for i in range(len(stats)):
            staginglist = stats[i]['stat']
            statdict.update({staginglist['name'] : stats[i]['base_stat']})
            
        self.datalist.update({'stats': statdict})
        return self.datalist
        
       
    def poke_csv(self):
        
        datalist = self.datalist
        
        tags = list(datalist.keys())
        with open ('pokeparser.csv', 'a', newline ='') as new_csv:
            csv_writer = csv.DictWriter(new_csv,fieldnames=tags)
            

            csv_writer.writerow(datalist)
                

    def poke_print(self,value):
        
        
        return self.datalist.get(value)


n=1
while n < 906:
    p1 = PokeScrapper(n)
    p1.poke_csv()
    print(n)
    n+=1


# 
