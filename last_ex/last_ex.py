# -*- coding: utf8 -*-

def check_my_wallet(my_money_dict) :
    #현재 상황을 보여준다. 
    print '내 주머니 상황'
    print '--------------------'
    for key,value in sorted(my_money_dict.items()):
        print "%d원이 %d개 있어요" % (key,value)

def insert_money(my_money_dict) :
    # 돈을 지갑에서 꺼내어 자판기에 투입하는 과정을 처리
    inserted_money = 0 
    while ( inserted_money not in my_money_dict or my_money_dict[inserted_money] < 1) :
        #돈을 입력받는 함수
        inserted_money = raw_input("\n돈을 넣으세요(입금을 마치려면 엔터) : ")    

        #숫자가 아닌 입력에 대한 예외 처리
        try : 
            #입력 데이터를 숫자형으로 형변환 (왜냐면 $raw_input()은 숫자입력도 문자열로 입력을 받기때문)
            inserted_money = int(inserted_money)
            #지갑에 없는 단위이거나 갯수가 0일 경우 에러메세지 출력 후 while문 반복
            if ( inserted_money not in my_money_dict or my_money_dict[inserted_money] < 1) :
                print "슬프지만.. 지갑에 존재하지 않는 돈이네요..."
        except :
            print "외국돈은 투입이 불가능 합니다^^^^^"

    # 지갑에서 투입한 금액만큼 빼준다.
    my_money_dict[inserted_money] -= 1
    return inserted_money

def show_menu(products_dict, inserted_money) :
    print '--------------------'
    goodinfo = dict()

    #!!!!!동일 금액 상품이 있을경우에 대한 추가적인 처리가 필요함!!!!!
    for product_name in products_dict :
        goodinfo[products_dict[product_name]['price']] = [product_name]

    # 그 금액으로 뽑을 수 있는 상품을 나열
    print goodinfo
    for product_price in goodinfo :
        if (inserted_money >= product_price ) :
           print "지금 넣으신 금액으로 %s을 뽑을 수 있겠네요^^ (개당 %d원, %d개 남음)" % (goodinfo[product_price][0],products_dict[goodinfo[product_price][0]]['price'],products_dict[goodinfo[product_price][0]]['number'])

    
def take_product(products_dict, inserted_money) :
    #입력된 금액을 이용하여 상품을 출력(상품갯수를 줄이고, 그 금액만큼 입력금액에서 빼기)
    selected_product = raw_input("상품을 고르세요 : ")    
    try :
        if ( selected_product in products_dict) :
            inserted_money -= products_dict[selected_product]['price']
            products_dict[selected_product]['number'] -= 1
            print "%s맛있게 드십시오~"  % selected_product
            print "남은 금액은 %d입니다. " % inserted_money
    except :
        print "없는 상품입니다."

def vending_machine(my_money_dict, products_dict) :

    #1: 돈을 투입합니다.
    inserted_money_sum = 0  #최종 투입된 금액

    while(True):
        #매번 지갑의 상황을 보여준다.
        check_my_wallet(my_money_dict);

        #자판기에 돈을 넣는다.
        inserted_money = insert_money(my_money_dict)

        #누적해서 투입된 돈의 합을 표시한다.
        inserted_money_sum += inserted_money
        print '지금까지 %d가 투입되었네요' % inserted_money_sum

        #menu를 출력
        show_menu(products_dict, inserted_money);

        #입력된 금액이 충분할 경우 while문을 탈출
        insert_flag = raw_input("충분합니까? (입금을 마치려면 yes) : ")    
        if insert_flag == 'yes':
            break
    
    #상품을 고른다. !!!!금액이 남았을 경우에 대한 처리가 추가로 필요함!!!!
    take_product(products_dict, inserted_money)


# 메인 로직
if __name__ == '__main__':

    products_dict = {
                    'vita500'   : {'price' : 500, 'number' : 2},
                    'milk'      : {'price' : 700, 'number' : 13},
                    'coffee'    : {'price' : 900, 'number' : 8}
                    }

    #               { 돈의종류 : 돈의갯수 }
    my_money_dict = {5000 : 2 , 1000 : 1,   500 : 2 , 100 : 8}

   
    #자판기 프로그램 실행 
    vending_machine(my_money_dict, products_dict)
