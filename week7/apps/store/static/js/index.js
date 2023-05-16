"use strict";

function clone(obj){
    return JSON.parse(JSON.stringify(obj));
}

function init() {
    var self={};
    self.data = {};    
    self.methods = {};
    self.data.user = window.user;
    self.data.products = [];
    self.data.cart = {};    
    self.methods.add_to_cart = function(product) {
        var item = clone(product);        
        if (item.id in self.vue.cart) {
            self.vue.cart[item.id].quantity += 1;
        } else {
            item.quantity = 1;
            self.vue.cart[item.id] = item;
        }
        self.vue.cart = clone(self.vue.cart);
    };
    self.methods.buy_cart = function() {
        var cart = self.vue.cart;
        axios.post("../api/buy_cart", cart).then(function(){alert("well done");});
        self.vue.cart = {};
    };
    self.vue = new Vue({el:"#vue", data: self.data, methods: self.methods});
    axios.get("../api/products").then(function(response){
        self.vue.products = response.data.products;
    })
    return self;
}

window.app = init();