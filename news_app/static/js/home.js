$(document).ready(function(){
  $('#usselector').click(function(event){
    $('#ustext').css('color','#6C6C6F');
    $('#natext').css('color','#aaaaaa');
    $('#worldtext').css('color','#aaaaaa');
    d3.json('static/json/us_states.json',
            function(json){
              drawUSChart(json);
            }
    );
  });

  $('#naselector').click(function(event){
    $('#ustext').css('color','#aaaaaa');
    $('#natext').css('color','#6C6C6F');
    $('#worldtext').css('color','#aaaaaa');
    d3.json('static/json/north_america.json',
            function(json){
              drawNAChart(json);
            }
    );
  });

  $('#worldselector').click(function(event){
    $('#ustext').css('color','#aaaaaa');
    $('#natext').css('color','#aaaaaa');
    $('#worldtext').css('color','#6C6C6F');
    d3.json('static/json/continents.json',
            function(json){
              drawWorldChart(json);
            }
    );
  });

  d3.json('static/json/us_states.json',
          function(json){
            drawUSChart(json);
          }
  );

  function equalToEventTarget() {
      return this == d3.event.target;
  };

  d3.select("body").on("click",function(){
      var state = d3.selectAll(".state");
      var outside = state.filter(equalToEventTarget).empty();
      if (outside) {
          state.classed("selected", false).style("fill", "#e1e2e1");
      };
  });
});


function drawUSChart(data_set) {

  var w = 630;
  var h = 350;

  var projection = d3
    .geoMercator()
    .scale(550)
    .translate([1250,580]);

  var path = d3
    .geoPath(projection);

  $('svg').remove();

  var svg = d3.select("#map")
      .append("svg")
      .attr("width", w)
      .attr("height", h)
      .attr("transform", "translate(1,1)");

  var statesGroup = svg.append("g").attr("id", "map");

  var states = statesGroup
        .selectAll("path")
        .data(data_set.features)
        .enter()
        .append("path")
        .attr("class", "state")
        .attr("d", path)
        .attr("id", function(d, i) {
          return "state" + d.properties.GEO_ID;
        })
        .on("mouseover", function(d, i) {
            d3.select("#state" + d.properties.GEO_ID).style("fill", "#66bb6a");
        })
        .on("mouseout", function(d, i) {
            if (d3.select("#state" + d.properties.GEO_ID).classed("selected") == false) {
              d3.select("#state" + d.properties.GEO_ID).style("fill", "#e1e2e1");
            };
        })
        .on("click", function(d, i){
            d3.select(".selected").classed("selected", false).style("fill", "#e1e2e1");
            d3.select("#state" + d.properties.GEO_ID).classed("selected", true).style("fill", "#66bb6a");
            var CSRFtoken = $('input[name=csrfmiddlewaretoken]').val();
            $.post('/log_user_query',
                   {geoid: d.properties.GEO_ID,
                    csrfmiddlewaretoken: CSRFtoken},
                   'json');
        });
};

function drawNAChart(data_set) {

  var w = 630;
  var h = 373;

  var projection = d3
    .geoMercator()
    .scale(300)
    .translate([875,440]);

  var path = d3
    .geoPath(projection);

  $('svg').remove();

  var svg = d3.select("#map")
      .append("svg")
      .attr("width", w)
      .attr("height", h)
      .attr("transform", "translate(2,2)");

  var statesGroup = svg.append("g").attr("id", "map");

  var states = statesGroup
        .selectAll("path")
        .data(data_set.features)
        .enter()
        .append("path")
        .attr("class", "state")
        .attr("d", path)
        .attr("id", function(d, i) {
          return "state" + d.properties.adm0_a3;
        })
        .on("mouseover", function(d, i) {
            d3.select("#state" + d.properties.adm0_a3).style("fill", "#66bb6a");
        })
        .on("mouseout", function(d, i) {
          if (d3.select("#state" + d.properties.adm0_a3).classed("selected") == false) {
            d3.select("#state" + d.properties.adm0_a3).style("fill", "#e1e2e1");
          };
        })
        .on("click", function(d, i){
            d3.select(".selected").classed("selected", false).style("fill", "#e1e2e1");
            d3.select("#state" + d.properties.adm0_a3).classed("selected", true).style("fill", "#66bb6a");
            var CSRFtoken = $('input[name=csrfmiddlewaretoken]').val();
            $.post('/log_user_query',
                   {geoid: d.properties.adm0_a3,
                    csrfmiddlewaretoken: CSRFtoken},
                   'json');
        });
};

function drawWorldChart(data_set) {

  var w = 630;
  var h = 350;

  var projection = d3
    .geoMercator()
    .scale(100)
    .translate([315,250]);

  var path = d3
    .geoPath(projection);

  $('svg').remove();

  var svg = d3.select("#map")
      .append("svg")
      .attr("width", w)
      .attr("height", h)
      .attr("transform", "translate(2,2)");

  var statesGroup = svg.append("g").attr("id", "map");

  var states = statesGroup
        .selectAll("path")
        .data(data_set.features)
        .enter()
        .append("path")
        .attr("class", "state")
        .attr("d", path)
        .attr("id", function(d, i) {
          return "state" + d.properties.cartodb_id;
        })
        .on("mouseover", function(d, i) {
            d3.select("#state" + d.properties.cartodb_id).style("fill", "#66bb6a");
        })
        .on("mouseout", function(d, i) {
            d3.select("#state" + d.properties.cartodb_id).style("fill", "#e1e2e1");
        });
};
