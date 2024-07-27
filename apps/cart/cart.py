class Cart:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        self.cart = self.session.get("cart", {})

    def add(self, item):
        if str(item.id) not in self.cart.keys():
            self.cart[str(item.id)] = {
                "product_id": item.id,
                "name": item.name,
                "price": item.price,
                "quantity": 1,
                "image": item.image.url,
            }
        else:
            self.cart[str(item.id)]["quantity"] += 1
        self.save_cart()

    def save_cart(self):
        self.session["cart"] = self.cart
        self.session.modified = True

    def delete(self, item):
        if str(item.id) in self.cart:
            del self.cart[str(item.id)]
            self.save_cart()

    def remove(self, item):
        if str(item.id) in self.cart.keys():
            self.cart[str(item.id)]["quantity"] -= 1
            if self.cart[str(item.id)]["quantity"] <= 0:
                del self.cart[str(item.id)]
            self.save_cart()

    def get(self, item):
        if str(item.id) in self.cart.keys():
            return self.cart[str(item.id)]
        else:
            return None

    def get_all(self):
        return self.cart

    def clear(self):
        self.cart = {}
        self.save_cart()
