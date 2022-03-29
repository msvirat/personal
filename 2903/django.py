from itertools import product
import django

#mouse
def mouse(request):
    list = products.objects.filter(sub_cat = 'mouse')
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)

def mouse_brand(request):
    brand_name = request.GET['brand_name']
    list = products.objects.filter(sub_cat = 'mouse', brand = brand_name)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)

def mouse_low_price(request):
    low_price = request.GET['low_price']
    list = products.objects.filter(sub_cat = 'mouse', price <= low_price)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)

def mouse_low_price_brand(request):
    low_price = request.GET['low_price']
    brand_name = request.GET['brand_name']
    list = products.objects.filter(sub_cat = 'mouse', price <= low_price, brand = brand_name)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)

def mouse_high_price(request):
    high_price = request.GET['high_price']
    list = products.objects.filter(sub_cat = 'mouse', price > high_price)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)

def mouse_high_price_brand(request):
    high_price = request.GET['high_price']
    brand_name = request.GET['brand_name']
    list = products.objects.filter(sub_cat = 'mouse', price > high_price, brand = brand_name)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)


#headset
def headset(request):
    list = products.objects.filter(sub_cat = 'headset')
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)

def headset_brand(request):
    brand_name = request.GET['brand_name']
    list = products.objects.filter(sub_cat = 'headset', brand = brand_name)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)

def headset_low_price(request):
    low_price = request.GET['low_price']
    list = products.objects.filter(sub_cat = 'headset', price <= low_price)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)

def headset_low_price_brand(request):
    low_price = request.GET['low_price']
    brand_name = request.GET['brand_name']
    list = products.objects.filter(sub_cat = 'headset', price <= low_price, brand = brand_name)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)

def headset_high_price(request):
    high_price = request.GET['high_price']
    list = products.objects.filter(sub_cat = 'headset', price > high_price)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)

def headset_high_price_brand(request):
    high_price = request.GET['high_price']
    brand_name = request.GET['brand_name']
    list = products.objects.filter(sub_cat = 'headset', price > high_price, brand = brand_name)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)




#tv
def tv(request):
    list = products.objects.filter(sub_cat = 'tv')
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)

def tv_brand(request):
    brand_name = request.GET['brand_name']
    list = products.objects.filter(sub_cat = 'tv', brand = brand_name)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)

def tv_low_price(request):
    low_price = request.GET['low_price']
    list = products.objects.filter(sub_cat = 'tv', price <= low_price)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)

def tv_low_price_brand(request):
    low_price = request.GET['low_price']
    brand_name = request.GET['brand_name']
    list = products.objects.filter(sub_cat = 'tv', price <= low_price, brand = brand_name)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)

def tv_high_price(request):
    high_price = request.GET['high_price']
    list = products.objects.filter(sub_cat = 'tv', price > high_price)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)

def tv_high_price_brand(request):
    high_price = request.GET['high_price']
    brand_name = request.GET['brand_name']
    list = products.objects.filter(sub_cat = 'tv', price > high_price, brand = brand_name)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)



#fridge
def fridge(request):
    list = products.objects.filter(sub_cat = 'fridge')
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)

def fridge_brand(request):
    brand_name = request.GET['brand_name']
    list = products.objects.filter(sub_cat = 'fridge', brand = brand_name)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)

def fridge_low_price(request):
    low_price = request.GET['low_price']
    list = products.objects.filter(sub_cat = 'fridge', price <= low_price)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)

def fridge_low_price_brand(request):
    low_price = request.GET['low_price']
    brand_name = request.GET['brand_name']
    list = products.objects.filter(sub_cat = 'fridge', price <= low_price, brand = brand_name)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)

def fridge_high_price(request):
    high_price = request.GET['high_price']
    list = products.objects.filter(sub_cat = 'fridge', price > high_price)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)

def fridge_high_price_brand(request):
    high_price = request.GET['high_price']
    brand_name = request.GET['brand_name']
    list = products.objects.filter(sub_cat = 'fridge', price > high_price, brand = brand_name)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)



#ac
def ac(request):
    list = products.objects.filter(sub_cat = 'ac')
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)

def ac_brand(request):
    brand_name = request.GET['brand_name']
    list = products.objects.filter(sub_cat = 'ac', brand = brand_name)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)

def ac_low_price(request):
    low_price = request.GET['low_price']
    list = products.objects.filter(sub_cat = 'ac', price <= low_price)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)

def ac_low_price_brand(request):
    low_price = request.GET['low_price']
    brand_name = request.GET['brand_name']
    list = products.objects.filter(sub_cat = 'ac', price <= low_price, brand = brand_name)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)

def ac_high_price(request):
    high_price = request.GET['high_price']
    list = products.objects.filter(sub_cat = 'ac', price > high_price)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)

def ac_high_price_brand(request):
    high_price = request.GET['high_price']
    brand_name = request.GET['brand_name']
    list = products.objects.filter(sub_cat = 'ac', price > high_price, brand = brand_name)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)




#washing
def washing(request):
    list = products.objects.filter(sub_cat = 'washing')
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)

def washing_brand(request):
    brand_name = request.GET['brand_name']
    list = products.objects.filter(sub_cat = 'washing', brand = brand_name)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)

def washing_low_price(request):
    low_price = request.GET['low_price']
    list = products.objects.filter(sub_cat = 'washing', price <= low_price)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)

def washing_low_price_brand(request):
    low_price = request.GET['low_price']
    brand_name = request.GET['brand_name']
    list = products.objects.filter(sub_cat = 'washing', price <= low_price, brand = brand_name)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)

def washing_high_price(request):
    high_price = request.GET['high_price']
    list = products.objects.filter(sub_cat = 'washing', price > high_price)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)

def washing_high_price_brand(request):
    high_price = request.GET['high_price']
    brand_name = request.GET['brand_name']
    list = products.objects.filter(sub_cat = 'washing', price > high_price, brand = brand_name)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)






#pumps
def pumps(request):
    list = products.objects.filter(sub_cat = 'pumps')
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)

def pumps_brand(request):
    brand_name = request.GET['brand_name']
    list = products.objects.filter(sub_cat = 'pumps', brand = brand_name)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)

def pumps_low_price(request):
    low_price = request.GET['low_price']
    list = products.objects.filter(sub_cat = 'pumps', price <= low_price)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)

