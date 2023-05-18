// This will be the object that will contain the Vue attributes
// and be used to initialize it.

// Given an empty app object, initializes it filling its attributes,
// creates a Vue instance, and then initializes the Vue instance.
let init = function () {

    var self = {};
    
    // This is the Vue data.
    self.data = {
        // Complete as you see fit.
    };    
    
    self.enumerate = function (a) {
        // This adds an _idx field to each element of the array.
        let k = 0;
        a.map((e) => {e._idx = k++;});
        return a;
    };    

    // This contains all the methods.
    self.methods = {
        // Complete as you see fit.
    };

    // This creates the Vue instance.
    self.vue = new Vue({
        el: "#vue-target",
        data: self.data,
        methods: self.methods
    });

    // Put here any initialization code.

    return self;
};

// This takes the (empty) app object, and initializes it,
// putting all the code in it. 
var app = init();
