"use strict";


function clone(obj) {
    return JSON.parse(JSON.stringify(obj));
}

function init() {
    var self = {};
    self.data = {};    
    self.methods = {};

    var empty_task = {
        body: "",
        assigned_to: 1,
        status: "pending",
        deadline: "2099-12-31T23:59",
    };

    // client side data example
    self.data.users_as_dict = {};
    self.data.users = [];
    self.data.statuses = ["pending", "completed", "rejected"];
    self.data.new_task = clone(empty_task);
    self.data.my_tasks = [];

    // client side methods
    self.methods.add_task = function() {
        // do validation
        if (self.vue.new_task.body.trim().length < 5)
        {
            alert("task description too short");
            return;
        }
        if (self.vue.new_task.assigned_to === null)
        {
            alert("you did not assign the task");
            return;
        }
        if (self.vue.new_task.status === null)
        {
            alert("you did not assign a status");
            return;
        }
        if (self.vue.new_task.deadline === null)
        {
            alert("you did not set a deadline");
            return;
        }
        // perform the action
        axios.post("../post_new_task", self.vue.new_task).then(function(){
            axios.get("../my_tasks").then(function(r){
                self.vue.my_tasks = r.data.my_tasks;
           });       
        });
        // var task = clone(self.vue.new_task);        
        // to be fixed!
        // task.created_on = (new Date()).toISOString();
        // task.created_by = 1;        
        // self.vue.my_tasks.push(task);
        // self.vue.new_task = clone(empty_task);
    };

    self.methods.set_completed = function(task) {
        task.status = "completed";
        axios.put("../update_task", task);
    };
    self.methods.set_rejected = function(task) {
        task.status = "rejected";
        axios.put("../update_task", task);
    };

    self.vue = new Vue({el: '#vue', data: self.data, methods:self.methods});

    axios.get("../users").then(function(r){
         self.vue.users = r.data.users;
         self.vue.users.map(function(user){ self.data.users_as_dict[user.id] = user.first_name + " " + user.last_name; });
    });

    axios.get("../my_tasks").then(function(r){
         self.vue.my_tasks = r.data.my_tasks;
    });


    return self;
}

window.app = init();