def pumps_low_price_brand(request):
    low_price = request.GET['low_price']
    brand_name = request.GET['brand_name']
    list = products.objects.filter(sub_cat = 'pumps', price <= low_price, brand = brand_name)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)

def pumps_high_price(request):
    high_price = request.GET['high_price']
    list = products.objects.filter(sub_cat = 'pumps', price > high_price)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)

def pumps_high_price_brand(request):
    high_price = request.GET['high_price']
    brand_name = request.GET['brand_name']
    list = products.objects.filter(sub_cat = 'pumps', price > high_price, brand = brand_name)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)




#tube
def tube(request):
    list = products.objects.filter(sub_cat = 'tube')
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)

def tube_brand(request):
    brand_name = request.GET['brand_name']
    list = products.objects.filter(sub_cat = 'tube', brand = brand_name)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)

def tube_low_price(request):
    low_price = request.GET['low_price']
    list = products.objects.filter(sub_cat = 'tube', price <= low_price)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)

def tube_low_price_brand(request):
    low_price = request.GET['low_price']
    brand_name = request.GET['brand_name']
    list = products.objects.filter(sub_cat = 'tube', price <= low_price, brand = brand_name)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)

def tube_high_price(request):
    high_price = request.GET['high_price']
    list = products.objects.filter(sub_cat = 'tube', price > high_price)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)

def tube_high_price_brand(request):
    high_price = request.GET['high_price']
    brand_name = request.GET['brand_name']
    list = products.objects.filter(sub_cat = 'tube', price > high_price, brand = brand_name)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)



##kids - hoodie


def kids_hoodie(request):       
    list = products.objects.filter(sub_cat = 'hoodie', age = 'kids')
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)

def kids_hoodie_color(request):       
    color = request.GET['color']
    list = products.objects.filter(sub_cat = 'hoodie', age = 'kids', color = color)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)



def kids_hoodie_size(request):   
    size = request.GET['size']    
    list = products.objects.filter(sub_cat = 'hoodie', age = 'kids', size = size)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)


def kids_hoodie_size_color(request):   
    size = request.GET['size']    
    color = request.GET['color']
    list = products.objects.filter(sub_cat = 'hoodie', age = 'kids', size = size, color = color)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)




def kids_hoodie_low(request):    
    low_price = request.GET['low_price']
    list = products.objects.filter(sub_cat = 'hoodie',  price <= low_price, age = 'kids')
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)

def kids_hoodie_low_size(request):    
    low_price = request.GET['low_price']
    size = request.GET['size']
    list = products.objects.filter(sub_cat = 'hoodie',  price <= low_price, age = 'kids', size = size)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)


def kids_hoodie_low_color(request):    
    low_price = request.GET['low_price']
    color = request.GET['color']
    list = products.objects.filter(sub_cat = 'hoodie',  price <= low_price, age = 'kids', color = color)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)



def kids_hoodie_low_color_size(request):    
    low_price = request.GET['low_price']
    color = request.GET['color']
    size = request.GET['size']
    list = products.objects.filter(sub_cat = 'hoodie',  price <= low_price, age = 'kids', color = color, size = size)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)


def kids_hoodie_high(request):    
    high_price = request.GET['high_price']
    list = products.objects.filter(sub_cat = 'hoodie', price > high_price, age = 'kids')
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)

def kids_hoodie_high_size(request):    
    high_price = request.GET['high_price']
    size = request.GET['size']
    list = products.objects.filter(sub_cat = 'hoodie',  price > high_price, age = 'kids', size = size)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)




def kids_hoodie_high_color(request):    
    high_price = request.GET['high_price']
    color = request.GET['color']
    list = products.objects.filter(sub_cat = 'hoodie',  price > high_price, age = 'kids', color = color)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)



def kids_hoodie_high_color_size(request):    
    high_price = request.GET['high_price']
    color = request.GET['color']
    size = request.GET['size']
    list = products.objects.filter(sub_cat = 'hoodie',  price > high_price, age = 'kids', color = color, size = size)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)






##kids - tshirt


def kids_tshirt(request):       
    list = products.objects.filter(sub_cat = 'tshirt', age = 'kids')
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)

def kids_tshirt_color(request):       
    color = request.GET['color']
    list = products.objects.filter(sub_cat = 'tshirt', age = 'kids', color = color)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)



def kids_tshirt_size(request):   
    size = request.GET['size']    
    list = products.objects.filter(sub_cat = 'tshirt', age = 'kids', size = size)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)


def kids_tshirt_size_color(request):   
    size = request.GET['size']    
    color = request.GET['color']
    list = products.objects.filter(sub_cat = 'tshirt', age = 'kids', size = size, color = color)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)




def kids_tshirt_low(request):    
    low_price = request.GET['low_price']
    list = products.objects.filter(sub_cat = 'tshirt',  price <= low_price, age = 'kids')
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)

def kids_tshirt_low_size(request):    
    low_price = request.GET['low_price']
    size = request.GET['size']
    list = products.objects.filter(sub_cat = 'tshirt',  price <= low_price, age = 'kids', size = size)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)


def kids_tshirt_low_color(request):    
    low_price = request.GET['low_price']
    color = request.GET['color']
    list = products.objects.filter(sub_cat = 'tshirt',  price <= low_price, age = 'kids', color = color)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)



def kids_tshirt_low_color_size(request):    
    low_price = request.GET['low_price']
    color = request.GET['color']
    size = request.GET['size']
    list = products.objects.filter(sub_cat = 'tshirt',  price <= low_price, age = 'kids', color = color, size = size)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)


def kids_tshirt_high(request):    
    high_price = request.GET['high_price']
    list = products.objects.filter(sub_cat = 'tshirt', price > high_price, age = 'kids')
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)

def kids_tshirt_high_size(request):    
    high_price = request.GET['high_price']
    size = request.GET['size']
    list = products.objects.filter(sub_cat = 'tshirt',  price > high_price, age = 'kids', size = size)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)




def kids_tshirt_high_color(request):    
    high_price = request.GET['high_price']
    color = request.GET['color']
    list = products.objects.filter(sub_cat = 'tshirt',  price > high_price, age = 'kids', color = color)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)



def kids_tshirt_high_color_size(request):    
    high_price = request.GET['high_price']
    color = request.GET['color']
    size = request.GET['size']
    list = products.objects.filter(sub_cat = 'tshirt',  price > high_price, age = 'kids', color = color, size = size)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)





