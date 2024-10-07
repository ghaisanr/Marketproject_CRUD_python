price_apple=10000
price_orange=15000
price_grape=20000

stock_apple=7
stock_orange=7
stock_grape=7

amount_apple=stock_apple+1
while amount_apple>stock_apple:
    amount_apple=int(input("masukkan jumlah apel="))
    if amount_apple>stock_apple:
        print("jumlah dimasukkan terlalu banyak")
    else:
        stock_apple=stock_apple-amount_apple
        break
amount_orange=stock_orange+1
while amount_orange>stock_orange:
    amount_orange=int(input("masukkan jumlah jeruk="))
    if amount_orange>stock_orange:
        print("jumlah dimasukkan terlalu banyak")
    else:
        stock_orange=stock_orange-amount_orange
        break
amount_grape=stock_grape+1
while amount_grape>stock_grape:
    amount_grape=int(input("masukkan jumlah grape="))
    if amount_grape>stock_grape:
        print("jumlah dimasukkan terlalu banyak")
    else:
        stock_grape=stock_grape-amount_grape
        break

total_apple=price_apple*amount_apple
total_orange=price_orange*amount_orange
total_grape=price_grape*amount_grape
total=total_apple+total_orange+total_grape

print("\n===detail Belanja===")
print(f"apel: {amount_apple} x {price_apple} = {total_apple}")
print(f"jeruk: {amount_orange} x {price_orange} = {total_orange}")
print(f"grape: {amount_grape} x {price_grape} = {total_grape}")
print("\ntotal belanja: ",total)

pay=0
while total>pay:
    pay=int(input("\nmasukkan jumlah uang:"))
    if total>pay:
        mines_money=total-pay
        print("transaksi anda dibatalkan")
        print(f"uang kurang sebesar {mines_money}\n\n")
    elif total==pay:
        print("terimakasih\n\n")
    else:
        surplus_money=pay-total
        print("terimakasih")
        print(f"\nuang kembali anda: {surplus_money}\n\n")