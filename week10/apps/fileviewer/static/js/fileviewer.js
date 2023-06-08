"use strict";

Vue.component('fileviewer', {
    props: ["myfiles"],  
    data: function() {
        console.log("creating a new fileviewer!");
        return {
            is_toggled: false
        };
    },
    methods: {
        toggle: function() { this.is_toggled = !this.is_toggled; }
    },
    template: `
    <ul style="border: 1px solid red; margin:5px">
      <li v-for="file in myfiles">
        <a v-if="file.type=='file'" v-bind:href="'../api/file/'+file.fullpath">{{file.name}}</a>
        <div v-if="file.type=='folder'">
          <a v-on:click="toggle()">{{file.name}}</a>
          <fileviewer v-if="is_toggled" :myfiles="file.content"></fileviewer>
        </div>
      </li>
    </ul>`
  });

function init() {
    var self = {};
    self.data = {};
    self.methods = {};
    self.data.files = [];

    self.vue = new Vue({el:"#vue", data:self.data, methods:self.methods});
    fetch("../api/files").then(r=>r.json()).then(function(r){
        self.vue.files = r.files;
    });
    return self;
}

window.app = init();