"use strict";

function debounce(func, timeout = 300){
    let timer;
    return (...args) => {
      clearTimeout(timer);
      timer = setTimeout(() => { func.apply(this, args); }, timeout);
    };
}

function init() {
    console.log("test!");
    var self = [];
    self.data = {};
    self.methods = {};
    self.data.new_thing = {
        "name": "",
        "features": []
    };
    self.data.new_tag = "";
    self.data.things = [];
    self.data.search = [];
    self.data.options = ["Apple", "Banana", "Strawberry"];
    self.methods.do_search = debounce(function() {
        var url = "../api/things";
        if (self.vue.search.length > 0) {
            url = url + '?tags=' + self.vue.search;
        }
        axios.get(url).then(function(response){
            self.vue.things = response.data.things;
        });
    }, 1000);
    self.methods.post_new_thing = function() {
        var data = {
            "name": self.vue.new_thing.name,
            "features": self.vue.new_thing.features
        };
        self.vue.new_thing.name = "";
        self.vue.new_thing.features = [];
        self.vue.new_tag = "";
        self.vue.things.unshift(data);
        axios.post("../api/create_thing", data).then(function(){}, function(){
            self.vue.things.shift();
            alert("Sorry unable to record it!");            
        });
    }
    self.methods.add_tag = function() {
        self.vue.new_thing.features.push(self.vue.new_tag);
        self.vue.new_tag = "";
    };
    self.methods.del_tag = function(tag) {
        self.vue.new_thing.features = self.vue.new_thing.features.filter(t=>{return t!=tag;})
    };
    self.vue = new Vue({el:"#vue", "data": self.data, "methods": self.methods});
    console.log("test!");
    self.methods.do_search();

    return self;
}

window.app = init();