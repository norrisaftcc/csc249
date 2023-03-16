#ifndef INVENTORY_H
#define INVENTORY_H

#include <iostream>
#include <string>
using namespace std;
/*
Inventory class - based on the linked list data structure
Inventories can do the following:
- list their contents (which are Product objects)
- retrieve a product by name
- add a product to their contents
- remove a product from their contents

Handling quantities (which are always "one" for now" in Product 
is left to the developer.)


*/

class Node {
public:
   string name;
   double price;

   Node* next;
   Node* previous;

   Node(string prod_name, double prod_price) {
      name = prod_name;
      price = prod_price;
      next = nullptr;
      previous = nullptr;
   }
};

class LinkedList {
private:
   Node* head;
   Node* tail;

public:
   string list_name;
   LinkedList() {
      list_name = "";
      head = nullptr;
      tail = nullptr;
   }
   
   virtual ~LinkedList() {
      Node* currentNode = head;
      while (currentNode) {
         Node* toBeDeleted = currentNode;
         currentNode = currentNode->next;
         delete toBeDeleted;
      }
   }
    
   void Append(Node* newNode) {
      if (head == nullptr) {
         head = newNode;
         tail = newNode;
      }
      else {
         tail->next = newNode;
         newNode->previous = tail;
         tail = newNode;
      }
   }
   /*
   void Prepend(Node* newNode) {
      if (head == nullptr) {
         head = newNode;
         tail = newNode;
      }
      else {
         newNode->next = head;
         head->previous = newNode;
         head = newNode;
      }
   }
   */
   
   void PrintList(std::ostream& printStream, const std::string& separator = ", ") {
      Node* probe = head;
      // Show name of inventory, then contents
      cout << list_name << " contains: "<< endl;
      while (probe != nullptr) {
         printStream << "\tProduct: ";
         printStream << probe->name << " ($" << probe->price << ")";
         printStream << std::endl;
         probe = probe->next;
        
      }
      printStream << std::endl;
   }
   /*
   void InsertAfter(Node* currentNode, Node* newNode) {
      if (head == nullptr) {
         head = newNode;
         tail = newNode;
      }
      else if (currentNode == tail) {
         tail->next = newNode;
         newNode->previous = tail;
         tail = newNode;
      }
      else {
         Node* successor = currentNode->next;
         newNode->next = successor;
         newNode->previous = currentNode;
         currentNode->next = newNode;
         successor->previous = newNode;
      }
   }
   */
   
   void Remove(Node* currentNode) {
      Node* successor = currentNode->next;
      Node* predecessor = currentNode->previous;
      
      if (successor) {
         successor->previous = predecessor;
      }
      if (predecessor) {
         predecessor->next = successor;
      }
         
      if (currentNode == head) {
         head = successor;
      }
      if (currentNode == tail) {
         tail = predecessor;
      }
      
      delete currentNode;
   }
};

#endif // INVENTORY_H