##kids - trouser


def kids_trouser(request):       
    list = products.objects.filter(sub_cat = 'trouser', age = 'kids')
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)

def kids_trouser_color(request):       
    color = request.GET['color']
    list = products.objects.filter(sub_cat = 'trouser', age = 'kids', color = color)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)



def kids_trouser_size(request):   
    size = request.GET['size']    
    list = products.objects.filter(sub_cat = 'trouser', age = 'kids', size = size)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)


def kids_trouser_size_color(request):   
    size = request.GET['size']    
    color = request.GET['color']
    list = products.objects.filter(sub_cat = 'trouser', age = 'kids', size = size, color = color)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)




def kids_trouser_low(request):    
    low_price = request.GET['low_price']
    list = products.objects.filter(sub_cat = 'trouser',  price <= low_price, age = 'kids')
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)

def kids_trouser_low_size(request):    
    low_price = request.GET['low_price']
    size = request.GET['size']
    list = products.objects.filter(sub_cat = 'trouser',  price <= low_price, age = 'kids', size = size)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)


def kids_trouser_low_color(request):    
    low_price = request.GET['low_price']
    color = request.GET['color']
    list = products.objects.filter(sub_cat = 'trouser',  price <= low_price, age = 'kids', color = color)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)



def kids_trouser_low_color_size(request):    
    low_price = request.GET['low_price']
    color = request.GET['color']
    size = request.GET['size']
    list = products.objects.filter(sub_cat = 'trouser',  price <= low_price, age = 'kids', color = color, size = size)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)


def kids_trouser_high(request):    
    high_price = request.GET['high_price']
    list = products.objects.filter(sub_cat = 'trouser', price > high_price, age = 'kids')
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)

def kids_trouser_high_size(request):    
    high_price = request.GET['high_price']
    size = request.GET['size']
    list = products.objects.filter(sub_cat = 'trouser',  price > high_price, age = 'kids', size = size)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)




def kids_trouser_high_color(request):    
    high_price = request.GET['high_price']
    color = request.GET['color']
    list = products.objects.filter(sub_cat = 'trouser',  price > high_price, age = 'kids', color = color)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)



def kids_trouser_high_color_size(request):    
    high_price = request.GET['high_price']
    color = request.GET['color']
    size = request.GET['size']
    list = products.objects.filter(sub_cat = 'trouser',  price > high_price, age = 'kids', color = color, size = size)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)





##kids - suits


def kids_suits(request):       
    list = products.objects.filter(sub_cat = 'suits', age = 'kids')
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)

def kids_suits_color(request):       
    color = request.GET['color']
    list = products.objects.filter(sub_cat = 'suits', age = 'kids', color = color)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)



def kids_suits_size(request):   
    size = request.GET['size']    
    list = products.objects.filter(sub_cat = 'suits', age = 'kids', size = size)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)


def kids_suits_size_color(request):   
    size = request.GET['size']    
    color = request.GET['color']
    list = products.objects.filter(sub_cat = 'suits', age = 'kids', size = size, color = color)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)




def kids_suits_low(request):    
    low_price = request.GET['low_price']
    list = products.objects.filter(sub_cat = 'suits',  price <= low_price, age = 'kids')
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)

def kids_suits_low_size(request):    
    low_price = request.GET['low_price']
    size = request.GET['size']
    list = products.objects.filter(sub_cat = 'suits',  price <= low_price, age = 'kids', size = size)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)


def kids_suits_low_color(request):    
    low_price = request.GET['low_price']
    color = request.GET['color']
    list = products.objects.filter(sub_cat = 'suits',  price <= low_price, age = 'kids', color = color)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)



def kids_suits_low_color_size(request):    
    low_price = request.GET['low_price']
    color = request.GET['color']
    size = request.GET['size']
    list = products.objects.filter(sub_cat = 'suits',  price <= low_price, age = 'kids', color = color, size = size)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)


def kids_suits_high(request):    
    high_price = request.GET['high_price']
    list = products.objects.filter(sub_cat = 'suits', price > high_price, age = 'kids')
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)

def kids_suits_high_size(request):    
    high_price = request.GET['high_price']
    size = request.GET['size']
    list = products.objects.filter(sub_cat = 'suits',  price > high_price, age = 'kids', size = size)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)




def kids_suits_high_color(request):    
    high_price = request.GET['high_price']
    color = request.GET['color']
    list = products.objects.filter(sub_cat = 'suits',  price > high_price, age = 'kids', color = color)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)



def kids_suits_high_color_size(request):    
    high_price = request.GET['high_price']
    color = request.GET['color']
    size = request.GET['size']
    list = products.objects.filter(sub_cat = 'suits',  price > high_price, age = 'kids', color = color, size = size)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)






##kids - boxers


def kids_boxers(request):       
    list = products.objects.filter(sub_cat = 'boxers', age = 'kids')
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)

def kids_boxers_color(request):       
    color = request.GET['color']
    list = products.objects.filter(sub_cat = 'boxers', age = 'kids', color = color)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)



def kids_boxers_size(request):   
    size = request.GET['size']    
    list = products.objects.filter(sub_cat = 'boxers', age = 'kids', size = size)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)


def kids_boxers_size_color(request):   
    size = request.GET['size']    
    color = request.GET['color']
    list = products.objects.filter(sub_cat = 'boxers', age = 'kids', size = size, color = color)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)




def kids_boxers_low(request):    
    low_price = request.GET['low_price']
    list = products.objects.filter(sub_cat = 'boxers',  price <= low_price, age = 'kids')
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)

def kids_boxers_low_size(request):    
    low_price = request.GET['low_price']
    size = request.GET['size']
    list = products.objects.filter(sub_cat = 'boxers',  price <= low_price, age = 'kids', size = size)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)


def kids_boxers_low_color(request):    
    low_price = request.GET['low_price']
    color = request.GET['color']
    list = products.objects.filter(sub_cat = 'boxers',  price <= low_price, age = 'kids', color = color)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)



def kids_boxers_low_color_size(request):    
    low_price = request.GET['low_price']
    color = request.GET['color']
    size = request.GET['size']
    list = products.objects.filter(sub_cat = 'boxers',  price <= low_price, age = 'kids', color = color, size = size)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)


