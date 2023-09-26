import abc, math

class Vehicule:
    def __init__(self, porte = 2):
        self.porte = porte
        
        
class Animal:
    def __init__(self, patte = 4, queue = False):
        self.patte = patte
        self.queue = queue
        
        
class Deplacement(abc.ABC):
    
    def __init__(self, value):
        self.value = value
        super().__init__()
        
    
    @property
    @abc.abstractmethod
    def x(self):
        return self._x
        
    @x.setter
    def set_x(self, value):
    	self._x = value
        
      
    @property
    @abc.abstractmethod
    def y(self):
        return self._y
    
    @y.setter
    def set_y(self, value):
    	self._y = value
    
    
    @property
    @abc.abstractmethod
    def z(self):
        return self._z
    
    @z.setter
    def set_z(self, value):
    	self._z = value

    
    @abc.abstractmethod
    def move_to(zone : str, x : float = None, y : float = None, z : float = None):
        print(f"se déplace vers {x}, {y}, {z} en ")
        
        
class Volant(Deplacement):

    def move_to(zone : str, x : float = None, y : float = None, z : float = None):
        if z > 0:
            print(f"se déplace vers {x}, {y}, {z} en volant")
        else:
            return ValueError
        
    
class Courant(Deplacement):
    
    def move_to(zone : str, x : float = None, y : float = None, z : float = None):
        if z == None and zone == "terre":
            print(f"se déplace vers {x}, {y} en courant")
            
        else:
            return ValueError
        
        
class Marchant(Deplacement):

    def move_to(zone : str, x : float = None, y : float = None, z : float = None):
        if z == None and zone == "terre":
            print(f"se déplace vers {x}, {y} en marchant")
        else:
            return ValueError
            
        
class Roulant(Deplacement):
    def move_to(zone : str, x : float = None, y : float = None, z : float = None):
        if z == None and zone == "terre":
            print(f"se déplace vers {x}, {y} en roulant")
        else:
            return ValueError


class Flotant(Deplacement):
    
    def move_to(zone : str, x : float = None, y : float = None, z : float = None):
        if z == None and zone == "mer":
            print(f"se déplace vers {x}, {y} en flotant" )
        else:
            return ValueError
        
      
class Nageant(Deplacement):
    def move_to(zone : str, x : float = None, y : float = None, z : float = None):
        if z < 0 and zone == "mer":
            print(f"se déplace vers {x}, {y}, {z} en nageant")
        else:
            return ValueError 
            
        
        
class Humain(Animal):
    
    def movement(zone : str, x : float = None, y : float = None, z : float = None):
        
        dist = math.dist((0, 0), (x, y))
        
        if zone == "mer" and z < 0:
            Nageant.move_to(zone, x, y, z)
        elif zone == "mer" and z == None:
            Flotant.move_to(zone, x, y, z)
        elif zone == "terre" and dist > 2.0:
            Courant.move_to(zone, x, y, z)
        elif zone == "terre" and dist < 10.0:
            Courant.move_to(zone, x, y, z)
        else:
            Marchant.move_to(zone, x, y, z)
                

class VoitureSansPermis(Vehicule):

    def movement(zone : str, x : float = None, y : float = None, z : float = None):
        if zone == "terre":
            Roulant.move_to(zone, x, y, z)
        else:
            print("Car destroyed!")
            

class Berline(Vehicule):
    
    def movement(zone : str, x : float = None, y : float = None, z : float = None):
        if zone == "terre":
            Roulant.move_to(zone, x, y, z)
        else:
            print("Car destroyed!")

class Moto(Vehicule):

    def movement(zone : str, x : float = None, y : float = None, z : float = None):
        if zone == "terre":
            Roulant.move_to(zone = zone, x = x, y = y, z = z)
        else:
            print("Motorcycle destroyed!")

class Hors_Bord(Vehicule):

    def movement(zone : str, x : float = None, y : float = None, z : float = None):
        if zone == "mer" and z == None:
            Flotant.move_to(zone, x, y, z)
        else:
            print("Error! Your boat won't go far ;)")

class Spitfire(Vehicule):
    
    def movement(zone : str, x : float = None, y : float = None, z : float = None):
        if z > 0:
            Volant.move_to(zone, x, y, z)
        elif zone == "terre" and z == None:
            Roulant.move_to(zone, x, y, z)
        else:
            print("Error!")


class Cygne(Animal):

    def movement(zone : str, x : float = None, y : float = None, z : float = None):
        
        if z > 0:
            Volant.move_to(zone, x, y, z)
        elif zone == "mer" and z == None:
            Flotant.move_to(zone, x, y, z)
        elif zone == "mer" and z < 0:
            Nageant.move_to(zone, x, y, z)              
        elif zone == "terre":
            print("Cygne too fat for 'Terre'")

class Canard(Animal):

    def movement(zone : str, x : float = None, y : float = None, z : float = None):
        if z > 0:
            Volant.move_to(zone, x, y, z)
        elif zone == "mer" and z == None:
            Flotant.move_to(zone, x, y, z)
        elif zone == "mer" and z < 0:
            Nageant.move_to(zone, x, y, z)
        else:
            Marchant.move_to(zone, x, y, z)

class Poisson(Animal):
        
    def movement(zone : str, x : float = None, y : float = None, z : float = None):
        if zone == "mer" and z < 0:
            Nageant.move_to(zone, x, y, z)
        else:
            print("Dead fish!")

