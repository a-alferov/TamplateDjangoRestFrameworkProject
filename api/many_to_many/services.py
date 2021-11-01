from api.models import Pizza, Topping


def topping_add(pizza: Pizza, topping: Topping):
    """
    Adding topping to pizza

    :param pizza: Pizza
    :type pizza: Pizza
    :param topping: Topping
    :type topping: Topping
    """
    pizza.toppings.add(topping)


def topping_remove(pizza: Pizza, topping: Topping):
    """
    Removing topping from pizza

    :param pizza: Pizza
    :type pizza: Pizza
    :param topping: Topping
    :type topping: Topping
    """
    pizza.toppings.remove(topping)
