import string
from web3 import Web3
from web3.middleware import geth_poa_middleware

w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))

w3.middleware_onion.inject(geth_poa_middleware, layer=0)

address_contract = "0x7270701c53C3fCEcBbf25a5108882c055FF41cF1"
abi = '''[
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": false,
				"internalType": "address",
				"name": "owner",
				"type": "address"
			},
			{
				"indexed": false,
				"internalType": "uint256",
				"name": "idEstate",
				"type": "uint256"
			},
			{
				"indexed": false,
				"internalType": "uint256",
				"name": "idAdvert",
				"type": "uint256"
			},
			{
				"indexed": false,
				"internalType": "uint256",
				"name": "price",
				"type": "uint256"
			}
		],
		"name": "AdCreated",
		"type": "event"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": false,
				"internalType": "address",
				"name": "owner",
				"type": "address"
			},
			{
				"indexed": false,
				"internalType": "uint256",
				"name": "idEstate",
				"type": "uint256"
			},
			{
				"indexed": false,
				"internalType": "uint256",
				"name": "idAdvert",
				"type": "uint256"
			},
			{
				"indexed": false,
				"internalType": "enum EstateAgency.AdvertisementStatus",
				"name": "adstatus",
				"type": "uint8"
			}
		],
		"name": "AdUpdated",
		"type": "event"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": false,
				"internalType": "address",
				"name": "owner",
				"type": "address"
			},
			{
				"indexed": false,
				"internalType": "uint256",
				"name": "idEstate",
				"type": "uint256"
			},
			{
				"indexed": false,
				"internalType": "enum EstateAgency.EstateType",
				"name": "eType",
				"type": "uint8"
			}
		],
		"name": "EstateCreated",
		"type": "event"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": false,
				"internalType": "address",
				"name": "owner",
				"type": "address"
			},
			{
				"indexed": false,
				"internalType": "address",
				"name": "buyer",
				"type": "address"
			},
			{
				"indexed": false,
				"internalType": "uint256",
				"name": "idEstate",
				"type": "uint256"
			},
			{
				"indexed": false,
				"internalType": "uint256",
				"name": "idAdvert",
				"type": "uint256"
			},
			{
				"indexed": false,
				"internalType": "uint256",
				"name": "price",
				"type": "uint256"
			},
			{
				"indexed": false,
				"internalType": "enum EstateAgency.AdvertisementStatus",
				"name": "adStatus",
				"type": "uint8"
			}
		],
		"name": "EstatePurchased",
		"type": "event"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": false,
				"internalType": "address",
				"name": "owner",
				"type": "address"
			},
			{
				"indexed": false,
				"internalType": "uint256",
				"name": "idEstate",
				"type": "uint256"
			},
			{
				"indexed": false,
				"internalType": "bool",
				"name": "isActive",
				"type": "bool"
			}
		],
		"name": "EstateUpdated",
		"type": "event"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": false,
				"internalType": "address",
				"name": "buyer",
				"type": "address"
			},
			{
				"indexed": false,
				"internalType": "uint256",
				"name": "price",
				"type": "uint256"
			}
		],
		"name": "FundsSent",
		"type": "event"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"name": "ads",
		"outputs": [
			{
				"internalType": "address",
				"name": "owner",
				"type": "address"
			},
			{
				"internalType": "address",
				"name": "buyer",
				"type": "address"
			},
			{
				"internalType": "uint256",
				"name": "price",
				"type": "uint256"
			},
			{
				"internalType": "enum EstateAgency.AdvertisementStatus",
				"name": "adStatus",
				"type": "uint8"
			},
			{
				"internalType": "uint256",
				"name": "estateID",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "adID",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "adID",
				"type": "uint256"
			}
		],
		"name": "buyEstate",
		"outputs": [],
		"stateMutability": "payable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "estateID",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "price",
				"type": "uint256"
			}
		],
		"name": "createAd",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "name",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "estateAddress",
				"type": "string"
			},
			{
				"internalType": "enum EstateAgency.EstateType",
				"name": "eType",
				"type": "uint8"
			},
			{
				"internalType": "uint256",
				"name": "rooms",
				"type": "uint256"
			},
			{
				"internalType": "string",
				"name": "describe",
				"type": "string"
			}
		],
		"name": "createEstate",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"name": "estates",
		"outputs": [
			{
				"internalType": "string",
				"name": "name",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "estateAddress",
				"type": "string"
			},
			{
				"internalType": "uint256",
				"name": "estateID",
				"type": "uint256"
			},
			{
				"internalType": "enum EstateAgency.EstateType",
				"name": "eType",
				"type": "uint8"
			},
			{
				"internalType": "uint256",
				"name": "rooms",
				"type": "uint256"
			},
			{
				"internalType": "string",
				"name": "describe",
				"type": "string"
			},
			{
				"internalType": "address",
				"name": "owner",
				"type": "address"
			},
			{
				"internalType": "bool",
				"name": "isActive",
				"type": "bool"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "getAds",
		"outputs": [
			{
				"components": [
					{
						"internalType": "address",
						"name": "owner",
						"type": "address"
					},
					{
						"internalType": "address",
						"name": "buyer",
						"type": "address"
					},
					{
						"internalType": "uint256",
						"name": "price",
						"type": "uint256"
					},
					{
						"internalType": "enum EstateAgency.AdvertisementStatus",
						"name": "adStatus",
						"type": "uint8"
					},
					{
						"internalType": "uint256",
						"name": "estateID",
						"type": "uint256"
					},
					{
						"internalType": "uint256",
						"name": "adID",
						"type": "uint256"
					}
				],
				"internalType": "struct EstateAgency.Advertisement[]",
				"name": "",
				"type": "tuple[]"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "getBalance",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "getEstates",
		"outputs": [
			{
				"components": [
					{
						"internalType": "string",
						"name": "name",
						"type": "string"
					},
					{
						"internalType": "string",
						"name": "estateAddress",
						"type": "string"
					},
					{
						"internalType": "uint256",
						"name": "estateID",
						"type": "uint256"
					},
					{
						"internalType": "enum EstateAgency.EstateType",
						"name": "eType",
						"type": "uint8"
					},
					{
						"internalType": "uint256",
						"name": "rooms",
						"type": "uint256"
					},
					{
						"internalType": "string",
						"name": "describe",
						"type": "string"
					},
					{
						"internalType": "address",
						"name": "owner",
						"type": "address"
					},
					{
						"internalType": "bool",
						"name": "isActive",
						"type": "bool"
					}
				],
				"internalType": "struct EstateAgency.Estate[]",
				"name": "",
				"type": "tuple[]"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "adID",
				"type": "uint256"
			},
			{
				"internalType": "enum EstateAgency.AdvertisementStatus",
				"name": "adstatus",
				"type": "uint8"
			}
		],
		"name": "updateAdStatus",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "estateID",
				"type": "uint256"
			},
			{
				"internalType": "bool",
				"name": "status",
				"type": "bool"
			}
		],
		"name": "updateEstateStatus",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "value",
				"type": "uint256"
			}
		],
		"name": "withDraw",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	}
]'''
contract = w3.eth.contract(address=address_contract, abi=abi)

