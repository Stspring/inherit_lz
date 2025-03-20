# файл main
#---------------------------------------------------------------------------------------

# Импортируем класс P 
from PcComp import Processor  

def main():
    
    # Создаем объект процессора с заданными параметрами
    processor = Processor(motherboard_model="ASUS ROG Strix B550-F",power_unit_model="Corsair RM750",              
        power_unit_port="24-pin", motherboard_socket="AM4",motherboard_voltage_port="12V", core_count=8,                                   
        power_consumption=65,processor_model="AMD Ryzen 7 5800X",socket="AM4" )

    
    print(processor.get_info())  
    print("Совместимость системы:", "Совместимо" 
        if processor.check_system_compatibility() else "Не совместимо")

if __name__ == "__main__": 
    main() 