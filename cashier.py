#-------------------------------------------------------
# Machine for a store.
#-------------------------------------------------------

#Functions:

def dis(a,b):
  return a - b

def tax(a):
  tx = (dis_price * 0.085)
  return dis_price + tx


#-------------------------------------------------------
# Main Program:


#-------------------------------------------------------
# Variables:

bag = 30
watch = 40
shoes = 35
total1 = 0
total2 = 0
total3 = 0

#-------------------------------------------------------
# Loop:

while True:

  sel = int(input('what do you want (1 = bag , 2 = watch, 3 = shoes, 4 = exit):'))
  if sel == 1:
    quan = int(input('enter quantity:'))
    total1 += bag * quan
  elif sel == 2:
     quan = int(input('enter quantity:'))
     total2 += watch * quan
  elif sel == 3:
     quan = int(input('enter quantity:'))
     total3 += shoes * quan
  elif sel == 4:
    f_total = total1 + total2 + total3
    print('order finished= $',f_total)
    break

else:
  print('invalid inbput')

#-------------------------------------------------------
# Discount Condi:

if 50 < f_total <= 100:
 discount = (f_total * 5) // 100
elif  100 < f_total <= 200:
  discount = (f_total * 10) // 100
elif 200 < f_total <= 500:
 discount = (f_total * 15) // 100
elif f_total >= 500:
  discount = (f_total * 20) // 100

#-------------------------------------------------------
# Cutting Discount:

dis_price = dis(f_total,discount)
print('the discounted price is $', round(dis_price,2))

#-------------------------------------------------------
# Taxation:

tax_p = tax(discount)
print('final price after tax= $', round(tax_p,2))