def auth():
    public_key = input("Введите публичный ключ: ")
    password = input("Введите пароль: ")
    try:
        w3.geth.personal.unlock_account(public_key, password)
        print("Авторизация прошла успешно.")
        return public_key
    except Exception as e:
        print(e)
        return None
def hasPunct(password):
    for i in password:
        if i in string.punctuation:
            return True
    return False

def hasCapital(password):
    for i in password:
        if i in string.ascii_uppercase:
            return True
    return False

def hasLowers(password):
    for i in password:
        if i in string.ascii_lowercase:
            return True
    return False

def hasDigit(password):
    for i in password:
        if i in string.digits:
            return True
    return False

def registration():
    while (True):
        password = input("Введите пароль: ")
        if (len(password) >= 12 and hasDigit(password) and
                hasCapital(password) and hasLowers(password) and
                hasPunct(password)):
            break
        else:
            print("Слишком слабый пароль.")
    address = w3.geth.personal.new_account(password)
    print(f"Адрес нового аккаунта: {address}")

def send_eth(account):
    amount = int(input("Введите сумму: "))
    try:
        tx_hash = contract.functions.sendEth().transact(
            {
                "from": account,
                "value": amount
            }
        )
        print("Транзакция успешно отправлена. Хэш транзакции: ", tx_hash.hex())
    except Exception as e:
        print("Ошибка при отправке эфира: ", e)

def get_balance(account):
    try:
        balance_wei = contract.functions.getBalance().call(
            {
                "from": account
            }
        )
        print("Баланс аккаунта: ", balance_wei, " WEI")
    except Exception as e:
        print("Ошибка при получении баланса: ", e)

def withdraw(account):
    amount = int(input("Введите сумму для снятия: "))
    try:
        tx_hash = contract.functions.withDraw(amount).transact(
            {
                "from": account
            }
        )
        print("Транзакция на снятие средств успешно отправлена. Хэш транзакции: ", tx_hash.hex())
    except Exception as e:
        print("Ошибка при снятии средств: ", e)

def createEstate(account):
    name = input("Введите название недвижимости: ")
    estAddress = input("Введите адрес недвижимости: ")
    print("\n\tТипы недвижимости:")
    print("1. Дом \n2. Апартамент \n3. Квартира \n4. Лофт")
    while(True):
        try:
            eType = int(input("Введите тип недвижимости: "))
            break
        except (ValueError):
            print("Введите число типа.")
            continue
    while (True):
        try:
            rooms = int(input("Введите количество комнат: "))
            break
        except (ValueError):
            print("Введите число комнат.")
            continue
    decr = input("Опишите недвижимость: ")
    try:
        tx_hash = contract.functions.createEstate(name, estAddress, eType, rooms, decr).transact(
            {
                "from": account
            }
        )
        print("Транзакция на создание недвижимости отправлена успешно. Хэш транзакции: ", tx_hash.hex())
    except Exception as e:
        print("Ошибка при создании недвижимости: ", e)

