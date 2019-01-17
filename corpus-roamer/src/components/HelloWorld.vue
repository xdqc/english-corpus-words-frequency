<template>
  <div class="hello">
    <!-- <h3>{{msg}}</h3> -->
    <p>Press <code>J</code> and <code>K</code> to go up and down.</p>
    <input type="number" v-model="cursor" :max="WL_size" min="0" step="10">
    <ul>
      <li v-for="(word,i) in word_list" :key="i">
        <a :href="'https://www.etymonline.com/word/'+word" target="_blank">
          <span :class="{ 'current-cursor': (cursor<10 ? cursor==i : i==10)}">{{ word }}</span>
        </a>
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
      WL_size: 61420,
      cursor: 4700,
      speakMsg: new SpeechSynthesisUtterance()
    };
  },
  computed: {
    word_list: function() {
      const start = this.cursor >10 ? parseInt(this.cursor)-10 : 0;
      return WL.slice(start, parseInt(this.cursor) + 10);
    },
  },
  mounted() {
    window.addEventListener("keypress", e => {
      if (e.keyCode === 106 && this.cursor > 0) {
        this.cursor--;
        this.speakWord(this.cursor);
      } else if (e.keyCode === 107 && this.cursor < this.WL_size) {
        this.cursor++;
        this.speakWord(this.cursor);
      } else if (e.keyCode === 113) {
        this.speakWord(this.cursor);
      } else {
        speechSynthesis.cancel();
      }
    });
  },
  methods: {
    speakWord(index) {
      this.speakMsg.text = WL[index];
      this.speakMsg.voice = speechSynthesis.getVoices()[9];
      speechSynthesis.speak(this.speakMsg);
    }
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
  margin: 10px 10px;
}
a {
  color: #2c3e5096;
  text-decoration:none
}
.current-cursor {
  color: #42b983;
  /* color:#f7786b; */
  font-size: x-large;
};
</style>
