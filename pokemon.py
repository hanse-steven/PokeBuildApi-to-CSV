class Pokemon:
    pokedexId: int
    name: str
    image: str
    sprite: str
    generation: int

    # stat
    hp: int
    attack: int
    defense: int
    special_attack: int
    special_defense: int
    speed: int

    # type:
    type: str

    # resistance
    type_fort: str
    type_faible: str

    def __init__(self, data: dict) -> None:
        self.pokedexId = data.get('pokedexId')
        self.name = data.get('name')
        self.image = data.get('image')
        self.sprite = data.get('sprite')
        self.generation = data.get('apiGeneration')

        stats = data.get('stats')
        self.hp = stats.get('HP')
        self.attack = stats.get('attack')
        self.defense = stats.get('defense')
        self.special_attack = stats.get('special_attack')
        self.special_defense = stats.get('special_defense')
        self.speed = stats.get('speed')

        self.type = ','.join([elm.get('name') for elm in data.get('apiTypes')])

        buffer_fort = []
        buffer_faible = []
        for elm in data.get('apiResistances'):
            if elm.get('damage_relation') == 'resistant':
                buffer_fort.append(elm.get('name'))
            elif elm.get('damage_relation') == 'vulnerable':
                buffer_faible.append(elm.get('name'))
        self.type_fort = ','.join(buffer_fort)
        self.type_faible = ','.join(buffer_faible)

    @staticmethod
    def header():
        return "pokedexId;name;image;sprite;generation;hp;attack;defense;special_attack;special_defense;speed;type;type_fort;type_faible"

    def to_line(self) -> str:
        return f"{self.pokedexId};{self.name};{self.image};{self.sprite};{self.generation};{self.hp};{self.attack};{self.defense};{self.special_attack};{self.special_defense};{self.speed};{self.type};{self.type_fort};{self.type_faible}"