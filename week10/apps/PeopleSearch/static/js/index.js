"use strict";

function init() {
    var self={};
    self.data = {};    
    self.methods = {};
    self.data.search_string = "";
    self.data.users = [];
    self.methods.search = function(search_string, user) {
        var words = search_string.toLowerCase().split(" ");
        for(var i=0; i<words.length; i++) {
            var word = words[i];
            if (!user.first_name.toLowerCase().includes(word) &&
                !user.last_name.toLowerCase().includes(word)) {
                    return false;
                }
        }
        return true;
    };
    self.vue = new Vue({el:"#vue", data:self.data, methods:self.methods})
    fetch("../api/users").then(r=>r.json()).then(function(response){        
        self.vue.users = response.users;
    });
    return self;
}

window.app = init();