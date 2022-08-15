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
        with open ('pokeparsertest.csv', 'a', newline ='') as new_csv:
            csv_writer = csv.DictWriter(new_csv,fieldnames=tags)
            csv_writer.writerow(datalist)

                

    def poke_print(self,value):
        
        
        return self.datalist.get(value)


n=1
while n < 10:
    p1 = PokeScrapper(n)
    p1.poke_csv()
    print(n)
    n+=1



class PokeParser():

    def __init__(self):
        with open('pokeparser.csv', 'r') as csvfile:
            csvreader = csv.DictReader(csvfile)
            pokedata = []
            for pokemon in csvreader:
                pokedata.append(pokemon)
        self.pokedata = pokedata
        self.typelist = []
        self.abilitylist = []
        self.statlist = []
        self.crosschecker =[]

    def type_checker(self,type):


        
            for pokemon in self.pokedata:
                if type in pokemon['types']:
                    self.typelist.append(pokemon)
            
               
    def ability_checker(self,ability):


            for pokemon in self.pokedata:
                if ability in pokemon['abilities']:
                    self.abilitylist.append(pokemon)

            
    def stat_checker(self,list):
        
            for pokemon in self.pokedata:
                if int(pokemon[list[0]]) >= list[1]:
                    self.statlist.append(pokemon)
                     
    def type_ability_checker(self,list1,list2):
        for pokemon in list1:
            for pokemon2 in list2:
                if pokemon == pokemon2:
                    self.crosschecker.append(pokemon)


p1 = PokeParser()
p1.ability_checker('blaze')
p1.type_checker('dragon')

p1.stat_checker(['attack',120])
p1.type_ability_checker(p1.statlist,p1.typelist)
print(p1.crosschecker)
