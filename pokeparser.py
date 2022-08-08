import requests as re
import json
 



class PokeParser():
    
    def __init__(self,name):
        self.name = name
        

    def pokedata(self):
        url = 'https://pokeapi.co/api/v2/pokemon/' + self.name
        result = re.get(url)

        data = result.text
        parse_json = json.loads(data)


        abilities = parse_json.get('abilities')
        name = parse_json['name']
        types = parse_json['types']
        stats = parse_json['stats']

        datalist={}

        datalist.update({'name': name})


        typelist=[]
        for i in range(len(types)):
            staginglist = types[i].pop('type')
            typelist.append(staginglist.pop('name'))
        datalist.update({'types' : typelist})
            
        abillist = []

        for i in range(len(abilities)):
            staginglist = abilities[i].pop('ability')
            abillist.append(staginglist.pop('name'))
        datalist.update({'abilities' :abillist})

        statdict = {}

        for i in range(len(stats)):
            staginglist = stats[i].pop('stat')
            statdict.update({staginglist.pop('name') : stats[i].pop('base_stat')})
            
        datalist.update({'stats': statdict})
        
        return datalist
       
   

    def poke_csv(self):
        pass
        

p1 = PokeParser('charizard')
p3 = PokeParser('unown')
print(p3.pokedata())