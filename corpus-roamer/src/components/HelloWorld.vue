<template>
  <div class="hello">
    <!-- <h3>{{msg}}</h3> -->
    <input type="number" v-bind="cursor_idx" @change="changeCursor()">
    <ul>
      <li v-for="(word,i) in word_list" :key="i" > 
        <!-- v-show="i < cursor_idx+10 && i>=cursor_idx" -->
        <span>{{ word }}</span>
      </li>
    </ul>
  </div>
</template>

<script>
import WL from "../assets/word_list.json";

export default {
  name: "HelloWorld",
  props: {
    msg: String
  },
  data() {
    return {
      cursor_idx: Number
    };
  },
  computed: {
    word_list : function(){
      return WL.slice(this.cursor_idx, this.cursor_idx+10);
    }
  },
  mounted() {
    this.cursor_idx = 0;
    window.addEventListener("keypress", e => {
      // console.log(e.keyCode);
      if (e.keyCode === 39 && this.cursor_idx > 0) {
        this.cursor_idx--;
      } else if (e.keyCode === 46) {
        this.cursor_idx++;
      }
    });
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  /* display: inline-block; */
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
