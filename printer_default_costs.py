#This will allow users to use and save default cost values for thier printers
import pickle


printer_vars = {'cost':10, 'life_expectancy':5, 'yearly_work_time':1200, 'bed_surface':16, 'belts':10, 'nozzles':11, 'hotend':49, 'power_per_hour':0.25, 'power_price':0.15}

# write python dict to a file
def save_defaults(printer_cost):
    printer_vars = printer_cost
    with open('printer_vars.pkl','wb') as printer_vars_stored:
        pickle.dump(printer_vars, printer_vars_stored, pickle.HIGHEST_PROTOCOL)
    printer_vars_stored.close()



# read python dict back from the file

def open_defaults():
    with open('printer_vars.pkl','rb') as printer_vars_open:
        printer_vars = pickle.load(printer_vars_open)
    printer_vars_open.close()
    return printer_vars

save_defaults(printer_vars)

test = open_defaults()

test


    #664.12
