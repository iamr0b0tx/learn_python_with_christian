class Animal:
    def __init__(self, sound, color, furry=True):
        self.color = color
        self.sound = sound
        self.furry = furry

    def __repr__(self):
        return 'Colour: {animal_color}\nSound: {animal_sound}\n'.format(animal_color=self.color, animal_sound=self.sound)
    
    def cry(self):
        print('Animal Cries {animal_sound} !!!\n'.format(animal_sound=self.sound))

    
class Dog(Animal):
    def __init__(self):
        super().__init__('bark', 'brown')

    def __repr__(self):
        return 'Animal Description\n=============\n Animal: {animal_name}\n{animal_description}\n'.format(animal_name='Dog', animal_description=super().__repr__())
    
##create a dog object
dog = Dog()
print('Animal object: {}'.format(dog))

##dog barks
dog.cry()

print(dog)
