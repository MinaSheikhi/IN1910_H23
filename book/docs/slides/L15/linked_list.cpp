#include <iostream>

struct Node
{
    int value;
    Node *next;
};

class LinkedList
{
  private:
    Node *head = nullptr;
    int _size = 0;

    Node *get_node(int index)
    {
        int current_index = 0;
        Node *current = head;
        while (current != nullptr)
        {
            if (current_index == index)
            {
                return current;
            }
            current = current->next;
            current_index++;
        }
        throw std::out_of_range("Index " + std::to_string(index) + " is out of range.");
    }

  public:
    int length()
    {
        return _size;
    }

    void append(int value)
    {
        Node *node = new Node{value};
        _size++;
        if (head == nullptr)
        {
            head = node;
            return;
        }
        Node *current = head;
        while (current->next != nullptr)
        {
            current = current->next;
        }
        current->next = node;
    }

    void print()
    {
        std::cout << "[ ";
        Node *current = head;
        while (current != nullptr)
        {
            std::cout << current->value << " ";
            current = current->next;
        }
        std::cout << "]\n";
    }

    int &operator[](int index)
    {
        Node *node = get_node(index);
        return node->value;
    }

    void push_front(int value)
    {
        Node *node = new Node{value, head};
        head = node;
    }
};
