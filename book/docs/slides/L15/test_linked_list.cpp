#include "linked_list.cpp"
#include <cassert>

void test_empty_list_has_length_zero()
{
    LinkedList ll;
    assert(ll.length() == 0);
}

void test_append_one_element_gives_length_one()
{
    LinkedList ll;
    ll.append(1);
    assert(ll.length() == 1);
}

void test_print()
{
    LinkedList ll;
    ll.append(1);
    ll.append(3);
    ll.append(42);
    ll.print();
}

void test_indexing()
{
    LinkedList ll;
    ll.append(1);
    assert(ll[0] == 1);
    ll.append(3);
    ll[1] = 2;
    assert(ll[1] == 2);
}

void test_push_front()
{
    LinkedList ll;
    ll.push_front(1);
    assert(ll[0] == 1);
    ll.push_front(2);
    assert(ll[0] == 2);
    assert(ll[1] == 1);
}

int main()
{

    test_empty_list_has_length_zero();
    test_print();
    test_indexing();
    test_push_front();

    return 0;
}
