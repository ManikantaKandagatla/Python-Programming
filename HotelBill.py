def get_input():
    item_amts = [50,100,200]
    item_codes = [1,2,3]
    menu_items = ['breakfast','north or south meal','non-veg']
    item_dict = {}
    print 'Breakfast Menu:'
    print 'Code 1:Rs 50/- plate for any kind of breakfast'
    print 'Code 2:Rs 100/- plate for north/south veg meal'
    print 'Code 3:Rs 200/- plate for non-veg meal'
    while (True):
        flag = raw_input("Enter y/n to Order: ")
        if flag == 'y':
            item = int(raw_input("     Choose item Code: "))
            if item not in item_codes:
                print '    Choose correct item code...'
            else:
                quantity = int(raw_input("     Enter quantity: "))
                if item not in item_dict.keys():
                    item_dict[item] = quantity
                else:
                    if item in item_dict.keys():
                        item_dict[item] = item_dict[item] + quantity
        elif flag == 'n':
            break
        else:
            print 'Please provide correct order...'
    cal_amount(item_dict,item_amts,menu_items)
def cal_amount(item_dict, item_amts,menu_items):
    total = 0
    order_items = item_dict.items()
    print '***********************************************'
    print 'Order Given'
    for pair in item_dict.items():
        print menu_items[pair[0]-1]," : ",pair[1] ,   item_amts[pair[0]-1]*pair[1]
        total = total + item_amts[pair[0]-1]*pair[1]
    print 'Total Bill: ', total

get_input()




