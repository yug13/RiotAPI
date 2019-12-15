class Champion(object):
    
    def __init__(self, data):
        self.name = data['id']
        self.id = data['key']
        self.title = data['title']
        self.stats = data['stats']
        self.info = data['info']
    
    def create_entry(self):
        temp_dict = {'championId': self.id, 'championTitle': self.title, 'championStats': self.stats, 'championInfo': self.info}
        return temp_dict