def kids_boxers_high(request):    
    high_price = request.GET['high_price']
    list = products.objects.filter(sub_cat = 'boxers', price > high_price, age = 'kids')
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)

def kids_boxers_high_size(request):    
    high_price = request.GET['high_price']
    size = request.GET['size']
    list = products.objects.filter(sub_cat = 'boxers',  price > high_price, age = 'kids', size = size)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)




def kids_boxers_high_color(request):    
    high_price = request.GET['high_price']
    color = request.GET['color']
    list = products.objects.filter(sub_cat = 'boxers',  price > high_price, age = 'kids', color = color)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)



def kids_boxers_high_color_size(request):    
    high_price = request.GET['high_price']
    color = request.GET['color']
    size = request.GET['size']
    list = products.objects.filter(sub_cat = 'boxers',  price > high_price, age = 'kids', color = color, size = size)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)




##adult - hoodie


def adult_hoodie(request):       
    list = products.objects.filter(sub_cat = 'hoodie', age = 'adult')
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)

def adult_hoodie_color(request):       
    color = request.GET['color']
    list = products.objects.filter(sub_cat = 'hoodie', age = 'adult', color = color)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)



def adult_hoodie_size(request):   
    size = request.GET['size']    
    list = products.objects.filter(sub_cat = 'hoodie', age = 'adult', size = size)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)


def adult_hoodie_size_color(request):   
    size = request.GET['size']    
    color = request.GET['color']
    list = products.objects.filter(sub_cat = 'hoodie', age = 'adult', size = size, color = color)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)




def adult_hoodie_low(request):    
    low_price = request.GET['low_price']
    list = products.objects.filter(sub_cat = 'hoodie',  price <= low_price, age = 'adult')
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)

def adult_hoodie_low_size(request):    
    low_price = request.GET['low_price']
    size = request.GET['size']
    list = products.objects.filter(sub_cat = 'hoodie',  price <= low_price, age = 'adult', size = size)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)


def adult_hoodie_low_color(request):    
    low_price = request.GET['low_price']
    color = request.GET['color']
    list = products.objects.filter(sub_cat = 'hoodie',  price <= low_price, age = 'adult', color = color)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)



def adult_hoodie_low_color_size(request):    
    low_price = request.GET['low_price']
    color = request.GET['color']
    size = request.GET['size']
    list = products.objects.filter(sub_cat = 'hoodie',  price <= low_price, age = 'adult', color = color, size = size)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)


def adult_hoodie_high(request):    
    high_price = request.GET['high_price']
    list = products.objects.filter(sub_cat = 'hoodie', price > high_price, age = 'adult')
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)

def adult_hoodie_high_size(request):    
    high_price = request.GET['high_price']
    size = request.GET['size']
    list = products.objects.filter(sub_cat = 'hoodie',  price > high_price, age = 'adult', size = size)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)




def adult_hoodie_high_color(request):    
    high_price = request.GET['high_price']
    color = request.GET['color']
    list = products.objects.filter(sub_cat = 'hoodie',  price > high_price, age = 'adult', color = color)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)



def adult_hoodie_high_color_size(request):    
    high_price = request.GET['high_price']
    color = request.GET['color']
    size = request.GET['size']
    list = products.objects.filter(sub_cat = 'hoodie',  price > high_price, age = 'adult', color = color, size = size)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)






##adult - tshirt


def adult_tshirt(request):       
    list = products.objects.filter(sub_cat = 'tshirt', age = 'adult')
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)

def adult_tshirt_color(request):       
    color = request.GET['color']
    list = products.objects.filter(sub_cat = 'tshirt', age = 'adult', color = color)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)



def adult_tshirt_size(request):   
    size = request.GET['size']    
    list = products.objects.filter(sub_cat = 'tshirt', age = 'adult', size = size)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)


def adult_tshirt_size_color(request):   
    size = request.GET['size']    
    color = request.GET['color']
    list = products.objects.filter(sub_cat = 'tshirt', age = 'adult', size = size, color = color)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)




def adult_tshirt_low(request):    
    low_price = request.GET['low_price']
    list = products.objects.filter(sub_cat = 'tshirt',  price <= low_price, age = 'adult')
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)

def adult_tshirt_low_size(request):    
    low_price = request.GET['low_price']
    size = request.GET['size']
    list = products.objects.filter(sub_cat = 'tshirt',  price <= low_price, age = 'adult', size = size)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)


def adult_tshirt_low_color(request):    
    low_price = request.GET['low_price']
    color = request.GET['color']
    list = products.objects.filter(sub_cat = 'tshirt',  price <= low_price, age = 'adult', color = color)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)



def adult_tshirt_low_color_size(request):    
    low_price = request.GET['low_price']
    color = request.GET['color']
    size = request.GET['size']
    list = products.objects.filter(sub_cat = 'tshirt',  price <= low_price, age = 'adult', color = color, size = size)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)


def adult_tshirt_high(request):    
    high_price = request.GET['high_price']
    list = products.objects.filter(sub_cat = 'tshirt', price > high_price, age = 'adult')
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)

def adult_tshirt_high_size(request):    
    high_price = request.GET['high_price']
    size = request.GET['size']
    list = products.objects.filter(sub_cat = 'tshirt',  price > high_price, age = 'adult', size = size)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)




def adult_tshirt_high_color(request):    
    high_price = request.GET['high_price']
    color = request.GET['color']
    list = products.objects.filter(sub_cat = 'tshirt',  price > high_price, age = 'adult', color = color)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)



def adult_tshirt_high_color_size(request):    
    high_price = request.GET['high_price']
    color = request.GET['color']
    size = request.GET['size']
    list = products.objects.filter(sub_cat = 'tshirt',  price > high_price, age = 'adult', color = color, size = size)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)





##adult - trouser


def adult_trouser(request):       
    list = products.objects.filter(sub_cat = 'trouser', age = 'adult')
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)

def adult_trouser_color(request):       
    color = request.GET['color']
    list = products.objects.filter(sub_cat = 'trouser', age = 'adult', color = color)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)



def adult_trouser_size(request):   
    size = request.GET['size']    
    list = products.objects.filter(sub_cat = 'trouser', age = 'adult', size = size)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)


def adult_trouser_size_color(request):   
    size = request.GET['size']    
    color = request.GET['color']
    list = products.objects.filter(sub_cat = 'trouser', age = 'adult', size = size, color = color)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)




