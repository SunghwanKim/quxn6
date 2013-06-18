coin50 = 10
coin100 = 10
coin500 = 5
coin1000 = 7
product = {pepsi : [10,300] , water : [10,200]}
signedmoney = 0

def showcase():
	#product의 내용을 랜덤으로 출력
	showstatus(1)

def inputmoney():
	#insert money(50,100,500,1000)
	#if (입력된 동전의 갯수가 갖고있는 돈보다 많을때는 )
		#경고메세지 출력)
	#else 
		#갖고있는 동전 갯수에서 입력된 동전의 갯수를 뺀다
		#입력된 액수만큼 자판기에 돈이 추가된다.
	showstatus(2)

def productpic():
	#insert (showcase에서 표시해준 product를 선택)
	#return 선택한 값
	showstatus(3)

def getProduct():
	#productpic의 리턴값을 갖고와서 (물품명)
	#자판기 물품 갯수 - 1
	#자판기에 입력된 금액 - 선택한 물품으 가격
	showstatus(4)


def change():
	#if(signedmoney > 0 )
		#coin1000 = coin1000 + (signedmoney / 1000) 
		#signedmoney % 1000
		#쭉쭉쭉쭉 거슬러준다.
	#else
		#print("거스름돈이 없습니다.")
	showstatus(5)


def showstatus():
	#if(1 -> showcase)
		#진열된 상품명이랑 갯수를 표시해준다
	#if(2 -> inputmoney)
		#자판기에 들어간 돈 액수와 내가 갖고있는 코인들의 갯수를 출력
	
