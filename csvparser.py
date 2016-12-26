import csv
from itertools import groupby


class GetProductsInformation:
  
  def __init__(self,file_name):
    self._file_name=file_name

  #Reading csv file and returning list of the list of lines in csv files separated by ',' 
  def get_csv_details_list(self):
    with open(self._file_name, 'rU') as csv_file:
      return list(list(record) for record in csv.reader(csv_file, delimiter=','))
  
  def get_resolved_list(self):
      csv_details_list = self.get_csv_details_list()[1:]
      csv_details_list.sort(key=lambda x: x[3])
      list_grouped = groupby(csv_details_list, key=lambda x: x[3])
      list_output=[sorted([item for item in value], key=lambda x:x[6]) for(key,value) in list_grouped]
      return list_output
    
  def print_cheapest_products_details(self,productid_list=None):
    if(productid_list==None):
      for grouped_list in self.get_resolved_list():
        print ", ".join(grouped_list[0]) 
    else:
      for grouped_list in self.get_resolved_list():
        if(grouped_list[0][3] in productid_list):
          print ", ".join(grouped_list[0])
      
  def print_priciest_products_details(self):
     for grouped_list in self.get_resolved_list():
        print ", ".join(grouped_list[-1])
    
class MainProgram:
  def __init__(self):
    obj= GetProductsInformation('csvdetails.csv') 
    print "***********CHEAPEST PRODUCT DETAILS*****************"
    obj.print_cheapest_products_details()
    print "***********PRICIEST PRODUCT DETAILS*****************"
    obj.print_priciest_products_details()
    print "***********CHEAPEST pRICE FOR PRODUCTS [3736, 4356, 3732, 3746, 3759, 3719, 3740, 4341]***********"    
    obj.print_cheapest_products_details(['3736', '4356', '3732', '3746', '3759', '3719', '3740', '4341'])
    
    print ("Enter name of the csv file (include '.csv') :")
    self._file_name=raw_input()
    gfi= GetProductsInformation(self._file_name)    
    
    print "***********CHEAPEST PRODUCT DETAILS*****************"
    gfi.print_cheapest_products_details()
    print "***********PRICIEST PRODUCT DETAILS*****************"
    gfi.print_priciest_products_details()
    print "***********CHEAPEST pRICE FOR PRODUCTS [3736, 4356, 3732, 3746, 3759, 3719, 3740, 4341]***********"    
    gfi.print_cheapest_products_details(['3736', '4356', '3732', '3746', '3759', '3719', '3740', '4341'])
    while(True):
      print("Enter an option:")
      print(" press 1- Cheapest Products")
      print(" press 2-Priciest Products")
      print(" press  3- Cheapest among entered productids")
      print("press Any other key to exit...")

      self._input=raw_input().strip()
      if(self._input=='1'):
          gfi.print_cheapest_products_details()
      elif(self._input=='2'): 
          gfi.print_priciest_products_details()
      elif(self._input=='3'):
          print ("Enter list of product ids separated by spaces and press enter:")
          self._productid_list=raw_input().strip().split()
          gfi.print_cheapest_products_details(self._productid_list)
      else:
          break
         
        
        
MainProgram()

  
  
  
  
  
  
  
  
  
  
  
  