def createAd(account):
    try:
        est = contract.functions.getEstates().call()
        print("Список недвижимостей: ", est)
    except Exception as e:
        print("Ошибка при выводе недвижимостей: ", e)

    while (True):
        try:
            idEst = int(input("\nВведите ID недвижимости: "))
            break
        except (ValueError):
            print("Такого ID нет.")
            continue
    while (True):
        try:
            price = int(input("Введите цену недвижимости: "))
            if (price < 0):
                price = 0
            break
        except (ValueError):
            print("Введите число.")
            continue
    try:
        tx_hash = contract.functions.createAd(idEst, price).transact(
            {
                "from": account
            }
        )
        print("Транзакция на создание объявления отправлена успешно. Хэш транзакции: ", tx_hash.hex())
    except Exception as e:
        print("Ошибка при создании объявления: ", e)

def buyEstate(account):
    try:
        est = contract.functions.getAds().call()
        print("Список объявлений: ", est)
    except Exception as e:
        print("Ошибка при выводе объявлений: ", e)
    while (True):
        try:
            idAD = int(input("\nВведите ID обьявления: "))
            break
        except (ValueError):
            print("Такого ID нет.")
            continue
    try:
        tx_hash = contract.functions.buyEstate(idAD).transact(
            {
                "from": account
            }
        )
        print("Транзакция на покупку недвижимости отправлена успешно. Хэш транзакции: ", tx_hash.hex())
    except Exception as e:
        print("Ошибка при покупке недвижимости: ", e)

def updateEstate(account):
    try:
        est = contract.functions.getEstates().call()
        print("Список недвижимостей: ", est)
    except Exception as e:
        print("Ошибка при выводе недвижимостей: ", e)
    while (True):
        try:
            idEst = int(input("\nВведите ID недвижимости: "))
            break
        except (ValueError):
            print("Такого ID нет.")
            continue
    while (True):
        try:
            status = bool(input("Заблокировать (false) или разблокировать (true) недвижимость?\n"))
            break
        except (ValueError):
            print("Введите true или false.")
            continue
    try:
        tx_hash = contract.functions.updateEstateStatus(idEst, status).transact(
            {
                "from": account
            }
        )
        print("Транзакция на обновление статуса недвижимости отправлена успешно. Хэш транзакции: ", tx_hash.hex())
    except Exception as e:
        print("Ошибка при обновлении статуса недвижимости: ", e)

def updateAd(account):
    try:
        est = contract.functions.getAds().call()
        print("Список объявлений: ", est)
    except Exception as e:
        print("Ошибка при выводе объявлений: ", e)
    while (True):
        try:
            idAd = int(input("\nВведите ID объявления: "))
            break
        except (ValueError):
            print("Такого ID нет.")
            continue
    while (True):
        try:
            status = int(input("Заблокировать (1) или разблокировать (0) объявление?\n"))
            break
        except (ValueError):
            print("Введите 0 или 1.")
            continue
    try:
        tx_hash = contract.functions.updateAdStatus(idAd, status).transact(
            {
                "from": account
            }
        )
        print("Транзакция на обновление статуса объявления отправлена успешно. Хэш транзакции: ", tx_hash.hex())
    except Exception as e:
        print("Ошибка при обновлении статуса объявления: ", e)



def main():
    account = ""
    is_auth = False
    while True:
        if not is_auth:
            choice = input("Выберите: \n1. Авторизация\n2. Регистрация\n")
            match choice:
                case "1":
                    account = auth()
                    if account is not None:
                        is_auth = True
                case "2":
                    registration()
        else:
            choice = input("Выберите: \n1. Создать недвижимость \n2. Создать объявление"
                           "\n3. Купить недвижимость \n4. Обновить недвижимость/объявление "
                           "\n5. Вывести средства \n6. Посмотреть баланс аккаунта \n7. Выйти\n")
            match choice:
                case "1":
                    createEstate(account)
                case "2":
                    createAd(account)
                case "3":
                    buyEstate(account)
                case "4":
                    ch = input("Выберите: \n1. Обновить статус недвижимости \n2. Обновить статус объявления\n")
                    if (ch == "1"):
                        updateEstate(account)
                    elif (ch == "2"):
                        updateAd(account)
                    else:
                        print("Такой опции нет.")
                case "5":
                    withdraw(account)
                case "6":
                    print(f"Баланс аккаунта: {w3.eth.get_balance(account)} WEI")
                case "7":
                    is_auth = False
                case _:
                    print("Введите корректное число!")

if __name__ == "__main__":
    main()