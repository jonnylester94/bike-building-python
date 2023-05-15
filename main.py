import math
from custom_exceptions import *

class Component:
    potential_conditions = ['Broken', 'Fragile', 'Satisfactory', 'Good', 'Pristine']
    # as %... broken: 0, fragile: 1-25, sat: 26-50, good: 51-75, p: 76-100

    def __init__(self, current_state, max_lifespan):
        try:
            if current_state <= 100:
                self.current_state = current_state
            else:  
                raise InvalidInput()
            if max_lifespan >= 0:
                self.max_lifespan = max_lifespan
            else:  
                raise InvalidInput()  
        except: 
            raise InvalidInput() 


    def check_condition(self):
        index = max(math.ceil(self.current_state / 25), 0)
        print(f'This component is {self.potential_conditions[index]}!')
        return self.current_state


class Bell(Component):

    def __init__(self, current_state, max_lifespan):
        super().__init__(current_state, max_lifespan)

    def warn_pedestrian(self):
        if self.current_state <= 0:
            print('bell is broken!')
        else: 
            print('bike incoming!')
            self.current_state -= 100 / self.max_lifespan


class Brakes(Component):

    def __init__(self, current_state, max_lifespan):
        super().__init__(current_state, max_lifespan)

    def squeeze_brakes(self):
        if self.current_state <= 0:
            print('brakes are broken!')
        else:
            print('screeching to a halt!')
            self.current_state -= 100 / self.max_lifespan


class Chain(Component):

    def __init__(self, current_state, max_lifespan):
        super().__init__(current_state, max_lifespan)

    def propels_bike(self):
        if self.current_state <= 0:
            print('chain needs more oil!')
        else: 
            print('accelerating!')
            self.current_state -= 100 / self.max_lifespan


class Tyres(Component):

    def __init__(self, current_state, max_lifespan):
        super().__init__(current_state, max_lifespan)

    def provides_grip(self):
        if self.current_state <= 0:
            print('tyres need inflating!')
        else: 
            print('keep cycling!')
            self.current_state -= 100 / self.max_lifespan


class Pedals(Component):

    def __init__(self, current_state, max_lifespan):
        super().__init__(current_state, max_lifespan)

    def holds_foot(self):
        if self.current_state <= 0:
            print('pedals need replacing!')
        else: 
            print('feet are supported!')
            self.current_state -= 100 / self.max_lifespan


class Bike:

    def __init__(self, Bell, Brakes, Chain, Tyres, Pedals):
        self.bell = Bell
        self.brakes = Brakes
        self.chain = Chain
        self.tyres = Tyres
        self.pedals = Pedals

    def ride(self):
        if min(self.bell.current_state, self.brakes.current_state, self.chain.current_state, self.tyres.current_state, self.pedals.current_state) <= 0:
            print('Take me to the repair shop!')
            return 'Take me to the repair shop!'

# if all components are good or pristine

        elif self.bell.current_state >= 51 and self.brakes.current_state >= 51 and self.chain.current_state >= 51 and self.tyres.current_state >= 51 and self.pedals.current_state >= 51:
            self.bell.warn_pedestrian()
            self.brakes.squeeze_brakes()
            self.chain.propels_bike()
            self.tyres.provides_grip()
            self.pedals.holds_foot()
            print('What an excellent ride!')
            return 'What an excellent ride!'

# if any component is fragile but none are broken

        elif self.bell.current_state or self.brakes.current_state or self.chain.current_state or self.tyres.current_state or self.pedals.current_state < 25 and self.bell.current_state and self.brakes.current_state and self.chain.current_state and self.tyres.current_state and self.pedals.current_state != 0:
            self.bell.warn_pedestrian()
            self.brakes.squeeze_brakes()
            self.chain.propels_bike()
            self.tyres.provides_grip()
            self.pedals.holds_foot()
            print('A great ride but part of me is about to break!!')
            return 'A great ride but part of me is about to break!'

# standard ride
        else:
            self.bell.warn_pedestrian()
            self.brakes.squeeze_brakes()
            self.chain.propels_bike()
            self.tyres.provides_grip()
            self.pedals.holds_foot()
            
            
    def ring_bell(self):

        if self.bell.current_state >= 51 and self.brakes.current_state >= 51 and self.chain.current_state >= 51 and self.tyres.current_state >= 51 and self.pedals.current_state >= 51:
            print('Ring! Ring! Ring!')
            return 'Ring! Ring! Ring!'


        elif min(self.bell.current_state, self.brakes.current_state, self.chain.current_state, self.tyres.current_state, self.pedals.current_state) == 0:
            print('The bell fell off!')
            return 'The bell fell off!'

        elif min(self.bell.current_state, self.brakes.current_state, self.chain.current_state, self.tyres.current_state, self.pedals.current_state) != 0 and min(self.bell.current_state, self.brakes.current_state, self.chain.current_state, self.tyres.current_state, self.pedals.current_state) < 26:
            print('Ring! Cling...')
            return 'Ring! Cling...'

        else: 
            print("I am in mixed condition!")
            return "I am in mixed condition!"


class RacingBike(Bike):
    pass