def adult_trouser_low(request):    
    low_price = request.GET['low_price']
    list = products.objects.filter(sub_cat = 'trouser',  price <= low_price, age = 'adult')
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)

def adult_trouser_low_size(request):    
    low_price = request.GET['low_price']
    size = request.GET['size']
    list = products.objects.filter(sub_cat = 'trouser',  price <= low_price, age = 'adult', size = size)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)


def adult_trouser_low_color(request):    
    low_price = request.GET['low_price']
    color = request.GET['color']
    list = products.objects.filter(sub_cat = 'trouser',  price <= low_price, age = 'adult', color = color)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)



def adult_trouser_low_color_size(request):    
    low_price = request.GET['low_price']
    color = request.GET['color']
    size = request.GET['size']
    list = products.objects.filter(sub_cat = 'trouser',  price <= low_price, age = 'adult', color = color, size = size)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)


def adult_trouser_high(request):    
    high_price = request.GET['high_price']
    list = products.objects.filter(sub_cat = 'trouser', price > high_price, age = 'adult')
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)

def adult_trouser_high_size(request):    
    high_price = request.GET['high_price']
    size = request.GET['size']
    list = products.objects.filter(sub_cat = 'trouser',  price > high_price, age = 'adult', size = size)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)




def adult_trouser_high_color(request):    
    high_price = request.GET['high_price']
    color = request.GET['color']
    list = products.objects.filter(sub_cat = 'trouser',  price > high_price, age = 'adult', color = color)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)



def adult_trouser_high_color_size(request):    
    high_price = request.GET['high_price']
    color = request.GET['color']
    size = request.GET['size']
    list = products.objects.filter(sub_cat = 'trouser',  price > high_price, age = 'adult', color = color, size = size)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)





##adult - suits


def adult_suits(request):       
    list = products.objects.filter(sub_cat = 'suits', age = 'adult')
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)

def adult_suits_color(request):       
    color = request.GET['color']
    list = products.objects.filter(sub_cat = 'suits', age = 'adult', color = color)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)



def adult_suits_size(request):   
    size = request.GET['size']    
    list = products.objects.filter(sub_cat = 'suits', age = 'adult', size = size)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)


def adult_suits_size_color(request):   
    size = request.GET['size']    
    color = request.GET['color']
    list = products.objects.filter(sub_cat = 'suits', age = 'adult', size = size, color = color)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)




def adult_suits_low(request):    
    low_price = request.GET['low_price']
    list = products.objects.filter(sub_cat = 'suits',  price <= low_price, age = 'adult')
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)

def adult_suits_low_size(request):    
    low_price = request.GET['low_price']
    size = request.GET['size']
    list = products.objects.filter(sub_cat = 'suits',  price <= low_price, age = 'adult', size = size)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)


def adult_suits_low_color(request):    
    low_price = request.GET['low_price']
    color = request.GET['color']
    list = products.objects.filter(sub_cat = 'suits',  price <= low_price, age = 'adult', color = color)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)



def adult_suits_low_color_size(request):    
    low_price = request.GET['low_price']
    color = request.GET['color']
    size = request.GET['size']
    list = products.objects.filter(sub_cat = 'suits',  price <= low_price, age = 'adult', color = color, size = size)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)


def adult_suits_high(request):    
    high_price = request.GET['high_price']
    list = products.objects.filter(sub_cat = 'suits', price > high_price, age = 'adult')
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)

def adult_suits_high_size(request):    
    high_price = request.GET['high_price']
    size = request.GET['size']
    list = products.objects.filter(sub_cat = 'suits',  price > high_price, age = 'adult', size = size)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)




def adult_suits_high_color(request):    
    high_price = request.GET['high_price']
    color = request.GET['color']
    list = products.objects.filter(sub_cat = 'suits',  price > high_price, age = 'adult', color = color)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)



def adult_suits_high_color_size(request):    
    high_price = request.GET['high_price']
    color = request.GET['color']
    size = request.GET['size']
    list = products.objects.filter(sub_cat = 'suits',  price > high_price, age = 'adult', color = color, size = size)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)






##adult - boxers


def adult_boxers(request):       
    list = products.objects.filter(sub_cat = 'boxers', age = 'adult')
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)

def adult_boxers_color(request):       
    color = request.GET['color']
    list = products.objects.filter(sub_cat = 'boxers', age = 'adult', color = color)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)



def adult_boxers_size(request):   
    size = request.GET['size']    
    list = products.objects.filter(sub_cat = 'boxers', age = 'adult', size = size)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)


def adult_boxers_size_color(request):   
    size = request.GET['size']    
    color = request.GET['color']
    list = products.objects.filter(sub_cat = 'boxers', age = 'adult', size = size, color = color)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)




def adult_boxers_low(request):    
    low_price = request.GET['low_price']
    list = products.objects.filter(sub_cat = 'boxers',  price <= low_price, age = 'adult')
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)

def adult_boxers_low_size(request):    
    low_price = request.GET['low_price']
    size = request.GET['size']
    list = products.objects.filter(sub_cat = 'boxers',  price <= low_price, age = 'adult', size = size)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)


def adult_boxers_low_color(request):    
    low_price = request.GET['low_price']
    color = request.GET['color']
    list = products.objects.filter(sub_cat = 'boxers',  price <= low_price, age = 'adult', color = color)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)



def adult_boxers_low_color_size(request):    
    low_price = request.GET['low_price']
    color = request.GET['color']
    size = request.GET['size']
    list = products.objects.filter(sub_cat = 'boxers',  price <= low_price, age = 'adult', color = color, size = size)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)


def adult_boxers_high(request):    
    high_price = request.GET['high_price']
    list = products.objects.filter(sub_cat = 'boxers', price > high_price, age = 'adult')
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)

def adult_boxers_high_size(request):    
    high_price = request.GET['high_price']
    size = request.GET['size']
    list = products.objects.filter(sub_cat = 'boxers',  price > high_price, age = 'adult', size = size)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)




def adult_boxers_high_color(request):    
    high_price = request.GET['high_price']
    color = request.GET['color']
    list = products.objects.filter(sub_cat = 'boxers',  price > high_price, age = 'adult', color = color)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)



def adult_boxers_high_color_size(request):    
    high_price = request.GET['high_price']
    color = request.GET['color']
    size = request.GET['size']
    list = products.objects.filter(sub_cat = 'boxers',  price > high_price, age = 'adult', color = color, size = size)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)





