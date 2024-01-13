class BankAccount {
    private String name;
    private int id;
    private int pin;
    private int balance;

    public BankAccount(String name, int id, int pin, int balance) {
        this.name = name;
        this.id = id;
        this.pin = pin;
        this.balance = balance;
    }

    public void deposit(int id, int pin, int amt) {
        if (id == this.id && pin == this.pin) {
            this.balance += amt;
            System.out.println("Deposited " + amt + " rupees into your bank account!");
        } else {
            System.out.println("Incorrect ID or PIN entered. Try again!");
            System.exit(0);
        }
    }

    public void withdraw(int id, int pin, int amt) {
        if (id == this.id && pin == this.pin) {
            if (amt <= this.balance) {
                this.balance -= amt;
                System.out.println("Withdrew " + amt + " rupees from your bank account!");
            } else {
                System.out.println("Insufficient funds. Try again!");
                System.exit(0);
            }
        } else {
            System.out.println("Incorrect ID or PIN entered. Try again!");
            System.exit(0);
        }
    }

    public String curr_balance() {
        return "Available Funds: " + this.balance + "!";
    }
}

class Main {
    public static void main(String[] args) {
        BankAccount customer1 = new BankAccount("Sankar Addala", 21314254, 111, 100);
        customer1.deposit(21314254, 111, 100);
        System.out.println(customer1.curr_balance());
        customer1.withdraw(21314254, 111, 50);
        System.out.println(customer1.curr_balance());
    }
}

"""
Output:
    

Deposited 100 rupees into your bank account!
Available Funds: 200!
Withdrew 50 rupees from your bank account!
Available Funds: 150!

"""
