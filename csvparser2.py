import csv

class GetProductsInformation:  
  
  def __init__(self,file_name):
    self._file_name=file_name

  #Reading csv file and returning list of the list of lines in csv files separated by ',' 
  def get_csv_details_list(self):
    with open(self._file_name, 'rU') as csv_file:
      return list(list(record) for record in csv.reader(csv_file, delimiter=','))
  
  
  def sorted_on_productid_then_price(self):    
    #sorted the "get_csv_details_list" on the basis of product id as well as price in ascending order
    #sclicing as [1:] for excluding 1st line which contains headers    
    return sorted(self.get_csv_details_list()[1:],key=lambda x:(x[3],x[6]))


  #for making cheapest_product_list and priciest_product_list on the basis of product_id
  def sorted_products_list_pricewise(self,query):
    resolved_list=self.sorted_on_productid_then_price()
    
    cheapest_product_list= [resolved_list[0]]   #first element of the list will be always in chipest
    priciest_product_list=[]
    for index in range(1,len(resolved_list)):
      if resolved_list[index-1][3] != resolved_list[index][3]:
        priciest_product_list.append(resolved_list[index-1])
        cheapest_product_list.append(resolved_list[index])
    priciest_product_list.append(resolved_list[-1])     #last element of the list will be always in priciest

    if(query==1):
      return cheapest_product_list
    elif(query==2):
      return priciest_product_list


  def list_of_cheapest_product(self,product_id_list=None):
    cheapest_product_list=self.sorted_products_list_pricewise(1)
    
    if product_id_list:
      for product in cheapest_product_list:
        if product[3] in product_id_list:
          print ','.join(product)
    else:
      for product in cheapest_product_list:
          print ','.join(product)
      
  def print_priciest_products_details(self):
     priciest_product_list= self.sorted_products_list_pricewise(2)
     for product in priciest_product_list:
          print ','.join(product)


class MainProgram:
  def __init__(self):
    obj=GetProductsInformation('CSVDetails.csv')
    print"******************CHEAPEST PRODUCT LIST************************"
    obj.list_of_cheapest_product()
    print"***************CHEAPEST PRICE FOR PRODUCT[3736, 4356, 3732, 3746, 3759, 3719, 3740, 4341]***************************"
    obj.list_of_cheapest_product(['3736', '4356', '3732', '3746', '3759', '3719', '3740', '4341'])
    print"***************PRICIEST PRODUCT LIST  ***************************"
    obj.print_priciest_products_details()
    
    print"WANT TO CONVERT OTHER CSV FILE?"
    
    print ("Enter name of the csv file (include '.csv') :")
    self._file_name=raw_input()
    gfi= GetProductsInformation(self._file_name)    
    #gfi.get_csv_details_list()
    print "***********CHEAPEST PRODUCT DETAILS*****************"
    gfi.list_of_cheapest_product()
    print "***********PRICIEST PRODUCT DETAILS*****************"
    gfi.print_priciest_products_details()
    print "***********CHEAPEST pRICE FOR PRODUCTS [3736, 4356, 3732, 3746, 3759, 3719, 3740, 4341]***********"    
    gfi.list_of_cheapest_product(['3736', '4356', '3732', '3746', '3759', '3719', '3740', '4341'])
    while(True):
      print("Enter an option:")
      print(" press 1- Cheapest Products")
      print(" press 2-Priciest Products")
      print(" press  3- Cheapest among entered productids")
      print("press Any other key to exit...")

      self._input=raw_input().strip()
      if(self._input=='1'):
          gfi.list_of_cheapest_product()
      elif(self._input=='2'): 
          gfi.print_priciest_products_details()
      elif(self._input=='3'):
          print ("Enter list of product ids separated by spaces and press enter:")
          self._productid_list=raw_input().strip().split()
          gfi.list_of_cheapest_product(self._productid_list)
      else:
          break

MainProgram()




  
  
  
  
  
  
  
  
  
