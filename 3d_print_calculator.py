'''

#input values

from user

estimated print time
setup time
finishing time
material type
weight of material
postage

model setup-time ---> Currently setup as hard code
model clean-up time ---> Currently setup as hard code


fixed figures

profit percentage ---> function profçit based on fixed 50 percent
depreciation ---> In Printer_3d Class ---> function fixed_overhead based on lifespan, cost, working time
maintenance cost ---> In Printer_3d Class ---> function maintenance_cost
electric --->In Printer_3d Class ---> function power_cost_per_hour

'''

#import printer_default_costs as pdc

#imports default printer costs
#printer_vars = pdc.open_defaults()

#printer_vars

import pickle

class Printer_3d(object):
    """Setup for printer"""
    def __init__(self, cost=664.12, life_expectancy=5, yearly_work_time=1200, bed_surface = 16, belts = 10, nozzles = 11, hotend = 49, power_per_hour = 0.25, power_price = 0.15):
        self.cost = cost
        self.life_expectancy = life_expectancy
        self.yearly_work_time = yearly_work_time
        self.bed_surface = bed_surface
        self.belts = belts
        self.nozzles = nozzles
        self.hotend = hotend
        self.power_per_hour = power_per_hour
        self.power_price = power_price


    def fixed_overhead(self):

        #depreciation = (printer cost / life expectancy) * (1 / working time per year)

        return round((self.cost / self.life_expectancy) * (1 / self.yearly_work_time), 2)

    def maintenance_cost(self):

        #estimated yearly maintenance cost for printer

        return round((self.bed_surface + self.belts + self.nozzles + self.hotend) / self.yearly_work_time, 2)

    def power_cost_per_hour(self):

        #cost of running printer per hour

        return self.power_per_hour * self.power_price


class Material():

    def __init__(self, material, cost):
        self.material = material
        #['PLA', 'PET-G', 'ABS']
        #cost per KG
        self.cost = cost

    def material_cost(self, weight):
        return (self.cost/1000)*weight

# read/write python dict to/from from the file

def open_defaults(name):
    with open(name + '.pkl','rb') as default_open:
        name = pickle.load(default_open)
    default_open.close()
    return name

#material_vars = {"PLA": 20.95, "PET-G": 27.15, "ABS": 28.04}

def save_defaults(name, vars):
    with open(name + '.pkl','wb') as default_save:
        pickle.dump(vars, default_save, pickle.HIGHEST_PROTOCOL)
    default_save.close()

#setup printer costs
def printer_costs(update=False):

    global printer_vars

    while update:
        for key in printer_vars:
            correct = False
            while(not correct):
                try:
                    printer_vars[key] = float(input(f"Enter {key}:\n"))
                    correct = True
                except ValueError:
                    print ('Please enter a valid input')
                    correct = False
        save_defaults('printer_vars', printer_vars)
        update = False
    else:
        printer_vars = open_defaults('printer_vars')
    return printer_vars

def material_costs(update=False):

    global material_vars

    while update:
        for key in material_vars:
            correct = False
            while(not correct):
                try:
                    material_vars[key] = float(input(f"Enter {key}:\n"))
                    correct = True
                except ValueError:
                    print ('Please enter a valid input')
                    correct = False
        save_defaults('material_vars', material_vars)
        update = False

    else:
        material_vars = open_defaults('material_vars')
    return material_vars

#calls / sets profit margin

def profit_rate(update=False):

    global profit

    while update:
        try:
            profit = int(input(f"Enter profit percentage:\n"))
            save_defaults('profit', profit)
            update = False
        except ValueError:
            print ('Please enter a valid percentage')
            continue
    else:
        profit = open_defaults('profit')
    return profit


def profit_calc(cost):

    profit = 1 + (profit_rate()/100)

    return cost * profit

def setup_cost(time):

    setup_per_hour = 20

    return (setup_per_hour/60) * time

def finishing_cost(time):

    finishing_per_hour = 15

    return (finishing_per_hour/60) * time

def quotation_cost(material, print_time, setup, finishing):

    #Overheads costs

    overhead = my_printer.fixed_overhead() + my_printer.maintenance_cost() + my_printer.power_cost_per_hour()

    cost_price = overhead + my_material.material_cost(material_weight) + my_setup + my_finishing

    return round(profit_calc(cost_price), 2)

#printer_vars = open_defaults('printer_vars')
printer_vars = printer_costs()
material_vars = material_costs()

#sets users material type

while True:

    material_type = input("Please select material type: PLA / PET-G / ABS\n(Type 'setup' to adjust costings)\n").upper()

    if material_type == 'PLA' or material_type.upper() == 'PET-G' or material_type.upper() == 'ABS':
        my_material = Material(material_type, material_vars[material_type])
        break
    else:
        #Calls setup cost functions if required
        if material_type.lower() == 'setup':
            material_type = input("Setup Printer/Material/Profit?")
            if material_type.lower() == 'printer':
                printer_vars = printer_costs(True)

            if material_type.lower() == 'material':
                material_vars = material_costs(True)

            if material_type.lower() == 'profit':
                profit = profit_rate(True)
            continue
        print('Please enter a valid material type')
        continue

#weight of material for part

while True:

    try:
        material_weight = int(input("Please enter weight in grams:\n"))
    except:
        print('Please enter a valid weight')
        continue
    else:
        break

#sets print times in minutes

while True:

    try:
        my_print_time = int(input("Please select estimated print time: (mins)\n"))
    except:
        print('Please enter a valid print time')
        continue
    else:
        break

#sets setup times in minutes

while True:

    try:
        setup_time = int(input("Please enter setup time: (mins)\n"))
    except:
        print('Please enter a valid time')
        continue
    else:
        my_setup = setup_cost(setup_time)
        break

#sets finishing times in minutes

while True:

    try:
        finishing_time = int(input("Please enter any finishing time: (mins)\n"))
    except:
        print('Please enter a valid time')
        continue
    else:
        my_finishing = finishing_cost(finishing_time)
        break


my_printer = Printer_3d(printer_vars['printer cost'], printer_vars['life expectancy'], printer_vars['yearly work time'], printer_vars['bed surface'], printer_vars['belts'], printer_vars['nozzles'], printer_vars['hotend'], printer_vars['power per hour'], printer_vars['power price'])
cost = quotation_cost(my_material, my_print_time, my_setup, my_finishing)


print(f'Print Price: £{cost}')
