function setOrder(orderList) {
  var enabled = orderList.filter(order => !$("#" + order.name).hasClass("disabled"))
  var disabled = orderList.filter(order => $("#" + order.name).hasClass("disabled"))
  for (var i = 0; i < enabled.length; i++) {
    var order = enabled[i]
    $("div").find("#" + order.name).css({order: i + 1});
  }
  for (var j = 0; j < disabled.length; j++) {
    var order = disabled[j]
    $("div").find("#" + order.name).css({order: i + j + 1});
  }
}

function getModelData() {
  var models = [];
  var boxes = $("div").find('[aria-type="model-box"]')
  for (var i = 0; i < boxes.length; i++) {
    var box = $(boxes[i]);
    var data = {
      name: box.data("name"),
      fps: box.data("fps"),
      resolution: box.data("resolution"),
      taskType: box.data("task-type"),
      order: box.css("order")
    }
    models.push(data)
  }
  return models;
}

function sortByName(asc) {
  var models = getModelData()
  models.sort(function(a, b) {
      if(a.name < b.name) { return asc ? -1 : 1; }
      if(a.name > b.name) { return asc ? 1 : -1; }
      return 0;
  });
  setOrder(models)
}

function sortByPerformance(asc) {
  var models = getModelData()
  models.sort(function(a, b) {
      if(a.fps < b.fps) { return asc ? -1 : 1; }
      if(a.fps > b.fps) { return asc ? 1 : -1; }
      return 0;
  });
  setOrder(models)
}

function sortByResolution(asc) {
  var models = getModelData()
  models.sort(function(a, b) {
      if(a.resolution < b.resolution) { return asc ? -1 : 1; }
      if(a.resolution > b.resolution) { return asc ? 1 : -1; }
      return 0;
  });
  setOrder(models)
}

function filterByCategory(event, categoryName) {
  var categories = $(".category")
  for (var k = 0; k < categories.length; k++) {
    var category = categories[k];
    category.classList.remove("category-active")
  }
  event.target.classList.add("category-active")
  var models = getModelData()
  var matching = models.filter(model => model.taskType === categoryName).sort((a, b) => a.order - b.order);
  var notMatching = models.filter(model => model.taskType !== categoryName).sort((a, b) => a.order - b.order);
  if(categoryName === "all") {
    matching = models;
    notMatching = [];
  }
  var i, j;

  for (i = 0; i < matching.length; i++) {
    var model = matching[i]
    $("div").find("#" + model.name).css({order: i + 1}).removeClass("disabled");
  }
  for (j = 0; j < notMatching.length; j++) {
    var model = notMatching[j]
    $("div").find("#" + model.name).css({order: i + j + 1}).addClass("disabled");
  }
}