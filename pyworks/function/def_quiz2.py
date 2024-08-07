def get_price(unit_price, cnt):
    total_price = unit_price * cnt
    if total_price < 20000:
        total_price += 2500
        return total_price
    else:
        return total_price

product1 = get_price(10000,3)
product2 = get_price(5000,3)

print(f"상품1 가격: {format(product1, ',d')}원")
print(f"상품2 가격: {format(product2, ',d')}원")
