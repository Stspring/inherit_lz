# Создать классы "Компьютерные комплектующие"
# Родительский класс: Component
# Атрибуты: motherboard_model, power_unit_model, power_unit_port, 
# motherboard_soccet, motherboard_voltage_port.
# Методы: get_info()(вывод информации о компонентах), chek_compatibility()(Проверка совместимости(Если motherboard_voltage_port =  power_unit_port выводи True; Если motherboard_soccet ))
# Дочерний класс: Processor
# Доп. атрибуты: core_count, power_consumption, processor_model, soccet
# Методы: get_info()(вывод информации о всех компонентах),
# chek_system_ompatibility()(Проверка совместимости всех модулей)
#
#--------------------------------------------------------------------------------------------------------------------------------------

# Создаем класс Component
class Component:
    def __init__(self, motherboard_model, power_unit_model, power_unit_port, motherboard_socket, motherboard_voltage_port):
        self.motherboard_model = motherboard_model                  # Модель материнской платы
        self.power_unit_model = power_unit_model                    # Модель блока питания
        self.power_unit_port = power_unit_port                      # Порт блока питания (например, 24-pin)
        self.motherboard_socket = motherboard_socket                # Сокет материнской платы (например, AM4)
        self.motherboard_voltage_port = motherboard_voltage_port    # Порт напряжения материнской платы

# Создаю метод для вывода информации о компонентах
    def get_info(self):
# Вывод информации
        return (f"Материнская плата: {self.motherboard_model},\n "f"Блок питания: {self.power_unit_model}, \n"
                f"Порт блока питания: {self.power_unit_port}, \n" f"Сокет материнской платы: {self.motherboard_socket}, \n"
                f"Порт напряжения материнской платы: {self.motherboard_voltage_port}")

# Создаю метод для проверка совместимости
    def check_compatibility(self):
        if self.motherboard_voltage_port == self.power_unit_port:
             print(f"Проверка совместимости портов: порты совместимы")
        else:
            print(f"Проверка совместимости портов: порты не совместимы")

    def __del__(self):
        pass

# Создаю дочерний класс Processor
class Processor(Component):
    def __init__(self, motherboard_model, power_unit_model, power_unit_port, motherboard_socket, motherboard_voltage_port,
                 core_count, power_consumption, processor_model, socket):
        
        super().__init__(motherboard_model, power_unit_model, power_unit_port, motherboard_socket, motherboard_voltage_port)
        self.core_count = core_count                                # Количество ядер процессора
        self.power_consumption = power_consumption                  # Потребление энергии процессора 
        self.processor_model = processor_model                      # Модель процессора
        self.socket = socket                                        # Сокет процессора 

# Создаю метод для вывода информации о свех компонентах
    def get_info(self):       
        base_info = super().get_info()      # Вызывает метод родительского класса для получения информации
# Выводим информацию о процессоре
        return (f"{base_info},\n "f"Процессор: {self.processor_model},\n "f"Количество ядер: {self.core_count},\n "  
                f"Потребление энергии: {self.power_consumption},\n "f"Сокет процессора: {self.socket}")

    def check_system_compatibility(self):
        if self.motherboard_socket == self.socket:
            print (f" Проверка совместимости сокетов: сокеты совместимы")
        else:
            print (f" Проверка совместимости сокетов: сокеты не совместимы")



