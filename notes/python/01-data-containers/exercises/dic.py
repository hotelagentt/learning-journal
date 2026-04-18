#字典案例-购物车系统
shopping_cart = {}#shopping_cart = {"goods_name": {"price":"goods_price","num" ="goods_num"}... }

menu = '''
########购物车系统########
#      1.添加购物车      #
#      2.修改购物车      #
#      3.删除购物车      #
#      4.查询购物车      #
#      5.退出购物车      #
#########################
'''
print("欢迎来到购物车系统")
print(menu)

while True :
    choice = input("请选择操作(1-5): ")
    match choice:
        # 添加购物车
        case "1":
            goods_name = input("请输入要添加的商品名称: ")
            if goods_name in shopping_cart:
                    print("商品已存在,请重新输入")
                    continue
            else:
                    goods_price = float(input("请输入商品价格: "))
                    goods_num = int(input("请输入商品数量: "))
                    shopping_cart[goods_name] = {"price":goods_price, "num":goods_num}
                    print(f"添加成功!商品{goods_name},价格{goods_price},数量{goods_num}")


        # 修改购物车
        case "2":
            goods_name = input("请输入要修改的商品名称: ")
            if goods_name not in shopping_cart:
                print("商品不存在,请重新输入")
                continue


            else:
                goods_price = float(input("请输入修改后的商品价格: "))
                goods_num = int(input("请输入修改后的商品数量: "))
                shopping_cart[goods_name] = {"price":goods_price, "num":goods_num}
                print(f"修改成功!商品{goods_name},价格{goods_price},数量{goods_num}")


        # 删除购物车
        case "3":
            goods_name = input("请输入要删除的商品名称: ")
            if goods_name not in shopping_cart:
                print("商品不存在,请重新输入")
                continue
            else:
                del shopping_cart[goods_name]
                print(f"删除成功!商品{goods_name}已删除")

        # 查询购物车
        case "4":
            print("购物车如下: ")
            if shopping_cart == {}:
                print("购物车为空")
                continue
            else:
                for goods_name in shopping_cart.keys():
                    goods_info = shopping_cart[goods_name]
                    print(f"商品名称: {goods_name},价格: {goods_info['price']},数量: {goods_info['num']}")



        # 退出购物车
        case "5":
            print("已退出购物车")
            break

        case _:
            print("输入错误,请重新输入")
