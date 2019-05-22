// This is adapted from https://bl.ocks.org/mbostock/2675ff61ea5e063ede2b5d63c08020c7

var svg = d3.select("svg"),
    width = +svg.attr("width"),
    height = +svg.attr("height");

var simulation = d3.forceSimulation()
    .force("link", d3.forceLink().id(function (d) {
        return d.id;
    }))
    .force("charge", d3.forceManyBody())
    .force("center", d3.forceCenter(width / 2, height / 2));

d3.json("view/sample.json", function (error, graph) {
    if (error) throw error;

    var link = svg.selectAll(".link")
        .data(graph.links)
        .enter().append("line")
        .attr("class", "link")
        .style("stroke-width", function (d) {
          return d.weight * 3 + "px"
        })
        .style("stroke", function (d) {
          return "black"
        })

    var node = svg.selectAll(".nodes")
        .data(graph.nodes)
        .enter().append("g")
        .attr("class", "nodes")

    node.append("circle")
        .attr("r", 5)
        .attr('x', function(d, i) {
          return d.x;
        })
        .attr('y', function(d, i) {
          return d.y;
        })
        .call(d3.drag()
            .on("start", dragstarted)
            .on("drag", dragged)
            .on("end", dragended));

    node.append("text")
        .attr('dx', function(d, i) {
          return 8;
        })
        .attr('dy', function(d, i) {
          return ".35em";
        })
        .text(function (d) {
            console.log(d.id)
            return d.id;
        })

    simulation
        .nodes(graph.nodes)
        .on("tick", ticked);

    simulation.force("link")
        .links(graph.links);

    function ticked() {
        link
            .attr("x1", function (d) {
                return d.source.x;
            })
            .attr("y1", function (d) {
                return d.source.y;
            })
            .attr("x2", function (d) {
                return d.target.x;
            })
            .attr("y2", function (d) {
                return d.target.y;
            });

        d3.selectAll("circle")
            .attr("cx", function (d) {
                return d.x;
            })
            .attr("cy", function (d) {
                return d.y;
            });
        d3.selectAll("text")
            .attr("x", function (d) {
               return d.x;
            })
            .attr("y", function (d) {
               return d.y;
            })
    }
});

function dragstarted(d) {
    if (!d3.event.active) simulation.alphaTarget(0.3).restart();
    d.fx = d.x;
    d.fy = d.y;
}

function dragged(d) {
    d.fx = d3.event.x;
    d.fy = d3.event.y;
}

function dragended(d) {
    if (!d3.event.active) simulation.alphaTarget(0);
    d.fx = null;
    d.fy = null;
}
