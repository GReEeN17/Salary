pragma solidity ^0.4.0;

contract Salary {
    //Структура рабочего
    struct Worker {
        address addr; //Адрес рабочего, получающего зарплату
        uint amount; //Количество денег уже переведённых ему на данный момент
    }

    //Переменная счёта босса
    uint amountOfOurOrganisation = 0;
    //Переменная, подсчитывающая количество рабочих на данный момент
    uint count;
    //Массив рабочих
    mapping (uint => Worker) public workers;
    //Функция добавдения нового рабочего
    function new_worker(address addr) public returns (uint) {
        workers[count++] = Worker(addr, 0);
    }
    //Функция пополнения кошелька
    function replenishment() public payable {
        amountOfOurOrganisation += msg.value;
    }
    //Функция вывода денег с переменной, отвечающей за подсчёт количества денег организации на кошелёк босса
    function replenishmentOfBoss() public payable {
        msg.sender.transfer(amountOfOurOrganisation);
        amountOfOurOrganisation = 0;
    }

    //Функция получения рабочим зарплаты
    function salary(uint index_of_worker) public payable {
        Worker storage wrkr;
        wrkr = workers[index_of_worker];
        wrkr.addr.transfer(msg.value);
        amountOfOurOrganisation -= msg.value;
    }
}
