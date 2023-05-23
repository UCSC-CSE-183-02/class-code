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
        "features": "[]"
    };
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
        var features = Q.eval(self.vue.new_thing.features);
        var data = {
            "name": self.vue.new_thing.name,
            "features": features
        };
        self.vue.new_thing.name = "";
        self.vue.new_thing.features = "[]"; // the tags_input plugin stores json as a string
        Q(".tags-list")[0].innerHTML = ""; // magic to clear the non vue.js tags
        self.vue.things.unshift(data);
        axios.post("../api/create_thing", data).then(function(){}, function(){
            self.vue.things.shift();
            alert("Sorry unable to record it!");            
        });
    }
    self.vue = new Vue({el:"#vue", "data": self.data, "methods": self.methods});
    console.log("test!");
    self.methods.do_search();

    Q.tags_input("#features"); // magic to turn the input into tags

    return self;
}

window.app = init();