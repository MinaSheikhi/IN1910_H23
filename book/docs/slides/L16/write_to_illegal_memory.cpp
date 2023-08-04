class Array
{
  private:
    int *data;

  public:
    Array()
    {
    }
    int &operator[](int index)
    {
        return data[index];
    }
};

void write_to_illegal_memory()
{
    Array arr;
    int value = 42;
    arr[0] = 42;
}

int main()
{
    write_to_illegal_memory();
    return 0;
}
