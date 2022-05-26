<template>
  <div>
    <p>{{ target }}</p>
    <button @click="wordcloud()">1</button>
    <svg :width="500" :height="300">
      <path fill="none" stroke="#76BF8A" stroke-width="3" :d="path"></path>
    </svg>
  </div>


</template>

<script>

import * as d3 from "d3";
export default {
  data() {
    return {
      data: [90, 72, 72, 25, 10, 92],
    };
  },
  computed: {
    target() {
      const result = {};
      this.data.forEach((x) => { 
        result[x] = (result[x] || 0)+1; 
      })
      return result
    }},

  methods: {
    wordcloud(){
      const width = 1000;
      const height = 700;

      const a = d3.select("p", data => show(data));
      console.log(a)
      function show(data) {
            d3.layout
                .cloud()
                .size([width, height])
                .words(data)
                // .rotate(function (d) { return Math.random() * 360; })
                .fontSize((d) => d.frequency/500)
                .on("end", draw)
                .start();
        }

      function draw(words) { 
          d3.select("body")
              .append("svg")
                  .attr("width", width)
                  .attr("height", height)
              .append("g")
                  .attr("transform", "translate(" + width / 2 + "," + height / 2 + ")")
              .selectAll("text")
                  .data(words)
              .enter().append("text")
                  .style("fill", function (d) {
                      if (parseInt(d.frequency) > parseInt(50000)) return "#dd3333";
                      else if (parseInt(d.frequency) > parseInt(40000)) return "#8224e3";
                      else if (parseInt(d.frequency) > parseInt(30000)) return "#81d742";
                      else if (parseInt(d.frequency) > parseInt(20000)) return "#00c280";
                      else if (parseInt(d.frequency) > parseInt(12000)) return "#1e73be";
                      else if (parseInt(d.frequency) > parseInt(8000)) return "#dd9933";
                      else if (parseInt(d.frequency) > parseInt(3000)) return "#626208";
                      else "#025275";
                  })
                  .style("font-family", "Impact")
                  .attr("text-anchor", "middle")
                  .style("font-size", (d) => d.size + "px")
                  .attr("transform", (d) => "translate(" + [d.x, d.y] + ")rotate(" + d.rotate + ")")
                  .text((d) => d.text)
      }     
     }
    }
  }
</script>