##kids - ghagras


def kids_ghagras(request):       
    list = products.objects.filter(sub_cat = 'ghagras', age = 'kids')
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)

def kids_ghagras_color(request):       
    color = request.GET['color']
    list = products.objects.filter(sub_cat = 'ghagras', age = 'kids', color = color)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)



def kids_ghagras_size(request):   
    size = request.GET['size']    
    list = products.objects.filter(sub_cat = 'ghagras', age = 'kids', size = size)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)


def kids_ghagras_size_color(request):   
    size = request.GET['size']    
    color = request.GET['color']
    list = products.objects.filter(sub_cat = 'ghagras', age = 'kids', size = size, color = color)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)




def kids_ghagras_low(request):    
    low_price = request.GET['low_price']
    list = products.objects.filter(sub_cat = 'ghagras',  price <= low_price, age = 'kids')
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)

def kids_ghagras_low_size(request):    
    low_price = request.GET['low_price']
    size = request.GET['size']
    list = products.objects.filter(sub_cat = 'ghagras',  price <= low_price, age = 'kids', size = size)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)


def kids_ghagras_low_color(request):    
    low_price = request.GET['low_price']
    color = request.GET['color']
    list = products.objects.filter(sub_cat = 'ghagras',  price <= low_price, age = 'kids', color = color)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)



def kids_ghagras_low_color_size(request):    
    low_price = request.GET['low_price']
    color = request.GET['color']
    size = request.GET['size']
    list = products.objects.filter(sub_cat = 'ghagras',  price <= low_price, age = 'kids', color = color, size = size)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)


def kids_ghagras_high(request):    
    high_price = request.GET['high_price']
    list = products.objects.filter(sub_cat = 'ghagras', price > high_price, age = 'kids')
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)

def kids_ghagras_high_size(request):    
    high_price = request.GET['high_price']
    size = request.GET['size']
    list = products.objects.filter(sub_cat = 'ghagras',  price > high_price, age = 'kids', size = size)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)




def kids_ghagras_high_color(request):    
    high_price = request.GET['high_price']
    color = request.GET['color']
    list = products.objects.filter(sub_cat = 'ghagras',  price > high_price, age = 'kids', color = color)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)



def kids_ghagras_high_color_size(request):    
    high_price = request.GET['high_price']
    color = request.GET['color']
    size = request.GET['size']
    list = products.objects.filter(sub_cat = 'ghagras',  price > high_price, age = 'kids', color = color, size = size)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)





##kids - tops


def kids_tops(request):       
    list = products.objects.filter(sub_cat = 'tops', age = 'kids')
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)

def kids_tops_color(request):       
    color = request.GET['color']
    list = products.objects.filter(sub_cat = 'tops', age = 'kids', color = color)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)



def kids_tops_size(request):   
    size = request.GET['size']    
    list = products.objects.filter(sub_cat = 'tops', age = 'kids', size = size)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)


def kids_tops_size_color(request):   
    size = request.GET['size']    
    color = request.GET['color']
    list = products.objects.filter(sub_cat = 'tops', age = 'kids', size = size, color = color)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)




def kids_tops_low(request):    
    low_price = request.GET['low_price']
    list = products.objects.filter(sub_cat = 'tops',  price <= low_price, age = 'kids')
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)

def kids_tops_low_size(request):    
    low_price = request.GET['low_price']
    size = request.GET['size']
    list = products.objects.filter(sub_cat = 'tops',  price <= low_price, age = 'kids', size = size)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)


def kids_tops_low_color(request):    
    low_price = request.GET['low_price']
    color = request.GET['color']
    list = products.objects.filter(sub_cat = 'tops',  price <= low_price, age = 'kids', color = color)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)



def kids_tops_low_color_size(request):    
    low_price = request.GET['low_price']
    color = request.GET['color']
    size = request.GET['size']
    list = products.objects.filter(sub_cat = 'tops',  price <= low_price, age = 'kids', color = color, size = size)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)


def kids_tops_high(request):    
    high_price = request.GET['high_price']
    list = products.objects.filter(sub_cat = 'tops', price > high_price, age = 'kids')
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)

def kids_tops_high_size(request):    
    high_price = request.GET['high_price']
    size = request.GET['size']
    list = products.objects.filter(sub_cat = 'tops',  price > high_price, age = 'kids', size = size)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)




def kids_tops_high_color(request):    
    high_price = request.GET['high_price']
    color = request.GET['color']
    list = products.objects.filter(sub_cat = 'tops',  price > high_price, age = 'kids', color = color)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)



def kids_tops_high_color_size(request):    
    high_price = request.GET['high_price']
    color = request.GET['color']
    size = request.GET['size']
    list = products.objects.filter(sub_cat = 'tops',  price > high_price, age = 'kids', color = color, size = size)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)





##kids - pants


def kids_pants(request):       
    list = products.objects.filter(sub_cat = 'pants', age = 'kids')
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)

def kids_pants_color(request):       
    color = request.GET['color']
    list = products.objects.filter(sub_cat = 'pants', age = 'kids', color = color)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)



def kids_pants_size(request):   
    size = request.GET['size']    
    list = products.objects.filter(sub_cat = 'pants', age = 'kids', size = size)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)


def kids_pants_size_color(request):   
    size = request.GET['size']    
    color = request.GET['color']
    list = products.objects.filter(sub_cat = 'pants', age = 'kids', size = size, color = color)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)




def kids_pants_low(request):    
    low_price = request.GET['low_price']
    list = products.objects.filter(sub_cat = 'pants',  price <= low_price, age = 'kids')
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)

def kids_pants_low_size(request):    
    low_price = request.GET['low_price']
    size = request.GET['size']
    list = products.objects.filter(sub_cat = 'pants',  price <= low_price, age = 'kids', size = size)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)


def kids_pants_low_color(request):    
    low_price = request.GET['low_price']
    color = request.GET['color']
    list = products.objects.filter(sub_cat = 'pants',  price <= low_price, age = 'kids', color = color)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)



def kids_pants_low_color_size(request):    
    low_price = request.GET['low_price']
    color = request.GET['color']
    size = request.GET['size']
    list = products.objects.filter(sub_cat = 'pants',  price <= low_price, age = 'kids', color = color, size = size)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)


