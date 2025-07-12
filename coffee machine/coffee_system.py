from product_List import Coffee_List

recourse = {
        "water" : [300, "ml"],
        "milk" : [300, "ml"],
        "coffee": [150,"g"]    
}
pricing = {
    "expresso": 50,
    "latte": 70,
    "coppucino": 100
}

def report_transfer():      
        if user_input in report_data:
                for i in report_data[user_item]:
                        recourse[i][0] -= report_data[user_item][i][0]       
def final_item_calculation():
    piso = int(input("please enter how many piso: "))
    limang_piso = int(input("please enter how many limang piso:"))
    sampung_piso = int(input("please enter how many sampung piso: "))
    user_total = 0
    informational = user_item
    user_total = piso + (5 * limang_piso) + (10 * sampung_piso) 
    if informational in pricing:
        if user_total < pricing[informational]:
                print("invalid funds")
        if user_total > pricing[informational] :
            final_total = user_total - pricing[informational]
            print(f"your change is {final_total}php")
        else:
               print(recourse)
               
end = True
while end:
        user_item = ""
        user_input = input("please enter your order(expresso, latte, or coppucino): ")
        chosen_drink_price = "expresso"
        user_item += user_input
        report_data = Coffee_List()
        if user_input == "report":
                print(recourse)

        else:
                if user_input == "expresso":
                        report_transfer()
                        final_item_calculation()
                elif user_input == "latte":
                        report_transfer()
                        final_item_calculation()
                elif user_input == "coppucino":
                        report_transfer()
                        final_item_calculation()
                else:
                        print("invalid option")

        
