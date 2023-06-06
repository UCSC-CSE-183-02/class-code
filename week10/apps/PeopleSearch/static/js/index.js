"use strict";

function init() {
    var self={};
    self.data = {};    
    self.methods = {};
    self.data.search_string = "";
    self.data.filtered_users = [];
    self.methods.filter_users = Q.debounce(function() {
        fetch("../api/users?q="+self.vue.search_string).then(r=>r.json())
        .then(function(response){
            self.vue.filtered_users = response.users;
        });
    }, 1000);
    self.vue = new Vue({el:"#vue", data:self.data, methods:self.methods})    
    return self;
}

window.app = init();