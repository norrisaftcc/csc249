#include <iostream>
#include "Inventory.h"
using namespace std;

/*
CSC 249 
M4HW1 - Store Inventory (planning phase)
norrisa
3/16/23

One way to build M4HW is to start from the lab, and add
features. Another would be to lay out the specific 
requirements (user stories), and build from scratch.
In this project I'll do the latter.

User story structure:
As a customer, I want to <X> so that I can shop for items.
In a larger program, the "As a..." and the "so that I can..." 
items may differ, as programs have multiple users and they 
have multiple goals. For this, all these stories are for the shopper.

I want to...(Iteration 1: Bronze)
- List the shop inventory
-   List my shopping cart contents
- Add items from the shop to my cart
(Iteration 2: Silver)
- Remove items from my cart
(Iteration 3: Gold)
- [I won't phrase this as user stories, but for Gold we have
  to properly handle quantities of items. For now we'll leave
  quantity at one in all cases.]
*/

int main() {
  cout << "Shopping Cart Application" << endl;

  // create a product (Node)
  Product* prod_apple = new Product("apple", 0.25);
  cout << prod_apple->name << " " << prod_apple->price << endl;

  
}