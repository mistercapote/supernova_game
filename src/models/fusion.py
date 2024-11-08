from models.element import Isotope
import numpy as np
import json

class Fusion:
    def __init__(self, process, element_a, element_b, product, description):
        self.process = process # Nome do processo quimico que a fusão pertence
        self.element_a = element_a # Objeto da classe Isotope
        self.element_b = element_b # Objeto da classe Isotope ou FuntamentalParticle ou None
        self.product = product # Lista de Objetos das classes Isotope e FuntamentalParticle
        self.description = description # Texto falando um pouco sobre a fusão

    # Energia gerada pela reação
    def get_energy(self):
        U_TO_KG = 1.66053906660e-27
        J_TO_MEV =  6.242e12
        C_2 = (2.99792458e8)**2
        m_initial = self.element_a.mass + self.element_b.mass if self.element_b else self.element_a.mass
        m_final = sum([obj.mass for obj in self.product if isinstance(obj, Isotope)])
        energy_mev = (m_initial - m_final) * U_TO_KG * C_2 * J_TO_MEV
        return round(energy_mev, 4)
    
    @classmethod
    def from_dict(cls, ISOTOPES, PARTICLES, data):
        """Cria uma instância da classe a partir de um dicionário."""
        def aux(data):
            if data["element_b"] == None:
                return None
            elif "-" in data["element_b"]:
                return next((obj for obj in ISOTOPES if obj.name_isotope == data["element_b"]), None) 
            else:
                return next((obj for obj in PARTICLES if obj.symbol == data["element_b"]), None) 
        
        def aux2(data):
            resultado = []
            for each in data["product"]:
                if "-" in each:
                    resultado.append(next((obj for obj in ISOTOPES if obj.name_isotope == each), None) )
                else:
                    resultado.append(next((obj for obj in PARTICLES if obj.symbol == each), None) )
            return resultado

        return cls(
            process = data["process"], # Nome do processo quimico que a fusão pertence
            element_a = next((obj for obj in ISOTOPES if obj.name_isotope == data["element_a"]), None), # Objeto da classe Isotope
            element_b = aux(data), # Objeto da classe Isotope ou FuntamentalParticle ou None
            product = aux2(data), # Lista de Objetos das classes Isotope e FuntamentalParticle
            description = data["description"] # Texto falando um pouco sobre a fusão
        )

    @staticmethod
    def load_elements_from_json(ISOTOPES, PARTICLES, filepath):
        """Carrega dados de elementos a partir de um arquivo JSON e cria objetos Element."""
        with open(filepath, "r") as f:
            fusion_data = json.load(f)
        return [Fusion.from_dict(ISOTOPES, PARTICLES, data) for data in fusion_data]

class Decay:
    def alpha_decay():
        """
        alpha = nucleo de He-4
        Ra-226 -> Rn-222 + alpha
        Transição para núcleo mais leve
        """
        pass
    def beta_decay():
        """
        beta = eletron
        n -> p + e- + v_ (beta menos)
        p -> n + e+ + v (beta mais)
        """
        pass
    def gamma_decay():
        """
        gamma = foton
        Co-60 -> Co-60 + gama
        Após decaimento alpha ou beta
        Nucleo excitado emite foton (raios gama)
        """
        pass
    def pair_production_decay():
        """
        gamma = e- + e+
        um particula cria um par de particulas
        """
        pass
    def heavy_particle_decay():
        """
        boson W, Z e H podem decair em varias particulas
        """
        pass
    def radioactive_decay():
        """
        O urânio-238 decai em uma série de passos até se tornar chumbo-206.
        """
        pass
    def fast_decay():
        """
        beta
        """
        pass
    def slow_decay():
        """
        decaimento de isótopos radioativos como o carbono-14
        """
        pass