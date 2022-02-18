from abc import ABCMeta, abstractmethod


class IEcommerceAPI(ABCMeta):

    @staticmethod
    @abstractmethod
    def get_products(name=''):
        """
        Returns the list of all the products filtered by name. If no name is given, it returns all the products
        :param name: the value to be used as a filter
        :return: list of products
        """
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    def add_item_to_cart(item):
        """
        Adds a new item to the items table
        :param item: the data of the item to be added
        :return: the new item added or HTML 400 response if the item cannot be added
        """
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    def delete_item(item_id):
        """
        Deletes an item from the items table gives its id
        :param item_id: the item's id
        :return: HTML 200 response if the item was deleted successfully
        """
        raise NotImplementedError
