node = vis
  .selectAll(".node")
  .data(nodes)
  .enter()
  .append("g")
  .attr("class", "node not-moved")
  .on("click", function (d) {
    if (d3.select(this).classed("moved")) {
      // Transition Back
      d3.select(this).classed({ "not-moved": true, moved: false });
      d3.select(this)
        .transition()
        .ease("quad")
        .duration(700)
        .attr("transform", "translate(0, " + (330 - d.cy) + ")");
      d3.select(this)
        .transition()
        .ease("linear")
        .delay(700)
        .duration(500)
        .attr("transform", "translate(0,0)");
      $(this).siblings(".node").delay(500).fadeToggle(2000);
      $(".field-of-study-text").fadeToggle(100);
      $(".web, .sub-connect, .sub-node-green-circle")
        .delay(1500)
        .fadeToggle(1000);
    } else {
      // Initial Transition
      d3.select(this)
        .transition()
        .ease("quad")
        .duration(700)
        .attr("transform", "translate(0, " + (330 - d.cy) + ")");
      d3.select(this)
        .transition()
        .ease("linear")
        .delay(700)
        .duration(500)
        .attr(
          "transform",
          "translate(" + (840 - d.cx) + "," + (200 - d.cy) + ")"
        );
      d3.select(this).classed({ moved: true, "not-moved": false });

      $(".web, .sub-connect, .sub-node-green-circle").toggle(200);
      $(this).siblings(".node").fadeToggle();
      $(".field-of-study-text").delay(500).fadeToggle(2000);

      // Show corresponding text based on content
      $(".text").text(d.content + " - This is the corresponding text.");
    }
  });