def kids_pants_high(request):    
    high_price = request.GET['high_price']
    list = products.objects.filter(sub_cat = 'pants', price > high_price, age = 'kids')
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)

def kids_pants_high_size(request):    
    high_price = request.GET['high_price']
    size = request.GET['size']
    list = products.objects.filter(sub_cat = 'pants',  price > high_price, age = 'kids', size = size)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)




def kids_pants_high_color(request):    
    high_price = request.GET['high_price']
    color = request.GET['color']
    list = products.objects.filter(sub_cat = 'pants',  price > high_price, age = 'kids', color = color)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)



def kids_pants_high_color_size(request):    
    high_price = request.GET['high_price']
    color = request.GET['color']
    size = request.GET['size']
    list = products.objects.filter(sub_cat = 'pants',  price > high_price, age = 'kids', color = color, size = size)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)





##kids - saree


def kids_saree(request):       
    list = products.objects.filter(sub_cat = 'saree', age = 'kids')
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)

def kids_saree_color(request):       
    color = request.GET['color']
    list = products.objects.filter(sub_cat = 'saree', age = 'kids', color = color)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)



def kids_saree_size(request):   
    size = request.GET['size']    
    list = products.objects.filter(sub_cat = 'saree', age = 'kids', size = size)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)


def kids_saree_size_color(request):   
    size = request.GET['size']    
    color = request.GET['color']
    list = products.objects.filter(sub_cat = 'saree', age = 'kids', size = size, color = color)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)




def kids_saree_low(request):    
    low_price = request.GET['low_price']
    list = products.objects.filter(sub_cat = 'saree',  price <= low_price, age = 'kids')
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)

def kids_saree_low_size(request):    
    low_price = request.GET['low_price']
    size = request.GET['size']
    list = products.objects.filter(sub_cat = 'saree',  price <= low_price, age = 'kids', size = size)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)


def kids_saree_low_color(request):    
    low_price = request.GET['low_price']
    color = request.GET['color']
    list = products.objects.filter(sub_cat = 'saree',  price <= low_price, age = 'kids', color = color)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)



def kids_saree_low_color_size(request):    
    low_price = request.GET['low_price']
    color = request.GET['color']
    size = request.GET['size']
    list = products.objects.filter(sub_cat = 'saree',  price <= low_price, age = 'kids', color = color, size = size)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)


def kids_saree_high(request):    
    high_price = request.GET['high_price']
    list = products.objects.filter(sub_cat = 'saree', price > high_price, age = 'kids')
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)

def kids_saree_high_size(request):    
    high_price = request.GET['high_price']
    size = request.GET['size']
    list = products.objects.filter(sub_cat = 'saree',  price > high_price, age = 'kids', size = size)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)




def kids_saree_high_color(request):    
    high_price = request.GET['high_price']
    color = request.GET['color']
    list = products.objects.filter(sub_cat = 'saree',  price > high_price, age = 'kids', color = color)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)



def kids_saree_high_color_size(request):    
    high_price = request.GET['high_price']
    color = request.GET['color']
    size = request.GET['size']
    list = products.objects.filter(sub_cat = 'saree',  price > high_price, age = 'kids', color = color, size = size)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)







##adult - ghagras


def adult_ghagras(request):       
    list = products.objects.filter(sub_cat = 'ghagras', age = 'adult')
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)

def adult_ghagras_color(request):       
    color = request.GET['color']
    list = products.objects.filter(sub_cat = 'ghagras', age = 'adult', color = color)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)



def adult_ghagras_size(request):   
    size = request.GET['size']    
    list = products.objects.filter(sub_cat = 'ghagras', age = 'adult', size = size)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)


def adult_ghagras_size_color(request):   
    size = request.GET['size']    
    color = request.GET['color']
    list = products.objects.filter(sub_cat = 'ghagras', age = 'adult', size = size, color = color)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)




def adult_ghagras_low(request):    
    low_price = request.GET['low_price']
    list = products.objects.filter(sub_cat = 'ghagras',  price <= low_price, age = 'adult')
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)

def adult_ghagras_low_size(request):    
    low_price = request.GET['low_price']
    size = request.GET['size']
    list = products.objects.filter(sub_cat = 'ghagras',  price <= low_price, age = 'adult', size = size)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)


def adult_ghagras_low_color(request):    
    low_price = request.GET['low_price']
    color = request.GET['color']
    list = products.objects.filter(sub_cat = 'ghagras',  price <= low_price, age = 'adult', color = color)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)



def adult_ghagras_low_color_size(request):    
    low_price = request.GET['low_price']
    color = request.GET['color']
    size = request.GET['size']
    list = products.objects.filter(sub_cat = 'ghagras',  price <= low_price, age = 'adult', color = color, size = size)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)


def adult_ghagras_high(request):    
    high_price = request.GET['high_price']
    list = products.objects.filter(sub_cat = 'ghagras', price > high_price, age = 'adult')
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)

def adult_ghagras_high_size(request):    
    high_price = request.GET['high_price']
    size = request.GET['size']
    list = products.objects.filter(sub_cat = 'ghagras',  price > high_price, age = 'adult', size = size)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)




def adult_ghagras_high_color(request):    
    high_price = request.GET['high_price']
    color = request.GET['color']
    list = products.objects.filter(sub_cat = 'ghagras',  price > high_price, age = 'adult', color = color)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)



def adult_ghagras_high_color_size(request):    
    high_price = request.GET['high_price']
    color = request.GET['color']
    size = request.GET['size']
    list = products.objects.filter(sub_cat = 'ghagras',  price > high_price, age = 'adult', color = color, size = size)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)





##adult - tops


def adult_tops(request):       
    list = products.objects.filter(sub_cat = 'tops', age = 'adult')
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)

def adult_tops_color(request):       
    color = request.GET['color']
    list = products.objects.filter(sub_cat = 'tops', age = 'adult', color = color)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)



def adult_tops_size(request):   
    size = request.GET['size']    
    list = products.objects.filter(sub_cat = 'tops', age = 'adult', size = size)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)


def adult_tops_size_color(request):   
    size = request.GET['size']    
    color = request.GET['color']
    list = products.objects.filter(sub_cat = 'tops', age = 'adult', size = size, color = color)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)




