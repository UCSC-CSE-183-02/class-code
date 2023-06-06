"use strict";

function init() {
    var self={};
    self.data = {};    
    self.methods = {};
    self.data.search_string = "";
    self.data.users = [];
    self.data.filtered_users = [];
    self.methods.filter_users = function() {
        self.vue.filtered_users = [];
        if (self.vue.search_string.length<3) return;
        var words = self.vue.search_string.toLowerCase().split(" ");
        self.vue.users.map(function(user){
            for(var i=0; i<words.length; i++) {
                var word = words[i];
                if (user.first_name.toLowerCase().includes(word) ||
                    user.last_name.toLowerCase().includes(word)) {
                        self.vue.filtered_users.push(user);
                    }
            }
        });
    };
    self.vue = new Vue({el:"#vue", data:self.data, methods:self.methods})    
    fetch("../api/users").then(r=>r.json()).then(function(response){        
        self.vue.users = response.users;
        // self.methods.filter_users();
    });
    return self;
}

window.app = init();