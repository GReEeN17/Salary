from web3 import Web3
import time
import json

w3 = Web3(Web3.HTTPProvider('HTTP://127.0.0.1:7545'))           #Подключение аккаунта ganache
accounts = w3.eth.accounts          #Получение адресов кошельков

fn_abi = "Salary.abi"       #Имена файлов, в которых хранится информация о контракте
fn_bin = "Salary.bin"

with open(fn_abi, 'r') as f:        #Запись информации в файлы
    abi = json.load(f)
with open(fn_bin, 'r') as f:
    bin = f.read()

factory = w3.eth.contract(abi=abi, bytecode=bin)        #Создание объекта смарт контракта
#Пример работы смарт контракта
factory.functions.new_worker(accounts[9])           #Создание аккаунтов трёх рабочих
factory.functions.new_worker(accounts[8])
factory.functions.new_worker(accounts[7])

tx_hash = factory.constructor().transact({'from': accounts[0]})         #Получение данных о переводах
receipt = w3.eth.waitForTransactionReceipt(tx_hash)
#Бесконечный цикл, смысл которого в том, что каждые пол месяца совершается две сделки, далее через ещё полмесяца сотрудники получают зарплату
bol = True
while bol:
    factory.functions.replenishment().transact({'from': accounts[1], 'to': receipt.contractAddress, 'value': Web3.toWei(0.001, 'ether')})
    factory.functions.replenishment().transact({'from': accounts[2], 'to': receipt.contractAddress, 'value': Web3.toWei(0.003, 'ether')})
    time.sleep(15 * 24 * 60 * 60)
    factory.functions.salary(0).transact({'from': accounts[0], 'to': receipt.contractAddress, 'value': Web3.toWei(0.001, 'ether')})
    factory.functions.salary(1).transact({'from': accounts[0], 'to': receipt.contractAddress, 'value': Web3.toWei(0.001, 'ether')})
    factory.functions.salary(2).transact({'from': accounts[0], 'to': receipt.contractAddress, 'value': Web3.toWei(0.001, 'ether')})
    time.sleep(15 * 24 * 60 * 60)
