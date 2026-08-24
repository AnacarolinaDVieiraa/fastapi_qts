import time

def calcular_frete(peso_kg: float, distancia_km: float) -> float:
      
      if peso_kg <= 0 or distancia_km <= 0:
            return 0.0

      time.sleep(0.05)

      valor_fixo = 10.0
      peso_add = peso_kg * 2.50
      quilometro_adiciona = distancia_km *  0.50
      taxa_adicional = 15.0 if distancia_km >= 100 else 0.0
      
