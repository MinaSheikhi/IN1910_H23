#include <cmath>
#include <iostream>
#include <math.h>

struct Point
{
    double x;
    double y;
};

class Circle
{
  private:
    double _radius;
    Point _center;

  public:
    Circle(double, double, double);
    Circle(double radius, Point center);
    double get_radius();
    void set_radius(double radius);
    double area();
    void print();
};

Circle::Circle(double radius, double cx = 0, double cy = 0) : _radius(radius), _center({cx, cy})
{
    if (_radius < 0)
        throw std::invalid_argument("Radius cannot negative");
}
Circle::Circle(double radius, Point center) : _center(center)
{
    set_radius(radius);
}

double Circle::get_radius()
{
    return _radius;
}
void Circle::set_radius(double radius)
{
    if (radius < 0)
    {
        throw std::invalid_argument("Radius cannot negative");
    }
    _radius = radius;
}

double Circle::area()
{
    return M_PI * std::pow(_radius, 2);
}
void Circle::print()
{
    std::cout << "Circle with radius " << _radius;
    std::cout << " and center (" << _center.x << ", " << _center.y << ")\n";
}

double distance(Point p1, Point p2)
{
    return std::sqrt(std::pow(p1.x - p2.x, 2) + std::pow(p1.y - p2.y, 2));
}

int main()
{

    Circle c1{1, 1.0, 2.0};
    Point p1{0.0, 0.0};
    Point p2{3.0, 4.0};
    std::cout << distance(p1, p2) << "\n";
    Circle c2{2, p1};

    c1.print();
    c2.print();

    return 0;
}
