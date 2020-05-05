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

profit percentage ---> function profit based on fixed 50 percent
depreciation ---> In Printer_3d Class ---> function fixed_overhead based on lifespan, cost, working time
maintenance cost ---> In Printer_3d Class ---> function maintenance_cost
electric --->In Printer_3d Class ---> function power_cost_per_hour

'''

#import printer_default_costs as pdc

#imports default printer costs
#printer_vars = pdc.open_defaults()

#printer_vars

import pickle

def save_printer_defaults(printer_cost):
    printer_vars = printer_cost
    with open('printer_vars.pkl','wb') as printer_vars_stored:
        pickle.dump(printer_vars, printer_vars_stored, pickle.HIGHEST_PROTOCOL)
    printer_vars_stored.close()



# read python dict back from the file

def open_printer_defaults():
    with open('printer_vars.pkl','rb') as printer_vars_open:
        printer_vars = pickle.load(printer_vars_open)
    printer_vars_open.close()
    return printer_vars

printer_vars = open_printer_defaults()







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

	def __init__(self, material):
		self.material = material
		#['PLA', 'PET-G', 'ABS']
		#cost per KG
		self.cost = {"PLA": 20.95, "PET-G": 27.15, "ABS": 28.04}

	def material_cost(self, weight):
		return (self.cost[self.material]/1000)*weight


def profit(cost):
	return cost * 1.5

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

	return round(profit(cost_price), 2)


#sets users material type

while True:

	material_type = input("Please select material type: PLA / PET-G / ABS\n(Type 'setup' to adjust costings)\n").upper()

	if material_type == 'PLA' or material_type.upper() == 'PET-G' or material_type.upper() == 'ABS':
		my_material = Material(material_type)
		break
	else:
		if material_type.lower() == 'setup':
            
			printer_vars['cost'] = float(input("Enter printers cost:\n"))
            printer_vars['life_expectancy'] = float(input("Enter printers life expectancy:\n"))
            printer_vars['yearly_work_time'] = float(input("Enter estimated yearly work time:\n"))
            printer_vars['bed_surface'] = float(input("Enter cost of bed surface per year:\n"))
            printer_vars['belts'] = float(input("Enter cost of belts per year:\n"))
            printer_vars['nozzles'] = float(input("Enter cost of nozzles per year:\n"))
            printer_vars['hotend'] = float(input("Enter cost of hotend parts per year:\n"))
            printer_vars['power_per_hour'] = float(input("Enter power comsumption per hour:\n"))
            printer_vars['power_price'] = float(input("Enter power price per year:\n"))

			print (printer_vars)
			save_printer_defaults(printer_vars)
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

my_printer = Printer_3d(printer_vars['cost'], printer_vars['life_expectancy'], printer_vars['yearly_work_time'], printer_vars['bed_surface'], printer_vars['belts'], printer_vars['nozzles'], printer_vars['hotend'], printer_vars['power_per_hour'], printer_vars['power_price'])
cost = quotation_cost(my_material, my_print_time, my_setup, my_finishing)

print(f'Print Price: £{cost}')
printer_vars = open_printer_defaults()
print(printer_vars['cost'])