def adult_tops_low(request):    
    low_price = request.GET['low_price']
    list = products.objects.filter(sub_cat = 'tops',  price <= low_price, age = 'adult')
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)

def adult_tops_low_size(request):    
    low_price = request.GET['low_price']
    size = request.GET['size']
    list = products.objects.filter(sub_cat = 'tops',  price <= low_price, age = 'adult', size = size)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)


def adult_tops_low_color(request):    
    low_price = request.GET['low_price']
    color = request.GET['color']
    list = products.objects.filter(sub_cat = 'tops',  price <= low_price, age = 'adult', color = color)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)



def adult_tops_low_color_size(request):    
    low_price = request.GET['low_price']
    color = request.GET['color']
    size = request.GET['size']
    list = products.objects.filter(sub_cat = 'tops',  price <= low_price, age = 'adult', color = color, size = size)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)


def adult_tops_high(request):    
    high_price = request.GET['high_price']
    list = products.objects.filter(sub_cat = 'tops', price > high_price, age = 'adult')
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)

def adult_tops_high_size(request):    
    high_price = request.GET['high_price']
    size = request.GET['size']
    list = products.objects.filter(sub_cat = 'tops',  price > high_price, age = 'adult', size = size)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)




def adult_tops_high_color(request):    
    high_price = request.GET['high_price']
    color = request.GET['color']
    list = products.objects.filter(sub_cat = 'tops',  price > high_price, age = 'adult', color = color)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)



def adult_tops_high_color_size(request):    
    high_price = request.GET['high_price']
    color = request.GET['color']
    size = request.GET['size']
    list = products.objects.filter(sub_cat = 'tops',  price > high_price, age = 'adult', color = color, size = size)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)





##adult - pants


def adult_pants(request):       
    list = products.objects.filter(sub_cat = 'pants', age = 'adult')
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)

def adult_pants_color(request):       
    color = request.GET['color']
    list = products.objects.filter(sub_cat = 'pants', age = 'adult', color = color)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)



def adult_pants_size(request):   
    size = request.GET['size']    
    list = products.objects.filter(sub_cat = 'pants', age = 'adult', size = size)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)


def adult_pants_size_color(request):   
    size = request.GET['size']    
    color = request.GET['color']
    list = products.objects.filter(sub_cat = 'pants', age = 'adult', size = size, color = color)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)




def adult_pants_low(request):    
    low_price = request.GET['low_price']
    list = products.objects.filter(sub_cat = 'pants',  price <= low_price, age = 'adult')
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)

def adult_pants_low_size(request):    
    low_price = request.GET['low_price']
    size = request.GET['size']
    list = products.objects.filter(sub_cat = 'pants',  price <= low_price, age = 'adult', size = size)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)


def adult_pants_low_color(request):    
    low_price = request.GET['low_price']
    color = request.GET['color']
    list = products.objects.filter(sub_cat = 'pants',  price <= low_price, age = 'adult', color = color)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)



def adult_pants_low_color_size(request):    
    low_price = request.GET['low_price']
    color = request.GET['color']
    size = request.GET['size']
    list = products.objects.filter(sub_cat = 'pants',  price <= low_price, age = 'adult', color = color, size = size)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)


def adult_pants_high(request):    
    high_price = request.GET['high_price']
    list = products.objects.filter(sub_cat = 'pants', price > high_price, age = 'adult')
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)

def adult_pants_high_size(request):    
    high_price = request.GET['high_price']
    size = request.GET['size']
    list = products.objects.filter(sub_cat = 'pants',  price > high_price, age = 'adult', size = size)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)




def adult_pants_high_color(request):    
    high_price = request.GET['high_price']
    color = request.GET['color']
    list = products.objects.filter(sub_cat = 'pants',  price > high_price, age = 'adult', color = color)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)



def adult_pants_high_color_size(request):    
    high_price = request.GET['high_price']
    color = request.GET['color']
    size = request.GET['size']
    list = products.objects.filter(sub_cat = 'pants',  price > high_price, age = 'adult', color = color, size = size)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)





##adult - saree


def adult_saree(request):       
    list = products.objects.filter(sub_cat = 'saree', age = 'adult')
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)

def adult_saree_color(request):       
    color = request.GET['color']
    list = products.objects.filter(sub_cat = 'saree', age = 'adult', color = color)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)



def adult_saree_size(request):   
    size = request.GET['size']    
    list = products.objects.filter(sub_cat = 'saree', age = 'adult', size = size)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)


def adult_saree_size_color(request):   
    size = request.GET['size']    
    color = request.GET['color']
    list = products.objects.filter(sub_cat = 'saree', age = 'adult', size = size, color = color)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)




def adult_saree_low(request):    
    low_price = request.GET['low_price']
    list = products.objects.filter(sub_cat = 'saree',  price <= low_price, age = 'adult')
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)

def adult_saree_low_size(request):    
    low_price = request.GET['low_price']
    size = request.GET['size']
    list = products.objects.filter(sub_cat = 'saree',  price <= low_price, age = 'adult', size = size)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)


def adult_saree_low_color(request):    
    low_price = request.GET['low_price']
    color = request.GET['color']
    list = products.objects.filter(sub_cat = 'saree',  price <= low_price, age = 'adult', color = color)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)



def adult_saree_low_color_size(request):    
    low_price = request.GET['low_price']
    color = request.GET['color']
    size = request.GET['size']
    list = products.objects.filter(sub_cat = 'saree',  price <= low_price, age = 'adult', color = color, size = size)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)


def adult_saree_high(request):    
    high_price = request.GET['high_price']
    list = products.objects.filter(sub_cat = 'saree', price > high_price, age = 'adult')
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)

def adult_saree_high_size(request):    
    high_price = request.GET['high_price']
    size = request.GET['size']
    list = products.objects.filter(sub_cat = 'saree',  price > high_price, age = 'adult', size = size)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)




def adult_saree_high_color(request):    
    high_price = request.GET['high_price']
    color = request.GET['color']
    list = products.objects.filter(sub_cat = 'saree',  price > high_price, age = 'adult', color = color)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)



def adult_saree_high_color_size(request):    
    high_price = request.GET['high_price']
    color = request.GET['color']
    size = request.GET['size']
    list = products.objects.filter(sub_cat = 'saree',  price > high_price, age = 'adult', color = color, size = size)
    data = []
    for x in list:
        data.append(x)
    return JsonResponse(data, safe = False)













