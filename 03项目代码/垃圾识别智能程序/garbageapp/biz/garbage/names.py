class GarbageDAO:
    def __init__(self):
        self.garbage_data = ["plastic", "toothpick", "sarcocarp", "power_bank", "hanger", "cans", "bag", "clothes", "wine_bottle", "plush_toys", "pot", "leftover", "battery", "plug"]    
    
    def validate(self, garbage_name):
        return garbage_name.lower() in self.garbage_data