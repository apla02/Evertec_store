from django.db import models


class Orders(models.Model):
    """Define the orders taken by the clients of the store"""
    PAYMENT_OPTIONS= (
        ('C', 'CREATED'),
        ('P', 'PAYED'),
        ('R', 'REJECTED'),
    )
    customer_name = models.CharField(max_length=80, null=False)
    customer_email = models.EmailField(max_length=120, null=False)
    customer_mobile = models.CharField(max_length=40, null=False)
    status = models.CharField(max_length=1, choices=PAYMENT_OPTIONS, default='C')
    created_at = models.DateField(auto_now_add=True, null=False)
    updated_at = models.DateField(auto_now=True, null=False)

    def __str__(self):
        """str method to return a str representation of Orders model"""
        return f'{self.customer_name} | {self.id}'

    def serializer(self):
        """Method implement to serialize object (pending search new ways)"""
        return {
            f'{key}': value for key, value in self.__dict__.items() if key != '_state'
        }



    class Meta:
        """class to set up the meta features"""
        db_table = "orders"
